"""
post_gen_project - Perform some actions that are not templated.
"""

# built-in
import subprocess
from typing import List


def git_cmd(args: List[str], check: bool = True) -> None:
    """Run a 'git' command."""

    subprocess.run(["git"] + args, check=check)


# initialize a repository, 'config' sub-module
git_cmd(["init"])
git_cmd(["submodule", "add", "https://github.com/vkottler/config"])
git_cmd(["submodule", "update", "--init", "--recursive"])

# run initial datazen sync
subprocess.run(
    ["mk", "-P", "{{cookiecutter.project_slug}}", "venv"], check=True
)
subprocess.run(
    ["mk", "-P", "{{cookiecutter.project_slug}}", "mk-upgrade"], check=True
)
subprocess.run(
    ["mk", "-P", "{{cookiecutter.project_slug}}", "dz-sync"], check=True
)

# make sure that the package is totally clean
subprocess.run(
    [
        "mk",
        "-P",
        "{{cookiecutter.project_slug}}",
        "python-lint",
        "python-sa",
        "python-test",
        "python-build",
        "yaml",
    ],
    check=True,
)

# stage everything and commit, it's okay if committing doesn't work (e.g.
# running in CI)
git_cmd(["add", "-A"])
git_cmd(["commit", "-m", "Initial commit."], False)
