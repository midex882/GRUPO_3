from flask import Flask, jsonify, request
import jwt
import urllib.request
import urllib.parse
import json
from datetime import datetime, timedelta
from functools import wraps
import os

app = Flask(__name__)
app.config['SECRET_KEY'] = 'cambia_esto_por_un_secreto_largo_y_unico'

# Configuración OAuth GitHub
GITHUB_CLIENT_ID = os.getenv("GITHUB_CLIENT_ID", "fjortegan")
GITHUB_CLIENT_SECRET = os.getenv("GITHUB_CLIENT_SECRET", "3cba795bf7a2f9ce6bcb9aa8220b18cc88b93240")

# --------------------
# Datos en memoria
# --------------------
nombres = []
ultimo_id = 0

# -------------------
# Login básico sin BD
# -------------------
USUARIO = "admin"
PASSWORD = "1234"

def generar_token(username):
    payload = {
        "sub": username,
        "iat": datetime.utcnow(),
        "exp": datetime.utcnow() + timedelta(minutes=30)
    }
    token = jwt.encode(payload, app.config['SECRET_KEY'], algorithm="HS256")
    return token

def verificar_token(token):
    data = jwt.decode(token, app.config['SECRET_KEY'], algorithms=["HS256"])
    return data

def token_requerido(f):
    @wraps(f)
    def wrapper(*args, **kwargs):
        auth = request.headers.get("Authorization", "")
        if not auth.startswith("Bearer "):
            return jsonify({"error": "Token faltante o malformado"}), 401
        token = auth.split(" ", 1)[1].strip()
        try:
            claims = verificar_token(token)
        except jwt.ExpiredSignatureError:
            return jsonify({"error": "Token expirado"}), 401
        except jwt.InvalidTokenError:
            return jsonify({"error": "Token inválido"}), 401
        return f(*args, **kwargs)
    return wrapper

@app.route('/login', methods=['POST'])
def login():
    data = request.get_json(silent=True) or {}
    username = data.get("username")
    password = data.get("password")
    if username == USUARIO and password == PASSWORD:
        token = generar_token(username)
        return jsonify({"message": "Login correcto", "token": token}), 200
    return jsonify({"message": "Credenciales inválidas"}), 401

# ------------------
# OAUTH GITHUB con urllib
# ------------------
@app.route('/github_oauth', methods=['POST'])
def github_oauth():
    """
    Endpoint para autenticación con GitHub OAuth usando urllib (sin requests)
    """
    data = request.get_json(silent=True) or {}
    code = data.get("code")
    
    if not code:
        return jsonify({"error": "Falta code"}), 400
    
    try:
        # 1. Intercambiar el code por un access_token de GitHub
        token_url = "https://github.com/login/oauth/access_token"
        
        # Preparar los datos para enviar
        payload = {
            "client_id": GITHUB_CLIENT_ID,
            "client_secret": GITHUB_CLIENT_SECRET,
            "code": code
        }
        
        # Convertir el payload a JSON
        json_data = json.dumps(payload).encode('utf-8')
        
        # Crear la petición POST
        token_request = urllib.request.Request(
            token_url,
            data=json_data,
            headers={
                "Accept": "application/json",
                "Content-Type": "application/json"
            },
            method='POST'
        )
        
        # Hacer la petición
        with urllib.request.urlopen(token_request) as response:
            token_response = json.loads(response.read().decode('utf-8'))
        
        # Verificar si obtuvimos el token
        if "access_token" not in token_response:
            error_msg = token_response.get("error_description", "No se pudo obtener token de GitHub")
            return jsonify({"error": error_msg}), 400
        
        github_access_token = token_response["access_token"]
        
        # 2. Obtener información del usuario de GitHub
        user_url = "https://api.github.com/user"
        
        user_request = urllib.request.Request(
            user_url,
            headers={
                "Authorization": f"Bearer {github_access_token}",
                "Accept": "application/json"
            }
        )
        
        with urllib.request.urlopen(user_request) as user_response:
            user_info = json.loads(user_response.read().decode('utf-8'))
        
        if "login" not in user_info:
            return jsonify({"error": "No se pudo obtener información del usuario"}), 400
        
        github_username = user_info["login"]
        
        # 3. Generar tu propio JWT para ese usuario
        jwt_token = generar_token(github_username)
        
        return jsonify({
            "jwt": jwt_token,
            "githubUser": github_username,
            "message": "Login con GitHub exitoso"
        }), 200
        
    except urllib.error.HTTPError as e:
        error_body = e.read().decode('utf-8')
        return jsonify({"error": f"Error HTTP {e.code}: {error_body}"}), 500
    except urllib.error.URLError as e:
        return jsonify({"error": f"Error de conexión: {str(e.reason)}"}), 500
    except Exception as e:
        return jsonify({"error": f"Error interno: {str(e)}"}), 500

# ------------------
# CRUD DE NOMBRES (protegido)
# ------------------

@app.route('/nombres/<string:nombre>', methods=['POST'])
@token_requerido
def crear_nombre(nombre):
    global ultimo_id, nombres
    if not nombre:
        return jsonify({'error': 'Nombre es requerido en la URL'}), 400
    ultimo_id += 1
    nuevo = {"id": ultimo_id, "nombre": nombre}
    nombres.append(nuevo)
    return jsonify(nuevo), 201

@app.route('/nombres', methods=['GET'])
@token_requerido
def listar_nombres():
    return jsonify(nombres)

@app.route('/nombres/<int:id>', methods=['GET'])
@token_requerido
def obtener_nombre(id):
    nombre = next((n for n in nombres if n['id'] == id), None)
    if nombre is None:
        return jsonify({'error': 'No encontrado'}), 404
    return jsonify(nombre)

@app.route('/nombres/<int:id>', methods=['PUT'])
@token_requerido
def actualizar_nombre(id):
    nombre = next((n for n in nombres if n['id'] == id), None)
    if nombre is None:
        return jsonify({'error': 'No encontrado'}), 404
    data = request.get_json(silent=True) or {}
    nuevo_nombre = data.get('nombre')
    if not nuevo_nombre:
        return jsonify({'error': 'campo nombre es requerido en JSON'}), 400
    nombre['nombre'] = nuevo_nombre
    return jsonify(nombre)

@app.route('/nombres/<int:id>', methods=['DELETE'])
@token_requerido
def eliminar_nombre(id):
    global nombres
    original_len = len(nombres)
    nombres = [n for n in nombres if n['id'] != id]
    if len(nombres) == original_len:
        return jsonify({'error': 'No encontrado'}), 404
    return jsonify({'mensaje': 'Nombre eliminado'})

# ------------------
# Ejecutar servidor
# ------------------
if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)
