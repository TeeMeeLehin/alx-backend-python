#!/usr/bin/env python3
"""testing the utils module"""
from utils import access_nested_map
import unittest
from parameterized import parameterized


class TestAccessNestedMap(unittest.TestCase):
    """Test Class"""

    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2),
    ])
    def test_access_nested_map(self, nested_map, path, xres):
        """test func"""
        res = access_nested_map(nested_map, path)
        self.assertEqual(res, xres)

    @parameterized.expand([
        ({}, ("a",)),
        ({"a": 1}, ("a", "b")),
    ])
    def test_access_nested_map_exception(self, nested_map, path):
        """xception test func"""
        with self.assertRaises(KeyError):
            access_nested_map(nested_map, path)
