import pytest

from src.calculator.operations import Calculator


@pytest.fixture
def calc():
    """Provide a fresh Calculator instance for each test"""
    return Calculator()


@pytest.fixture
def calc_with_result(calc):
    """Provide a Calculator instance with a previous calculation"""
    calc.add(2, 3)
    return calc


def pytest_configure(config):
    """Register custom markers."""
    config.addinivalue_line(
        "markers", "smoke: mark test as smoke test (quick sanity check)"
    )
    config.addinivalue_line("markers", "slow: mark test as slow running")
    config.addinivalue_line(
        "markers", "edge_cases: mark tests that handle boundary and special cases"
    )
    config.addinivalue_line(
        "markers", 
        "integration: mark tests that verify multiple operations together"
    )
