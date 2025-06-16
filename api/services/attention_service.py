from api.models.attention import Attention

class AttentionService:
    def __init__(self, mysql):
        self.mysql = mysql

    def get_attention_by_pet_id(self, pet_id):
        cursor = self.mysql.connection.cursor()
        query = "SELECT id, tipo, fecha, precio, mascota_id FROM consulta WHERE mascota_id = %s"
        cursor.execute(query, (pet_id,))
        attention_data = cursor.fetchall()
        attentions = [Attention(id=row[0], tipo=row[1], fecha=row[2], precio=row[3], mascota_id=row[4]).to_dict() for row in attention_data]

        return attentions  
    
    def create_attention(self, tipo, fecha, precio, mascota_id):
        cursor = self.mysql.connection.cursor()
        query = "INSERT INTO consulta (tipo, fecha, precio, mascota_id) VALUES (%s, %s, %s, %s)"
        try:
            cursor.execute(query, (tipo, fecha, precio, mascota_id))
            self.mysql.connection.commit()
            return {"message": "Consulta creada exitosamente"}
        except Exception as e:
            return {"error": str(e)}
        
    def delete_attention(self, attention_id):
        cursor = self.mysql.connection.cursor()
        query = "DELETE FROM consulta WHERE id = %s"
        try:
            cursor.execute(query, (attention_id,))
            self.mysql.connection.commit()
            if cursor.rowcount == 0:
                return {"error": "Consulta no encontrada"}
            return {"message": "Consulta eliminada exitosamente"}
        except Exception as e:
            return {"error": str(e)}