
from flask import Flask, jsonify, request
import jwt
from datetime import datetime, timedelta
from functools import wraps

app = Flask(__name__)
app.config['SECRET_KEY'] = 'cambia_esto_por_un_secreto_largo_y_unico'

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
        "exp": datetime.utcnow() + timedelta(minutes=30)  # token expira en 30 min
    }
    token = jwt.encode(payload, app.config['SECRET_KEY'], algorithm="HS256")
    # PyJWT >= 2 ya devuelve str; si devuelve bytes, haz .decode("utf-8")
    return token

def verificar_token(token):
    # Lanza excepciones si el token no es válido o expiró
    data = jwt.decode(token, app.config['SECRET_KEY'], algorithms=["HS256"])
    return data  # contiene sub, iat, exp

def token_requerido(f):
    @wraps(f)
    def wrapper(*args, **kwargs):
        auth = request.headers.get("Authorization", "")
        # Esperado: "Bearer <token>"
        if not auth.startswith("Bearer "):
            return jsonify({"error": "Token faltante o malformado"}), 401
        token = auth.split(" ", 1)[1].strip()
        try:
            claims = verificar_token(token)
            # Opcional: puedes guardar claims en g si lo necesitas
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
