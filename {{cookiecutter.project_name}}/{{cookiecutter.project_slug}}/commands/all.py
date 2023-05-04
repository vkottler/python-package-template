"""
A module aggregating package commands.
"""

# built-in
from typing import List as _List
from typing import Tuple as _Tuple

# third-party
from vcorelib.args import CommandRegister as _CommandRegister


def commands() -> _List[_Tuple[str, str, _CommandRegister]]:
    """Get this package's commands."""

    return [
        ("noop", "command stub (does nothing)", lambda _: lambda _: 0),
    ]
