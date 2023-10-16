#!/usr/bin/python3
"""Unit tests module"""
from models.base_model import BaseModel
import unittest


first_model = BaseModel()
first_model.name = "First Model"
first_model.type = "Setting"
second_model = BaseModel()


class TestBaseModel(unittest.TestCase):
    def test_uuid(self):
        self.assertFalse(first_model.id == second_model.id)

    def test_datetime_attributes(self):
        self.assertEqual(first_model.created_at, first_model.updated_at)

    def test_updated_datetime(self):
        first_model.save()
        self.assertFalse(first_model.created_at == first_model.updated_at)

    def test_str(self):
        """Test correct output for str method"""
        output = "[BaseModel] ({}) {}".format(first_model.id, first_model.__dict__)
        self.assertEqual(output, str(first_model))

    def test_json_formating(self):
        """Test to_dict method"""
        self.assertTrue("__class__" in first_model.to_dict())
