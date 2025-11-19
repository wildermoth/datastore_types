"""Type stubs for pydantic.functional_validators module.

This module contains decorators and classes for field and model validation.
"""

from __future__ import annotations

import dataclasses
import sys
from functools import partialmethod
from typing import TYPE_CHECKING, Annotated, Any, Callable, Literal, Protocol, TypeVar, Union, overload

from pydantic_core import PydanticUndefined, core_schema
from typing_extensions import Self, TypeAlias

from .annotated_handlers import GetCoreSchemaHandler

if sys.version_info < (3, 11):
    from typing_extensions import Protocol
else:
    from typing import Protocol

__all__ = (
    'AfterValidator',
    'BeforeValidator',
    'PlainValidator',
    'WrapValidator',
    'field_validator',
    'model_validator',
    'SkipValidation',
    'InstanceOf',
    'ValidateAs',
    'ModelWrapValidatorHandler',
)

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~ VALIDATOR CLASSES ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

@dataclasses.dataclass(frozen=True)
class AfterValidator:
    """A metadata class that indicates that a validation should be applied after the inner validation logic.

    Attributes:
        func: The validator function.

    Example:
        ```python
        from typing import Annotated
        from pydantic import AfterValidator, BaseModel, ValidationError

        MyInt = Annotated[int, AfterValidator(lambda v: v + 1)]

        class Model(BaseModel):
            a: MyInt

        print(Model(a=1).a)
        #> 2
        ```
    """

    func: core_schema.NoInfoValidatorFunction | core_schema.WithInfoValidatorFunction

    def __get_pydantic_core_schema__(self, source_type: Any, handler: GetCoreSchemaHandler) -> core_schema.CoreSchema:
        """Get the pydantic core schema.

        Args:
            source_type: The source type.
            handler: The core schema handler.

        Returns:
            The core schema.
        """
        ...

    @classmethod
    def _from_decorator(cls, decorator: Any) -> Self:
        """Create an AfterValidator from a decorator.

        Args:
            decorator: A decorator instance.

        Returns:
            A new AfterValidator instance.
        """
        ...

@dataclasses.dataclass(frozen=True)
class BeforeValidator:
    """A metadata class that indicates that a validation should be applied before the inner validation logic.

    Attributes:
        func: The validator function.
        json_schema_input_type: The input type used to generate the appropriate JSON Schema (in validation mode).
            The actual input type is `Any`.

    Example:
        ```python
        from typing import Annotated
        from pydantic import BaseModel, BeforeValidator

        MyInt = Annotated[int, BeforeValidator(lambda v: v + 1)]

        class Model(BaseModel):
            a: MyInt

        print(Model(a=1).a)
        #> 2
        ```
    """

    func: core_schema.NoInfoValidatorFunction | core_schema.WithInfoValidatorFunction
    json_schema_input_type: Any = PydanticUndefined

    def __get_pydantic_core_schema__(self, source_type: Any, handler: GetCoreSchemaHandler) -> core_schema.CoreSchema:
        """Get the pydantic core schema.

        Args:
            source_type: The source type.
            handler: The core schema handler.

        Returns:
            The core schema.
        """
        ...

    @classmethod
    def _from_decorator(cls, decorator: Any) -> Self:
        """Create a BeforeValidator from a decorator.

        Args:
            decorator: A decorator instance.

        Returns:
            A new BeforeValidator instance.
        """
        ...

@dataclasses.dataclass(frozen=True)
class PlainValidator:
    """A metadata class that indicates that a validation should be applied instead of the inner validation logic.

    Attributes:
        func: The validator function.
        json_schema_input_type: The input type used to generate the appropriate JSON Schema (in validation mode).
            The actual input type is `Any`.
    """

    func: core_schema.NoInfoValidatorFunction | core_schema.WithInfoValidatorFunction
    json_schema_input_type: Any = Any

    def __get_pydantic_core_schema__(self, source_type: Any, handler: GetCoreSchemaHandler) -> core_schema.CoreSchema:
        """Get the pydantic core schema.

        Args:
            source_type: The source type.
            handler: The core schema handler.

        Returns:
            The core schema.
        """
        ...

    @classmethod
    def _from_decorator(cls, decorator: Any) -> Self:
        """Create a PlainValidator from a decorator.

        Args:
            decorator: A decorator instance.

        Returns:
            A new PlainValidator instance.
        """
        ...

