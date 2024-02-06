#!/usr/bin/python3
"""Unit test for the City class."""


import unittest
import os
import models
import datetime
from models.city import City
from models.base_model import BaseModel


class TestCity(unittest.TestCase):
    """ General test cases for the city class """

    def test_city(self):
        """ Test the city class """
        city = City()
        self.assertIsInstance(city, City)
        self.assertTrue(issubclass(type(city), BaseModel))

    def test_empty_city(self):
        """ Test an empty city """
        city = City()
        self.assertEqual(city.state_id, "")
        self.assertEqual(city.name, "")

    def test_city_id(self):
        """ Test the city id """
        city = City()
        self.assertEqual(str, type(city.id))

    def test_city_created_at(self):
        """ Test the city created_at """
        city = City()
        self.assertEqual(datetime.datetime, type(city.created_at))

    def test_city_name(self):
        """ Test the city name """
        city = City()
        self.assertEqual(str, type(city.name))

    def test_city_state_id(self):
        """ Test the city state_id """
        city = City()
        self.assertEqual(str, type(city.state_id))

class TestCity_save(unittest.TestCase):
    """ Unit test for saving city """

    @classmethod
    def SetUp(Self):
        try:
            os.remove("file.json")
        except FileNotFoundError:
            pass

    def TearDown(self):
        try:
            os.remove("file.json")
        except FileNotFoundError:
            pass
        try:
            os.rename("tmp", "file.json")
        except FileNotFoundError:
            pass

    def test_save(self):
        city = City()
        city.save()
        self.assertNotEqual(city.created_at, city.updated_at)

    def test_save_with_arg(self):
        city = City()
        with self.assertRaises(TypeError):
            city.save(None)

    

if __name__ == '__main__':
    unittest.main()
