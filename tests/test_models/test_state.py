#!/usr/bin/python3
"""Unit test for the State class."""

"""Unittest Classes
    TestState_start
    TestState_save
    TestState_to_dictionary
"""

import unittest
import os
import models
from time import sleep
from models.state import State
from datetime import datetime


class TestState_start(unittest.TestCase):
    """ Unittest for testing the State Class """

    def test_no_args(self):
        self.assertIsInstance(State(), State)

    def test_stored(self):
        self.assertIn(State(), models.storage.all().values())

    def test_public_id(self):
        self.assertEqual(str, type(State().id))

    def test_updated_time(self):
        self.assertEqual(datetime, type(State().updated_at))

    def test_created_time(self):
        self.assertEqual(datetime, type(State().created_at))

    def test_all_times(self):
        self.assertEqual(datetime, type(State().created_at))
        self.assertEqual(datetime, type(State().updated_at))

    def test_two_states(self):
        FirstState = State()
        SecondState = State()
        self.assertNotEqual(FirstState.id, SecondState.id)

    def test_one_state(self):
        FirstState = State()
        self.assertIsNotNone(FirstState.id)

    def test_different_time_creations(self):
        FirstState = State()
        sleep(5)
        SecondState = State()
        self.assertNotEqual(FirstState.created_at, SecondState.created_at)

class Test_state_save(unittest.TestCase):
    """Unittest for testing the save method in the State class"""

    @classmethod
    def SetUp(self):
        try:
            os.rename("file.json", "tmp")
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
        state = State()
        state.save()
        self.assertNotEqual(state.created_at, state.updated_at)

    def test_arg_save(self):
        state = State()
        with self.assertRaises(TypeError):
            state.save(None)

    def test_update_save(self):
        state = State()
        first_updated_at = state.updated_at
        sleep(1.69)
        state.save()
        self.assertLess(first_updated_at, state.updated_at)


class TestState_to_dictionary(unittest.TestCase):
    """Unit tests for testing to the dictionary, obviously."""

    def test_to_dictionary(self):
        self.assertTrue(dict, type(State().to_dict()))

    def test_to_dictionary_with_keys(self):
        self.assertIn("id", State().to_dict())
        self.assertIn("created_at", State().to_dict())
        self.assertIn("updated_at", State().to_dict())
        self.assertIn("__class__", State().to_dict())

    def test_to_dict_output(self):
        dt = datetime.today()
        st = State()
        st.id = "123456"
        st.created_at = st.updated_at = dt
        tdict = {
            'id': '123456',
            '__class__': 'State',
            'created_at': dt.isoformat(),
            'updated_at': dt.isoformat(),
        }
        self.assertDictEqual(st.to_dict(), tdict)

if __name__ == "__main__":
    unittest.main()