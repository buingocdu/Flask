import email
from enum import unique
from tkinter.tix import Tree
from flask_sqlalchemy import SQLAlchemy
db= SQLAlchemy()
class User(db.Model):
    __tablename__="user"
    id= db.Column(db.Interger, primary_key=True)
    email= db.Column(db.Text, nullable=False, unique= True)
class Product(db.Model):
    __tablename__="product"
    id=db.Column(db.Interger, primary_key=True)
    name=db.Column(db.Text,nullable=False)