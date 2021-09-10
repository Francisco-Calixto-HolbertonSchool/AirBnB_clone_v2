#!/usr/bin/python3
"""This module defines a class to manage file storage for hbnb clone"""

from models.base_model import Base
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from os import getenv


classes = {'User': User, 'Place': Place, 'Review': Review,
           'State': State, 'City': City}


class DBStorage():
    """new engine, sqlalchemy"""
    __engine = None
    __session = None

    def __init__(self):
        """constructor"""
        self.__engine = create_engine("mysql+mysqldb://{}:{}@{}/{}"
                                      .format(getenv('HBNB_MYSQL_USER'),
                                              getenv('HBNB_MYSQL_PWD'),
                                              getenv('HBNB_MYSQL_HOST'),
                                              getenv('HBNB_MYSQL_DB')),
                                      pool_pre_ping=True)
        self.reload()
        if getenv('HBNB_ENV') == 'test':
            Base.metadata.drop_all(bind=self.__engine, checkfirst=True)

    def all(self, cls=None):
        """queries on the current database session"""
        objects = {}
        for current_class in classes.values():
            if current_class is cls or cls is None:
                for elem in self.__session.query(current_class).all():
                    objects[elem.__class__.__name__+'.'+elem.id] = elem
        return objects

    def new(self, obj):
        """add the object to the current database session"""
        self.__session.add(obj)

    def save(self):
        """ commit all changes of the current database session """
        self.__session.commit()

    def delete(self, obj=None):
        """delete from the current database session obj if not None"""
        if obj:
            self.__session.delete(obj)
            self.save()

    def reload(self):
        """ no lo se rik """
        Base.metadata.create_all(self.__engine)
        session_fac = sessionmaker(bind=self.__engine, expire_on_commit=False)
        Session = scoped_session(session_fac)
        self.__session = Session

    def close(self):
        """calls remove method"""
        self.__session.remove()
