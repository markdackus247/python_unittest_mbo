import unittest

from main import ask_all_marks, average

from unittest.mock import patch


class TestAskAllMarks(unittest.TestCase):
    @patch('builtins.input', side_effect=['8.0', '8.3', '2.8', '5.4', '1.2', 'q'])
    def test_multiple_values(self, mock_input):
        self.assertEqual(ask_all_marks('Cijfer'), [8.0, 8.3, 2.8, 5.4, 1.2], "De ingevoerde cijfers zijn 8.0, 8.3, 2.8, 5.4 en 1.2.")

    @patch('builtins.input', side_effect=['8.0', '8.3', '2.8', '5.4', '1.2', 'q'])
    def test_multiple_values_average(self, mock_input):
        marks = ask_all_marks('Cijfer')
        self.assertEqual(average(marks), 5.14, "Het gemiddelde van deze getallen moet 5.14 zijn.")
