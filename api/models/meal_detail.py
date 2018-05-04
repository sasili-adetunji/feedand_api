from .model_mixin import ModelMixin, db

class MealDetail(ModelMixin):
    """MealDetail Model for storing the meal detail of a user"""
    __tablename__="MealDetail"

    _id = db.Column(db.String(255), primary_key=True, nullable=False)
    meal_id = db.Column(db.String(), db.ForeignKey('Meal._id'))
    menu_detail_id = db.Column(db.String(), db.ForeignKey('MenuDetail._id'))

    def __init__(self, _id, meal_id, menu_detail_id):
        self._id = _id
        self.meal_id = meal_id
        self.menu_detail_id = menu_detail_id
