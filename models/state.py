#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from models.city import City
import models


class State(BaseModel, Base):
    """ State class """
    __tablename__ = 'states'

    name = Column(String(128), nullable=False)
    cities = relationship('City', cascade='all, delete, delete-orphan',
                          backref='state')

    @property
    def cities(self):
        """Return City instances with state_id equals to the
        current State.id"""
        instances = []
        result = []
        temp = models.storage.all()
        for key in temp.keys():
            if key.startswith('City.'):
                instances.append(temp[key])
        for instance in instances:
            if instance.state_id == self.id:
                result.append(instance)
        return result
