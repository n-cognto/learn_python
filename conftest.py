"""
Pytest configuration and shared fixtures for the learn_python project.

This file provides common test fixtures and configuration used across
all test modules in the project.
"""

import sys
from pathlib import Path
from typing import Generator

import pytest

# Add project root to Python path
project_root = Path(__file__).parent
sys.path.insert(0, str(project_root))


@pytest.fixture
def sample_data() -> dict:
    """Provide sample data for testing."""
    return {
        "numbers": [1, 2, 3, 4, 5],
        "strings": ["hello", "world", "python"],
        "mixed": [1, "two", 3.0, True],
    }


@pytest.fixture
def temp_file(tmp_path: Path) -> Generator[Path, None, None]:
    """Create a temporary file for testing file operations."""
    file_path = tmp_path / "test_file.txt"
    file_path.write_text("Test content\n")
    yield file_path
    # Cleanup happens automatically with tmp_path


@pytest.fixture
def sample_dict() -> dict:
    """Provide a sample dictionary for testing."""
    return {
        "name": "Alice",
        "age": 30,
        "city": "New York",
        "skills": ["Python", "JavaScript", "SQL"],
    }


@pytest.fixture
def sample_list() -> list:
    """Provide a sample list for testing."""
    return [10, 20, 30, 40, 50]


@pytest.fixture(autouse=True)
def reset_test_environment():
    """Reset environment before each test."""
    # Setup
    yield
    # Teardown - add any cleanup needed between tests


def pytest_configure(config):
    """Configure pytest with custom markers."""
    config.addinivalue_line("markers", "unit: Unit tests")
    config.addinivalue_line("markers", "integration: Integration tests")
    config.addinivalue_line("markers", "slow: Slow running tests")
