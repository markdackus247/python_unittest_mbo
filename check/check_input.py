import unittest

from check.input import ask_all_marks


from unittest.mock import patch

class TestAskAllMarks(unittest.TestCase):
    @patch('builtins.input', side_effect=['q'])
    def test_empty_list(self, mock_input):
        self.assertEqual(ask_all_marks('Cijfer'), [], "Als de lijst leeg is dan is het cijfer onvoldoende.")

    @patch('builtins.input', side_effect=['5', 'q'])
    def test_single_value(self, mock_input):
        self.assertEqual(ask_all_marks('Cijfer'), [5], "Het gemiddelde van één cijfer is het cijfer zelf.")

    @patch('builtins.input', side_effect=['8.0', '8.3', '2.8', '5.4', '1.2', 'q'])
    def test_multiple_values(self, mock_input):
        self.assertEqual(ask_all_marks('Cijfer'), [8.0, 8.3, 2.8, 5.4, 1.2], "Het gemiddelde van deze getallen moet 5.54 zijn.")

    @patch('builtins.input', side_effect=['1', '2', '3', '4', '5', 'q'])
    def test_rounded_average(self, mock_input):
        self.assertEqual(ask_all_marks('Cijfer'), [1, 2, 3, 4, 5], "Het gemiddelde van de lijst [1, 2, 3, 4, 5] is een 3.0.")

if __name__ == '__main__':
    unittest.main()