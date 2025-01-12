import unittest
from io import StringIO

from main import ask_all_marks, average

from unittest.mock import patch


class TestAskAllMarks(unittest.TestCase):
    @patch('builtins.input', side_effect=['8.0', '8.3', '2.8', '5.4', '1.2', 'q'])
    @patch('sys.stdout', new_callable=StringIO)
    def test_multiple_values_output(self, mock_stdout, mock_input):
        marks = ask_all_marks('Cijfer')
        average_marks = average(marks)
        print(f'Het gemiddelde van de {len(marks)} ingevoerd cijfers is {average_marks:.1f}')
        self.assertIn('Het gemiddelde van de 5 ingevoerd cijfers is 5.1', mock_stdout.getvalue())