@dataclasses.dataclass(frozen=True)
class WrapValidator:
    """A metadata class that indicates that a validation should be applied around the inner validation logic.

    Attributes:
        func: The validator function.
        json_schema_input_type: The input type used to generate the appropriate JSON Schema (in validation mode).
            The actual input type is `Any`.
    """

    func: core_schema.NoInfoWrapValidatorFunction | core_schema.WithInfoWrapValidatorFunction
    json_schema_input_type: Any = PydanticUndefined

    def __get_pydantic_core_schema__(self, source_type: Any, handler: GetCoreSchemaHandler) -> core_schema.CoreSchema:
        """Get the pydantic core schema.

        Args:
            source_type: The source type.
            handler: The core schema handler.

        Returns:
            The core schema.
        """
        ...

    @classmethod
    def _from_decorator(cls, decorator: Any) -> Self:
        """Create a WrapValidator from a decorator.

        Args:
            decorator: A decorator instance.

        Returns:
            A new WrapValidator instance.
        """
        ...

# ~~~~~~~~~~~~~~~~~~~~~~~~~ VALIDATOR PROTOCOLS ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

if TYPE_CHECKING:

    class _OnlyValueValidatorClsMethod(Protocol):
        def __call__(self, cls: Any, value: Any, /) -> Any: ...

    class _V2ValidatorClsMethod(Protocol):
        def __call__(self, cls: Any, value: Any, info: core_schema.ValidationInfo[Any], /) -> Any: ...

    class _OnlyValueWrapValidatorClsMethod(Protocol):
        def __call__(self, cls: Any, value: Any, handler: core_schema.ValidatorFunctionWrapHandler, /) -> Any: ...

    class _V2WrapValidatorClsMethod(Protocol):
        def __call__(
            self,
            cls: Any,
            value: Any,
            handler: core_schema.ValidatorFunctionWrapHandler,
            info: core_schema.ValidationInfo[Any],
            /,
        ) -> Any: ...

    _V2Validator = Union[
        _V2ValidatorClsMethod,
        core_schema.WithInfoValidatorFunction,
        _OnlyValueValidatorClsMethod,
        core_schema.NoInfoValidatorFunction,
    ]

    _V2WrapValidator = Union[
        _V2WrapValidatorClsMethod,
        core_schema.WithInfoWrapValidatorFunction,
        _OnlyValueWrapValidatorClsMethod,
        core_schema.NoInfoWrapValidatorFunction,
    ]

    _PartialClsOrStaticMethod: TypeAlias = Union[classmethod[Any, Any, Any], staticmethod[Any, Any], partialmethod[Any]]

    _V2BeforeAfterOrPlainValidatorType = TypeVar(
        '_V2BeforeAfterOrPlainValidatorType',
        bound=Union[_V2Validator, _PartialClsOrStaticMethod],
    )
    _V2WrapValidatorType = TypeVar('_V2WrapValidatorType', bound=Union[_V2WrapValidator, _PartialClsOrStaticMethod])

FieldValidatorModes: TypeAlias = Literal['before', 'after', 'wrap', 'plain']
"""Type alias for field validator modes."""

# ~~~~~~~~~~~~~~~~~~~~~~~~~ FIELD VALIDATOR ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

@overload
def field_validator(
    field: str,
    /,
    *fields: str,
    mode: Literal['wrap'],
    check_fields: bool | None = ...,
    json_schema_input_type: Any = ...,
) -> Callable[[_V2WrapValidatorType], _V2WrapValidatorType]: ...

@overload
def field_validator(
    field: str,
    /,
    *fields: str,
    mode: Literal['before', 'plain'],
    check_fields: bool | None = ...,
    json_schema_input_type: Any = ...,
) -> Callable[[_V2BeforeAfterOrPlainValidatorType], _V2BeforeAfterOrPlainValidatorType]: ...

@overload
def field_validator(
    field: str,
    /,
    *fields: str,
    mode: Literal['after'] = ...,
    check_fields: bool | None = ...,
) -> Callable[[_V2BeforeAfterOrPlainValidatorType], _V2BeforeAfterOrPlainValidatorType]: ...

