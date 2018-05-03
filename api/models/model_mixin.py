"""Module contains App Models, utility functions and Constants."""
from datetime import datetime
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.exc import SQLAlchemyError
from main import db, app


class ModelMixin(db.Model):
    """Base models.

    - Contains the serialize method to convert objects to a dictionary
    - Save and Delete utilities
    - Common field atrributes in the models
    """

    __abstract__ = True

    def serialize(self):
        """Map model objects to dict representation."""
        return {to_camel_case(column.name): getattr(self, column.name)
                for column in self.__table__.columns}

    def save(self):
        """Save an instance of the model to the database."""
        try:
            db.session.add(self)
            db.session.commit()
            return True
        except SQLAlchemyError:
            db.session.rollback()
            return False

    def __repr__(self):
        """REPL representation of model instance."""
        string_representation = self.__str__().replace("{", "(").replace(
            "}", ")").replace(":", "=")
        return f"{type(self).__name__}{string_representation}"

    def __str__(self):
        """String representation of model."""
        return str(self.serialize())

    def delete(self):
        """Delete an instance of the model from the database."""
        try:
            db.session.delete(self)
            db.session.commit()
            return True
        except SQLAlchemyError:
            db.session.rollback()
            return False
