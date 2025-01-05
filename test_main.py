import unittest
from io import StringIO

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

    @patch('builtins.input', side_effect=['8.0', '8.3', '2.8', '5.4', '1.2', 'q'])
    @patch('sys.stdout', new_callable=StringIO)
    def test_multiple_values_output(self, mock_stdout, mock_input):
        marks = ask_all_marks('Cijfer')
        average_marks = average(marks)
        print(f'Het gemiddelde van de {len(marks)} ingevoerd cijfers is {average_marks:.1f}')
        self.assertIn('Het gemiddelde van de 5 ingevoerd cijfers is 5.1', mock_stdout.getvalue())


if __name__ == '__main__':
    unittest.main()