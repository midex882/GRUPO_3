const express = require('express');
const app = express();
const fs = require('fs');
app.use(express.json());

data_path = "./datos.json"


function readData() {
  const data = fs.readFileSync(data_path, 'utf-8');
  return JSON.parse(data);
}


function writeData(data) {
  fs.writeFileSync(data_path, JSON.stringify(data, null, 2));
}

const basicAuth = require('basic-auth');

function auth(req, res, next) {
  const user = basicAuth(req);
  const validUser = user && user.name === 'user' && user.pass === 'password';

  if (!validUser) {
    res.set('WWW-Authenticate', 'Basic realm="API Authentication"');
    return res.status(401).send('Authentication required.');
  }
  next();
}

// Apply the middleware to your API routes
app.use('/', auth); // Protects all routes under /api




app.get('/saludo', (req, res) => {
  res.json({ mensaje: '(con tono de disnay channel) Hola, soy Node.js y estás viendo la inevitable autodestrucción de nuestra especie!' });
});

app.get('/', (req, res)=>{
  res.json({ mensaje: 'Hola. Funciono y no estás muy seguro de cómo, a que no?'})
})





app.get('/nombres', (req, res) => {
  const nombres = readData();
  res.json(nombres);
});

+

app.get('/nombres/:nombre', (req, res) => {
  const nombre = req.params.nombre; // Captura directa y correcta

  if (!nombre) {
    return res.status(400).json({ error: 'Debes proporcionar un nombre, por ejemplo /nombres/Jose' });
  }

  const nombres = readData();
  const resultado = nombres.filter(p => 
    p.nombre.toLowerCase().includes(nombre.toLowerCase())
  );

  if (resultado.length === 0) {
    return res.status(404).json({ mensaje: 'No se encontró ningún registro con ese nombre' });
  }

  res.json(resultado);
});

app.put('/nombres/:id', (req, res) => {
  const nombres = readData();
  const id = parseInt(req.params.id);
  const index = nombres.findIndex(p => p.id === id);

  if (index === -1) return res.status(404).json({ error: 'Nombre no encontrado' });

  nombres[index].nombre = req.body.nombre;
  writeData(nombres);
  res.json(nombres[index]);
});

app.delete('/nombres/:id', (req, res) => {
  const nombres = readData();
  const id = parseInt(req.params.id);
  const nuevos = nombres.filter(p => p.id !== id);

  if (nombres.length === nuevos.length)
    return res.status(404).json({ error: 'Nombre no encontrado' });

  writeData(nuevos);
  res.status(204).send();
});

const PORT = 3000;
app.listen(PORT, () => {
  console.log(`Servidor escuchando en http://localhost:${PORT}`);
});




