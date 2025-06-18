import jwt
import datetime
from api.models.user import User
import bcrypt
from flask import current_app as app  # Para acceder a la configuración de la clave secreta

class UserService:
    def __init__(self, mysql):
        self.mysql = mysql

    def get_user_by_id(self, user_id):
        cursor = self.mysql.connection.cursor()
        query = "SELECT id, nombre, correo, password, comuna FROM usuario WHERE id = %s"
        cursor.execute(query, (user_id,))
        user_data = cursor.fetchone()

        if user_data:
            return User(*user_data).to_dict()
        else:
            return {"error": "Usuario no encontrado"}

    def get_all_users(self):
        cursor = self.mysql.connection.cursor()
        query = "SELECT id, nombre, correo, password, comuna FROM usuario"
        cursor.execute(query)
        users_data = cursor.fetchall()
        users = [User(id=row[0], nombre=row[1], correo=row[2], password=row[3], comuna=row[4]).to_dict() for row in users_data]
        return users

    def login_user(self, correo, password):
        cursor = self.mysql.connection.cursor()
        query = "SELECT id, nombre, correo, password, comuna FROM usuario WHERE correo = %s"
        cursor.execute(query, (correo,))
        user_data = cursor.fetchone()

        if user_data:
            user = User(*user_data)

            # Verificar si la contraseña es correcta
            if bcrypt.checkpw(password.encode('utf-8'), user.password.encode('utf-8')):
                # Generar el token JWT
                payload = {
                    'user_id': user.id,  # El payload incluye el id del usuario
                    'exp': datetime.datetime.utcnow() + datetime.timedelta(hours=1)  # Expiración del token (1 hora)
                }
                
                # Clave secreta para firmar el token (Asegúrate de no exponerla en el código fuente)
                secret_key = app.config['SECRET_KEY']  # Usamos la clave secreta del archivo de configuración de Flask
                
                token = jwt.encode(payload, secret_key, algorithm='HS256')  # Generar el token

                # Devolver el token y los datos del usuario
                return {
                    'token': token,
                    'user': {
                        'id': user.id,
                        'nombre': user.nombre,
                        'correo': user.correo,
                        'comuna': user.comuna
                    }
                }
            else:
                return {"error": "Contraseña incorrecta"}
        else:
            return {"error": "Usuario no encontrado"}
