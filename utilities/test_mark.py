from unittest import TestCase

from utilities.mark import is_mark

class TestMark(TestCase):
    def test_is_mark(self):
        self.assertEqual(is_mark(0.9), False, 'Getal is kleiner dan 1.')
        self.assertEqual(is_mark(1.0), True, '...')
        self.assertEqual(is_mark(5.5), True, '...')
        self.assertEqual(is_mark(10.0), True, '...')
        self.assertEqual(is_mark(10.1), False, 'Getal is groter dan 10')
