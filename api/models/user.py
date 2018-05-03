import datetime
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
