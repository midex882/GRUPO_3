// Program.cs
using System.Collections.Concurrent;
using System.Text.Json;
using System.Text.Json.Serialization;
using System.Threading;

var builder = WebApplication.CreateBuilder(args);
var app = builder.Build();

var jsonOptions = new JsonSerializerOptions
{
    PropertyNameCaseInsensitive = true,
    WriteIndented = true
};

string fileName = "personas.json";
string filePath = Path.Combine(AppContext.BaseDirectory, fileName);
filePath = Path.GetFullPath(filePath);
Console.WriteLine($"📂 Archivo JSON usado: {filePath}");

// Estructuras en memoria (thread-safe)
var personas = new ConcurrentDictionary<long, Persona>();
long idCounter = 0;
object fileLock = new();

// Helper: cargar desde archivo (al iniciar)
void CargarDesdeJson()
{
    try
    {
        if (!File.Exists(filePath))
        {
            Console.WriteLine("ℹ️ No se encontró personas.json — iniciando vacío.");
            return;
        }

        lock (fileLock)
        {
            var text = File.ReadAllText(filePath);
            var lista = JsonSerializer.Deserialize<List<Persona>>(text, jsonOptions) ?? new List<Persona>();
            personas.Clear();
            foreach (var p in lista)
            {
                personas[p.Id] = p;
            }

            if (personas.Count > 0)
            {
                idCounter = personas.Keys.Max();
            }

            Console.WriteLine("✅ Datos cargados desde personas.json");
        }
    }
    catch (Exception ex)
    {
        Console.WriteLine("❌ Error al cargar personas.json: " + ex.Message);
    }
}

// Helper: guardar en archivo
void GuardarEnJson()
{
    try
    {
        lock (fileLock)
        {
            var lista = personas.Values.OrderBy(p => p.Id).ToList();
            var txt = JsonSerializer.Serialize(lista, jsonOptions);
            File.WriteAllText(filePath, txt);
            Console.WriteLine("✅ Datos guardados en personas.json");
        }
    }
    catch (Exception ex)
    {
        Console.WriteLine("❌ Error al guardar personas.json: " + ex.Message);
    }
}

// Cargar al iniciar
CargarDesdeJson();

// Rutas: mismas rutas y comportamiento que el Spring Boot ejemplo

// LOGIN - POST /nombres/login
app.MapPost("/nombres/login", ([FromBody] Dictionary<string, string> credenciales) =>
{
    if (credenciales.TryGetValue("usuario", out var usuario) &&
        credenciales.TryGetValue("contrasena", out var contrasena) &&
        usuario == "username" && contrasena == "password")
    {
        return Results.Ok("Login correcto");
    }
    return Results.Ok("Credenciales incorrectas");
});

// CREATE - POST /nombres/{nombre}
app.MapPost("/nombres/{nombre}", (string nombre) =>
{
    var nuevoId = Interlocked.Increment(ref idCounter);
    var persona = new Persona { Id = nuevoId, Nombre = nombre };
    personas[nuevoId] = persona;
    GuardarEnJson();
    return Results.Created($"/nombres/{nuevoId}", persona);
});

// READ ALL - GET /nombres
app.MapGet("/nombres", () =>
{
    var lista = personas.Values.OrderBy(p => p.Id).ToList();
    return Results.Json(lista);
});

// READ ONE - GET /nombres/{id}
app.MapGet("/nombres/{id:long}", (long id) =>
{
    if (personas.TryGetValue(id, out var persona))
        return Results.Json(persona);

    return Results.NotFound(new { message = $"Persona no encontrada con id: {id}" });
});

// UPDATE - PUT /nombres/{id}
app.MapPut("/nombres/{id:long}", (long id, Persona personaActualizada) =>
{
    if (!personas.ContainsKey(id))
        return Results.NotFound(new { message = $"Persona no encontrada con id: {id}" });

    // Asegurar que se conserve el id y actualizar campos
    var existing = personas[id];
    existing.Nombre = personaActualizada.Nombre ?? existing.Nombre;

    personas[id] = existing;
    GuardarEnJson();
    return Results.Json(existing);
});

// DELETE - DELETE /nombres/{id}
app.MapDelete("/nombres/{id:long}", (long id) =>
{
    if (!personas.TryRemove(id, out _))
        return Results.NotFound(new { message = $"Persona no encontrada con id: {id}" });

    GuardarEnJson();
    return Results.Ok(new { message = $"Persona eliminada con id: {id}" });
});

app.Run();

public class Persona
{
    [JsonPropertyName("id")]
    public long Id { get; set; }

    [JsonPropertyName("nombre")]
    public string? Nombre { get; set; }
}
