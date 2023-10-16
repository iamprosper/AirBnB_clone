#!/usr/bin/python3
"""Base module module file"""
from uuid import uuid4
from datetime import datetime
from . import storage


class BaseModel:
    """Base class"""
    def __init__(self, *args, **kwargs):
        if kwargs:
            for k, v in kwargs.items():
                if k != "__class__":
                    if k == "created_at" or k == "updated_at":
                        v = datetime.fromisoformat(v)
                    setattr(self, k, v)
        else:
            self.id = str(uuid4())
            self.created_at = datetime.now()
            self.updated_at = self.created_at
            storage.new(self)

    def __str__(self):
        return "[{}] ({}) {}".format(
                self.__class__.__name__,
                self.id, self.__dict__)

    def save(self):
        self.updated_at = datetime.now().isoformat()
        storage.save()

    def to_dict(self):
        self.__dict__["__class__"] = self.__class__.__name__
        self.created_at = self.created_at.isoformat()
        self.updated_at = self.updated_at.isoformat()
        return self.__dict__
