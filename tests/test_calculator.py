from calculator.calculator import Calculator
import pytest

class TestCalculator:
    def test_add(self):
        # Arrange
        a = 4321
        b = 1234
        cal = Calculator()

        # Act
        result = cal.add(a, b)

        # Assert
        expected = 5555
        assert result == expected
        
    def test_minus(self):
        # Arrange
        a = 5000
        b = 4000
        cal = Calculator()

        # Act
        result2 = cal.subtract(a, b)
        
        # Assert
        expected2 = 1000
        assert result2 == expected2

    def test_divide(self):
        # Arrange
        a = 4
        b = 2
        cal = Calculator()

        # Act & Assert for ZeroDivisionError
        with pytest.raises(ZeroDivisionError, match="Division by zero error"):
            cal.divide(a, 0)
        
        # Act for normal division
        result3 = cal.divide(a, b)
        
        # Assert
        expected3 = 2
        assert result3 == expected3

    def test_multiply(self):
        # Arrange
        a = 4
        b = 2
        cal = Calculator()

        # Act
        result4 = cal.multiply(a, b)
        
        # Assert
        expected4 = 8
        assert result4 == expected4

    def test_divide_by_zero(self):
        # Arrange
        a = 4
        cal = Calculator()

        # Act & Assert
        with pytest.raises(ZeroDivisionError, match="Division by zero error"):
            cal.divide(a, 0)
