from flask import request, make_response, jsonify
from functools import wraps
from main import app, bcrypt


def hash_pwd(password):
    return bcrypt.generate_password_hash(password, app.config.get('BCRYPT_LOG_ROUNDS')).decode()

def validate_type(item, input_type):
    return type(item) is input_type

def validate_request(*expected_args):
    """ This method validates the Request payload.

    Args
        expected_args(tuple): where i = 0 is type and i > 0 is argument to be
                            validated

    Returns
      f(*args, **kwargs)
    """

    def real_validate_request(f):
        type_map = {"str": "string",
                    "list": "list",
                    "dict": "dictionary",
                    "int": "integer"}
        @wraps(f)
        def decorated(*args, **kwargs):
            if not request.json:
                responseObject= {
                        "status": "fail",
                        "message": "Request must be a valid JSON"
                    }
                return make_response(jsonify(responseObject)), 400
            payload = request.get_json()
            if payload:
                for values in expected_args:
                    for value in values:
                        if value == values[0]:
                            continue
                        if value not in payload or ((
                                values[0] != dict and not payload[value])):
                            responseObject= {
                                "status": "fail",
                                "message": value + " is required"
                            }
                            return make_response(jsonify(responseObject)), 400
                        elif not validate_type(payload[value], values[0]) or not payload[value].strip(
                            ' '):
                            responseObject = {
                                "status": "fail",
                                "message": value + " must be a valid " +
                                         type_map[ values[0].__name__]
                                }
                            return make_response(jsonify(responseObject)), 400
            return f(*args, **kwargs)
        return decorated
    return real_validate_request
