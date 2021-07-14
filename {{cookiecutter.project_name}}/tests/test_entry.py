"""
{{cookiecutter.project_slug}} - Test the program's entry-point.
"""

# module under test
from {{cookiecutter.project_slug}} import PKG_NAME
from {{cookiecutter.project_slug}}.entry import main as {{cookiecutter.project_slug}}_main


def test_entry_basic():
    """Test basic argument parsing."""

    args = [PKG_NAME]
    assert {{cookiecutter.project_slug}}_main(args) == 0
