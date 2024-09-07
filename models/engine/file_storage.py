#!/usr/bin/python3
"""Defines FileStorage class."""
import json


class FileStorage:
    """
    Handles serialization of objects to JSON and deserialization
    of JSON to objects.
    """
    __file_path = 'file.json'
    __objects = {}

    def all(self):
        """Returns the dictionary __objects."""
        return self.__objects

    def new(self, obj):
        """Sets obj in __objects with key <obj_class_name>.id"""
        key = f'{obj.__class__.__name__}.{obj.id}'
        self.__objects[key] = obj

    def save(self):
        """Serializes __objects to JSON file."""
        with open(self.__file_path, 'w') as file:
            json.dump({key: obj.to_dict() for key, obj in self.__objects.items()}, file)

    def reload(self):
        """Deserializes JSON file to __objects, if file exists."""
        from models.base_model import BaseModel

        try:
            with open(self.__file_path) as file:
                serialized_content = json.load(file)
                for item in serialized_content.values():
                    class_name = item['__class__']
                    self.new(eval(f"{class_name}(**{item})"))
        except FileNotFoundError:
            pass
