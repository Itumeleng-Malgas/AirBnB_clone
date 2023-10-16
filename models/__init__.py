#!/usr/bin/python3
"""defines the models module"""

from models.engine.file_storage import FileStorage
from .base_model import BaseModel
from .user import User
from .city import City
from .place import Place
from .state import State
from .review import Review

storage = FileStorage()
storage.reload()
