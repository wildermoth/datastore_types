"""
Type stubs for click.formatting module.

This module provides help text formatting functionality.
"""

from typing import Any, Iterable, List, Optional, Sequence, Tuple

class HelpFormatter:
    """
    Formats help pages for commands and options.
    This class is responsible for the layout and styling of help text.
    """

    width: Optional[int]
    max_width: Optional[int]
    buffer: List[str]
    current_indent: int
    indent_increment: int

    def __init__(
        self,
        indent_increment: int = ...,
        width: Optional[int] = ...,
        max_width: Optional[int] = ...,
    ) -> None: ...

    def write(self, string: str) -> None:
        """Write a string to the help output."""
        ...

    def indent(self) -> None:
        """Increase the current indentation level."""
        ...

    def dedent(self) -> None:
        """Decrease the current indentation level."""
        ...

    def write_usage(
        self,
        prog: str,
        args: str = ...,
        prefix: Optional[str] = ...,
    ) -> None:
        """Write usage information."""
        ...

    def write_heading(self, heading: str) -> None:
        """Write a section heading."""
        ...

    def write_paragraph(self) -> None:
        """Write a paragraph separator."""
        ...

    def write_text(self, text: str) -> None:
        """Write formatted text that respects indentation and wrapping."""
        ...

    def write_dl(
        self,
        rows: Sequence[Tuple[str, str]],
        col_max: int = ...,
        col_spacing: int = ...,
    ) -> None:
        """
        Write a definition list. This is used for options and commands lists.

        Args:
            rows: List of (term, definition) tuples
            col_max: Maximum width for the first column
            col_spacing: Spacing between columns
        """
        ...

    def section(self, name: str) -> Any:
        """
        Context manager for a help section with a heading.
        """
        ...

    def indentation(self) -> Any:
        """
        Context manager that increases indentation level.
        """
        ...

    def getvalue(self) -> str:
        """Get the formatted help text as a string."""
        ...


def measure_table(rows: Sequence[Tuple[str, str]]) -> Tuple[int, ...]:
    """
    Measure the width requirements for a table.
    """
    ...


def iter_rows(rows: Sequence[Tuple[str, str]], col_count: int) -> Iterable[Tuple[str, ...]]:
    """
    Iterate over table rows.
    """
    ...


def wrap_text(
    text: str,
    width: int = ...,
    initial_indent: str = ...,
    subsequent_indent: str = ...,
    preserve_paragraphs: bool = ...,
) -> str:
    """
    Wrap text to a specific width with proper indentation.
    """
    ...
