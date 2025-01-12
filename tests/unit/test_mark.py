from unittest import TestCase, main

from calc.marks import average

# Unit test class
class TestAverage(TestCase):
    def test_empty_list(self):
        self.assertEqual(average([]), 0, "Als de lijst leeg is dan is het cijfer onvoldoende.")

    def test_single_value(self):
        self.assertEqual(average([5]), 5, "Het gemiddelde van één cijfer is het cijfer zelf.")

    def test_multiple_values(self):
        self.assertAlmostEqual(average([8.0, 8.3, 2.8, 5.4, 1.2]), 5.14, places=1, msg="Het gemiddelde van deze getallen moet 5.54 zijn.")

    def test_rounded_average(self):
        self.assertAlmostEqual(average([1, 2, 3, 4, 5]), 3.0, places=1, msg="Het gemiddelde van de lijst [1, 2, 3, 4, 5] is een 3.0.")

if __name__ == '__main__':
    main()
