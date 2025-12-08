"""
Test suite for the Calculator class.
"""

import pytest
from calculator.calculator import Calculator, InvalidInputException


@pytest.fixture
def calc():
    """Fixture to create a Calculator instance for tests."""
    return Calculator()


class TestAddition:
    """Tests for the add method."""

    def test_add_with_too_large_value_raises_exception(self, calc):
        """Test that adding with a value > 1000000 raises InvalidInputException."""
        # Arrange
        a = 1000001
        b = 5

        # Act & Assert
        with pytest.raises(InvalidInputException):
            calc.add(a, b)

    def test_add_with_second_param_too_large_raises_exception(self, calc):
        """Test that adding with second value > 1000000 raises InvalidInputException."""
        # Arrange
        a = 5
        b = 1000001

        # Act & Assert
        with pytest.raises(InvalidInputException):
            calc.add(a, b)

    def test_add_with_too_small_value_raises_exception(self, calc):
        """Test that adding with a value < -1000000 raises InvalidInputException."""
        # Arrange
        a = -1000001
        b = 5

        # Act & Assert
        with pytest.raises(InvalidInputException):
            calc.add(a, b)

    def test_add_with_second_param_too_small_raises_exception(self, calc):
        """Test that adding with second value < -1000000 raises InvalidInputException."""
        # Arrange
        a = 5
        b = -1000001

        # Act & Assert
        with pytest.raises(InvalidInputException):
            calc.add(a, b)

    def test_subtract_with_too_large_value_raises_exception(self, calc):
        """Test that subtracting with a value > 1000000 raises InvalidInputException."""
        # Arrange
        a = 1000001
        b = 5

        # Act & Assert
        with pytest.raises(InvalidInputException):
            calc.subtract(a, b)

    def test_subtract_with_second_param_too_large_raises_exception(self, calc):
        """Test that subtracting with second value > 1000000 raises InvalidInputException."""
        # Arrange
        a = 5
        b = 1000001

        # Act & Assert
        with pytest.raises(InvalidInputException):
            calc.subtract(a, b)

    def test_multiply_with_too_small_value_raises_exception(self, calc):
        """Test that multiplying with a value < -1000000 raises InvalidInputException."""
        # Arrange
        a = 5
        b = -1000001

        # Act & Assert
        with pytest.raises(InvalidInputException):
            calc.multiply(a, b)

    def test_multiply_with_first_param_too_small_raises_exception(self, calc):
        """Test that multiplying with first value < -1000000 raises InvalidInputException."""
        # Arrange
        a = -1000001
        b = 5

        # Act & Assert
        with pytest.raises(InvalidInputException):
            calc.multiply(a, b)

    def test_divide_with_too_large_value_raises_exception(self, calc):
        """Test that dividing with a value > 1000000 raises InvalidInputException."""
        # Arrange
        a = 1000001
        b = 2

        # Act & Assert
        with pytest.raises(InvalidInputException):
            calc.divide(a, b)

    def test_divide_with_second_param_too_large_raises_exception(self, calc):
        """Test that dividing with second value > 1000000 raises InvalidInputException."""
        # Arrange
        a = 5
        b = 1000001

        # Act & Assert
        with pytest.raises(InvalidInputException):
            calc.divide(a, b)

    def test_add_at_max_boundary(self, calc):
        """Test adding at the maximum boundary value."""
        # Arrange
        a = 1000000
        b = 0
        expected = 1000000

        # Act
        result = calc.add(a, b)

        # Assert
        assert result == expected

    def test_add_at_min_boundary(self, calc):
        """Test adding at the minimum boundary value."""
        # Arrange
        a = -1000000
        b = 0
        expected = -1000000

        # Act
        result = calc.add(a, b)

        # Assert
        assert result == expected

    def test_subtract_at_max_boundary(self, calc):
        """Test subtracting at the maximum boundary value."""
        # Arrange
        a = 1000000
        b = 0
        expected = 1000000

        # Act
        result = calc.subtract(a, b)

        # Assert
        assert result == expected

    def test_multiply_at_min_boundary(self, calc):
        """Test multiplying at the minimum boundary value."""
        # Arrange
        a = -1000000
        b = 1
        expected = -1000000

        # Act
        result = calc.multiply(a, b)

        # Assert
        assert result == expected

    def test_divide_at_max_boundary(self, calc):
        """Test dividing at the maximum boundary value."""
        # Arrange
        a = 1000000
        b = 1
        expected = 1000000

        # Act
        result = calc.divide(a, b)

        # Assert
        assert result == expected

    def test_both_values_at_boundaries(self, calc):
        """Test operation with both values at boundaries."""
        # Arrange
        a = 1000000
        b = -1000000
        expected = 0

        # Act
        result = calc.add(a, b)

        # Assert
        assert result == expected


