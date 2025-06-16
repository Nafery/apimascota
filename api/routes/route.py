from flask import Blueprint, jsonify, request
from api.services.user_service import UserService
from api.services.pet_service import PetService
from api.services.attention_service import AttentionService

def register_routes(app, mysql):
    
    api_bp = Blueprint('api', __name__)

    user_service = UserService(mysql)
    pet_service = PetService(mysql)
    attention_service = AttentionService(mysql)

    # Ruta para obtener usuarios
    @api_bp.route('/users', methods=['GET'])
    def get_users():
        return jsonify(user_service.get_all_users())
    
    # Ruta para obtener mascotas
    @api_bp.route('/pets', methods=['GET'])
    def get_pets():
        return jsonify(pet_service.get_all_pets())
    
    # Ruta para obtener mascota por ID
    @api_bp.route('/pets/<int:id>', methods=['GET'])
    def get_pet_by_id(id):
        return jsonify(pet_service.get_mascota_by_id(id))
    
    # Ruta para iniciar sesión
    @api_bp.route('/login', methods=['POST'])
    def login_user():
        # Obtenemos los datos del cuerpo de la solicitud
        data = request.get_json()

        # Validamos que se envíen los campos requeridos
        correo = data.get('correo')
        password = data.get('password')

        if not correo or not password:
            return jsonify({"error": "Correo y contraseña son requeridos"})
        
        result = user_service.login_user(correo, password)

        if "error" in result:
            return jsonify(result), 401 # Error de autenticación
        return jsonify(result), 200 # Autenticación exitosa
    
    @api_bp.route('/pets/<int:pet_id>/attentions', methods=['GET'])
    def get_attentions_by_pet_id(pet_id):
        return jsonify(attention_service.get_attention_by_pet_id(pet_id))
    
    @api_bp.route('attentions', methods=['POST'])
    def create_sonculta():
        data = request.get_json()
        result = attention_service.create_attention

    app.register_blueprint(api_bp, url_prefix='/')