"""
Type stubs for click.decorators module.

This module contains all the decorator functions used to build Click commands.
These are the primary interface for defining command-line applications with Click.
"""

from typing import Any, Callable, Dict, List, Optional, Sequence, Tuple, TypeVar, Union, overload, Type
from click.core import Command, Group, Context, Parameter, Option, Argument
from click.types import ParamType

_F = TypeVar("_F", bound=Callable[..., Any])
_T = TypeVar("_T")


@overload
def command(name: str) -> Callable[[_F], Command]: ...
@overload
def command(name: None = ..., **attrs: Any) -> Callable[[_F], Command]: ...
@overload
def command(__func: _F) -> Command: ...


@overload
def group(name: str) -> Callable[[_F], Group]: ...
@overload
def group(name: None = ..., **attrs: Any) -> Callable[[_F], Group]: ...
@overload
def group(__func: _F) -> Group: ...


def argument(
    *param_decls: str,
    cls: Type[Argument] = ...,
    type: Optional[Union[type[Any], ParamType]] = ...,
    required: Optional[bool] = ...,
    default: Optional[Any] = ...,
    callback: Optional[Callable[[Context, Parameter, Any], Any]] = ...,
    nargs: Optional[int] = ...,
    metavar: Optional[str] = ...,
    expose_value: bool = ...,
    is_eager: bool = ...,
    envvar: Optional[Union[str, List[str]]] = ...,
    shell_complete: Optional[Callable[[Context, Parameter, str], List[Union[str, Tuple[str, str]]]]] = ...,
) -> Callable[[_F], _F]:
    """
    Decorator to add an argument to a command.

    Arguments are positional parameters to commands. Unlike options,
    they are required by default and do not have flag prefixes.
    """
    ...


def option(
    *param_decls: str,
    cls: Type[Option] = ...,
    show_default: Union[bool, str] = ...,
    prompt: Optional[Union[bool, str]] = ...,
    confirmation_prompt: Union[bool, str] = ...,
    prompt_required: bool = ...,
    hide_input: bool = ...,
    is_flag: Optional[bool] = ...,
    flag_value: Optional[Any] = ...,
    multiple: bool = ...,
    count: bool = ...,
    allow_from_autoenv: bool = ...,
    type: Optional[Union[type[Any], ParamType]] = ...,
    help: Optional[str] = ...,
    hidden: bool = ...,
    show_choices: bool = ...,
    show_envvar: bool = ...,
    default: Optional[Any] = ...,
    required: bool = ...,
    callback: Optional[Callable[[Context, Parameter, Any], Any]] = ...,
    nargs: Optional[int] = ...,
    metavar: Optional[str] = ...,
    expose_value: bool = ...,
    is_eager: bool = ...,
    envvar: Optional[Union[str, List[str]]] = ...,
    shell_complete: Optional[Callable[[Context, Parameter, str], List[Union[str, Tuple[str, str]]]]] = ...,
) -> Callable[[_F], _F]:
    """
    Decorator to add an option to a command.

    Options are optional parameters triggered by flags like --flag.
    They can have default values and help text.
    """
    ...


def password_option(
    *param_decls: str,
    **kwargs: Any,
) -> Callable[[_F], _F]:
    """
    Decorator that adds a password option (hidden input with confirmation).
    """
    ...


def confirmation_option(
    *param_decls: str,
    **kwargs: Any,
) -> Callable[[_F], _F]:
    """
    Decorator that adds a confirmation option that prompts for confirmation.
    """
    ...


def version_option(
    version: Optional[str] = ...,
    *param_decls: str,
    package_name: Optional[str] = ...,
    prog_name: Optional[str] = ...,
    message: Optional[str] = ...,
    **kwargs: Any,
) -> Callable[[_F], _F]:
    """
    Decorator that adds a --version option which prints version information.
    """
    ...


def help_option(
    *param_decls: str,
    **kwargs: Any,
) -> Callable[[_F], _F]:
    """
    Decorator that adds a help option to a command.
    """
    ...


def pass_context(f: _F) -> _F:
    """
    Decorator that marks a callback as wanting to receive the current context
    as first argument.
    """
    ...


def pass_obj(f: _F) -> _F:
    """
    Decorator that marks a callback as wanting to receive the context object
    as first argument. This is similar to pass_context but only passes the obj.
    """
    ...


def make_pass_decorator(
    object_type: Type[_T],
    ensure: bool = ...,
) -> Callable[[Callable[..., Any]], Callable[..., Any]]:
    """
    Creates a decorator that passes an object of a specific type from the context.
    """
    ...


def pass_meta_key(
    key: str,
    *,
    doc_description: Optional[str] = ...,
) -> Callable[[_F], _F]:
    """
    Decorator that passes a specific key from the context metadata.
    """
    ...
