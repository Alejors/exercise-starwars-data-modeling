import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy import render_er

Base = declarative_base()

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    username = Column(String(100), unique=True, nullable=False)
    firstname = Column(String(100))
    lastname = Column(String(100))
    email = Column(String(100), unique=True, nullable=False)
    favorite_characters =  relationship('People', secondary="favorite_characters")
    favorite_planets =  relationship('Planet', secondary="favorite_planets")
    favorite_vehicles =  relationship('Vehicle', secondary="favorite_vehicles")

class Favorite_character(Base):
    __tablename__ = 'favorite_characters'
    character_id = Column(Integer, ForeignKey('people.id'),  primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'), primary_key=True)

class Favorite_planet(Base):
    __tablename__ = 'favorite_planets'
    planet_id = Column(Integer, ForeignKey('planets.id'),  primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'), primary_key=True)

class Favorite_vehicle(Base):
    __tablename__ = 'favorite_vehicles'
    vehicle_id = Column(Integer, ForeignKey('vehicles.id'),  primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'), primary_key=True)

class People(Base):
    __tablename__ = 'people'
    id = Column(Integer, primary_key=True)
    name = Column(String(100), unique=True, nullable=False)
    height = Column(Integer)
    mass = Column(Integer)
    hair_color = Column(String(100))
    skin_color = Column(String(100))
    eye_color = Column(String(100))
    birth_year = Column(String(100))
    gender = Column(String(100)) 

class Planet(Base):
    __tablename__ = 'planets'
    id = Column(Integer, primary_key=True)
    name = Column(String(100), unique=True, nullable=False)
    rotation_period = Column(Integer)
    orbital_period = Column(Integer)
    diameter = Column(Integer)
    climate = Column(String(100))
    gravity = Column(String(100))
    terrain = Column(String(100))
    surface_water = Column(String(100))
    population = Column(Integer)

class Vehicle(Base):
    __tablename__ = 'vehicles'
    id = Column(Integer, primary_key=True)
    name = Column(String(100), unique=True, nullable=False)
    model = Column(String(100), unique=True, nullable=False)
    manufacturer = Column(String(100))
    cost_in_credits = Column(Integer)
    length = Column(Integer)
    max_atmosphering_speed = Column(Integer)
    crew = Column(Integer)
    passengers = Column(Integer)
    cargo_capacity = Column(Integer)
    consumables = Column(String(100))
    vehicle_class = Column(String(100))

render_er(Base, 'diagram.png')