#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from models.city import City
from models import storage_type
from os import getenv


class State(BaseModel, Base):
    """ State class """
    __tablename__ = 'states'
    if storage_type == 'db':
        name = Column(String(128), nullable=False)
        cities = relationship('City', cascade='all, delete, delete-orphan',
                              backref='state')
    else:
        name = ""

        @property
        def cities(self):
            """Return City instances with state_id equals to the
            current State.id"""
            from models import storage
            instances = []
            result = []
            temp = storage.all()
            for key in temp.keys():
                if key.startswith('City.'):
                    instances.append(temp[key])
            for instance in instances:
                if instance.state_id == self.id:
                    result.append(instance)
            return result
