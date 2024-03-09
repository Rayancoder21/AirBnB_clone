#!/usr/bin/python3
""" Defines the BaseModel class"""
import models
import uuid
import datetime from datetime


class BaseModel():
    """Represents the BaseModel of the HBnB project """
    def __init__(self, *args, **kwargs):
        """ Initialize a new BaseModel"""
        self.id = str(uuid.uuid4())
        form_time = "%Y-%m-%dT%H:%M:%S.%f"
        self.created_at = datetime.now()
        self.updated_at = datetime.now()
        if len(kwargs) != 0:
            for k, v in kwargs.items():
                if k == "created_at" or k == "updated_at":
                    self.__dict__[k] = datetime.strptime(v, tform)
                else:
                    self.__dict__[k] = v
        else:
            models.storage.new(self)

    def __str__(self):
        """ Return the print/str representation of the BaseModel instance"""
        class_name = self.__class__.__name__
        return "[{}] ({}) {}".format(class_name, self.id, self.__dict__)

    def save(self):
        """ updates the public instance attribute updated_at"""
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """ returns a dictionary containing values of __dict__"""
        dictionary = self.__dict__.copy()
        dictionary["created_at"] = self.created_at.isoformat()
        dictionary["updated_at"] = self.updated_at.isoformat()
        dictionary["__class__"] = self.__class__.__name__
        return dictionary
