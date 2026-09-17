import unittest

from temperature import celsius_to_fahrenheit


class CelsiusToFahrenheitTests(unittest.TestCase):
    def test_converts_common_reading(self) -> None:
        self.assertEqual(celsius_to_fahrenheit(25), 77)

    def test_converts_freezing_point(self) -> None:
        self.assertEqual(celsius_to_fahrenheit(0), 32)

    def test_converts_negative_reading(self) -> None:
        self.assertEqual(celsius_to_fahrenheit(-40), -40)


if __name__ == "__main__":
    unittest.main()
