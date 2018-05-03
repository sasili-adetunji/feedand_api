import datetime
import jwt
from api.helpers import hash_pwd
from .model_mixin import ModelMixin, db, app

class User(ModelMixin):
    """ User Model for storing user related details """
    __tablename__ = "users"

    user_id = db.Column(db.String(255), primary_key=True, nullable=False)
    email = db.Column(db.String(255), unique=True, nullable=False)
    password = db.Column(db.String(255), nullable=False)
    registered_on = db.Column(db.DateTime, nullable=False, default=datetime.datetime.now())

    def __init__(self, email, password, user_id):
        self.email = email
        self.user_id = user_id
        self.password = hash_pwd(password)

    def encode_auth_token(self, user_id):
        """
        Generates the Auth Token
        :return: string
        """
        try:
            payload = {
                'exp': datetime.datetime.utcnow() + datetime.timedelta(days=0, seconds=50000),
                'iat': datetime.datetime.utcnow(),
                'sub': user_id
            }
            return jwt.encode(payload, 'secret', algorithm='HS256')
        except Exception as e:
            return e

    @staticmethod
    def decode_auth_token(auth_token):
        """
        Validates the auth token
        :param auth_token:
        :return: integer|string
        """

        try:
            payload = jwt.decode(auth_token, 'secret', algorithms=['HS256'])
        except jwt.ExpiredSignatureError:
            return 'Signature expired. Please log in again.'
        except jwt.InvalidTokenError:
            return 'Invalid token. Please log in again.'