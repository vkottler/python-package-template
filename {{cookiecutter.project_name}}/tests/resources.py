"""
A module for working with test data.
"""

# built-in
from pathlib import Path


def resource(resource_name: str, *parts: str, valid: bool = True) -> Path:
    """Locate the path to a test resource."""

    return Path(__file__).parent.joinpath(
        "data", "valid" if valid else "invalid", resource_name, *parts
    )
