#!/usr/bin/python3
import json
from models.base_model import BaseModel
from models.user import User


class FileStorage:
    """Representing abstracted Storage engine."""
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """returns the dictionary object"""
        return FileStorage.__objects

    def new(self, obj):
        """sets in __objects obj with key <obj class name>.id"""
        ojname = obj.__class__.__name__
        FileStorage.__objects["{}.{}".format(ojname, obj.id)] = obj

    def save(self):
        """Serialize __objects to the JSON file __file_path."""
        objdict = FileStorage.__objects
        objdict = {obj: objdict[obj].to_dict() for obj in objdict.keys()}
        with open(FileStorage.__file_path, "w") as f:
            json.dump(objdict, f)

    def reload(self):
        """Deserializes the JSON file __file_path to __objects, if exists."""
        try:
            with open(FileStorage.__file_path) as f:
                objdict = json.load(f)
                for i, o in objdict.items():
                    if o["__class__"] == "BaseModel":
                        self.new(BaseModel(**o))
                    elif o["__class__"] == "User":
                        self.new(User(**o))
        except FileNotFoundError:
            return
