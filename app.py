from flask import Flask, jsonify
from api.db.database import init_db
from api.routes.route import register_routes

app = Flask(__name__)

# Configuración de la base de datos
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'mascota'

mysql = init_db(app)

register_routes(app, mysql)

if __name__ == '__main__':
    app.run(debug=True, port=5000)