from .model_mixin import ModelMixin, db

class MenuDetail(ModelMixin):
    """MenuDetails Model for storing all the details in the menu """
    __tablename__ = "MenuDetail"

    _id = db.Column(db.String(255), primary_key=True, nullable=False)
    menu_id = db.Column(db.String(), db.ForeignKey("Menu._id"))
    menu_name = db.Column(db.String(255), unique=True, nullable=False)
    category_id = db.Column(db.String(255), db.ForeignKey("Category._id"))

    menu_detail_meal = db.relationship('MealDetail', backref='menu_detail', lazy='dynamic')

    def __init__(self, _id, menu_id, category_id, menu_name, menu_detail_meal):
        self._id = _id
        self.menu_id = menu_id
        self.menu_name = menu_name
        self.category_id = category_id
        self.menu_detail_meal = menu_detail_meal
