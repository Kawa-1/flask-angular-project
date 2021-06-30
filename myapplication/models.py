from os import name
from myapplication import db, recepies
from flask_login import UserMixin
from dataclasses import dataclass
# from werkzeug.security import generate_password_hash
# from werkzeug.security import check_password_hash

@dataclass
class Recepies(db.Model):
    id:int
    recipe:str
    user_id:int
    tags:str

    id = db.Column(db.Integer, primary_key=True)
    recipe = db.Column(db.String(400), nullable=False)
    user_id = db.Column(db.Integer, nullable=False)
    tags = db.Column(db.String(200), nullable=False)

    def __init__(self, recipe, user_id, tags) -> None:
        self.recipe = recipe
        self.user_id = user_id
        self.tags = tags

    #def __repr__(self) -> str:
    #    return f"Recepies('{self.id}', '{self.recipe}', '{self.user_id}', '{self.tags}')"

@dataclass
class Opinions(db.Model):
    id:int
    name_of_restaurant:str
    city_of_restaurant:str
    type_of_restaurant:str
    opinion:str
    user_id:int

    id = db.Column(db.Integer, primary_key=True)
    name_of_restaurant = db.Column(db.String(400), nullable=False)
    city_of_restaurant = db.Column(db.String(400), nullable=False)
    type_of_restaurant = db.Column(db.String(400), nullable=False)
    opinion = db.Column(db.String(2000), nullable=False)
    user_id = db.Column(db.Integer, nullable=False)

    def __init__(self, name_of_restaurant, city_of_restaurant, type_of_restaurant,\
        opinion, user_id) -> None:
        self.name_of_restaurant = name_of_restaurant
        self.city_of_restaurant = city_of_restaurant
        self.type_of_restaurant = type_of_restaurant
        self.opinion = opinion
        self.user_id = user_id
        
@dataclass
class Users(db.Model, UserMixin):
    id:int
    email:str
    first_name:str
    last_name:str
    username:str
    password:str
    
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100), nullable=False)
    first_name = db.Column(db.String(100), nullable=False)
    last_name = db.Column(db.String(100), nullable=False)
    username = db.Column(db.String(100), nullable=False)
    password = db.Column(db.String(500), nullable=False)

    def __init__(self, email, first_name, last_name, username, password) -> None:
        self.email = email
        self.first_name = first_name
        self.last_name = last_name
        self.username = username
        self.password = password

    def __repr__(self) -> str:
        #return f{id:'{self.id}',email:'{self.email}',first_name:'{self.first_name}',last_name:'{self.last_name}',username:'{self.username}',password:'{self.password}'}"
        return f'{self.id}:{self.email}'

