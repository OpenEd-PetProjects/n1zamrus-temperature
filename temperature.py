"""Small, hardware-independent temperature calculations."""


def celsius_to_fahrenheit(celsius: float) -> float:
    """Convert a Celsius reading to Fahrenheit."""
    return celsius * 9 / 5 + 32
