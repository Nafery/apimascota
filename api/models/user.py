import bcrypt

class User:
    def __init__(self, id, nombre, correo, password, comuna):
        self.id = id
        self.nombre = nombre
        self.correo = correo
        self.password = self.hash_password(password) #Ciframos la contraseña
        self.comuna = comuna

    def hash_password (self, password):
        salt = bcrypt.gensalt()
        hashed_password = bcrypt.hashpw(password.encode('utf-8'), salt)
        return hashed_password.decode('utf-8')

    def to_dict(self):
        return {
            'id': self.id,
            'nombre': self.nombre,
            'correo': self.correo,
            'comuna': self.comuna
        }