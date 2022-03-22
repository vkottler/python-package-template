"""
post_gen_project - Perform some actions that are not templated.
"""

# built-in
import subprocess
from typing import List


def git_cmd(args: List[str], check: bool = True) -> None:
    """Run a 'git' command."""

    subprocess.run(["git"] + args, check=check)


def mk_cmd(args: List[str], check: bool = True) -> None:
    """Run an 'mk' command."""

    subprocess.run(["mk"] + args, check=check)


# initialize a repository, 'config' sub-module
git_cmd(["init"])
git_cmd(["submodule", "add", "https://github.com/vkottler/config"])
git_cmd(["submodule", "update", "--init", "--recursive"])

# run initial datazen sync
mk_cmd(["venv"])
mk_cmd(["dz-sync"])

# make sure that the package is totally clean
mk_cmd(
    [
        "python-lint",
        "python-sa",
        "python-test",
        "python-build",
        "yaml",
    ]
)

# stage everything and commit, it's okay if committing doesn't work (e.g.
# running in CI)
git_cmd(["add", "-A"])
git_cmd(["commit", "-m", "Initial commit."], False)
