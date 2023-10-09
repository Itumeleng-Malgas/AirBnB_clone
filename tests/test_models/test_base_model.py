#!/usr/bin/python3
"""This module defines all the test cases for BaseModel class"""

from datetime import datetime as dt
import unittest
import models


class TestBaseModel(unittest.TestCase):
    def test_initialization(self):
        model = models.BaseModel()

        # Test correct datatype object initialization
        self.assertIsInstance(model.created_at, dt)
        self.assertIsInstance(model.updated_at, dt)
        self.assertIsInstance(model.id, str)

    def test_save(self):
        # Test that calling save updates the updated_at attribute
        model = models.BaseModel()
        old_updated_at = model.updated_at
        model.save()

        self.assertNotEqual(old_updated_at, model.updated_at)

    def test_to_dict(self):
        model = models.BaseModel()

        # Test the to_dict method
        d = model.to_dict()
        self.assertIsInstance(d, dict)

        # Test if required fields exists In created dictionary
        self.assertIn('created_at', d)
        self.assertIn('updated_at', d)
        self.assertIn('__class__', d)
        self.assertIn('id', d)

        # Test if timestamps follow isoformat
        self.assertEqual(d['created_at'], model.created_at.isoformat())
        self.assertEqual(d['updated_at'], model.updated_at.isoformat())

    def test_str_representation(self):
        model = models.BaseModel()

        # Test the __str__ method
        expected_str = f"[BaseModel] ({model.id}) {model.__dict__}"
        self.assertEqual(str(model), expected_str)
