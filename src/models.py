import os
import sys
import datetime
from sqlalchemy import Column, ForeignKey, Integer, String,DateTime
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class Favorite(Base):
    __tablename__ = 'favorite'
    id= Column(Integer,primary_key=True)
    user_id=Column(Integer,ForeignKey('user.id'))
    fav_planet=Column(String,ForeignKey('planet.name'))
    fav_character=Column(String,ForeignKey('character.name'))
class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    Email=Column(String(250),unique=True)
    password=Column(String(250))
    user=relationship(Favorite,backref='user')
class Planet(Base):
    __tablename__ = 'planet'
    planet=relationship(Favorite,backref='Planet')
    id = Column(Integer, primary_key=True)
    name=Column(String(200), nullable=False)
    diameter  = Column(String(250), nullable=False)
    rotation_period  = Column(String(250), nullable=False)
    orbital_period  = Column(String(250), nullable=False)
    gravity  = Column(String(250), nullable=False)
    population  = Column(String(250), nullable=False)
    climate  = Column(String(250), nullable=False)
    surface_water   = Column(String(250), nullable=False)
    residents   = Column(String(250), nullable=False)
    url   = Column(String(250), nullable=False)
    created   = Column(DateTime,default=datetime.datetime.now(datetime.timezone.utc))
    edited  = Column(DateTime,default=datetime.datetime.now(datetime.timezone.utc))

class Character(Base):
    __tablename__ = 'character'
    character= relationship(Favorite,backref='character')
    id = Column(Integer, primary_key=True)
    name=Column(String(200))
    birth_year = Column(String(250))
    eye_color  = Column(String(250))
    gender  = Column(String(250))
    hair_color  = Column(String(250))
    height  = Column(String(250))
    mass  = Column(String(250))
    homeworld  = Column(String(250))
    created   = Column(DateTime,default=datetime.datetime.now(datetime.timezone.utc))
    edited  = Column(DateTime,default=datetime.datetime.now(datetime.timezone.utc))



    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')
