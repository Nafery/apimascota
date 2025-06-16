class Pet:
    def __init__(self, id, nombre, raza, tipo, edad, sexo, usuario_id):
        self.id = id
        self.nombre = nombre
        self.raza = raza
        self.tipo = tipo
        self.edad = edad
        self.sexo = sexo
        self.usuario_id = usuario_id

    def to_dict(self):
        return {
            'id': self.id,
            'nombre': self.nombre,
            'raza': self.raza,
            'tipo': self.tipo,
            'edad': self.edad,
            'sexo': self.sexo,
            'usuario_id': self.usuario_id
        }