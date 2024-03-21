#!/usr/bin/python3

"""

This module defines a class that serializes/deserializes

"""
from models.base_model import BaseModel
from models.user import User
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
import json
import os


class FileStorage:
    """Class that serializes/deserializes"""

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Returns the dictionary __objects"""
        return self.__objects

    def new(self, obj):
        """Setter for __objects"""
        if obj:
            key = f"{obj.__class__.__name__}.{obj.id}"
            self.__objects[key] = obj

    def save(self):
        """Serializes __objects to JSON file"""
        obj_dict = {}
        for key, obj in self.__objects.items():
            obj_dict[key] = obj.to_dict()

        with open(self.__file_path, 'w') as file:
            json.dump(obj_dict, file)

    def reload(self):
        """Deserializes the JSON file to __objects"""
        classes = {
            'BaseModel': BaseModel,
            'User': User,
            'State': State,
            'City': City,
            'Amenity': Amenity,
            'Place': Place,
            'Review': Review
            }
        try:
            with open(self.__file_path, 'r') as file:
                dictionnaries_obj = json.load(file)
                for key, obj in dictionnaries_obj.items():
                    class_name, instance_id = key.split('.')
                    cls = classes[class_name]
                    self.__objects[key] = cls(**obj)
        except FileNotFoundError:
            pass
