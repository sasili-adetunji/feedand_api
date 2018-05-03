from flask import jsonify, make_response

def response_object(status, message, status_code):
    responseObject = {
              'status': status,
              'message': message
          }
    return make_response(jsonify(responseObject)), status_code