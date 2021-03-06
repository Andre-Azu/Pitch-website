# where the databases will be created
from . import db

#gives users ability to log in
from flask_login import UserMixin

#allows for sql achemy to take care of the date thing 
from sqlalchemy.sql import func

# db.model ensures that a blueprint is being followed
class Pitch(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    data=db.Column(db.String(10000))
    date=db.Column(db.DateTime(timezone=True),default=func.now())
    #How to link the pitches to the users, therefore a relationship has to be created via a forein key
    user_id=db.Column(db.Integer,db.ForeignKey('user.id'))



class User(db.Model, UserMixin):
    id=db.Column(db.Integer, primary_key=True)
    email=db.Column(db.String(150),unique=True)
    password=db.Column(db.String(150))
    first_name=db.Column(db.String(150))
    pitchs=db.relationship('Pitch')

