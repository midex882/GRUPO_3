// Dependencias necesarias en pom.xml:
/*
<dependencies>
    <dependency>
        <groupId>org.springframework.boot</groupId>
        <artifactId>spring-boot-starter-web</artifactId>
    </dependency>
    <dependency>
        <groupId>com.fasterxml.jackson.core</groupId>
        <artifactId>jackson-databind</artifactId>
    </dependency>
</dependencies>
*/

package com.example.demo;

import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;
import org.springframework.web.bind.annotation.*;
import com.fasterxml.jackson.databind.ObjectMapper;
import com.fasterxml.jackson.core.type.TypeReference;
import java.io.*;
import java.util.*;
import java.util.concurrent.atomic.AtomicLong;

@SpringBootApplication
@RestController
@RequestMapping("/nombres")
public class Main {

	private final Map<Long, Persona> personas = new HashMap<>();
	private final AtomicLong contador = new AtomicLong();
	private final ObjectMapper objectMapper = new ObjectMapper();
	private final String ARCHIVO_JSON = "personas.json";

	public static void main(String[] args) {
		SpringApplication.run(Main.class, args);
	}

	// Constructor: carga datos del JSON al iniciar
	public Main() {
		cargarDesdeJSON();
	}


	// LOGIN - POST /nombres/login
	@PostMapping("/login")
	public String login(@RequestBody Map<String, String> credenciales) {
		if ("username".equals(credenciales.get("usuario")) &&
				"password".equals(credenciales.get("contrasena"))) {
			return "Login correcto";
		}
		return "Credenciales incorrectas";
	}

	// CREATE - POST /nombres/{nombre}
	@PostMapping("/{nombre}")
	public Persona crear(@PathVariable String nombre) {
		long id = contador.incrementAndGet();
		Persona persona = new Persona(id, nombre);
		personas.put(id, persona);
		guardarEnJSON();
		return persona;
	}

	// READ ALL - GET /nombres
	@GetMapping
	public List<Persona> obtenerTodos() {
		return new ArrayList<>(personas.values());
	}

	// READ ONE - GET /nombres/{id}
	@GetMapping("/{id}")
	public Persona obtenerPorId(@PathVariable Long id) {
		Persona persona = personas.get(id);
		if (persona == null) {
			throw new RuntimeException("Persona no encontrada con id: " + id);
		}
		return persona;
	}

	// UPDATE - PUT /nombres/{id}
	@PutMapping("/{id}")
	public Persona actualizar(@PathVariable Long id, @RequestBody Persona personaActualizada) {
		if (!personas.containsKey(id)) {
			throw new RuntimeException("Persona no encontrada con id: " + id);
		}
		personaActualizada.setId(id);
		personas.put(id, personaActualizada);
		guardarEnJSON();
		return personaActualizada;
	}

	// DELETE - DELETE /nombres/{id}
	@DeleteMapping("/{id}")
	public String eliminar(@PathVariable Long id) {
		if (!personas.containsKey(id)) {
			throw new RuntimeException("Persona no encontrada con id: " + id);
		}
		personas.remove(id);
		guardarEnJSON();
		return "Persona eliminada con id: " + id;
	}

	// Método para guardar en JSON
	private void guardarEnJSON() {
		try {
			objectMapper.writerWithDefaultPrettyPrinter()
					.writeValue(new File(ARCHIVO_JSON), personas);
			System.out.println("✅ Datos guardados en " + ARCHIVO_JSON);
		} catch (IOException e) {
			System.err.println("❌ Error al guardar en JSON: " + e.getMessage());
		}
	}

	// Método para cargar desde JSON
	private void cargarDesdeJSON() {
		try {
			File archivo = new File(ARCHIVO_JSON);
			if (archivo.exists()) {
				Map<Long, Persona> datos = objectMapper.readValue(
						archivo,
						new TypeReference<Map<Long, Persona>>() {}
				);
				personas.putAll(datos);

				// Actualizar el contador al ID más alto
				if (!personas.isEmpty()) {
					long maxId = personas.keySet().stream()
							.max(Long::compareTo)
							.orElse(0L);
					contador.set(maxId);
				}

				System.out.println("✅ Datos cargados desde " + ARCHIVO_JSON);
			}
		} catch (IOException e) {
			System.out.println("ℹ️ No se encontró archivo JSON previo, iniciando vacío");
		}
	}

	// Clase interna para representar una Persona
	public static class Persona {
		private Long id;
		private String nombre;

		public Persona() {}

		public Persona(Long id, String nombre) {
			this.id = id;
			this.nombre = nombre;
		}

		public Long getId() { return id; }
		public void setId(Long id) { this.id = id; }

		public String getNombre() { return nombre; }
		public void setNombre(String nombre) { this.nombre = nombre; }
	}
}

// Archivo application.properties (src/main/resources)
/*
server.port=8081
*/