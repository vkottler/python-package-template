"""
post_gen_project - Perform some actions that are not templated.
"""

# built-in
from pathlib import Path
from platform import system
import subprocess
from typing import List


def git_cmd(args: List[str], check: bool = True) -> None:
    """Run a 'git' command."""

    subprocess.run(["git"] + args, check=check)


def mk_cmd(args: List[str], check: bool = True) -> None:
    """Run an 'mk' command."""

    subprocess.run(["mk"] + args, check=check)


def initialize() -> None:
    """Initialize a repository, 'config' sub-module."""

    git_cmd(["init"])
    git_cmd(["submodule", "add", "https://github.com/vkottler/config"])
    git_cmd(["submodule", "update", "--init", "--recursive"])


def commit() -> None:
    """
    Stage everything and commit, it's okay if committing doesn't work (e.g.
    running in CI).
    """

    git_cmd(["add", "-A"])
    git_cmd(["commit", "-m", "Initial commit."], False)


def datazen() -> None:
    """Run initial datazen sync."""

    # Render everything.
    mk_cmd(["dz-sync"])


def remove_conditionals() -> None:
    """
    Don't render '<slug>/app.py' or 'tests/test_entry.py' if we're not a
    command-line package.
    """

    if "{{cookiecutter.has_cli}}" != "True":
        to_remove = [
            Path("{{cookiecutter.project_slug}}", "commands", "__init__.py"),
            Path("tests", "test_entry.py"),
        ]
        for path in to_remove:
            path.unlink()


def verify() -> None:
    """Make sure that the package is totally clean."""

    # Install the package as editable to sanity check that the package
    # structure is healthy. This may already be satisfied.
    mk_cmd(["python-editable"])

    mk_cmd(["python-install-yamllint", "python-build-once"])

    # Only run certain analysis tasks if we're not on Windows. More
    # troubleshooting to do here.
    if system() != "Windows":
        mk_cmd(["python-lint", "python-sa", "yaml", "docs"])

    # Only run tests for command-line packages.
    if "{{cookiecutter.has_cli}}" == "True":
        mk_cmd(["python-test"])

    # For some reason requirements' files are getting deleted, so try to
    # render them again.
    mk_cmd(["dz-sync"])


initialize()
datazen()
remove_conditionals()
verify()
commit()
