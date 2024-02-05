#!/usr/bin/python3
"""Unit test for the Place class."""


import unittest
import os
from datetime import datetime
from models.place import Place
from models.base_model import BaseModel


class TestPlace(unittest.TestCase):
    """Test cases for the Place class."""

    def test_init(self):
        """Test initialization of Place instances."""
        place = Place()
        self.assertIsInstance(place, Place)
        self.assertTrue(issubclass(type(place), BaseModel))

        # Test that attributes exist and are of correct type
        self.assertIsInstance(place.city_id, str)
        self.assertIsInstance(place.user_id, str)
        self.assertIsInstance(place.name, str)
        self.assertIsInstance(place.description, str)
        self.assertIsInstance(place.number_rooms, int)
        self.assertIsInstance(place.number_bathrooms, int)
        self.assertIsInstance(place.max_guest, int)
        self.assertIsInstance(place.price_by_night, int)
        self.assertIsInstance(place.latitude, float)
        self.assertIsInstance(place.longitude, float)
        self.assertIsInstance(place.amenity_ids, list)

    def test_attr_values(self):
        """Test that attributes are correctly assigned."""
        place = Place()
        place.city_id = "city_id"
        place.user_id = "user_id"
        place.name = "My lovely place"
        place.description = "A cozy place"
        place.number_rooms = 3
        place.number_bathrooms = 2
        place.max_guest = 4
        place.price_by_night = 100
        place.latitude = 36.778259
        place.longitude = -119.417931
        place.amenity_ids = ["amenity_id1", "amenity_id2"]

        # Test that attribute values are correctly assigned
        self.assertEqual(place.city_id, "city_id")
        self.assertEqual(place.user_id, "user_id")
        self.assertEqual(place.name, "My lovely place")
        self.assertEqual(place.description, "A cozy place")
        self.assertEqual(place.number_rooms, 3)
        self.assertEqual(place.number_bathrooms, 2)
        self.assertEqual(place.max_guest, 4)
        self.assertEqual(place.price_by_night, 100)
        self.assertEqual(place.latitude, 36.778259)
        self.assertEqual(place.longitude, -119.417931)
        self.assertEqual(place.amenity_ids, ["amenity_id1", "amenity_id2"])

    def test_no_args(self):
        self.assertEqual(place, type(Place()))

    def test_instance_no_kwargs(self):
        with self.assertRaises(TypeError):
            Place(id = None, created_at = None, updated_at = None)

    def test_instance_with_kwargs(self):
        dttime = datetime.today()
        dttime_iso = datetime.isoformat()
        pl = Place(id = "957", created_at = dttime, updated_at = dttime_iso)
        self.assertEqual(pl.id, "957")
        self.assertEqual(pl.created_at, dttime)
        self.assertEqual(pl.updated_at, dttime_iso)


class TestPlace_save(unittest.TestCase):
    """ Unittest for saving stuff """

    @classmethod
    def setUp(self):
        try:
            os.rename("file.json", "tmp")
        except IOerror:
            pass

    def tearDown(self):
        try:
            os.remove("file.json")
        except IOerror:
            pass
        try:
            os.rename("tmp", "file.json")
        except IOerror:
            pass

    def test_save(self):
        """ Test for saving """
        place = Place()
        place.save()
        self.assertNotEqual(place.created_at, place.updated_at)

    def test_save_witharg(self):
        """ Test for saving with arg """
        place = Place()
        with self.assertRaises(TypeError):
            place.save(None)

if __name__ == '__main__':
    unittest.main()
