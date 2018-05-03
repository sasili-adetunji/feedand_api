from .model_mixin import ModelMixin, db

class Category(ModelMixin):
    """Category Model for storing meal course """
    __tablename__="Category"

    _id = db.Column(db.String(255), primary_key=True, nullable=False)
    name = db.Column(db.String(255), unique=True, nullable=False)
    isActive = db.Column(db.Boolean, default=True)


    def __init__(self, _id, name, isActive):
        self._id = _id
        self.name = name
        self.isActive = isActive
