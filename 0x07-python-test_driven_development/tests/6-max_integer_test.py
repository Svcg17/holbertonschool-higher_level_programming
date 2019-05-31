#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    """ A TestMaxInteger class """

    def test_list(self):
        """ Test for no parameter """
        self.assertEqual(max_integer(), None)

    def test_sstring_list(self):
        """ Test for other data types """
        string_list = [1, "es", 3]
        self.assertRaises(TypeError, max_integer, string_list)

    def test_max_integervalid(self):
        """ Normal output test """
        lista = [1, 2, 3, 4]
        self.assertEqual(max_integer(lista), 4)

    def test_zerolist(self):
        """ List filled with zeros """
        lista = [0, 0, 0]
        self.assertEqual(max_integer(lista), 0)

    def test_juno(self):
        """ Normal output test """
        self.assertEqual(max_integer([1, 5, 88, 7, 11]), 88)

    def test_beginning(self):
        """ Test for name error """
        lista = [32, 3, 4]
        self.assertEqual(max_integer(lista), 32)

    def test_oneonly(self):
        """ Test for only one number """
        lista = [1]
        self.assertEqual(max_integer(lista), 1) 

    def test_negative(self):
        """ Test for all negative numbers """
        lista = [-1, -2, -3]
        self.assertEqual(max_integer(lista), -1)

    def test_oneneg(self):
        """ Tesst for only one negative num """
        lista = [-3]
        self.assertEqual(max_integer(lista), -3)

    def test_mix(self):
        """ Test with both negative and positive integerrs """
        lista = [1, 2, -3]
        self.assertEqual(max_integer(lista), 2)

    if __name__ == '__main__':
        unittest.main()
