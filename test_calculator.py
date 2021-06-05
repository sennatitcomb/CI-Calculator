"""
Tests for calc app
"""
import calculator


class TestCalculatorApp:
    def test_add(self):
        assert 5 == calculator.add(3, 2)

    def test_subtract(self):
        assert 5 == calculator.sub(10, 5)

    def test_multiply(self):
        assert 4 == calculator.multiply(2, 2)

    def test_divide(self):
        assert 8 == calculator.divide(16, 2)
