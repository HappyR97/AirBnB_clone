#!/usr/bin/python3
"""
A unittest for Amenity class
"""

import unittest
from models.base_model import BaseModel
from models.amenity import Amenity
from models import storage
from datetime import datetime
import os
import time


class Test_Amenity_Class(unittest.TestCase):
    """Unittest class for testing class Amenity
    Test the following attributes
    name = ""
"""
    def setUp(self):
        """setUp method"""
        self.c1 = Amenity()
        self.s2 = Amenity()

    def tearDown(self):
        """tearDown method"""
        del self.c1
        del self.s2
        if os.path.exists("file.json"):
            os.remove("file.json")

    def test_Amenity_id(self):
        """Test Amenity instance id"""
        self.assertNotEqual(self.c1.id, self.s2.id)

    # ***************************************************************

    # *********************************************************
    def test_datetime_attr(self):
        """Test datetime attributes"""
        self.assertIsInstance(self.c1.created_at, datetime)
        self.assertIsInstance(self.c1.updated_at, datetime)

    def test_initial_values(self):
        """Test initial values for Amenity class attributes"""
        self.assertEqual(self.c1.name, "")

    def test_Amenity_inherits_BaseModel(self):
        """Test if Amenity inherits from BaseModel"""
        self.assertIsInstance(self.c1, BaseModel)

    def test_Amenity_type(self):
        """Test if Amenity instance is of the same type"""
        self.assertEqual(type(self.c1), Amenity)

    def test_storage_contains_instances(self):
        """Test storage contains the instances"""
        search_key = f"{self.c1.__class__.__name__}.{self.c1.id}"
        self.assertTrue(search_key in storage.all().keys())
        search_key = f"{self.s2.__class__.__name__}.{self.s2.id}"
        self.assertTrue(search_key in storage.all().keys())

    def test_to_dict_id(self):
        """Test to_dict method from BaseModel"""
        dict_c1 = self.c1.to_dict()
        self.assertIsInstance(dict_c1, dict)
        self.assertIn('id', dict_c1.keys())

    def test_to_dict_created_at(self):
        """Test to_dict method from BaseModel"""
        dict_c1 = self.c1.to_dict()
        self.assertIsInstance(dict_c1, dict)
        self.assertIn('created_at', dict_c1.keys())

    def test_to_dict_updated_at(self):
        """Test to_dict method from BaseModel"""
        dict_c1 = self.c1.to_dict()
        self.assertIsInstance(dict_c1, dict)
        self.assertIn('updated_at', dict_c1.keys())

    def test_to_dict_class_name(self):
        """Test to_dict method from BaseModel"""
        dict_c1 = self.c1.to_dict()
        self.assertEqual(self.c1.__class__.__name__, dict_c1["__class__"])

    def test_str_(self):
        """Test __str__ method from BaseModel"""
        cls_rp = str(self.c1)
        format = "[{}] ({}) {}".format(self.c1.__class__.__name__,
                                       self.c1.id, self.c1.__dict__)
        self.assertEqual(format, cls_rp)

    def test_check_two_instances_with_dict(self):
        """Test to check an instance created from a dict is different from
another"""
        dict_c1 = self.c1.to_dict()
        instance = Amenity(**dict_c1)
        self.assertIsNot(self.c1, instance)
        self.assertEqual(str(self.c1), str(instance))
        self.assertFalse(instance is self.c1)

    def test_save(self):
        """Test save() method from BaseModel"""
        update_old = self.c1.updated_at
        time.sleep(0.1)
        self.c1.save()
        updated_new = self.c1.updated_at
        self.assertNotEqual(update_old, updated_new)


if __name__ == "__main__":
    unittest.main()
