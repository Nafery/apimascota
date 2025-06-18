from flask import Blueprint, jsonify, request
from api.services.user_service import UserService
from api.services.pet_service import PetService
from api.services.attention_service import AttentionService
from api.utils.decorators import token_required  # Importar el decorador

def register_routes(app, mysql):
    
    api_bp = Blueprint('api', __name__)

    user_service = UserService(mysql)
    pet_service = PetService(mysql)
    attention_service = AttentionService(mysql)

    # Ruta para obtener usuarios
    @api_bp.route('/users', methods=['GET'])
    def get_users():
        return jsonify(user_service.get_all_users())
    
    # Ruta para obtener usuario
    @api_bp.route('/user/<user_id>', methods=['GET'])
    @token_required  # Aplicar el decorador para proteger esta ruta
    def get_user_by_id(current_user, user_id):
        # Validar que el `user_id` en la URL coincida con el `current_user` del token
        if int(user_id) != current_user:
            return jsonify({"error": "Unauthorized"}), 403
        return jsonify(user_service.get_user_by_id(user_id))
    
    # Ruta para obtener mascotas
    @api_bp.route('/pets', methods=['GET'])
    def get_pets():
        return jsonify(pet_service.get_all_pets())
    
    # Ruta para obtener mascota por ID
    @api_bp.route('/pets/<int:id>', methods=['GET'])
    @token_required  # Aplicar el decorador para proteger esta ruta
    def get_pet_by_id(current_user, id):
        return jsonify(pet_service.get_mascota_by_id(id))
    
    @api_bp.route('/user/pets/<int:user_id>', methods=['GET'])
    @token_required  # Aplicar el decorador para proteger esta ruta
    def get_pets_by_user_id(current_user, user_id):
        # Validar que el `user_id` en la URL coincida con el `current_user` del token
        if user_id != current_user:
            print(f"Error: El user_id de la URL ({user_id}) no coincide con el current_user del token ({current_user})")
            return jsonify({"error": "Unauthorized"}), 403  # Si no coinciden, se devuelve un 403
    
        # Si coinciden, obtenemos las mascotas del usuario
        return jsonify(pet_service.get_mascota_by_user_id(user_id))

    
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
    @token_required  # Aplicar el decorador para proteger esta ruta
    def get_attentions_by_pet_id(current_user, pet_id):
        print(f"Current User ID: {current_user}")  # Imprime el user_id desde el token
        print(f"Pet ID: {pet_id}")  # Imprime el pet_id desde la URL
        if current_user != pet_id:
            return jsonify({"error": "Unauthorized"}), 403
        return jsonify(attention_service.get_attention_by_pet_id(pet_id))

    
    @api_bp.route('/attentions', methods=['POST'])
    @token_required  # Aseguramos que el token sea validado antes de permitir la creación
    def create_consulta(current_user):
        data = request.get_json()  # Obtener los datos enviados en el cuerpo de la solicitud
        result = attention_service.create_attention(data)  # Llamamos al servicio para crear la consulta
        return jsonify(result)
    
    @api_bp.route('/attentionslist', methods=['GET'])
    def get_attentions_list():
        return jsonify(attention_service.get_all_attentions())


    app.register_blueprint(api_bp, url_prefix='/')
