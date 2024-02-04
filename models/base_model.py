#!/usr/bin/python3

"""Base Model Module for AirBnB Clone.
    """


import uuid
import models
from datetime import datetime

class BaseModel:
    def __init__(self, *args, **kwargs):
        if kwargs:
            # Loop through each key, value pair in kwargs
            for key, value in kwargs.items():
                # Skip __class__ attribute
                if key == "__class__":
                    continue
                # Convert string datetime to datetime object for created_at and updated_at
                if key in ["created_at", "updated_at"]:
                    value = datetime.fromisoformat(value)
                setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = self.created_at
            models.storage.new(self)
 
    def __str__(self):
        return "[{}] ({}) {}".format(self.__class__.__name__, self.id, self.__dict__)
    
    def save(self):
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """Returns a dictionary containing all keys/values of __dict__ of the instance."""
        # Copy __dict__ to avoid modifying the original
        dict_copy = self.__dict__.copy()
        # Add class name to the dictionary
        dict_copy["__class__"] = self.__class__.__name__
        # Format datetime objects to strings
        dict_copy["created_at"] = self.created_at.isoformat()
        dict_copy["updated_at"] = self.updated_at.isoformat()
        return dict_copy
