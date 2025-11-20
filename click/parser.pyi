"""
Type stubs for click.parser module.

This module provides the option parser used by Click to parse command-line arguments.
"""

from typing import Any, Callable, Dict, List, Optional, Sequence, Set, Tuple, Union
from click.core import Context

class Option:
    """Represents a parsed option."""

    obj: Any
    _short_opts: List[str]
    _long_opts: List[str]
    prefixes: Set[str]
    action: Optional[str]
    dest: Optional[str]
    nargs: int
    const: Any
    count: bool

    def __init__(
        self,
        opts: Sequence[str],
        dest: Optional[str] = ...,
        action: Optional[str] = ...,
        nargs: int = ...,
        const: Optional[Any] = ...,
        obj: Optional[Any] = ...,
    ) -> None: ...

    def takes_value(self) -> bool: ...
    def process(self, value: Any, state: ParsingState) -> None: ...


class Argument:
    """Represents a parsed argument."""

    obj: Any
    dest: Optional[str]
    nargs: int

    def __init__(
        self,
        dest: Optional[str] = ...,
        nargs: int = ...,
        obj: Optional[Any] = ...,
    ) -> None: ...

    def process(self, value: Any, state: ParsingState) -> None: ...


class ParsingState:
    """
    State object used during parsing.
    """

    opts: Dict[str, Any]
    largs: List[str]
    rargs: List[str]
    order: List[Any]

    def __init__(self, rargs: List[str]) -> None: ...


class OptionParser:
    """
    The option parser is responsible for parsing command-line arguments
    and options according to Click's rules.
    """

    ctx: Optional[Context]
    allow_interspersed_args: bool
    ignore_unknown_options: bool
    _short_opt: Dict[str, Option]
    _long_opt: Dict[str, Option]
    _opt_prefixes: Set[str]
    _args: List[Argument]

    def __init__(
        self,
        ctx: Optional[Context] = ...,
    ) -> None: ...

    def add_option(
        self,
        opts: Sequence[str],
        dest: Optional[str] = ...,
        action: Optional[str] = ...,
        nargs: int = ...,
        const: Optional[Any] = ...,
        obj: Optional[Any] = ...,
    ) -> Option: ...

    def add_argument(
        self,
        dest: Optional[str] = ...,
        nargs: int = ...,
        obj: Optional[Any] = ...,
    ) -> Argument: ...

    def parse_args(
        self,
        args: List[str],
    ) -> Tuple[Dict[str, Any], List[str], List[Any]]: ...


def split_opt(opt: str) -> Tuple[str, str]: ...


def normalize_opt(opt: str, ctx: Optional[Context]) -> str: ...


def split_arg_string(string: str) -> List[str]:
    """
    Split an argument string as a shell would.
    """
    ...
