#!/usr/bin/python3
"""Unit tests module"""
from models.base_model import BaseModel
import unittest


first_model = BaseModel()
first_model.name = "First Model"
first_model.type = "Setting"
second_model = BaseModel()


class Test(unittest.TestCase):
    def test_unique_id(self):
        self.assertFalse(first_model.id == second_model.id)

    def test_initial_datetime(self):
        self.assertEqual(first_model.created_at, first_model.updated_at)

    def test_updated_datetime(self):
        first_model.save()
        self.assertFalse(first_model.created_at == first_model.updated_at)
