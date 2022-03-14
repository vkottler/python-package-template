"""
{{cookiecutter.project_slug}} - Test the program's entry-point.
"""

# built-in
from subprocess import check_output
from sys import executable
from unittest.mock import patch

# module under test
from {{cookiecutter.project_slug}} import PKG_NAME
from {{cookiecutter.project_slug}}.entry import main as {{cookiecutter.project_slug}}_main


def test_entry_basic():
    """Test basic argument parsing."""

    args = [PKG_NAME]
    assert {{cookiecutter.project_slug}}_main(args) == 0

    with patch("{{cookiecutter.project_slug}}.entry.entry", side_effect=SystemExit(1)):
        assert {{cookiecutter.project_slug}}_main(args) != 0


def test_package_entry():
    """Test the command-line entry through the 'python -m' invocation."""

    check_output([executable, "-m", "{{cookiecutter.project_slug}}", "-h"])
