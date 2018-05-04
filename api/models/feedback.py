from .model_mixin import ModelMixin, db
import datetime

class FeedBack(ModelMixin):
    """MenuDetails Model for storing all the details in the menu """
    __tablename__ = "FeedBack"

    _id = db.Column(db.String(255), primary_key=True, nullable=False)
    meal_id = db.Column(db.String(), db.ForeignKey("Meal._id"))
    comment = db.Column(db.String(255), nullable=False)
    comment_by = db.Column(db.String(255), nullable=False)
    rating = db.Column(db.Integer, nullable=False)
    date = db.Column(db.DateTime, nullable=False, default=datetime.datetime.now())

    
    def __init__(self, _id, meal_id, comment, comment_by, rating, date):
        self._id = _id
        self.meal_id = meal_id
        self.comment = comment
        self.comment_by = comment_by
        self.rating = rating
        self.date = date
