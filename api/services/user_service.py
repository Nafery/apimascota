from api.models.user import User
import bcrypt

class UserService:
    def __init__(self, mysql):
        self.mysql = mysql

    def get_all_users(self):
        cursor = self.mysql.connection.cursor()
        query = "SELECT id, nombre, correo, password, comuna FROM usuario"
        cursor.execute(query)
        users_data = cursor.fetchall()
        users = [User(id=row[0], nombre=row[1], correo=row[2], password=row[3], comuna=row[4]).to_dict() for row in users_data]
        return users

    def login_user(self, correo, password):
        cursor = self.mysql.connection.cursor()
        query = "SELECT id, nombre, correo, password, comuna FROM user WHERE correo = %s"
        cursor.execute(query, (correo,))
        user_data = cursor.fetchone()

        if user_data:
            user = User(*user_data)

            if bcrypt.checkpw(password.encode('utf-8'), user.password.encode('utf-8')):
                return {
                    'id': user.id,
                    'nombre': user.nombre,
                    'correo': user.correo,
                    'comuna': user.comuna
                }
            else:
                return {"error": "Contraseña incorrecta"}
        else:
            return {"error": "Usuario no encontrado"}