import pytest
from app.calculator import Calculator


class TestCalc:
    def setup_class(self):
        self.calc = Calculator()

    def test_multiply_calculate_correctly(self):
        assert self.calc.multiply(3, 3) == 9

    def test_division_calculate_correctly(self):
        assert self.calc.division(49, 7) == 7

    def test_subtraction_calculate_correctly(self):
        assert self.calc.subtraction( 10, 9) == 1

    def test_adding_calculate_correctly(self):
        assert self.calc.adding(6, 6) == 12
