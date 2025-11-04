from flask import Flask, jsonify, request

app = Flask(__name__)

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

@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    username = data.get("username")
    password = data.get("password")

    if username == USUARIO and password == PASSWORD:
        return jsonify({"message": "Login correcto"}), 200
    else:
        return jsonify({"message": "Credenciales inválidas"}), 401
    
# ------------------
# CRUD DE NOMBRES
# ------------------

# Crear nombre pasando el nombre en la URL
@app.route('/nombres/<string:nombre>', methods=['POST'])
def crear_nombre(nombre):
    global ultimo_id
    if not nombre:
        return jsonify({'error': 'Nombre es requerido en la URL'}), 400
    ultimo_id += 1
    nuevo = {"id": ultimo_id, "nombre": nombre}
    nombres.append(nuevo)
    return jsonify(nuevo), 201

# Listar todos los nombres
@app.route('/nombres', methods=['GET'])
def listar_nombres():
    return jsonify(nombres)

# Obtener nombre por id
@app.route('/nombres/<int:id>', methods=['GET'])
def obtener_nombre(id):
    nombre = next((n for n in nombres if n['id'] == id), None)
    if nombre is None:
        return jsonify({'error': 'No encontrado'}), 404
    return jsonify(nombre)

# Actualizar nombre por id (nombre nuevo en JSON)
@app.route('/nombres/<int:id>', methods=['PUT'])
def actualizar_nombre(id):
    nombre = next((n for n in nombres if n['id'] == id), None)
    if nombre is None:
        return jsonify({'error': 'No encontrado'}), 404
    data = request.get_json()
    nuevo_nombre = data.get('nombre')
    if not nuevo_nombre:
        return jsonify({'error': 'campo nombre es requerido en JSON'}), 400
    nombre['nombre'] = nuevo_nombre
    return jsonify(nombre)

# Eliminar por id
@app.route('/nombres/<int:id>', methods=['DELETE'])
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
