import pytest

from src.calculator.operations import CalculatorError


class TestCalculatorInitialization:
    def test_initial_state(self, calc):
        """Test that calculator starts with no last result"""
        assert calc.last_result is None

    def test_initial_get_last_result_raises_error(self, calc):
        """Test that getting initial last result raises error"""
        with pytest.raises(CalculatorError) as exc_info:
            calc.get_last_result()
        assert str(exc_info.value) == "No result available"


class TestAddition:
    @pytest.mark.parametrize(
        "x, y, expected",
        [
            (1, 1, 2),
            (-1, 1, 0),
            (0, 0, 0),
            (0.1, 0.2, 0.3),
            (-1.5, -1.5, -3.0),
            (1000000, 1000000, 2000000),
        ],
        ids=[
            "positive_integers",
            "mixed_signs",
            "zeros",
            "decimals",
            "negative_decimals",
            "large_numbers",
        ],
    )
    def test_add(self, calc, x, y, expected):
        """Test addition with various number combinations"""
        result = calc.add(x, y)
        assert result == pytest.approx(expected)
        assert calc.last_result == pytest.approx(expected)


class TestSubtraction:
    @pytest.mark.parametrize(
        "x, y, expected",
        [
            (5, 3, 2),
            (1, 1, 0),
            (0, 5, -5),
            (10.5, 0.5, 10),
            (-5, -3, -2),
            (1000000, 1, 999999),
        ],
        ids=[
            "positive_diff",
            "zero_diff",
            "negative_result",
            "decimals",
            "negative_numbers",
            "large_numbers",
        ],
    )
    def test_subtract(self, calc, x, y, expected):
        """Test subtraction with various number combinations"""
        result = calc.subtract(x, y)
        assert result == pytest.approx(expected)
        assert calc.last_result == pytest.approx(expected)


class TestMultiplication:
    @pytest.mark.parametrize(
        "x, y, expected",
        [
            (2, 3, 6),
            (0, 5, 0),
            (-2, 3, -6),
            (0.5, 0.5, 0.25),
            (-2, -2, 4),
            (1000, 1000, 1000000),
        ],
        ids=[
            "positive_numbers",
            "zero",
            "mixed_signs",
            "decimals",
            "negative_numbers",
            "large_numbers",
        ],
    )
    def test_multiply(self, calc, x, y, expected):
        """Test multiplication with various number combinations"""
        result = calc.multiply(x, y)
        assert result == pytest.approx(expected)
        assert calc.last_result == pytest.approx(expected)


class TestDivision:
    @pytest.mark.parametrize(
        "x, y, expected",
        [
            (6, 2, 3),
            (5, 2, 2.5),
            (-6, 2, -3),
            (0, 5, 0),
            (10.5, 0.5, 21),
            (1000000, 1000, 1000),
        ],
        ids=[
            "even_division",
            "decimal_result",
            "negative_dividend",
            "zero_dividend",
            "decimal_division",
            "large_numbers",
        ],
    )
    def test_divide(self, calc, x, y, expected):
        """Test division with various number combinations"""
        result = calc.devide(x, y)
        assert result == pytest.approx(expected)
        assert calc.last_result == pytest.approx(expected)

    def test_divide_by_zero(self, calc):
        """Test that division by zero raises an error"""
        with pytest.raises(CalculatorError) as exc_info:
            calc.devide(1, 0)
        assert str(exc_info.value) == "Cannot devide by zero"


class TestLastResult:
    @pytest.mark.parametrize(
        "operation, x, y, expected",
        [
            ("add", 2, 3, 5),
            ("subtract", 5, 3, 2),
            ("multiply", 4, 5, 20),
            ("devide", 10, 2, 5),
        ],
        ids=["addition", "subtraction", "multiplication", "division"],
    )
    def test_last_result_updated(self, calc, operation, x, y, expected):
        """Test that last_result is updated after each operation"""
        operation_method = getattr(calc, operation)
        result = operation_method(x, y)
        assert result == expected
        assert calc.get_last_result() == expected

    def test_last_result_persistence(self, calc):
        """Test that last_result persists between operations"""
        calc.add(2, 2)  # result = 4
        assert calc.get_last_result() == 4

        calc.multiply(3, 3)  # result = 9
        assert calc.get_last_result() == 9

        calc.subtract(5, 2)  # result = 3
        assert calc.get_last_result() == 3

        calc.devide(10, 2)  # result = 5
        assert calc.get_last_result() == 5
