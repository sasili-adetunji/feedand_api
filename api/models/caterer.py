import datetime
from .model_mixin import ModelMixin, db

class Caterer(ModelMixin):
    """Caterer Model for storing caterers hired"""
    __tablename__='Caterer'

    caterer_id = db.Column(db.String(255), primary_key=True, nullable=False)
    business_name = db.Column(db.String(250), nullable=False)
    contact_person = db.Column(db.String(255), nullable=False)
    email = db.Column(db.String(255), nullable=False)
    phone_number = db.Column(db.String(255), nullable=False)
    username = db.Column(db.String(255), nullable=False)
    password = db.Column(db.String(255), nullable=False)
    engagement_start= db.Column(db.DateTime, nullable=False, default=datetime.datetime.now())
    engagement_end = db.Column(db.DateTime, nullable = True)
    isActive = db.Column(db.Boolean, default=True)
    isCurrent = db.Column(db.Boolean, default=True)
    caterer_menu = db.relationship('Menu', backref='caterer', lazy='dynamic')
    caterer_log_caterer = db.relationship('CatererLog', backref='caterer', lazy='dynamic')

<<<<<<< HEAD
    def __init__(self, _id, caterer_name, description, engagement_start, engagement_end, isActive, isCurrent, caterer_menu, caterer_log_caterer):
        self._id = _id
        self.caterer_name = caterer_name
        self.description = description
        self.engagement_start = engagement_start
        self.engagement_end = engagement_end
        self.caterer_menu = caterer_menu
        self.isActive = isActive
        self.isCurrent = isCurrent
        self.caterer_log_caterer = caterer_log_caterer
=======
    def __init__(self, caterer_id, business_name, contact_person, email, phone_number, username, password):
        self.caterer_id = caterer_id
        self.business_name = business_name
        self.contact_person = contact_person
        self.email = email
        self.phone_number = phone_number
        self.username = username
        self.password = password
>>>>>>> add caterer endpoints