class TestSubtraction:
    """Tests for the subtract method."""

    def test_subtract_positive_numbers(self, calc):
        """Test subtracting positive numbers."""
        # Arrange
        a = 10
        b = 3
        expected = 7

        # Act
        result = calc.subtract(a, b)

        # Assert
        assert result == expected

    def test_subtract_negative_numbers(self, calc):
        """Test subtracting two negative numbers."""
        # Arrange
        a = -5
        b = -3
        expected = -2

        # Act
        result = calc.subtract(a, b)

        # Assert
        assert result == expected

    def test_subtract_positive_from_negative(self, calc):
        """Test subtracting positive from negative number."""
        # Arrange
        a = -5
        b = 3
        expected = -8

        # Act
        result = calc.subtract(a, b)

        # Assert
        assert result == expected

    def test_subtract_negative_from_positive(self, calc):
        """Test subtracting negative from positive number."""
        # Arrange
        a = 5
        b = -3
        expected = 8

        # Act
        result = calc.subtract(a, b)

        # Assert
        assert result == expected

    def test_subtract_zero(self, calc):
        """Test subtracting zero from a number."""
        # Arrange
        a = 5
        b = 0
        expected = 5

        # Act
        result = calc.subtract(a, b)

        # Assert
        assert result == expected

    def test_subtract_from_zero(self, calc):
        """Test subtracting a number from zero."""
        # Arrange
        a = 0
        b = 5
        expected = -5

        # Act
        result = calc.subtract(a, b)

        # Assert
        assert result == expected

    def test_subtract_floats(self, calc):
        """Test subtracting floating point numbers."""
        # Arrange
        a = 5.5
        b = 2.3
        expected = 3.2

        # Act
        result = calc.subtract(a, b)

        # Assert
        assert result == pytest.approx(expected)


class TestMultiplication:
    """Tests for the multiply method."""

    def test_multiply_positive_numbers(self, calc):
        """Test multiplying positive numbers."""
        # Arrange
        a = 5
        b = 3
        expected = 15

        # Act
        result = calc.multiply(a, b)

        # Assert
        assert result == expected

    def test_multiply_negative_numbers(self, calc):
        """Test multiplying two negative numbers."""
        # Arrange
        a = -5
        b = -3
        expected = 15

        # Act
        result = calc.multiply(a, b)

        # Assert
        assert result == expected

    def test_multiply_positive_and_negative(self, calc):
        """Test multiplying positive and negative numbers."""
        # Arrange
        a = 5
        b = -3
        expected = -15

        # Act
        result = calc.multiply(a, b)

        # Assert
        assert result == expected

    def test_multiply_negative_and_positive(self, calc):
        """Test multiplying negative and positive numbers."""
        # Arrange
        a = -5
        b = 3
        expected = -15

        # Act
        result = calc.multiply(a, b)

        # Assert
        assert result == expected

    def test_multiply_by_zero(self, calc):
        """Test multiplying by zero."""
        # Arrange
        a = 5
        b = 0
        expected = 0

        # Act
        result = calc.multiply(a, b)

        # Assert
        assert result == expected

    def test_multiply_zero_by_number(self, calc):
        """Test multiplying zero by a number."""
        # Arrange
        a = 0
        b = 5
        expected = 0

        # Act
        result = calc.multiply(a, b)

        # Assert
        assert result == expected

    def test_multiply_by_one(self, calc):
        """Test multiplying by one."""
        # Arrange
        a = 5
        b = 1
        expected = 5

        # Act
        result = calc.multiply(a, b)

        # Assert
        assert result == expected

    def test_multiply_floats(self, calc):
        """Test multiplying floating point numbers."""
        # Arrange
        a = 2.5
        b = 4.0
        expected = 10.0

        # Act
        result = calc.multiply(a, b)

        # Assert
        assert result == pytest.approx(expected)


