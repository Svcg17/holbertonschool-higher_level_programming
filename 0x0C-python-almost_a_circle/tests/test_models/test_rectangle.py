"""Unittest for the Rectangle class
"""


import unittest
import sys
from io import StringIO
from models.base import Base
from models.rectangle import Rectangle


class Test_rectangle(unittest.TestCase):
    """A Test_rectangle class
    """
    def set_up(self):
        """Resets __nb_objects"""
        Base._Base__nb_objects = 0

    """A Test_rectangle class"""
    def test_assignment(self):
        """Creating instance with values"""
        r1 = Rectangle(10, 2)
        self.assertTrue(type(r1), Rectangle)

    def test_oneparam(self):
        """Passing one arg to instance declaration"""
        with self.assertRaises(TypeError):
            r1 = Rectangle(3)

    def test_allparams(self):
        """Passing all valid parameters"""
        r1 = Rectangle(1, 2, 3, 4, 5)

    def test_str(self):
        """Passing str to the instance"""
        with self.assertRaises(TypeError):
            r1 = Rectangle("sdf")

    def test_stringmoerparam(self):
        """Passing string in different position"""
        with self.assertRaises(TypeError):
            r1 = Rectangle(1, "2")
            r1 = Rectangle(1, 2, "3")
            r1 = Rectangle(1, 2, 3, "4")

    def test_noparam(self):
        """Passing no arguments"""
        with self.assertRaises(TypeError):
            r1 = Rectangle()

    def test_unknowntype(self):
        """Passing unknown parameter"""
        with self.assertRaises(NameError):
            r1 = Rectangle(soda)

    def test_toomany(self):
        """Passing more args than expected"""
        with self.assertRaises(TypeError):
            r1 = Rectangle(1, 2, 3, 4, 5, 6, 7)

    def test_negatives(self):
        """Passing only negative numbers"""
        with self.assertRaises(ValueError):
            r1 = Rectangle(-1, -3, -2, -2, -3)
            r1 = Rectangle(1, 2, 3, -4)

    def test_neganndpos(self):
        """Passing both negative and positve integers"""
        with self.assertRaises(ValueError):
            r2 = Rectangle(-1, 2)
            r3 = Rectangle(1, -2)
            r4 = Rectangle(1, 0)
            r1 = Rectangle(2, -3, 23, -2, -3)

    def test_zero(self):
        """Passing zeros
            r1 = pass 0 to x or y
            r2 = pass 0 to width or height
        """
        r1 = Rectangle(32, 3, 0, 4, 4)
        with self.assertRaises(ValueError):
            r2 = Rectangle(0, 8, 8, 7, 6)

    def test_specialfloat(self):
        """Passing different floats as param
            r1 = pass float to x or y
            r2 = pass float to width or heigth
        """
        with self.assertRaises(TypeError):
            r1 = Rectangle(23.4, 3, 4, 5, 4)
            r2 = Rectangle(45, 6, 5.4, 5.4, 5)
            r3 = Rectangle(3, float('inf'), 3, 4)
            r4 = Rectangle(3, 3, float('nan'), 4, 4)

    def test_None(self):
        """Passing none as arg"""
        with self.assertRaises(TypeError):
            r1 = Rectangle(None, 67)

    def test_area(self):
        """Testing area method"""
        r1 = Rectangle(8, 7, 0, 0, 12)
        self.assertEqual(r1.area(), 56)

    def test_areawithparam(self):
        """Test params being passed to area function"""
        r1 = Rectangle(8, 7, 0, 0, 12)
        with self.assertRaises(TypeError):
            r1.area(3)

    def test_display(self):
        """Testing display method"""
        outvar = StringIO()
        sys.stdout = outvar
        r2 = Rectangle(2, 2)
        r2.display()
        sys.stdout = sys.__stdout__
        assert outvar.getvalue() == '##\n##\n'

    def test_display_x_y_(self):
        """Testing display method with x and y variables"""
        outvar = StringIO()
        sys.stdout = outvar
        r2 = Rectangle(2, 3, 2, 2)
        r2.display()
        sys.stdout = sys.__stdout__
        assert outvar.getvalue() == '\n\n  ##\n  ##\n  ##\n'

    def test_sttrr(self):
        """Testing the __str__ method"""
        outvar = StringIO()
        sys.stdout = outvar
        r3 = Rectangle(4, 6, 2, 1, 12)
        print(r3)
        sys.stdout = sys.__stdout__
        assert outvar.getvalue() == "[Rectangle] (12) 2/1 - 4/6\n"

    def test_strnameerror(self):
        """trying to print unknown value"""
        outvar = StringIO()
        sys.stdout = outvar
        with self.assertRaises(NameError):
            r3 = Rectangle(4, 6, 2, 1, 12)
            print(sf)
        sys.stdout = sys.__stdout__

    def test_update(self):
        """Testing update method"""
        outvar = StringIO()
        sys.stdout = outvar
        r3 = Rectangle(10, 10, 10, 10)
        r3.update(89, 2, 3, 4, 5)
        print(r3)
        sys.stdout = sys.__stdout__

    def test_updatemore(self):
        """Testing too many params in update"""
        outvar = StringIO()
        sys.stdout = outvar
        r3 = Rectangle(10, 10, 10, 10, 10)
        r3.update(89, 2, 3, 4, 5, 6)
        print(r3)
        sys.stdout = sys.__stdout__

    def test_updatenonint(self):
        """Testing for ints in the update methods"""
        outvar = StringIO()
        sys.stdout = outvar
        with self.assertRaises(TypeError):
            r3 = Rectangle(10, 10, 10, 10, 10)
            r3.update(89, 2, "Df")
            r3.update(34.4, 4, 4)
        sys.stdout = sys.__stdout__

    def test_updatenoparam(self):
        """Testing for no params """
        outvar = StringIO()
        sys.stdout = outvar
        r3 = Rectangle(10, 10, 10, 10, 10)
        r3.update()
        print(r3)
        sys.stdout = sys.__stdout__

    def test_updatenegative(self):
        """Testing for neg params """
        outvar = StringIO()
        sys.stdout = outvar
        with self.assertRaises(ValueError):
            r3 = Rectangle(10, 10, 10, 10, 10)
            r3.update(-34, -4, 4)
        sys.stdout = sys.__stdout__

    def test_updatekwargs(self):
        """Testing update with *kwargs"""
        outvar = StringIO()
        sys.stdout = outvar
        rr = Rectangle(10, 10, 10, 10, 10)
        rr.update(x=3, id=89, y=1, width=2)
        print(rr)
        self.assertTrue(rr.x == 3)
        self.assertTrue(rr.id == 89)
        self.assertTrue(rr.y == 1)
        self.assertTrue(rr.width == 2)
        sys.stdout = sys.__stdout__

    def test_morekwargs(self):
        """Testing for unknown arggs:"""
        outvar = StringIO()
        sys.stdout = outvar
        r3 = Rectangle(10, 10, 10, 10, 10)
        r3.update(x=3, y=4, width=4, height=5, id=3, fakename=34)
        self.assertTrue(r3.x == 3)
        self.assertTrue(r3.y == 4)
        self.assertTrue(r3.width == 4)
        print(r3)
        sys.stdout = sys.__stdout__
        self.assertEqual(outvar.getvalue(), "[Rectangle] (3) 3/4 - 4/5\n")

    def test_to_dictionary(self):
        """Testing to_dictionary function"""
        r1 = Rectangle(10, 2, 1, 9, 3)
        r1_dic = r1.to_dictionary()
        self.assertEqual(r1_dic, {
            'x': 1, 'y': 9, 'id': 3, 'height': 2, 'width': 10})

    def test_to_dictionary_with_update(self):
        """Testing passing a dict with to_dictioanry in update method"""
        outvarr = StringIO()
        sys.stdout = outvarr
        r1 = Rectangle(10, 2, 1, 9, 3)
        r1_dic = r1.to_dictionary()
        r2 = Rectangle(1, 1)
        r2.update(**r1_dic)
        print(r2)
        sys.stdout = sys.__stdout__
        self.assertEqual(outvarr.getvalue(), "[Rectangle] (3) 1/9 - 10/2\n")

    def test_to_dictionary_with_params(self):
        """Testing passing a parameter to t_dictionary metthod"""
        with self.assertRaises(TypeError):
            r1 = Rectangle(10, 2, 1, 9, 3)
            r1_dic = r1.to_dictionary(33)
            r1_dic = r1.to_dictionary(None)
            r1_dic = r1.to_dictionary("sdf")


if __name__ == "__main__":
    unittest.main()
