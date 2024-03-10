#!/usr/bin/python3
"""recreate a BaseModel from another one"""
import json
import os
from models.base_model import BaseModel


class FileStorage:
    """serializes instances to and deserializes JSON file"""

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """ returns the dictionary __objects"""
        return FileStorage.__objects

    def new(self, obj):
        """sets in __objects the obj with key"""
        class_name = obj.__class__.__name__
        k = "{}.{}".format(class_name, obj.id)
        FileStorage.__objects[k] = obj

    def save(self):
        """serializes __objects to the JSON file"""
        objects = FileStorage.__objects

        o_dictionary = {}
        for obj in objects.keys():
            o_dictionary[obj] = objects[obj].to_dict()
        with open(FileStorage.__file_path, "w") as f:
            json.dump(o_dictionary, f)

    def reload(self):
        """deserializes the JSON file to __objects"""
        if os.path.isfile(FileStorage.__file_path):
            with open(FileStorage.__file_path, "r", encoding="utf-8") as file:
                try:
                    o_dictionary = json.load(file)
                    for k, v in o_dictionary.items():
                        className, obj_id = k.split('.')
                        cls = eval(className)
                        inste = cls(**v)
                        FileStorage.__objects[k] = inste
                except Exception:
                    pass
