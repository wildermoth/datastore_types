"""Decorator for validating function calls stubs."""

from __future__ import annotations as _annotations

import inspect
from functools import partial
from types import BuiltinFunctionType
from typing import TYPE_CHECKING, Any, Callable, TypeVar, cast, overload

from pydantic._internal import _generate_schema, _typing_extra, _validate_call
from pydantic.errors import PydanticUserError

if TYPE_CHECKING:
    from pydantic.config import ConfigDict

    AnyCallableT = TypeVar('AnyCallableT', bound=Callable[..., Any])

@overload
def validate_call(
    *, config: ConfigDict | None = None, validate_return: bool = False
) -> Callable[[AnyCallableT], AnyCallableT]:
    """Decorator for validating function calls with configuration.

    Args:
        config: The configuration dictionary for validation.
        validate_return: Whether to validate the return value.

    Returns:
        A decorator that can be applied to a function.
    """
    ...

@overload
def validate_call(func: AnyCallableT, /) -> AnyCallableT:
    """Decorator for validating function calls without configuration.

    Args:
        func: The function to be decorated.

    Returns:
        The decorated function with validation applied.
    """
    ...

def validate_call(
    func: AnyCallableT | None = None,
    /,
    *,
    config: ConfigDict | None = None,
    validate_return: bool = False,
) -> AnyCallableT | Callable[[AnyCallableT], AnyCallableT]:
    """!!! abstract "Usage Documentation"
        [Validation Decorator](../concepts/validation_decorator.md)

    Returns a decorated wrapper around the function that validates the arguments and, optionally, the return value.

    Usage may be either as a plain decorator `@validate_call` or with arguments `@validate_call(...)`.

    Args:
        func: The function to be decorated.
        config: The configuration dictionary.
        validate_return: Whether to validate the return value.

    Returns:
        The decorated function with validation applied.

    Raises:
        PydanticUserError: If the function type is not supported or has an invalid signature.

    Example:
        ```python
        from pydantic import validate_call

        @validate_call
        def add(x: int, y: int) -> int:
            return x + y

        # This will validate the arguments
        result = add(1, 2)  # OK: returns 3
        result = add('1', '2')  # Raises ValidationError

        # With validate_return
        @validate_call(validate_return=True)
        def get_number() -> int:
            return "not an int"

        get_number()  # Raises ValidationError during return validation
        ```
    """
    ...
