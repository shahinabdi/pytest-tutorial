# Calculator Project

A simple calculator implementation with comprehensive test suite demonstrating pytest features.

## Setup

```bash
# Install dependencies
poetry install

# Run tests
poetry run pytest
```

## Project Structure

```
calculator-project/
├── src/
│   └── calculator/
│       ├── __init__.py
│       └── operations.py
└── tests/
    ├── __init__.py
    ├── conftest.py
    ├── test_operations.py
    └── test_operations_markers.py
```

## Features

- Basic arithmetic operations
- Input validation
- Last result tracking
- Comprehensive test suite with markers

## Testing

Different test categories marked with pytest markers:
- `@pytest.mark.smoke`: Basic functionality tests
- `@pytest.mark.edge_cases`: Input validation
- `@pytest.mark.slow`: Performance tests

## Development

Uses Poetry for dependency management and pytest for testing.
