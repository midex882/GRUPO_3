const express = require('express');
const app = express();
const fs = require('fs');
const jwt = require('jsonwebtoken');
const OAuth2Server = require('@node-oauth/oauth2-server');
const Request = OAuth2Server.Request;
const Response = OAuth2Server.Response;
require('dotenv').config();

app.use(express.json());
app.use(express.urlencoded({ extended: true }));

const data_path = "./datos.json";

const oauthModel = require('./oauth-model');
const oauth = new OAuth2Server({
  model: oauthModel,
  accessTokenLifetime: 3600, // 1 hour
  allowBearerTokensInQueryString: true
});

const users = [
  { id: 1, username: 'user', password: 'password' },
  { id: 2, username: 'admin', password: 'admin123' }
];

function readData() {
  const data = fs.readFileSync(data_path, 'utf-8');
  return JSON.parse(data);
}

function writeData(data) {
  fs.writeFileSync(data_path, JSON.stringify(data, null, 2));
}


function authenticateJWT(req, res, next) {
  const authHeader = req.headers.authorization;
  
  if (!authHeader) {
    return res.status(401).json({ error: 'No se proporcionó token de autenticación' });
  }
  
  const token = authHeader.split(' ')[1];
  
  if (!token) {
    return res.status(401).json({ error: 'Token inválido' });
  }
  
  try {
    const decoded = jwt.verify(token, process.env.JWT_SECRET);
    req.user = decoded;
    next();
  } catch (err) {
    return res.status(403).json({ error: 'Token expirado o inválido' });
  }
}

app.post('/login', (req, res) => {
  const { username, password } = req.body;
  
  if (!username || !password) {
    return res.status(400).json({ error: 'Debes proporcionar username y password' });
  }
  
  const user = users.find(u => u.username === username && u.password === password);
  
  if (!user) {
    return res.status(401).json({ error: 'Credenciales inválidas' });
  }
  
  const payload = {
    id: user.id,
    username: user.username
  };
  
  const token = jwt.sign(payload, process.env.JWT_SECRET, { expiresIn: '1h' });
  
  res.json({ 
    mensaje: 'Login exitoso con JWT',
    token: token,
    usuario: user.username,
    tipo: 'JWT'
  });
});

app.post('/oauth/token', async (req, res) => {
  const request = new Request(req);
  const response = new Response(res);
  
  try {
    const token = await oauth.token(request, response);
    res.json({
      access_token: token.accessToken,
      token_type: 'Bearer',
      expires_in: 3600,
      tipo: 'OAuth 2.0'
    });
  } catch (err) {
    res.status(err.code || 500).json({
      error: err.name,
      error_description: err.message
    });
  }
});

async function authenticateOAuth(req, res, next) {
  const request = new Request(req);
  const response = new Response(res);
  
  try {
    await oauth.authenticate(request, response);
    next();
  } catch (err) {
    res.status(err.code || 500).json({
      error: 'OAuth authentication failed',
      message: err.message
    });
  }
}

app.get('/saludo', (req, res) => {
  res.json({ mensaje: '(con tono de disnay channel) Hola, soy Node.js y estás viendo la inevitable autodestrucción de nuestra especie!' });
});

app.get('/', (req, res) => {
  res.json({ mensaje: 'Hola. Funciono y no estás muy seguro de cómo, a que no?' })
});


app.get('/nombres', authenticateOAuth, (req, res) => {
  const nombres = readData();
  res.json(nombres);
});

app.get('/nombres/:nombre', authenticateOAuth, (req, res) => {
  const nombre = req.params.nombre;

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

app.put('/nombres/:id', authenticateOAuth, (req, res) => {
  const nombres = readData();
  const id = parseInt(req.params.id);
  const index = nombres.findIndex(p => p.id === id);

  if (index === -1) return res.status(404).json({ error: 'Nombre no encontrado' });

  nombres[index].nombre = req.body.nombre;
  writeData(nombres);
  res.json(nombres[index]);
});

app.delete('/nombres/:id', authenticateOAuth, (req, res) => {
  const nombres = readData();
  const id = parseInt(req.params.id);
  const nuevos = nombres.filter(p => p.id !== id);

  if (nombres.length === nuevos.length)
    return res.status(404).json({ error: 'Nombre no encontrado' });

  writeData(nuevos);
  res.status(204).send();
});

const PORT = process.env.PORT || 3000;
app.listen(PORT, () => {
  console.log(`Servidor escuchando en http://localhost:${PORT}`);
  console.log(`Endpoints disponibles:`);
  console.log(`  - POST /login (JWT)`);
  console.log(`  - POST /oauth/token (OAuth 2.0)`);
  console.log(`  - GET /nombres (OAuth protegido)`);
});
