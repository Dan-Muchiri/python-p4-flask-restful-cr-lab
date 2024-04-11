from flask_sqlalchemy import SQLAlchemy
from sqlalchemy_serializer import SerializerMixin

db = SQLAlchemy()

class Plant(db.Model, SerializerMixin):
    __tablename__ = 'plants'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100)) 
    image = db.Column(db.String(255)) 
    price = db.Column(db.Numeric(10, 2))  # Assuming 10 digits in total with 2 digits after the decimal point for the price