def field_validator(
    field: str,
    /,
    *fields: str,
    mode: FieldValidatorModes = 'after',
    check_fields: bool | None = None,
    json_schema_input_type: Any = PydanticUndefined,
) -> Callable[[Any], Any]:
    """Decorate methods on the class indicating that they should be used to validate fields.

    Args:
        field: The first field the field_validator should be called on.
        *fields: Additional field(s) the field_validator should be called on.
        mode: Specifies whether to validate the fields before or after validation.
        check_fields: Whether to check that the fields actually exist on the model.
        json_schema_input_type: The input type of the function for JSON Schema generation.

    Returns:
        A decorator that can be used to decorate a function to be used as a field_validator.

    Example:
        ```python
        from pydantic import BaseModel, field_validator

        class Model(BaseModel):
            a: str

            @field_validator('a')
            @classmethod
            def ensure_foobar(cls, v):
                if 'foobar' not in v:
                    raise ValueError('"foobar" not found in a')
                return v
        ```
    """
    ...

# ~~~~~~~~~~~~~~~~~~~~~~~~~ MODEL VALIDATOR ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

_ModelType = TypeVar('_ModelType')
_ModelTypeCo = TypeVar('_ModelTypeCo', covariant=True)

class ModelWrapValidatorHandler(core_schema.ValidatorFunctionWrapHandler, Protocol[_ModelTypeCo]):
    """@model_validator decorated function handler argument type. This is used when mode='wrap'."""

    def __call__(
        self,
        value: Any,
        outer_location: str | int | None = None,
        /,
    ) -> _ModelTypeCo: ...

class ModelWrapValidatorWithoutInfo(Protocol[_ModelType]):
    """A @model_validator decorated function signature.
    This is used when mode='wrap' and the function does not have info argument.
    """

    def __call__(
        self,
        cls: type[_ModelType],
        value: Any,
        handler: ModelWrapValidatorHandler[_ModelType],
        /,
    ) -> _ModelType: ...

class ModelWrapValidator(Protocol[_ModelType]):
    """A @model_validator decorated function signature. This is used when mode='wrap'."""

    def __call__(
        self,
        cls: type[_ModelType],
        value: Any,
        handler: ModelWrapValidatorHandler[_ModelType],
        info: core_schema.ValidationInfo,
        /,
    ) -> _ModelType: ...

class FreeModelBeforeValidatorWithoutInfo(Protocol):
    """A @model_validator decorated function signature.
    This is used when mode='before' and the function does not have info argument.
    """

    def __call__(
        self,
        value: Any,
        /,
    ) -> Any: ...

class ModelBeforeValidatorWithoutInfo(Protocol):
    """A @model_validator decorated function signature.
    This is used when mode='before' and the function does not have info argument.
    """

    def __call__(
        self,
        cls: Any,
        value: Any,
        /,
    ) -> Any: ...

class FreeModelBeforeValidator(Protocol):
    """A @model_validator decorated function signature. This is used when mode='before'."""

    def __call__(
        self,
        value: Any,
        info: core_schema.ValidationInfo[Any],
        /,
    ) -> Any: ...

class ModelBeforeValidator(Protocol):
    """A @model_validator decorated function signature. This is used when mode='before'."""

    def __call__(
        self,
        cls: Any,
        value: Any,
        info: core_schema.ValidationInfo[Any],
        /,
    ) -> Any: ...

ModelAfterValidatorWithoutInfo = Callable[[_ModelType], _ModelType]
"""A @model_validator decorated function signature. This is used when mode='after'."""

ModelAfterValidator = Callable[[_ModelType, core_schema.ValidationInfo[Any]], _ModelType]
"""A @model_validator decorated function signature. This is used when mode='after'."""

_AnyModelWrapValidator = Union[ModelWrapValidator[_ModelType], ModelWrapValidatorWithoutInfo[_ModelType]]
_AnyModelBeforeValidator = Union[
    FreeModelBeforeValidator, ModelBeforeValidator, FreeModelBeforeValidatorWithoutInfo, ModelBeforeValidatorWithoutInfo
]
_AnyModelAfterValidator = Union[ModelAfterValidator[_ModelType], ModelAfterValidatorWithoutInfo[_ModelType]]

@overload
def model_validator(
    *,
    mode: Literal['wrap'],
) -> Callable[[_AnyModelWrapValidator[_ModelType]], Any]: ...

@overload
def model_validator(
    *,
    mode: Literal['before'],
) -> Callable[[_AnyModelBeforeValidator], Any]: ...

