import unittest
import sys
import os
import json
from io import StringIO
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square

"""Unittest for Base class"""


class Test_base(unittest.TestCase):
    """ A Test_base class"""

    def resetnb(self):
        """Resets __nb_objects"""
        Base._Base__nb_objects = 0

    def test_type(self):
        """ Testing for type of instance"""
        base1 = Base()
        self.assertTrue(type(base1) == Base)

    def test_withparam(self):
        """Testing creating instance with parameter"""
        base3 = Base(12)
        self.assertTrue(type(base3) == Base)

    def test_difffloats(self):
        """Testing for floats, special numbers"""
        b1 = Base(12.4)
        self.assertEqual(b1.id, 12.4)
        b2 = Base(float('nan'))
        self.assertTrue(b2)
        self.assertEqual(b2 is float('nan'), False)
        b3 = Base(float('inf'))
        self.assertTrue(b3)
        self.assertEqual(b2 is float('nan'), False)

    def test_noneid(self):
        """Testing for a None id"""
        bb = Base(None)
        self.assertEqual(bb.id, 16)

    def test_unknowd(self):
        """Testing for unknown type"""
        with self.assertRaises(NameError):
            bbb = Base(sfo)

    def test_checkid(self):
        """Testing id of instance base"""
        b1 = Base()
        self.assertEqual(b1.id, 1)
        b2 = Base()
        self.assertEqual(b2.id, 2)
        b3 = Base(12)
        self.assertEqual(b3.id, 12)
        b4 = Base()
        self.assertEqual(b4.id, 3)

    def test_to_json_string(self):
        """Testing for test_to_json_string method"""
        r1 = Rectangle(10, 7, 2, 8, 1)
        dictionary = r1.to_dictionary()
        json_dictionary = Base.to_json_string([dictionary])
        self.assertEqual(len(json_dictionary), len(str([{
            "x": 2, "width": 10, "id": 1, "height": 7, "y": 8}])))
        self.assertTrue(type(json_dictionary), dict)

    def test_to_json_string_square(self):
        """Testing for test_to_json_string method square"""
        r1 = Square(10, 7, 2, 8)
        dictionary = r1.to_dictionary()
        json_dictionary = Base.to_json_string([dictionary])
        self.assertEqual(len(json_dictionary), len(str([{
            "x": 7, "size": 10, "id": 8, "y": 2}])))
        self.assertTrue(type(json_dictionary), dict)

    def test_to_json_non_dictionary(self):
        """Passing a non dictionary parameter to test_to_json_string
        And passing empty parameter
        """
        with self.assertRaises(TypeError):
            r1 = Rectangle(10, 7, 2, 8, 1)
            json_dic = Base.to_json_string(r1)
            json_dic = Base.to_json_string(23)
            json_dic = Base.to_json_string(float(inf))
            json_dic = Base.to_json_string(float(nan))
            json_dic = Base.to_json_string(32.3)
            json_dic = Base.to_json_string("sfsgd")
            json_dic = Base.to_json_string(None)
            json_dic = Base.to_json_string()

    def test_save_to_file(self):
        """Testing save_to_file method in rectangle"""
        r1 = Rectangle(10, 7, 2, 8)
        r2 = Rectangle(2, 4)
        Rectangle.save_to_file([r1, r2])
        with open("Rectangle.json", "r") as files:
            self.assertEqual(len(files.read()), len(str(
                [{"y": 8, "x": 2, "id": 71, "width": 10, "height": 7}, {
                    "y": 0, "x": 0, "id": 82, "width": 2, "height": 4}])))

    def test_save_to_file_sqaure(self):
        """Testing save_to_file method in square"""
        r1 = Square(10, 7, 2, 8)
        r2 = Square(2, 4, 3, 4)
        Square.save_to_file([r1, r2])
        with open("Square.json", "r") as files:
            self.assertEqual(len(files.read()), len(str(
                [{"y": 2, "x": 7, "id": 8, "size": 10}, {
                    "y": 3, "x": 4, "id": 4, "size": 2}])))

    def test_ssave_to_file(self):
        """Testing save_to_file none"""
        Rectangle.save_to_file(None)
        with open("Rectangle.json", "r") as files:
            self.assertEqual(files.read(), "[]")

    def test_ssave_to_file(self):
        """Testing save_to_file none"""
        Square.save_to_file(None)
        with open("Square.json", "r") as files:
            self.assertEqual(files.read(), "[]")

    def test_empty_list_to_json(self):
        """Testing for an empty list as parameter"""
        json_dictionary = Base.to_json_string(None)
        self.assertEqual(json_dictionary, "[]")

    def test_save_to_file_empty_list(self):
        """Testing for an empty list"""
        Rectangle.save_to_file([])
        with open("Rectangle.json", "r") as files:
            self.assertEqual(files.read(), "[]")

    def test_save_to_file_no_param(self):
        """Testing for no parameters in save_to_file"""
        Rectangle.save_to_file(None)
        with open("Rectangle.json", "r") as files:
            self.assertEqual(files.read(), "[]")

    def test_to_file_emptylist(self):
        """Ttesting forr empty list as param"""
        Square.save_to_file([])
        with open("Square.json", "r") as files:
            self.assertEqual(files.read(), "[]")

    def test_from_json_string(self):
        """Testing for from_json_string"""
        list_input = [{'id': 89, 'width': 10, 'height': 4}, {
            'id': 7, 'width': 1, 'height': 7}]
        json_list = Rectangle.to_json_string(list_input)
        list_out = Rectangle.from_json_string(json_list)
        self.assertEqual(list_out, [{'height': 4, 'width': 10, 'id': 89}, {
            'height': 7, 'width': 1, 'id': 7}])
        self.assertTrue(type(list_out) == list)

    def test_from_json_string_square(self):
        """Testing for from_json_string square"""
        list_input = [{'id': 89, 'size': 3}, {
            'id': 7, 'size': 4}]
        json_list = Square.to_json_string(list_input)
        list_out = Square.from_json_string(json_list)
        self.assertEqual(list_out, [{'size': 3, 'id': 89}, {
         'size': 4, 'id': 7}])
        self.assertTrue(type(list_out) == list)


    def test_from_json_string_emptty(self):
        """Testing for none as a parameter"""
        lista = None
        json_list = Rectangle.to_json_string(lista)
        list_out = Rectangle.from_json_string(json_list)
        self.assertEqual(list_out, [])

    def test_from_json_string_None(self):
        """Testing for empty list as a parameter"""
        lista = []
        json_list = Rectangle.to_json_string(lista)
        list_out = Rectangle.from_json_string(json_list)
        self.assertEqual(list_out, [])

    def test_create(self):
        """Testing create method"""
        outvarr = StringIO()
        sys.stdout = outvarr
        r1 = Rectangle(3, 5, 1)
        r1_dictionary = r1.to_dictionary()
        r2 = Rectangle.create(**r1_dictionary)
        print(r1)
        sys.stdout = sys.__stdout__
        self.assertEqual(outvarr.getvalue(), "[Rectangle] (4) 1/0 - 3/5\n")
        self.assertTrue(type(r1) == Rectangle)

    def test_create_sqaure(self):
        """Testing create method"""
        outvarr = StringIO()
        sys.stdout = outvarr
        r1 = Square(3, 5, 1, 3)
        r1_dictionary = r1.to_dictionary()
        r2 = Square.create(**r1_dictionary)
        print(r1)
        sys.stdout = sys.__stdout__
        self.assertEqual(outvarr.getvalue(), "[Square] (3) 5/1 - 3\n")
        self.assertTrue(type(r1) == Square)

    def test_create_more(self):
        """Testing create method"""
        outvarr = StringIO()
        sys.stdout = outvarr
        r1 = Rectangle(3, 5, 1, 0, 4)
        r1_dictionary = r1.to_dictionary()
        r2 = Rectangle.create(**r1_dictionary)
        print(r2)
        sys.stdout = sys.__stdout__
        self.assertEqual(outvarr.getvalue(), "[Rectangle] (4) 1/0 - 3/5\n")
        self.assertTrue(type(r2) == Rectangle)

    def test_create_wrong_param(self):
        """Testing create method with wrong parameters"""
        r1 = Rectangle(3, 5, 1, 0, 4)
        r1_dictionary = r1.to_dictionary()
        with self.assertRaises(TypeError):
            r1 = Rectangle.create(None)
            r1 = Rectangle.create(213)
            r1 = Rectangle.create("asdf")
            r2 = Rectangle.create(float(inf))
        with self.assertRaises(NameError):
            r1 = Rectangle.create(asdf)

    def test_load_from_json(self):
        """Testin test_load_from_json"""
        outvarr = StringIO()
        sys.stdout = outvarr
        r1 = Rectangle(10, 7, 2, 8)
        r2 = Rectangle(2, 4)
        list_rectangles_input = [r1, r2]
        Rectangle.save_to_file(list_rectangles_input)
        list_rectangles_output = Rectangle.load_from_file()

        print(format(list_rectangles_output[0]))
        sys.stdout = sys.__stdout__
        self.assertEqual(outvarr.getvalue(), "[Rectangle] (8) 2/8 - 10/7\n")
        self.assertTrue(type(list_rectangles_output) == list)

        outvarr = StringIO()
        sys.stdout = outvarr
        print(format(list_rectangles_output[1]))
        sys.stdout = sys.__stdout__
        self.assertEqual(outvarr.getvalue(), "[Rectangle] (9) 0/0 - 2/4\n")

        outvarr = StringIO()
        sys.stdout = outvarr
        s1 = Square(5)
        s2 = Square(7, 9, 1)
        list_squares_input = [s1, s2]
        Square.save_to_file(list_squares_input)
        list_squares_output = Square.load_from_file()
        print(format(list_squares_output[0]))
        sys.stdout = sys.__stdout__
        self.assertEqual(outvarr.getvalue(), "[Square] (12) 0/0 - 5\n")
        self.assertTrue(type(list_squares_output) == list)

        outvarr = StringIO()
        sys.stdout = outvarr
        print(format(list_squares_output[1]))
        sys.stdout = sys.__stdout__
        self.assertEqual(outvarr.getvalue(), "[Square] (13) 9/1 - 7\n")


if __name__ == "__main__":
    unittest.main()