class TestDivision:
    """Tests for the divide method."""

    def test_divide_positive_numbers(self, calc):
        """Test dividing positive numbers."""
        # Arrange
        a = 10
        b = 2
        expected = 5

        # Act
        result = calc.divide(a, b)

        # Assert
        assert result == expected

    def test_divide_negative_numbers(self, calc):
        """Test dividing two negative numbers."""
        # Arrange
        a = -10
        b = -2
        expected = 5

        # Act
        result = calc.divide(a, b)

        # Assert
        assert result == expected

    def test_divide_positive_by_negative(self, calc):
        """Test dividing positive by negative number."""
        # Arrange
        a = 10
        b = -2
        expected = -5

        # Act
        result = calc.divide(a, b)

        # Assert
        assert result == expected

    def test_divide_negative_by_positive(self, calc):
        """Test dividing negative by positive number."""
        # Arrange
        a = -10
        b = 2
        expected = -5

        # Act
        result = calc.divide(a, b)

        # Assert
        assert result == expected

    def test_divide_by_one(self, calc):
        """Test dividing by one."""
        # Arrange
        a = 5
        b = 1
        expected = 5

        # Act
        result = calc.divide(a, b)

        # Assert
        assert result == expected

    def test_divide_zero_by_number(self, calc):
        """Test dividing zero by a number."""
        # Arrange
        a = 0
        b = 5
        expected = 0

        # Act
        result = calc.divide(a, b)

        # Assert
        assert result == expected

    def test_divide_with_remainder(self, calc):
        """Test dividing numbers with remainder (float result)."""
        # Arrange
        a = 7
        b = 2
        expected = 3.5

        # Act
        result = calc.divide(a, b)

        # Assert
        assert result == pytest.approx(expected)

    def test_divide_floats(self, calc):
        """Test dividing floating point numbers."""
        # Arrange
        a = 10.5
        b = 2.0
        expected = 5.25

        # Act
        result = calc.divide(a, b)

        # Assert
        assert result == pytest.approx(expected)

    def test_divide_by_zero_raises_exception(self, calc):
        """Test that dividing by zero raises ValueError."""
        # Arrange
        a = 5
        b = 0

        # Act & Assert
        with pytest.raises(ValueError):
            calc.divide(a, b)

    def test_divide_zero_by_zero_raises_exception(self, calc):
        """Test that dividing zero by zero raises ValueError."""
        # Arrange
        a = 0
        b = 0

        # Act & Assert
        with pytest.raises(ValueError):
            calc.divide(a, b)


class TestInputValidation:
    """Tests for input validation."""

    def test_add_with_too_large_value_raises_exception(self, calc):
        """Test that adding with a value > 1000000 raises InvalidInputException."""
        # Arrange
        a = 1000001
        b = 5

        # Act & Assert
        with pytest.raises(InvalidInputException):
            calc.add(a, b)

    def test_add_with_too_small_value_raises_exception(self, calc):
        """Test that adding with a value < -1000000 raises InvalidInputException."""
        # Arrange
        a = -1000001
        b = 5

        # Act & Assert
        with pytest.raises(InvalidInputException):
            calc.add(a, b)

    def test_subtract_with_too_large_value_raises_exception(self, calc):
        """Test that subtracting with a value > 1000000 raises InvalidInputException."""
        # Arrange
        a = 1000001
        b = 5

        # Act & Assert
        with pytest.raises(InvalidInputException):
            calc.subtract(a, b)

    def test_multiply_with_too_small_value_raises_exception(self, calc):
        """Test that multiplying with a value < -1000000 raises InvalidInputException."""
        # Arrange
        a = 5
        b = -1000001
        # Act & Assert
        with pytest.raises(InvalidInputException):
            calc.multiply(a, b)

    def test_divide_with_too_large_value_raises_exception(self, calc):
        """Test that dividing with a value > 1000000 raises InvalidInputException."""
        # Arrange
        a = 1000001
        b = 2

        # Act & Assert
        with pytest.raises(InvalidInputException):
            calc.divide(a, b)