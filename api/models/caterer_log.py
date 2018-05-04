import datetime
from .model_mixin import ModelMixin,db 

class CatererLog(ModelMixin):
    """CatererLog Model for storing caterers log"""
    __tablename__="CatererLog"

    _id = db.Column(db.String(255), primary_key=True, nullable=False)
    caterer_id = db.Column(db.String(), db.ForeignKey('Caterer._id'))
    month = db.Column(db.String(15), primary_key=True, nullable=False)
    isCompleted = db.Column(db.Boolean, default=True)
    wasTerminated = db.Column(db.Boolean, default=True)
    startDate = db.Column(db.DateTime, nullable=False)
    endDate = db.Column(db.DateTime, nullable=True)

    def __init__(self, _id, caterer_id, month, isCompleted, wasTerminated, startDate, endDate):
        self._id = _id
        self.caterer_id = caterer_id
        self.month = month
        self.isCompleted = isCompleted
        self.wasTerminated = wasTerminated
        self.startDate = startDate
        self.endDate = endDate
