"""Type stubs for pydantic.dataclasses module.

This module provides an enhanced dataclass decorator that performs validation,
similar to the standard Python dataclass but with added Pydantic validation.
"""

from __future__ import annotations as _annotations

import sys
import types
from typing import TYPE_CHECKING, Any, Callable, Generic, Literal, NoReturn, TypeVar, overload

from typing_extensions import TypeGuard, dataclass_transform

from .config import ConfigDict

if TYPE_CHECKING:
    from ._internal._dataclasses import PydanticDataclass
    from ._internal._namespace_utils import MappingNamespace

__all__ = ('dataclass', 'rebuild_dataclass', 'is_pydantic_dataclass')

_T = TypeVar('_T')

if sys.version_info >= (3, 10):

    @dataclass_transform(field_specifiers=(Any, Any, Any))
    @overload
    def dataclass(
        *,
        init: Literal[False] = False,
        repr: bool = True,
        eq: bool = True,
        order: bool = False,
        unsafe_hash: bool = False,
        frozen: bool = False,
        config: ConfigDict | type[object] | None = None,
        validate_on_init: bool | None = None,
        kw_only: bool = ...,
        slots: bool = ...,
    ) -> Callable[[type[_T]], type[PydanticDataclass]]: ...

    @dataclass_transform(field_specifiers=(Any, Any, Any))
    @overload
    def dataclass(
        _cls: type[_T],
        *,
        init: Literal[False] = False,
        repr: bool = True,
        eq: bool = True,
        order: bool = False,
        unsafe_hash: bool = False,
        frozen: bool | None = None,
        config: ConfigDict | type[object] | None = None,
        validate_on_init: bool | None = None,
        kw_only: bool = ...,
        slots: bool = ...,
    ) -> type[PydanticDataclass]: ...

else:

    @dataclass_transform(field_specifiers=(Any, Any, Any))
    @overload
    def dataclass(
        *,
        init: Literal[False] = False,
        repr: bool = True,
        eq: bool = True,
        order: bool = False,
        unsafe_hash: bool = False,
        frozen: bool | None = None,
        config: ConfigDict | type[object] | None = None,
        validate_on_init: bool | None = None,
    ) -> Callable[[type[_T]], type[PydanticDataclass]]: ...

    @dataclass_transform(field_specifiers=(Any, Any, Any))
    @overload
    def dataclass(
        _cls: type[_T],
        *,
        init: Literal[False] = False,
        repr: bool = True,
        eq: bool = True,
        order: bool = False,
        unsafe_hash: bool = False,
        frozen: bool | None = None,
        config: ConfigDict | type[object] | None = None,
        validate_on_init: bool | None = None,
    ) -> type[PydanticDataclass]: ...

@dataclass_transform(field_specifiers=(Any, Any, Any))
def dataclass(
    _cls: type[_T] | None = None,
    *,
    init: Literal[False] = False,
    repr: bool = True,
    eq: bool = True,
    order: bool = False,
    unsafe_hash: bool = False,
    frozen: bool | None = None,
    config: ConfigDict | type[object] | None = None,
    validate_on_init: bool | None = None,
    kw_only: bool = False,
    slots: bool = False,
) -> Callable[[type[_T]], type[PydanticDataclass]] | type[PydanticDataclass]:
    """Create a Pydantic-enhanced dataclass, similar to the standard Python dataclass, but with added validation.

    This decorator is used similarly to dataclasses.dataclass, but it performs Pydantic validation on initialization.

    Args:
        _cls: The target dataclass. Optional when using as a decorator factory.
        init: Included for signature compatibility with dataclasses.dataclass, and is passed through to
            dataclasses.dataclass when appropriate. If specified, must be set to False, as pydantic inserts its
            own __init__ function.
        repr: A boolean indicating whether to include the field in the __repr__ output.
        eq: Determines if a __eq__ method should be generated for the class.
        order: Determines if comparison magic methods should be generated, such as __lt__, but not __eq__.
        unsafe_hash: Determines if a __hash__ method should be included in the class, as in dataclasses.dataclass.
        frozen: Determines if the generated class should be a 'frozen' dataclass, which does not allow its
            attributes to be modified after it has been initialized. If not set, the value from the provided
            config argument will be used (and will default to False otherwise).
        config: The Pydantic config to use for the dataclass. Can be a ConfigDict or a type with __pydantic_config__.
        validate_on_init: A deprecated parameter included for backwards compatibility; in V2, all Pydantic dataclasses
            are validated on init.
        kw_only: Determines if __init__ method parameters must be specified by keyword only. Defaults to False.
            Only available on Python 3.10+.
        slots: Determines if the generated class should be a 'slots' dataclass, which does not allow the addition of
            new attributes after instantiation. Only available on Python 3.10+.

    Returns:
        A decorator that accepts a class as its argument and returns a Pydantic dataclass.

    Raises:
        AssertionError: Raised if init is not False or validate_on_init is False.
        PydanticUserError: Raised if the class is already a Pydantic model.

    Example:
        ```python
        from pydantic.dataclasses import dataclass

        @dataclass
        class User:
            name: str
            age: int

        user = User(name='John', age=30)
        ```
    """
    ...

def rebuild_dataclass(
    cls: type[PydanticDataclass],
    *,
    force: bool = False,
    raise_errors: bool = True,
    _parent_namespace_depth: int = 2,
    _types_namespace: MappingNamespace | None = None,
) -> bool | None:
    """Try to rebuild the pydantic-core schema for the dataclass.

    This may be necessary when one of the annotations is a ForwardRef which could not be resolved
    during the initial attempt to build the schema, and automatic rebuilding fails.

    This is analogous to BaseModel.model_rebuild.

    Args:
        cls: The class to rebuild the pydantic-core schema for.
        force: Whether to force the rebuilding of the schema, defaults to False.
        raise_errors: Whether to raise errors, defaults to True.
        _parent_namespace_depth: The depth level of the parent namespace, defaults to 2.
        _types_namespace: The types namespace, defaults to None.

    Returns:
        Returns None if the schema is already "complete" and rebuilding was not required.
        If rebuilding _was_ required, returns True if rebuilding was successful, otherwise False.
    """
    ...

def is_pydantic_dataclass(class_: type[Any], /) -> TypeGuard[type[PydanticDataclass]]:
    """Check whether a class is a pydantic dataclass.

    Args:
        class_: The class to check.

    Returns:
        True if the class is a pydantic dataclass, False otherwise.
    """
    ...
