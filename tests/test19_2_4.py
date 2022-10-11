import pytest

from app.calc import Calculator


class TestCalc:
    def setup(self):
        self.calc = Calculator()

    def test_adding_success(self):
        assert self.calc.adding(1, 1) == 2

    def test_substraction_success(self):
        assert self.calc.substraction(5, 5) == 0

    def test_multiply_success(self):
        assert self.calc.multiply(3, 4) == 12

    def test_division_success(self):
        assert self.calc.division(18, 6) == 3

    def teardown(self):
        print('Выполнение метода Teardown')
