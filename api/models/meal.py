import datetime
from .model_mixin import ModelMixin, db

class Meal(ModelMixin):
    """Meal Model for storing the meals for the user"""
    __tablename__="Meal"

    _id = db.Column(db.String(255), primary_key=True, nullable=False)
    date = db.Column(db.DateTime, nullable=False, default=datetime.datetime.now())
    meal_period = db.Column(db.String(15), unique=True, nullable=False)
    username = db.Column(db.String(255), nullable=False)


    def __init__(self, _id, date, meal_period, username):
        self._id = _id
        self.date = date
        self. meal_period = meal_period
        self.username = username
