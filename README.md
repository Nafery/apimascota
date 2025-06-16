# 🛠️ Mascota Feliz API (Arquitectura en capas)

API RESTful para gestión de consultas, usuarios para inicio de sesión, mascotas de cada usuario.

## 🚀 Tecnologías

- Python 3
- Flask
- MySQL

## 📁 Estructura del proyecto
```plaintext
apimascota/
├── app.py
├── README.md
└── api/
    ├── db/
    ├── models/
    ├── routes/
    └── services/
```

## 🧱 Arquitectura en capas

La API sigue una arquitectura en capas para mantener un código organizado, reutilizable y escalable. Las capas son:

- **`routes/`**: Define las rutas de la API y maneja las solicitudes.
- **`models/`**: Define los modelos de datos.
- **`services/`**: Contiene la lógica del negocio y maneja el flujo de datos entre los modelos y las rutas.
- **`db/`**: Puede contener configuraciones adicionales para la conexión a la base de datos.

Trabajar la API con este enfoque facilita el mantenimiento del proyecto y realizar pruebas o cambios en una capa sin afectar las otras.

## 🔧 Instalación y ejecución

```bash
git clone https://github.com/Nafery/apimascota
cd apimascota
python3 app.py
```

## 🛠️ Configuración de la base de datos
### 1.- Crear una base de datos

Abre la terminal o línea de comandos y ejecuta el siguiente comando:

```bash
mysql -u root -p
```

Luego dentro de tu editor de MySQL de preferencia ejecuta el siguiente código:
```bash
CREATE DATABASE ferramas;
EXIT;
```

### 2.- Importar el archivo de la base de datos mascota.sql

Asegurándote de tener el archivo mascota.sql en la carpeta del repositorio, ejecuta:
```bash
mysql -u root -p ferramas <ferramas.sql
```

### 3.- Configurar la conexión en app.py

En el archivo app.py verifica las siguientes lineas de código
```python
app.config['MYSQL_HOST'] = 'localhost' 
app.config['MYSQL_USER'] = 'root' #Tu usuario mysql propio
app.config['MYSQL_PASSWORD'] = '' #Contraseña del usuario
app.config['MYSQL_DB'] = 'mascota'
```

## 🌐 Endpoints de la API

### Usuarios

| Método | Ruta        | Descripción                |
| ------ | ----------- | -------------------------- |
| GET    | `/users`    | Obtener todos los usuarios |

### Consultas

| Método | Ruta                            | Descripción                         |
| ------ | ------------------------------- | ----------------------------------- |
| GET    | `/pets/<int:pet_id>/attentions` | Obtener consultas por id de mascota |

### Mascotas

| Método | Ruta     | Descripción                |
| ------ | -------- | -------------------------- |
| GET    | `/pets`  | Obtener todas las mascotas |