import math

import pytest


@pytest.mark.edge_cases
class TestEdgeCases:
    @pytest.mark.parametrize(
        "operation, x, y, expected_error",
        [
            (
                "add",
                "not a number",
                5,
                "Calculator operations require numeric inputs (int or float)",
            ),
            (
                "subtract",
                "invalid",
                10,
                "Calculator operations require numeric inputs (int or float)",
            ),
            (
                "multiply",
                None,
                3,
                "Calculator operations require numeric inputs (int or float)",
            ),
            (
                "devide",
                "5",
                2,
                "Calculator operations require numeric inputs (int or float)",
            ),
            (
                "add",
                5,
                "10",
                "Calculator operations require numeric inputs (int or float)",
            ),
            (
                "multiply",
                [],
                5,
                "Calculator operations require numeric inputs (int or float)",
            ),
            (
                "subtract",
                {},
                3,
                "Calculator operations require numeric inputs (int or float)",
            ),
            (
                "devide",
                5,
                True,
                "Calculator operations require numeric inputs (int or float)",
            ),
        ],
        ids=[
            "string_first_arg",
            "invalid_string_first_arg",
            "none_first_arg",
            "numeric_string_first_arg",
            "string_second_arg",
            "list_first_arg",
            "dict_first_arg",
            "bool_second_arg",
        ],
    )
    def test_operation_type_validation(self, calc, operation, x, y, expected_error):
        """Test that operations handle invalid input types"""
        with pytest.raises(TypeError) as exc_info:
            method = getattr(calc, operation)
            method(x, y)
        assert str(exc_info.value) == expected_error

    @pytest.mark.parametrize(
        "x, y",
        [
            (1, 2),
            (1.0, 2.0),
            (1, 2.0),
            (1.0, 2),
            (-1, 5),
            (-1.5, 2.5),
        ],
    )
    def test_valid_numeric_types(self, calc, x, y):
        """Test that valid numeric types are accepted"""
        calc.add(x, y)
        calc.subtract(x, y)
        calc.multiply(x, y)
        if y != 0:
            calc.devide(x, y)

    def test_float_infinity(self, calc):
        """Test operations with float infinity"""
        inf = float("inf")
        assert calc.add(inf, 1) == inf
        assert calc.multiply(inf, 2) == inf

    def test_float_nan(self, calc):
        """Test operations with NaN"""
        nan = float("nan")
        result = calc.add(nan, 1)
        assert math.isnan(result)


@pytest.mark.smoke
class TestCalculatorSmoke:
    """Basic smoke tests to verify core functionality"""

    def test_basic_addition(self, calc):
        """Verify basic addition works"""
        assert calc.add(2, 2) == 4

    def test_basic_subtraction(self, calc):
        """Verify basic subtraction works"""
        assert calc.subtract(5, 3) == 2

    def test_basic_multiply(self, calc):
        """Verify basic multiplication works"""
        assert calc.multiply(3, 3) == 9

    def test_basic_divide(self, calc):
        """Verify basic division works"""
        assert calc.devide(8, 2) == 4


@pytest.mark.slow
class TestCalculatorSlow:
    """Tests that might take longer to execute"""

    @pytest.mark.parametrize("n", [10000, 100000, 1000000])
    def test_large_numbers_addition(self, calc, n):
        """Test addition with increasingly large numbers"""
        result = calc.add(n, n)
        assert result == 2 * n

    @pytest.mark.parametrize("n", range(1000))
    def test_multiple_operations(self, calc, n):
        """Test chain of operations"""
        calc.add(n, n)
        calc.multiply(2, n)
        calc.subtract(n, 50)
        calc.devide(n, 2)
        assert isinstance(calc.get_last_result(), float)


@pytest.mark.slow
class TestCalculatorPrecision:
    """Tests that verify numerical precision"""

    @pytest.mark.parametrize(
        "x, y",
        [(1 / 3, 1 / 6), (0.1111111111, 0.2222222222), (0.999999999, 0.000000001)],
    )
    def test_floating_point_precision(self, calc, x, y):
        """Test precision with floating point calculations"""
        result = calc.add(x, y)
        assert abs(result - (x + y)) < 1e-10
