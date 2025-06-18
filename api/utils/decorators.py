import jwt
from functools import wraps
from flask import request, jsonify, current_app as app

# Decorador para verificar el token en las rutas protegidas
def token_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        token = None

        # Verificamos si el token está en el encabezado de la solicitud
        if 'Authorization' in request.headers:
            token = request.headers['Authorization'].split(" ")[1]  # Obtener el token del encabezado

        if not token:
            return jsonify({'message': 'Token is missing!'}), 403  # Si no hay token, respondemos con un error 403

        try:
            # Decodificamos el token usando la clave secreta para verificar su autenticidad
            data = jwt.decode(token, app.config['SECRET_KEY'], algorithms=["HS256"])
            current_user = data['user_id']  # Extraemos el user_id del payload del token
        except jwt.ExpiredSignatureError:
            return jsonify({'message': 'Token has expired!'}), 403  # Si el token ha expirado, respondemos con un error 403
        except jwt.InvalidTokenError:
            return jsonify({'message': 'Invalid token!'}), 403  # Si el token no es válido, respondemos con un error 403

        # Pasamos el user_id a la función decorada
        return f(current_user, *args, **kwargs)

    return decorated_function
