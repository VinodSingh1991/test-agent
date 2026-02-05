"""Test configuration and fixtures."""
import pytest


@pytest.fixture
def sample_query():
    """Sample query for testing."""
    return "create a primary button"


@pytest.fixture
def sample_component():
    """Sample component response."""
    return {
        "component_name": "Button",
        "code": "<Button variant='primary'>Click me</Button>",
        "documentation": "Primary button component",
        "confidence": 0.95
    }
