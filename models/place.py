#!/usr/bin/python3
"""
This module defines the Place class, which represents a place entity in the
application.

"""
from models.base_model import BaseModel


class Place(BaseModel):
    """
    Represents a Place in the application

    Attributes:
        city_id (str): The City id.
        user_id (str): The User id.
        name (str): The Place name.
        description (str): The Place description.
        number_rooms (int): The Place number of rooms.
        number_bathrooms (int): The Place number of bathrooms.
        max_guest (int): The Place maximum number of guests.
        price_by_night (int): The Place price by night.
        latitude (float): The Place latitude.
        longitude (float): The Place longitude.
        amenity_ids (list): Amenity ids.
    """

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
