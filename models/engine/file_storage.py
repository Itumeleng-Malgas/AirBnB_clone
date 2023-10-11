#!/usr/bin/python3
""" This ...."""

import json

class FileStorage:
    __file_path = "file.json"
    __objects = {}

    def all(self):
        return FileStorage.__objects

    def new(self, obj):
        key = f"{obj.__class__.____name__}.{obj.id}"
        FileStorage.__objects[key] = obj

    def save(self):
        data = {}
        for key, obj in FileStorage.__objects.items():
            data[key] = obj.to_dict()
        with open(FileStorage.__file_path, 'w') as file:
            json.dump(data, file)

    def reload(self):
        try:
            with open(FileStorage.__file_path, 'r') as file:
                data = json.load(file)
                for key, value in data.items():
                    class_name, obj_id = key.split('.')
                    obj = models[class_name](**value)
                    FileStorage.__objects[key] = obj
        except FileNotFoundError:
            pass
