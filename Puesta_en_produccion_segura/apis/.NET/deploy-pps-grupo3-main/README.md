# 🐳 Puesta en Producción Segura — Grupo 3  
### Despliegue de arquitecturas web con Docker y APIs Laravel / .NET

---

## 📘 Introducción

Este proyecto forma parte de la asignatura **“Puesta en Producción Segura”**, perteneciente al *Curso de Especialización en Ciberseguridad en las Tecnologías de la Información (IES Rafael Alberti, Cádiz)*.

El trabajo consiste en el **despliegue seguro de arquitecturas web con Docker**, mediante la implementación de distintas **APIs REST básicas** usando varios frameworks.  
En este repositorio se incluyen las APIs desarrolladas por el **Grupo 3** correspondientes a los frameworks:

- **Laravel (PHP 8.3)**  
- **.NET 8 (Minimal API)**  

Cada API expone operaciones CRUD (`GET`, `POST`, `PUT`, `DELETE`) sobre un recurso de ejemplo:  
un conjunto de **20 productos almacenados en un archivo JSON** (`data.json`).

---

## ⚙️ Requisitos previos

Para ejecutar este proyecto se necesita:

- **Docker Desktop** (última versión)
- **Docker Compose v2 o superior**
- (Opcional) **curl** o **Postman** para probar las peticiones

> 💡 Compatible con **Windows 11 + WSL2 (Ubuntu 24.04)**

---

## 🧱 Estructura del proyecto

```plaintext
deploy-pps-grupo3/
├── docker-compose.yml          # Orquesta ambos contenedores
├── .gitignore
├── README.md
│
├── laravel-api/
│   ├── Dockerfile              # Configuración de Laravel en contenedor
│   ├── composer.json           # Dependencias PHP
│   ├── artisan
│   ├── data.json               # Datos de ejemplo (20 productos)
│   ├── routes/
│   │   └── api.php             # Definición de rutas /api/items
│   ├── app/
│   │   └── Http/
│   │       └── Controllers/
│   │           └── ItemController.php
│   └── ...
│
└── dotnet-api/
    ├── Dockerfile              # Imagen multi-stage de .NET 8
    ├── dotnet-api.csproj
    ├── Program.cs              # Lógica CRUD minimalista
    ├── data.json               # Datos de productos compartidos
    └── Properties/
        └── launchSettings.json



```
---

## 🚀 Cómo ejecutar el proyecto

### 1️⃣ Clonar el repositorio

```bash
git clone git@github.com:samSepioll01/deploy-pps-grupo3.git
cd deploy-pps-grupo3
````

### 2️⃣ Construir y levantar los contenedores
```bash
docker-compose up --build
```
### 3️⃣ Acceder a las APIs
| Framework | URL base                          | Descripción                |
| --------- | --------------------------------- | -------------------------- |
| Laravel   | `http://localhost:8000/api/items` | API CRUD en PHP/Laravel    |
| .NET 8    | `http://localhost:8001/api/items` | API CRUD minimalista en C# |

### 4️⃣ Detener los servicios
```bash
docker-compose down
```

### 🧪 Endpoints de la API

####   Endpoints comunes para ambas APIs

| Método   | Ruta              | Descripción                     |
| -------- | ----------------- | ------------------------------- |
| `GET`    | `/api/items`      | Devuelve todos los productos    |
| `GET`    | `/api/items/{id}` | Devuelve un producto concreto   |
| `POST`   | `/api/items`      | Crea un nuevo producto          |
| `PUT`    | `/api/items/{id}` | Actualiza un producto existente |
| `DELETE` | `/api/items/{id}` | Elimina un producto             |


### 🔧 Ejemplos de peticiones con curl

#### Crear un producto (POST)

```bash
curl -X POST http://localhost:8001/api/items \
     -H "Content-Type: application/json" \
     -d '{"nombre":"Tarta de queso casera","precio":3.80}'
```

#### Actualizar un producto (PUT)
```bash
curl -X PUT http://localhost:8001/api/items/5 \
     -H "Content-Type: application/json" \
     -d '{"nombre":"Croissant de mantequilla","precio":1.90}'
```

#### Eliminar un producto (DELETE)

```bash
curl -X DELETE http://localhost:8001/api/items/5
```

### 💡 Estos ejemplos usan la API .NET (puerto 8001), pero las mismas rutas funcionan en la API de Laravel (puerto 8000).

#### 🐘 Notas sobre la API de Laravel

* Basada en Laravel 11 sobre PHP 8.3.

* Usa el archivo data.json para almacenar y recuperar los datos.

* Incluye el controlador ItemController y rutas definidas en routes/api.php.

* Servidor levantado con php artisan serve --host=0.0.0.0 --port=8000.

* Imagen ligera sin vendor/ en el repositorio (se genera dentro del contenedor).

### ⚙️ Notas sobre la API de .NET 8

* Construida como Minimal API.

* Imagen multi-stage optimizada (compilación → ejecución).

* Lectura y escritura de datos desde data.json.

* Expuesta en el puerto 8001.

* CRUD completo (sin persistencia en base de datos).

### 🧩 Docker Compose

* Orquesta ambos contenedores en una red api-net.

* Puedes levantar servicios por separado:
```bash
      docker-compose up laravel-api
      docker-compose up dotnet-api
```

### 👨‍💻 Autores

Grupo 3 — Asignatura: Puesta en Producción Segura
IES Rafael Alberti (Cádiz) — Curso 2025

API Laravel — desarrollada en PHP (Laravel 11)

API .NET — desarrollada en C# (.NET 8)

### 🛡️ Licencia

Proyecto de carácter educativo.
Distribuido bajo la licencia MIT.



