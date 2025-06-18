from api.models.pet import Pet

class PetService:
    def __init__(self, mysql):
        self.mysql = mysql

    def get_all_pets(self):
        cursor = self.mysql.connection.cursor()
        query = "SELECT id, nombre, raza, tipo, edad, sexo, usuario_id FROM mascota"
        cursor.execute(query)
        pets_data = cursor.fetchall()
        pets = [Pet(id=row[0], nombre=row[1], raza=row[2], tipo=row[3], edad=row[4], sexo=row[5], usuario_id=row[6]).to_dict() for row in pets_data]
        return pets
    
    def get_mascota_by_id(self, id):
        cursor = self.mysql.connection.cursor()
        query = "SELECT id, nombre, raza, tipo, edad, sexo, usuario_id FROM mascota WHERE id = %s"
        cursor.execute(query, (id,))
        pet_data = cursor.fetchone()
        
        if pet_data:
            return Pet(
                id=pet_data[0],
                nombre=pet_data[1],
                raza=pet_data[2],
                tipo=pet_data[3],
                edad=pet_data[4],
                sexo=pet_data[5],
                usuario_id=pet_data[6]
            ).to_dict()
        else:
            return {"error": "Mascota no encontrada"}
        
    def get_mascota_by_user_id(self, user_id):
        cursor = self.mysql.connection.cursor()
        query = """
                    SELECT m.id, m.nombre, m.raza, m.tipo, m.edad, m.sexo, m.usuario_id, u.nombre 
                    FROM mascota m JOIN usuario u ON m.usuario_id = u.id 
                    WHERE m.usuario_id = %s
                """
        cursor.execute(query, (user_id,))
        pets_data = cursor.fetchall()
        if pets_data:
            pets = [
                Pet(
                    id=row[0],
                    nombre=row[1],
                    raza=row[2],
                    tipo=row[3],
                    edad=row[4],
                    sexo=row[5],
                    usuario_id=row[6],
                ).to_dict() | {'usuario_nombre': row[7]}
                for row in pets_data
            ]
            return pets
        else:
            return {"error": "No se encontraron mascotas para este usuario"}