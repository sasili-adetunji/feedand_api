import datetime
from .model_mixin import ModelMixin, db

class Caterer(ModelMixin):
    """Caterer Model for storing caterers hired"""
    __tablename__='Caterer'

    _id = db.Column(db.String(255), primary_key=True, nullable=False)
    caterer_name = db.Column(db.String(250), nullable=False)
    description = db.Column(db.String(255), nullable=False)
    engagement_start= db.Column(db.DateTime, nullable=False, default=datetime.datetime.now())
    engagement_end = db.Column(db.DateTime, nullable = True)
    isActive = db.Column(db.Boolean, default=True)
    isCurrent = db.Column(db.Boolean, default=True)
    caterer_menu = db.relationship('Menu', backref='caterer', lazy='dynamic')

    def __init__(self, _id, caterer_name, description, engagement_start, engagement_end, isActive, isCurrent):
        self._id = _id
        self.caterer_name = caterer_name
        self.description = description
        self.engagement_start = engagement_start
        self.engagement_end = engagement_end
        self.caterer_menu = caterer_menu
        self.isActive = isActive
        self.isCurrent = isCurrent
