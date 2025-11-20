"""
Type stubs for click.termui module.

This module provides terminal UI utilities like prompts, confirmations,
progress bars, and styled output.
"""

from typing import Any, Callable, Dict, IO, Iterable, List, Optional, Sequence, TextIO, Tuple, TypeVar, Union, overload
from click.core import Context
from click.types import ParamType

_T = TypeVar("_T")

def hidden_prompt_func(prompt: str) -> str:
    """Prompt for hidden input (like passwords)."""
    ...


def echo(
    message: Optional[Any] = ...,
    file: Optional[IO[Any]] = ...,
    nl: bool = ...,
    err: bool = ...,
    color: Optional[bool] = ...,
) -> None:
    """
    Print a message to the console.

    Args:
        message: The message to output
        file: The file to write to (defaults to stdout)
        nl: Whether to append a newline
        err: Whether to write to stderr instead of stdout
        color: Whether to force color output
    """
    ...


def echo_via_pager(
    text_or_generator: Union[str, Iterable[str]],
    color: Optional[bool] = ...,
) -> None:
    """
    Display text through a pager (like 'less').
    """
    ...


def prompt(
    text: str,
    default: Optional[Any] = ...,
    hide_input: bool = ...,
    confirmation_prompt: Union[bool, str] = ...,
    type: Optional[Union[type[Any], ParamType]] = ...,
    value_proc: Optional[Callable[[str], Any]] = ...,
    prompt_suffix: str = ...,
    show_default: bool = ...,
    err: bool = ...,
    show_choices: bool = ...,
) -> Any:
    """
    Prompt the user for input.

    Args:
        text: The prompt text
        default: Default value if user provides no input
        hide_input: Whether to hide input (for passwords)
        confirmation_prompt: Whether to ask for confirmation
        type: Parameter type for validation
        value_proc: Custom value processing function
        prompt_suffix: Suffix to append to prompt
        show_default: Whether to show the default value
        err: Whether to prompt on stderr
        show_choices: Whether to show available choices
    """
    ...


def confirm(
    text: str,
    default: bool = ...,
    abort: bool = ...,
    prompt_suffix: str = ...,
    show_default: bool = ...,
    err: bool = ...,
) -> bool:
    """
    Prompt for confirmation (yes/no).

    Args:
        text: The prompt text
        default: Default answer
        abort: Whether to abort on 'no'
        prompt_suffix: Suffix to append to prompt
        show_default: Whether to show the default answer
        err: Whether to prompt on stderr
    """
    ...


def get_terminal_size() -> Tuple[int, int]:
    """
    Get the terminal size as (width, height).
    """
    ...


def echo_via_pager(text_or_generator: Union[str, Iterable[str]], color: Optional[bool] = ...) -> None:
    """
    Echo text through a pager.
    """
    ...


def progressbar(
    iterable: Optional[Iterable[_T]] = ...,
    length: Optional[int] = ...,
    label: Optional[str] = ...,
    show_eta: bool = ...,
    show_percent: Optional[bool] = ...,
    show_pos: bool = ...,
    item_show_func: Optional[Callable[[Optional[_T]], Optional[str]]] = ...,
    fill_char: str = ...,
    empty_char: str = ...,
    bar_template: str = ...,
    info_sep: str = ...,
    width: int = ...,
    file: Optional[TextIO] = ...,
    color: Optional[bool] = ...,
    update_min_steps: int = ...,
) -> Any:
    """
    Create a progress bar context manager.

    Example:
        with click.progressbar(items) as bar:
            for item in bar:
                process(item)
    """
    ...


def clear() -> None:
    """Clear the terminal screen."""
    ...


def style(
    text: str,
    fg: Optional[Union[int, Tuple[int, int, int], str]] = ...,
    bg: Optional[Union[int, Tuple[int, int, int], str]] = ...,
    bold: Optional[bool] = ...,
    dim: Optional[bool] = ...,
    underline: Optional[bool] = ...,
    overline: Optional[bool] = ...,
    italic: Optional[bool] = ...,
    blink: Optional[bool] = ...,
    reverse: Optional[bool] = ...,
    strikethrough: Optional[bool] = ...,
    reset: bool = ...,
) -> str:
    """
    Style text with ANSI colors and formatting.

    Args:
        text: The text to style
        fg: Foreground color (name, ANSI code, or RGB tuple)
        bg: Background color (name, ANSI code, or RGB tuple)
        bold: Bold text
        dim: Dim text
        underline: Underlined text
        overline: Overlined text
        italic: Italic text
        blink: Blinking text
        reverse: Reverse video
        strikethrough: Strikethrough text
        reset: Reset all styles
    """
    ...


def unstyle(text: str) -> str:
    """Remove ANSI styling from text."""
    ...


def secho(
    message: Optional[Any] = ...,
    file: Optional[IO[Any]] = ...,
    nl: bool = ...,
    err: bool = ...,
    color: Optional[bool] = ...,
    **styles: Any,
) -> None:
    """
    Combination of echo() and style(). Outputs styled text.
    """
    ...


def edit(
    text: Optional[str] = ...,
    editor: Optional[str] = ...,
    env: Optional[Dict[str, str]] = ...,
    require_save: bool = ...,
    extension: str = ...,
    filename: Optional[str] = ...,
) -> Optional[str]:
    """
    Open an editor to edit text.

    Args:
        text: Initial text content
        editor: Editor command to use
        env: Environment variables
        require_save: Whether to require the file to be saved
        extension: File extension for temporary file
        filename: Specific filename to edit
    """
    ...


def launch(
    url: str,
    wait: bool = ...,
    locate: bool = ...,
) -> int:
    """
    Launch a URL or file in the default application.
    """
    ...


def getchar(echo: bool = ...) -> str:
    """
    Get a single character from terminal input.
    """
    ...


def raw_terminal() -> Any:
    """
    Context manager for raw terminal mode.
    """
    ...


def pause(info: str = ..., err: bool = ...) -> None:
    """
    Pause execution and wait for user to press a key.
    """
    ...
