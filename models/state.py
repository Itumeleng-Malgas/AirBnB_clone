#!/usr/bin/python3
"""
This module defines the State class, which represents the state entity in the
application.

"""
from models.base_model import BaseModel



class State(BaseModel):
    """Represent a state.

    Attributes:
        name (str): The name of the state.
    """

    name = ""
