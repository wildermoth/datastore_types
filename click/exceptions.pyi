"""
Type stubs for click.exceptions module.

This module contains all exception classes used by Click.
"""

from typing import Any, List, Optional, Sequence
from click.core import Context, Parameter

class ClickException(Exception):
    """
    Base exception for all Click exceptions.
    All exceptions raised by Click inherit from this class.
    """

    exit_code: int
    message: str

    def __init__(self, message: str) -> None: ...
    def format_message(self) -> str: ...
    def show(self, file: Any = ...) -> None: ...


class UsageError(ClickException):
    """
    Exception raised when the command is used incorrectly.
    This includes invalid arguments, missing required parameters, etc.
    """

    exit_code: int
    ctx: Optional[Context]

    def __init__(self, message: str, ctx: Optional[Context] = ...) -> None: ...
    def show(self, file: Any = ...) -> None: ...


class BadParameter(UsageError):
    """
    Exception raised when a parameter receives an invalid value.
    """

    param: Optional[Parameter]
    param_hint: Optional[str]

    def __init__(
        self,
        message: str,
        ctx: Optional[Context] = ...,
        param: Optional[Parameter] = ...,
        param_hint: Optional[str] = ...,
    ) -> None: ...


class MissingParameter(BadParameter):
    """
    Exception raised when a required parameter is missing.
    """

    param_type: str

    def __init__(
        self,
        message: Optional[str] = ...,
        ctx: Optional[Context] = ...,
        param: Optional[Parameter] = ...,
        param_hint: Optional[str] = ...,
        param_type: Optional[str] = ...,
    ) -> None: ...


class NoSuchOption(UsageError):
    """
    Exception raised when an unknown option is provided.
    """

    option_name: str
    possibilities: Optional[Sequence[str]]

    def __init__(
        self,
        option_name: str,
        message: Optional[str] = ...,
        possibilities: Optional[Sequence[str]] = ...,
        ctx: Optional[Context] = ...,
    ) -> None: ...


class BadOptionUsage(UsageError):
    """
    Exception raised when an option is used incorrectly.
    """

    option_name: Optional[str]

    def __init__(
        self,
        option_name: Optional[str],
        message: str,
        ctx: Optional[Context] = ...,
    ) -> None: ...


class BadArgumentUsage(UsageError):
    """
    Exception raised when an argument is used incorrectly.
    """
    ...


class FileError(ClickException):
    """
    Exception raised when file operations fail.
    """

    ui_filename: str
    filename: str

    def __init__(self, filename: str, hint: Optional[str] = ...) -> None: ...


class Abort(RuntimeError):
    """
    Exception raised when the user aborts the application.
    This is typically raised by Ctrl+C or when explicitly calling ctx.abort().
    """
    ...


class Exit(RuntimeError):
    """
    Exception raised to exit the application with a specific exit code.
    """

    exit_code: int

    def __init__(self, exit_code: int = ...) -> None: ...
