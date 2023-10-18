#!/usr/bin/python3
"""
This module defines the Review class, which represents the review entity in the
application.

"""
from models.base_model import BaseModel


class Review(BaseModel):
    """Represent a review in the application

    Attributes:
        place_id (str): The Place id.
        user_id (str): The User id.
        text (str): A review text.
    """

    place_id = ""
    user_id = ""
    text = ""
