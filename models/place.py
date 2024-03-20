#!/usr/bin/python3
""" Place Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, Integer, Float, String, ForeignKey
from sqlalchemy.orm import relationship
from models.review import Review
import models


class Place(BaseModel, Base):
    """ A place to stay """
    __tablename__ = 'places'

    city_id = Column(String(60), ForeignKey('cities.id'))
    user_id = Column(String(60), ForeignKey('users.id'))
    name = Column(String(128), nullable=False)
    description = Column(String(1024))
    number_rooms = Column(Integer, default=0, nullable=False)
    number_bathrooms = Column(Integer, default=0, nullable=False)
    max_guest = Column(Integer, default=0, nullable=False)
    price_by_night = Column(Integer, default=0, nullable=False)
    latitude = Column(Float)
    longitude = Column(Float)
    amenity_ids = []
    reviews = relationship('Review', cascade='all, delete, delete-orphan',
                           backref='place')

    @property
    def reviews(self):
        """ Returns the list of Review instances with place_id equals
            to the current Place.id """
        instances = []
        result = []
        temp = models.storage.all()
        for key in temp.keys():
            if key.startswith('Review.'):
                instances.append(temp[key])
        for instance in instances:
            if instance.place_id == self.id:
                result.append(instance)
        return result
