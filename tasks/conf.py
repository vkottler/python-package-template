"""
A module for project-specific task registration.
"""

# built-in
from pathlib import Path
from shutil import rmtree
from typing import Dict

# third-party
from vcorelib.task import Inbox, Outbox, Phony
from vcorelib.task.manager import TaskManager
from vcorelib.task.subprocess.run import SubprocessLogMixin, is_windows


class TestTemplate(SubprocessLogMixin):
    """A task for generating this package template as a test."""

    default_requirements = {"venv"}

    async def run(self, inbox: Inbox, outbox: Outbox, *args, **kwargs) -> bool:
        """Run a Python linter."""

        cwd: Path = args[0]

        # Remove the 'package-name' directory first.
        rmtree(cwd.joinpath("package-name"), ignore_errors=True)

        return await self.exec(
            str(
                inbox["venv"]["venv{python_version}"]["bin"].joinpath(
                    "cookiecutter"
                )
            ),
            "--no-input",
            "-o",
            str(cwd),
            str(cwd),
        )


def register(
    manager: TaskManager,
    project: str,
    cwd: Path,
    substitutions: Dict[str, str],
) -> bool:
    """Register project tasks to the manager."""

    # Don't run yamllint on Windows because it will fail on newlines.
    manager.register(
        Phony("yaml"),
        [] if is_windows() else ["yaml-lint-local", "yaml-lint-manifest.yaml"],
    )

    # Register a 'test' task that attempts to generate the package.
    manager.register(TestTemplate("test", cwd), [])

    del project
    del substitutions
    return True