@overload
def model_validator(
    *,
    mode: Literal['after'],
) -> Callable[[_AnyModelAfterValidator[_ModelType]], Any]: ...

def model_validator(
    *,
    mode: Literal['wrap', 'before', 'after'],
) -> Any:
    """Decorate model methods for validation purposes.

    Args:
        mode: A required string literal that specifies the validation mode.
            It can be one of the following: 'wrap', 'before', or 'after'.

    Returns:
        A decorator that can be used to decorate a function to be used as a model validator.

    Example:
        ```python
        from pydantic import BaseModel, model_validator
        from typing_extensions import Self

        class Square(BaseModel):
            width: float
            height: float

            @model_validator(mode='after')
            def verify_square(self) -> Self:
                if self.width != self.height:
                    raise ValueError('width and height do not match')
                return self
        ```
    """
    ...

# ~~~~~~~~~~~~~~~~~~~~~~~~~ UTILITY CLASSES ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

AnyType = TypeVar('AnyType')

if TYPE_CHECKING:
    InstanceOf = Annotated[AnyType, ...]
    """Generic type for annotating a type that is an instance of a given class."""
else:

    @dataclasses.dataclass
    class InstanceOf:
        """Generic type for annotating a type that is an instance of a given class.

        Example:
            ```python
            from pydantic import BaseModel, InstanceOf

            class Foo:
                ...

            class Bar(BaseModel):
                foo: InstanceOf[Foo]

            Bar(foo=Foo())
            ```
        """

        @classmethod
        def __class_getitem__(cls, item: AnyType) -> AnyType: ...

        @classmethod
        def __get_pydantic_core_schema__(cls, source: Any, handler: GetCoreSchemaHandler) -> core_schema.CoreSchema: ...

if TYPE_CHECKING:
    SkipValidation = Annotated[AnyType, ...]
    """If this is applied as an annotation, validation will be skipped."""
else:

    @dataclasses.dataclass
    class SkipValidation:
        """If this is applied as an annotation, validation will be skipped.

        This can be useful if you want to use a type annotation for documentation/IDE purposes,
        and know that it is safe to skip validation for one or more of the fields.

        Example:
            ```python
            from typing import Annotated
            from pydantic import BaseModel, SkipValidation

            class Model(BaseModel):
                a: Annotated[int, SkipValidation]

            m = Model(a='not an int')  # No validation error
            ```
        """

        def __class_getitem__(cls, item: Any) -> Any: ...

        @classmethod
        def __get_pydantic_core_schema__(cls, source: Any, handler: GetCoreSchemaHandler) -> core_schema.CoreSchema: ...

_FromTypeT = TypeVar('_FromTypeT')

class ValidateAs:
    """A helper class to validate a custom type from a type that is natively supported by Pydantic.

    This class allows you to validate using one type (like a Pydantic model) and then convert
    the validated result into another type using an instantiation hook.

    Attributes:
        from_type: The type natively supported by Pydantic to use to perform validation.
        instantiation_hook: A callable taking the validated type as an argument, and returning
            the populated custom type.

    Example:
        ```python
        from typing import Annotated
        from pydantic import BaseModel, TypeAdapter, ValidateAs

        class MyCls:
            def __init__(self, a: int) -> None:
                self.a = a

            def __repr__(self) -> str:
                return f"MyCls(a={self.a})"

        class Model(BaseModel):
            a: int

        ta = TypeAdapter(
            Annotated[MyCls, ValidateAs(Model, lambda v: MyCls(a=v.a))]
        )

        print(ta.validate_python({'a': 1}))
        #> MyCls(a=1)
        ```
    """

    from_type: type[_FromTypeT]
    instantiation_hook: Callable[[_FromTypeT], Any]

    def __init__(self, from_type: type[_FromTypeT], /, instantiation_hook: Callable[[_FromTypeT], Any]) -> None:
        """Initialize ValidateAs.

        Args:
            from_type: The type natively supported by Pydantic to use to perform validation.
            instantiation_hook: A callable taking the validated type as an argument, and returning
                the populated custom type.
        """
        ...

    def __get_pydantic_core_schema__(self, source: Any, handler: GetCoreSchemaHandler) -> core_schema.CoreSchema:
        """Get the pydantic core schema for this ValidateAs instance.

        Args:
            source: The source type.
            handler: The GetCoreSchemaHandler instance.

        Returns:
            The pydantic core schema.
        """
        ...
