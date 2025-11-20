"""
Type stubs for click.types module.

This module contains various parameter types used in Click commands.
Parameter types are responsible for converting and validating command-line arguments.
"""

from typing import Any, Callable, Dict, Iterable, List, Optional, Sequence, Tuple, TypeVar, Union, IO
from click.core import Context, Parameter
import pathlib
import uuid

_T = TypeVar("_T")

class ParamType:
    """
    Base class for all parameter types in Click.
    Parameter types handle conversion and validation of command-line arguments.
    """

    name: str
    is_composite: bool
    envvar_list_splitter: Optional[str]

    def __call__(
        self,
        value: Optional[str],
        param: Optional[Parameter] = ...,
        ctx: Optional[Context] = ...,
    ) -> Any: ...

    def get_metavar(self, param: Parameter) -> Optional[str]: ...
    def get_missing_message(self, param: Parameter) -> Optional[str]: ...
    def convert(
        self,
        value: Any,
        param: Optional[Parameter],
        ctx: Optional[Context],
    ) -> Any: ...
    def split_envvar_value(self, rv: str) -> Sequence[str]: ...
    def fail(
        self,
        message: str,
        param: Optional[Parameter] = ...,
        ctx: Optional[Context] = ...,
    ) -> None: ...
    def shell_complete(
        self,
        ctx: Context,
        param: Parameter,
        incomplete: str,
    ) -> List[Union[str, Tuple[str, str]]]: ...


class CompositeParamType(ParamType):
    """A parameter type that represents a composite of multiple values."""

    is_composite: bool
    arity: int

    @property
    def name(self) -> str: ...


class FuncParamType(ParamType):
    """
    A parameter type that wraps a conversion function.
    """

    func: Callable[[str], Any]

    def __init__(self, func: Callable[[str], Any]) -> None: ...


class UnprocessedParamType(ParamType):
    """A parameter type that does no conversion."""

    name: str


class StringParamType(ParamType):
    """
    A string parameter type. This is the default parameter type.
    """

    name: str


class Choice(ParamType):
    """
    A parameter type for a set of predefined choices.
    Only values from the choice list are accepted.
    """

    name: str
    choices: Sequence[str]
    case_sensitive: bool

    def __init__(self, choices: Sequence[str], case_sensitive: bool = ...) -> None: ...


class DateTime(ParamType):
    """
    A parameter type for parsing datetime strings into datetime objects.
    """

    name: str
    formats: Sequence[str]

    def __init__(self, formats: Optional[Sequence[str]] = ...) -> None: ...


class IntParamType(ParamType):
    """
    A parameter type for integer values.
    """

    name: str


class IntRange(IntParamType):
    """
    A parameter type for integers within a specific range.
    """

    name: str
    min: Optional[int]
    max: Optional[int]
    min_open: bool
    max_open: bool
    clamp: bool

    def __init__(
        self,
        min: Optional[int] = ...,
        max: Optional[int] = ...,
        min_open: bool = ...,
        max_open: bool = ...,
        clamp: bool = ...,
    ) -> None: ...


class FloatParamType(ParamType):
    """
    A parameter type for float values.
    """

    name: str


class FloatRange(FloatParamType):
    """
    A parameter type for floats within a specific range.
    """

    name: str
    min: Optional[float]
    max: Optional[float]
    min_open: bool
    max_open: bool
    clamp: bool

    def __init__(
        self,
        min: Optional[float] = ...,
        max: Optional[float] = ...,
        min_open: bool = ...,
        max_open: bool = ...,
        clamp: bool = ...,
    ) -> None: ...


class BoolParamType(ParamType):
    """
    A parameter type for boolean values.
    """

    name: str


class UUIDParameterType(ParamType):
    """
    A parameter type for UUID values.
    """

    name: str


class File(ParamType):
    """
    A parameter type for file objects.
    Can open files in various modes for reading or writing.
    """

    name: str
    mode: str
    encoding: Optional[str]
    errors: Optional[str]
    lazy: bool
    atomic: bool

    def __init__(
        self,
        mode: str = ...,
        encoding: Optional[str] = ...,
        errors: Optional[str] = ...,
        lazy: Optional[bool] = ...,
        atomic: bool = ...,
    ) -> None: ...

    def resolve_lazy_flag(self, value: Any) -> bool: ...


class Path(ParamType):
    """
    A parameter type for paths.
    Can validate existence, file type, readability, etc.
    """

    name: str
    exists: bool
    file_okay: bool
    dir_okay: bool
    writable: bool
    readable: bool
    resolve_path: bool
    allow_dash: bool
    path_type: Optional[Union[type[str], type[bytes], type[pathlib.Path]]]

    def __init__(
        self,
        exists: bool = ...,
        file_okay: bool = ...,
        dir_okay: bool = ...,
        writable: bool = ...,
        readable: bool = ...,
        resolve_path: bool = ...,
        allow_dash: bool = ...,
        path_type: Optional[Union[type[str], type[bytes], type[pathlib.Path]]] = ...,
    ) -> None: ...


class Tuple(CompositeParamType):
    """
    A parameter type for tuples of other parameter types.
    """

    types: Sequence[ParamType]

    def __init__(self, types: Sequence[Union[type[Any], ParamType]]) -> None: ...


# Singleton instances of common parameter types
STRING: StringParamType
INT: IntParamType
FLOAT: FloatParamType
BOOL: BoolParamType
UUID: UUIDParameterType
UNPROCESSED: UnprocessedParamType


def convert_type(
    ty: Optional[Union[type[Any], ParamType]],
    default: Optional[Any] = ...,
) -> ParamType:
    """
    Converts a type annotation into a ParamType instance.
    """
    ...
