from flask_sqlalchemy import SQLAlchemy
from app import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    password_hash = db.Column(db.String(128))

    def __repr__(self):
        return '<User {}>'.format(self.username)


class Item(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    item_name = db.Column(db.String(64), index=True, unique=True)
    quantity = db.Column(db.Integer)
    unit = db.Column(db.String(64))

    # TODO: Use more general methods
    @property
    def serialize(self):
       return {
            'id'         : self.id,
            'item_name'  : self.item_name,
            'quantity'   : self.quantity,
            'unit'       : self.unit
       }

    def __repr(self):
        return '<Item {}>'.format(self.itemname)


class Receipe(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    receipe_name = db.Column(db.String(64), index=True, unique=True)
    ingredients = db.Column(db.PickleType)
    cooking_time = db.Column(db.Integer)
    optional_ingredients = db.Column(db.PickleType)

    # TODO: Use more general methods
    @property
    def serialize(self):
        return {
            'id'            : self.id,
            'receipe_name'  : self.receipe_name,
            'ingredients'   : self.ingredients,
            'cooking_time'  : self.cooking_time,
            'optional_ingredients': self.optional_ingredients
        }

    def __repr__(self):
        return '<Receipe {}>'.format(self.receipe_name)
