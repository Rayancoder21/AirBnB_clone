#!/usr/bin/python3
""" Defines the BaseModel class"""
import uuid
from datetime import datetime
import models


class BaseModel:
    """Represents the BaseModel of the HBnB project """
    def __init__(self, *args, **kwargs):
        """ Initialize a new BaseModel"""
        self.id = str(uuid.uuid4())
        self.created_at = datetime.utcnow()
        self.updated_at = datetime.utcnow()
        tFormat = "%Y-%m-%dT%H:%M:%S.%f"

        if kwargs:
            for k, v in kwargs.items():
                if k == "__class__":
                    continue
                elif k == "created_at" or k == "updated_at":
                    setattr(self, k, datetime.strptime(v, tFormat))
                else:
                    setattr(self, k, v)
        models.storage.new(self)

    def __str__(self):
        """ Return the print/str representation of the BaseModel instance"""
        class_name = self.__class__.__name__
        return "[{}] ({}) {}".format(class_name, self.id, self.__dict__)

    def save(self):
        """ updates the public instance attribute updated_at"""
        self.updated_at = datetime.utcnow()
        models.storage.save()

    def to_dict(self):
        """ returns a dictionary containing values of __dict__"""
        dictionary = self.__dict__.copy()
        dictionary["__class__"] = self.__class__.__name__
        dictionary["created_at"] = self.created_at.isoformat()
        dictionary["updated_at"] = self.updated_at.isoformat()
        return dictionary


if __name__ == "__main__":
    my_model = BaseModel()
    my_model.name = "My First Model"
    my_model.my_number = 89
    print(my_model)
    my_model.save()
    print(my_model)
    myJson = my_model.to_dict()
    print(myJson)
    print("JSON of my_model:")
    for key in myJson.keys():
        print("\t{}: ({}) - {}".format(key, type(myJson[key]), myJson[key]))
