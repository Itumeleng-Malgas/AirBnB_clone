#!/usr/bin/python3
"""
This module defines the BaseModel class, which defines all common attributes/
methods for other classes.

"""
from datetime import datetime as dt
import uuid


class BaseModel:
    """
    Implements the base class of the project

    Attributes:
        id (string): assign with an uuid when an instance is created.

        created_at (datetime): assign with the current datetime when an
        instance is created.

        updated_at: datetime - assign with the current datetime when an
        instance is created.
    """

    def __init__(self, *args, **kwargs):
        """
        Initialize the BaseModel class

        Arguments:
            *args (any): unused

            **kwargs (dict): obj attr key/value pair

        """

        if kwargs:
            for key, value in kwargs.items():
                if key == "__class__":
                    continue
                if key in ("created_at", "updated_at"):
                    value = dt.strptime(value, "%Y-%m-%dT%H:%M:%S.%f")
                setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = dt.now()
            self.updated_at = dt.now()

    def __str__(self):
        """Returns a formated string representation of an instance"""
        class_name = self.__class__.__name__
        return f"[{class_name}] ({self.id}) {self.__dict__}"

    def save(self):
        """Updates the attribute updated_at with the current datetime"""
        self.updated_at = dt.now()

    def to_dict(self):
        """Returns a dictionary representation of a given object"""
        obj_dict = self.__dict__.copy()

        obj_dict['__class__'] = self.__class__.__name__
        obj_dict['created_at'] = self.created_at.isoformat()
        obj_dict['updated_at'] = self.updated_at.isoformat()

        return obj_dict
