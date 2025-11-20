"""
Type stubs for click.shell_completion module.

This module provides shell completion support for Click commands.
"""

from typing import Any, Callable, Dict, List, Optional, Tuple, Union
from click.core import Context, Parameter, Command, MultiCommand

class CompletionItem:
    """
    Represents a completion suggestion with optional help text.
    """

    value: str
    help: Optional[str]

    def __init__(self, value: str, help: Optional[str] = ...) -> None: ...


class ShellComplete:
    """
    Base class for shell completion implementations.
    """

    name: str
    source_template: str

    def __init__(
        self,
        cli: Command,
        ctx_settings: Optional[Dict[str, Any]],
        prog_name: str,
        complete_var: str,
    ) -> None: ...

    def source(self) -> str:
        """Generate the shell-specific completion script source."""
        ...

    def get_completion_args(self) -> Tuple[List[str], str]:
        """
        Get the arguments and incomplete value from environment variables.
        """
        ...

    def get_completions(
        self,
        args: List[str],
        incomplete: str,
    ) -> List[CompletionItem]:
        """
        Get completion suggestions for the given arguments.
        """
        ...

    def format_completion(self, item: CompletionItem) -> str:
        """
        Format a completion item for the shell.
        """
        ...

    def complete(self) -> str:
        """
        Generate and return the completion output.
        """
        ...


class BashComplete(ShellComplete):
    """Shell completion for Bash."""

    name: str
    source_template: str


class ZshComplete(ShellComplete):
    """Shell completion for Zsh."""

    name: str
    source_template: str


class FishComplete(ShellComplete):
    """Shell completion for Fish."""

    name: str
    source_template: str


def get_completion_class(shell: str) -> Optional[type[ShellComplete]]:
    """
    Get the completion class for a specific shell.

    Args:
        shell: Shell name ('bash', 'zsh', 'fish')
    """
    ...


def add_completion_class(
    cls: type[ShellComplete],
    name: Optional[str] = ...,
) -> None:
    """
    Register a custom shell completion class.
    """
    ...
