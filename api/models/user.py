import datetime
from .model_mixin import ModelMixin, db, app

class User(ModelMixin):
    """ User Model for storing user related details """
    __tablename__ = "users"

    _id = db.Column(db.String(255), primary_key=True, nullable=False)
    isActive = db.Column(db.Boolean, default=True)
    caterer_id = db.Column(db.Integer())
    role_id = db.Column(db.Integer(), nullable=False)
    registered_on = db.Column(db.DateTime, nullable=False, default=datetime.datetime.now())

    def __init__(self, _id, isActive, caterer_id, role_id, registered_on):
        self._id = _id
        self.isActive = isActive
        self.caterer_id = caterer_id
        self.role_id = role_id
        self.registered_on = registered_on