"""
Type stubs for click.utils module.

This module provides various utility functions used throughout Click.
"""

from typing import Any, Callable, Dict, IO, Iterable, List, Optional, Sequence, TypeVar, Union
import os

_T = TypeVar("_T")

def echo(
    message: Optional[Any] = ...,
    file: Optional[IO[Any]] = ...,
    nl: bool = ...,
    err: bool = ...,
    color: Optional[bool] = ...,
) -> None:
    """Print a message (re-exported from termui)."""
    ...


def get_app_dir(app_name: str, roaming: bool = ..., force_posix: bool = ...) -> str:
    """
    Get the application configuration directory.

    Args:
        app_name: Application name
        roaming: Whether to use roaming profile (Windows)
        force_posix: Force POSIX-style paths
    """
    ...


def get_os_args() -> List[str]:
    """
    Get command-line arguments in a way that works across platforms.
    """
    ...


def format_filename(filename: Union[str, bytes, os.PathLike[Any]], shorten: bool = ...) -> str:
    """
    Format a filename for display.
    """
    ...


def safecall(func: Callable[..., _T]) -> Optional[_T]:
    """
    Safely call a function, catching and ignoring exceptions.
    """
    ...


def make_str(value: Any) -> str:
    """
    Convert a value to a string.
    """
    ...


def make_default_short_help(help: str, max_length: int = ...) -> str:
    """
    Generate a short help string from a longer help text.
    """
    ...


class LazyFile:
    """
    A lazy file wrapper that only opens the file when accessed.
    """

    name: str
    mode: str
    encoding: Optional[str]
    errors: Optional[str]
    atomic: bool

    def __init__(
        self,
        filename: Union[str, os.PathLike[Any]],
        mode: str = ...,
        encoding: Optional[str] = ...,
        errors: Optional[str] = ...,
        atomic: bool = ...,
    ) -> None: ...

    def open(self) -> IO[Any]: ...
    def close(self) -> None: ...
    def close_intelligently(self) -> None: ...
    def __enter__(self) -> LazyFile: ...
    def __exit__(self, *args: Any) -> None: ...
    def __iter__(self) -> Any: ...


class KeepOpenFile:
    """
    Wrapper that prevents a file from being closed.
    """

    def __init__(self, file: IO[Any]) -> None: ...
    def __enter__(self) -> KeepOpenFile: ...
    def __exit__(self, *args: Any) -> None: ...
    def __iter__(self) -> Any: ...


class PacifyFlushWrapper:
    """
    Wrapper that prevents flush() calls on a file.
    """

    def __init__(self, wrapped: IO[Any]) -> None: ...
