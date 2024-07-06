
from sqlalchemy import MetaData

from flask_sqlalchemy import SQLAlchemy

#import datetime
from datetime import datetime

from sqlalchemy_serializer import SerializerMixin


metadata = MetaData(naming_convention={
    "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
})

db = SQLAlchemy(metadata=metadata)

class Message(db.Model, SerializerMixin):

    __tablename__ = 'messages'

    id = db.Column(db.Integer, primary_key=True)
    #Add the body, username, created_at, and updated_at fields

    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    username = db.Column(db.String, nullable=False)

    body = db.Column(db.String, nullable=False)

    created_at = db.Column(db.DateTime, default=datetime.utcnow)


    #Define a to_dict method to serialize the model
    def to_dict(self):
        return {
            'id': self.id,
            'body': self.body,
            'username': self.username,
            'created_at': self.created_at.isoformat(),
            'updated_at': self.updated_at.isoformat(),
        }

