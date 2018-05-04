import datetime
from .model_mixin import ModelMixin, db

class Menu(ModelMixin):
    """ Menu Model for storing food in menu """
    __tablename__='Menu'

    _id = db.Column(db.String(255), primary_key=True, nullable=False)
    meal_period = db.Column(db.String(15), unique=True, nullable=False)
<<<<<<< HEAD
    caterer_id = db.Column(db.String(), db.ForeignKey('Caterer._id'))
    date = db.Column(db.DateTime, nullable=False)
=======
    caterer_id = db.Column(db.String(), db.ForeignKey('Caterer.caterer_id'))
    date = db.Column(db.DateTime, nullable=False, default=datetime.datetime.now())
>>>>>>> add caterer endpoints

    def __init__(self, _id, meal_period, caterer_id, date):
        self._id = _id
        self.meal_period = meal_period
        self.caterer_id = caterer_id
        self.date = date
