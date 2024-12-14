from unittest import TestCase, main
from math import pi

from utilities.is_float import is_float


# Unit test class
class TestIsFloat(TestCase):
    # Test drie verschillende gehele getallen om te controleren
    # of integers ook worden gezien als floats.
    def test_is_integer(self):
        # Test positief getal 5
        self.assertEqual(
            is_float(5),
            True,
            'Integer 5 is also a float'
        )

        # Test negatief getal -12
        self.assertEqual(
            is_float(-12),
            True,
            'Integer -12 is also a float'
        )

        # Test neutraal getal 0
        self.assertEqual(
            is_float(0),
            True,
            'Integer 0 is also a float'
        )

    # Test drie verschillende gehele getallen om te controleren
    # of decimale getallen ook worden gezien als floats.
    def test_is_float(self):
        # Test of 7.3 een float is.
        self.assertEqual(
            is_float(7.3),
            True,
            msg='Number 7.3 is a float.'
        )

        # Test of -0.777 een float is
        self.assertEqual(
            is_float(-0.777),
            True,
            msg='Number -0.777 is a float.'
        )

        # Test of pi een float is
        self.assertEqual(
            is_float(pi),
            True,
            msg='Number pi is a float.'
        )

    # Test drie verschillende strings met gehele getallen om te controleren
    # of deze ook worden gezien als floats.
    def test_is_string_is_integer(self):
        # Test of '7' een float is.
        self.assertEqual(
            is_float('7'),
            True,
            msg='String "7" is a float.'
        )

        # Test of '12' een float is.
        self.assertEqual(
            is_float('12'),
            True,
            msg='String "12" is a float.'
        )

        # Test of '0' een float is.
        self.assertEqual(
            is_float('0'),
            True,
            msg='String "0" is a float.'
        )

    # Test drie verschillende strings met decimale getallen om te controleren
    # of deze ook worden gezien als floats.
    def test_is_float_is_integer(self):
        # Test of '7.3' een float is.
        self.assertEqual(
            is_float('7.3'),
            True,
            msg='Number "7.3" is a float.'
        )

        # Test of "-0.777" een float is
        self.assertEqual(
            is_float('-0.777'),
            True,
            msg='Number "-0.777" is a float.'
        )

        # Test of "pi" een float is
        self.assertEqual(
            is_float('pi'),
            True,
            msg='Number "pi" is a float.'
        )


if __name__ == '__main__':
    main()
