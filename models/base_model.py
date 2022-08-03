#!/usr/bin/python3
"""BaseModel module."""
from uuid import uuid4
from datetime import datetime


class BaseModel:
    """BaseModel class"""

    def __init__(self, *args, **kwargs):
        """Initilize a new BaseModel."""


        tform = "%Y-%m-%dT%H:%M:%S.%f"
        self.id = str(uuid4())
        self.created_at = datetime.today()
        self.updated_at = datetime.today()
        if len(kwargs) != 0:
            for k, v in kwargs.items():
                if k == "created_at" or k == "updated_at":
                    self.__dict__[k] = datetime.strptime(v, tform)
                else:
                    self.__dict__[k] = v

        def save(self):
            """Save method."""
            self.update_at = datetime.today()

        def to_dict(self):
            """to_dict method."""
            rdict = self.__dict__.copy()
            tdict["created_at"] = self.created_at.isoformat()
            rdict["updated-at"] = self.updated_at.isoformat()
            rdict["__class__"} = self.__class__.__name__
            return rdict

        def __str__(self):
            """Return the print/str representation of the BaseModel instance."""
            classname = self.__class__.__name__
            return "[{}] ({}) {}".format(classname, self.id, self.__dict__)
