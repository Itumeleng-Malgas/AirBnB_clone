#!/usr/bin/python3
"""
This module defines the Amenity class, which represents a amenity entity in
the application.

"""
from models.base_model import BaseModel


class Amenity(BaseModel):
    """
    Represents a Amenity in the application.

    Attributes:
        name (str): The name of amenity.
        Default: ""

    """

    name: str = ""
