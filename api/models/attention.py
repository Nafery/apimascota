class Attention:
    def __init__(self, id, tipo, fecha, precio, mascota_id):
        self.id = id
        self.tipo = tipo
        self.fecha = fecha
        self.precio = precio
        self.mascota_id = mascota_id

    def to_dict(self):
        return {
            'id': self.id,
            'tipo': self.tipo,
            'fecha': self.fecha,
            'precio': self.precio,
            'mascota_id': self.mascota_id
        }