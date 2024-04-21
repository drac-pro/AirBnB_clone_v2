#!/usr/bin/python3
""" Place Module for HBNB project """
from os import getenv
from models.base_model import BaseModel, Base
from sqlalchemy import Column, Integer, Float, String, ForeignKey, Table
from sqlalchemy.orm import relationship
from models.review import Review
from models.amenity import Amenity
from models import storage_type


place_amenity = Table(
    'place_amenity',
    Base.metadata,
    Column(
        'place_id',
        String(60),
        ForeignKey('places.id'),
        nullable=False,
        primary_key=True
    ),
    Column(
        'amenity_id',
        String(60),
        ForeignKey('amenities.id'),
        nullable=False,
        primary_key=True
    )
)


class Place(BaseModel, Base):
    """ A place to stay """
    __tablename__ = 'places'
    if storage_type == 'db':
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
        amenities = relationship('Amenity', secondary='place_amenity',
                                 back_populates='place_amenities',
                                 viewonly=False)
    else:
        city_id = ""
        user_id = ""
        name = ""
        description = ""
        number_rooms = 0
        number_bathrooms = 0
        max_guest = 0
        price_by_night = 0
        latitude = 0.0
        longitude = 0.0
        amenity_ids = []


        @property
        def reviews(self):
            """ Returns the list of Review instances with place_id equals
                to the current Place.id """
            from models import storage
            instances = []
            result = []
            temp = storage.all()
            for key in temp.keys():
                if key.startswith('Review.'):
                    instances.append(temp[key])
            for instance in instances:
                if instance.place_id == self.id:
                    result.append(instance)
            return result

        @property
        def amenities(self):
            """ returns the list of Amenity instances based on the attribute
                amenity_ids that contains all Amenity.id linked
                to the Place """
            from models import storage
            amenities_in_place = []
            for amenity in storage.all(Amenity).values():
                if amenity.id in amenity_ids:
                    amenities_in_place.append(amenity)
            return amenities_in_place

        @amenities.setter
        def amenities(sel, obj=None):
            if type(obj) is Amenity and obj.id not in amenity_ids:
                self.amenity_ids.append(obj.id)
