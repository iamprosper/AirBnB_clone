#!/usr/bin/python3
"""storage module egine"""
import json


class FileStorage:
    """Main class"""
    __file_path = "file.json"
    __objects = {}

    def all(self):
        return self.__objects

    def new(self, obj):
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        FileStorage.__objects[key] = obj.to_dict()

    def save(self):
        if FileStorage.__file_path != "":
            json_str = ""
            json_str += json.dumps(FileStorage.__objects)
            with open(FileStorage.__file_path, "w") as json_file:
                json_file.write(json_str)

    def reload(self):
        if FileStorage.__file_path != "":
            try:
                with open(FileStorage.__file_path) as json_file:
                    FileStorage.__objects = json.load(json_file)
            except Exception as e:
                pass
