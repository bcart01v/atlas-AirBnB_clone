#!/usr/bin/python3
"""Module for FileStorage class."""


import json
from models.base_model import BaseModel


class FileStorage:
    """Class for serializing and deserializing instances to and from JSON file."""
    __file_path = "file.json" 
    __objects = {}

    def all(self):
        """Returns the dictionary __objects."""
        return FileStorage.__objects

    def new(self, obj):
        """Sets in __objects the obj with key <obj class name>.id."""
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        FileStorage.__objects[key] = obj

    def save(self):
        """Serializes __objects to JSON file """
        obj_dict = {obj_id: obj.to_dict() for obj_id, obj in FileStorage.__objects.items()}
        with open(FileStorage.__file_path, "w") as file:
            json.dump(obj_dict, file)

    def reload(self):
        """Deserialization of the json file to __objects """
        try:
            with open(FileStorage.__file_path, 'r') as f:
                obj_dict = json.load(f)
            for obj_id, obj in obj_dict.items():
                cls_name = obj["__class__"]
                if cls_name == 'BaseModel':
                    obj = BaseModel(**obj)
                    FileStorage.__objects[obj_id] = obj
        except FileNotFoundError:
            pass