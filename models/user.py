#!/usr/bin/python3
"""
This module defines the User class, which represents a user entity in the
application.

"""
from models.base_model import BaseModel


class User(BaseModel):
    """
    Represents a User in the application.

    Attributes:
        email (str): The user's email address.
        Default: ""

        password (str): The user's password.
        Default: ""

        first_name (str): The user's first name.
        Default: ""

        last_name (str): The user's last name.
        Default: ""
    """

    first_name: str = ""
    last_name: str = ""
    password: str = ""
    email: str = ""
