"""Unittest for Base class
"""
import unittest
from models.base import Base


class Test_base(unittest.TestCase):
    """ A Test_base class"""
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
        self.assertEqual(bb.id, 4)

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


if __name__ == "__main__":
    unittest.main()
