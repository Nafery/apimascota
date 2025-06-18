from flask import Flask, jsonify
from flask_cors import CORS
from dotenv import load_dotenv
from api.db.database import init_db
from api.routes.route import register_routes
import os

load_dotenv()

app = Flask(__name__)

app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')

# Habilitar CORS solo para el origen específico de tu frontend
CORS(app, origins="http://localhost:5173")  # Permite solicitudes solo desde el frontend

# Configuración de la base de datos
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'mascota'

mysql = init_db(app)

register_routes(app, mysql)

if __name__ == '__main__':
    app.run(debug=True, port=5000)
