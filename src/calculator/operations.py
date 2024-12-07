from numbers import Real


class CalculatorError(Exception):
    """Custom exception class for calculator operations."""

    pass


class Calculator:
    """A simple calculator class to demonstrate testing concepts"""

    def __init__(self) -> None:
        self.last_result = None

    def _validate_numbers(self, x: float, y: float) -> tuple[float, float]:
        """
        Validate that inputs are numeric types.
        Raises TypeError if inputs are not numeric (int or float).
        """
        if not (
            isinstance(x, Real)
            and not isinstance(x, bool)
            and isinstance(y, Real)
            and not isinstance(y, bool)
        ):
            raise TypeError(
                "Calculator operations require numeric inputs (int or float)"
            )
        return float(x), float(y)

    def add(self, x: float, y: float) -> float:
        """Add two numbers"""
        x, y = self._validate_numbers(x, y)
        self.last_result = x + y
        return self.last_result

    def devide(self, x: float, y: float) -> float:
        """Devide two numbers"""
        x, y = self._validate_numbers(x, y)
        if y == 0:
            raise CalculatorError("Cannot devide by zero")
        self.last_result = x / y
        return self.last_result

    def multiply(self, x: float, y: float) -> float:
        """Multiply two numbers"""
        x, y = self._validate_numbers(x, y)
        self.last_result = x * y
        return self.last_result

    def subtract(self, x: float, y: float) -> float:
        """Subtract two numbers"""
        x, y = self._validate_numbers(x, y)
        self.last_result = x - y
        return self.last_result

    def get_last_result(self) -> float:
        """Get the last result"""
        if self.last_result is None:
            raise CalculatorError("No result available")
        return self.last_result
