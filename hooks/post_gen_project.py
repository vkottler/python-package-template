"""
post_gen_project - Perform some actions that are not templated.
"""

# built-in
from pathlib import Path
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

    mk_cmd(["venv"])
    mk_cmd(["dz-sync"])


def remove_conditionals() -> None:
    """
    Don't render '<slug>/app.py' or 'tests/test_entry.py' if we're not a
    command-line package.
    """

    if "{{cookiecutter.has_cli}}" != "True":
        to_remove = [
            Path("{{cookiecutter.project_slug}}", "app.py"),
            Path("tests", "test_entry.py"),
        ]
        for path in to_remove:
            path.unlink()


def verify() -> None:
    """Make sure that the package is totally clean."""

    mk_cmd(
        [
            "python-lint",
            "python-sa",
            "python-build",
            "yaml",
        ]
    )

    # Only run tests for command-line packages.
    if "{{cookiecutter.has_cli}}" == "True":
        mk_cmd(["python-test"])

    # Make sure the package can be installed in editable mode (this likely
    # already happened if the datazen manifest tried to get 'help' output).
    mk_cmd(["python-editable"])


initialize()
datazen()
remove_conditionals()
verify()
commit()
