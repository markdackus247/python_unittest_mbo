import unittest
from Models.MarkProcessor import MarkProcessor

class TestMarkProcessor(unittest.TestCase):
    def setUp(self):
        self.processor = MarkProcessor()

    def test_check_exit_command(self):
        self.assertTrue(self.processor.check_exit_command('q'))
        self.assertTrue(self.processor.check_exit_command('quit'))
        self.assertTrue(self.processor.check_exit_command('exit'))
        self.assertFalse(self.processor.check_exit_command('continue'))

    def test_check_characters(self):
        self.assertTrue(self.processor.check_characters('123'))
        self.assertTrue(self.processor.check_characters('12.3'))
        self.assertTrue(self.processor.check_characters('12,3'))
        self.assertFalse(self.processor.check_characters('12a3'))

    def test_replace_comma_with_dot(self):
        self.assertEqual(self.processor.replace_comma_with_dot('12,3'), '12.3')
        self.assertEqual(self.processor.replace_comma_with_dot('1.234.356'), '1234356')
        self.assertEqual(self.processor.replace_comma_with_dot('1.234.356,98'), '1234356.98')
        self.assertEqual(self.processor.replace_comma_with_dot('1,234,356,98'), '123435698')
        self.assertEqual(self.processor.replace_comma_with_dot('1,234,356.98'), '1234356.98')
        # self.assertFalse(self.processor.replace_comma_with_dot('1.234,356.98'))   # Moet false returneren maar dat doet deze functie nog niet.

    def test_is_float(self):
        self.assertTrue(self.processor.is_float(1.23))
        self.assertTrue(self.processor.is_float('123'))
        self.assertTrue(self.processor.is_float('12.3'))
        self.assertFalse(self.processor.is_float('12.3.4'))
        self.assertFalse(self.processor.is_float('abc'))

    def test_convert_to_number(self):
        self.assertEqual(self.processor.convert_to_number('12.3'), 12.3)
        self.assertEqual(self.processor.convert_to_number('123'), 123.0)
        self.assertFalse(self.processor.convert_to_number('abc'))

    def test_is_mark(self):
        self.assertTrue(self.processor.is_mark(1.0))
        self.assertTrue(self.processor.is_mark(5.5))
        self.assertTrue(self.processor.is_mark(10.0))
        self.assertFalse(self.processor.is_mark(0.9))
        self.assertFalse(self.processor.is_mark(10.1))

if __name__ == '__main__':
    unittest.main()
