"""Type stubs for pydantic.functional_serializers module.

This module contains decorators and classes for field and model serialization.
"""

from __future__ import annotations

import dataclasses
from functools import partial, partialmethod
from typing import TYPE_CHECKING, Annotated, Any, Callable, Literal, TypeVar, overload

from pydantic_core import PydanticUndefined, core_schema
from pydantic_core.core_schema import SerializationInfo, SerializerFunctionWrapHandler, WhenUsed
from typing_extensions import TypeAlias

from . import PydanticUndefinedAnnotation
from .annotated_handlers import GetCoreSchemaHandler

__all__ = (
    'PlainSerializer',
    'WrapSerializer',
    'field_serializer',
    'model_serializer',
    'SerializeAsAny',
)

# ~~~~~~~~~~~~~~~~~~~~~~~~~ SERIALIZER CLASSES ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

@dataclasses.dataclass(frozen=True)
class PlainSerializer:
    """Plain serializers use a function to modify the output of serialization.

    Attributes:
        func: The serializer function.
        return_type: The return type for the function. If omitted it will be inferred from the type annotation.
        when_used: Determines when this serializer should be used. Accepts a string with values 'always',
            'unless-none', 'json', and 'json-unless-none'. Defaults to 'always'.
    """

    func: core_schema.SerializerFunction
    return_type: Any = PydanticUndefined
    when_used: WhenUsed = 'always'

    def __get_pydantic_core_schema__(self, source_type: Any, handler: GetCoreSchemaHandler) -> core_schema.CoreSchema:
        """Get the pydantic core schema.

        Args:
            source_type: The source type.
            handler: The GetCoreSchemaHandler instance.

        Returns:
            The Pydantic core schema.
        """
        ...

@dataclasses.dataclass(frozen=True)
class WrapSerializer:
    """Wrap serializers receive the raw inputs along with a handler function that applies the standard serialization
    logic, and can modify the resulting value before returning it as the final output of serialization.

    Attributes:
        func: The serializer function to be wrapped.
        return_type: The return type for the function. If omitted it will be inferred from the type annotation.
        when_used: Determines when this serializer should be used. Accepts a string with values 'always',
            'unless-none', 'json', and 'json-unless-none'. Defaults to 'always'.
    """

    func: core_schema.WrapSerializerFunction
    return_type: Any = PydanticUndefined
    when_used: WhenUsed = 'always'

    def __get_pydantic_core_schema__(self, source_type: Any, handler: GetCoreSchemaHandler) -> core_schema.CoreSchema:
        """Get the Pydantic core schema.

        Args:
            source_type: Source type.
            handler: Core schema handler.

        Returns:
            The generated core schema of the class.
        """
        ...

# ~~~~~~~~~~~~~~~~~~~~~~~~~ SERIALIZER TYPE ALIASES ~~~~~~~~~~~~~~~~~~~~~~~~~~~

if TYPE_CHECKING:
    _Partial: TypeAlias = 'partial[Any] | partialmethod[Any]'

    FieldPlainSerializer: TypeAlias = 'core_schema.SerializerFunction | _Partial'
    """A field serializer method or function in plain mode."""

    FieldWrapSerializer: TypeAlias = 'core_schema.WrapSerializerFunction | _Partial'
    """A field serializer method or function in wrap mode."""

    FieldSerializer: TypeAlias = 'FieldPlainSerializer | FieldWrapSerializer'
    """A field serializer method or function."""

    _FieldPlainSerializerT = TypeVar('_FieldPlainSerializerT', bound=FieldPlainSerializer)
    _FieldWrapSerializerT = TypeVar('_FieldWrapSerializerT', bound=FieldWrapSerializer)

# ~~~~~~~~~~~~~~~~~~~~~~~~~ FIELD SERIALIZER ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

@overload
def field_serializer(
    field: str,
    /,
    *fields: str,
    mode: Literal['wrap'],
    return_type: Any = ...,
    when_used: WhenUsed = ...,
    check_fields: bool | None = ...,
) -> Callable[[_FieldWrapSerializerT], _FieldWrapSerializerT]: ...

@overload
def field_serializer(
    field: str,
    /,
    *fields: str,
    mode: Literal['plain'] = ...,
    return_type: Any = ...,
    when_used: WhenUsed = ...,
    check_fields: bool | None = ...,
) -> Callable[[_FieldPlainSerializerT], _FieldPlainSerializerT]: ...

def field_serializer(
    *fields: str,
    mode: Literal['plain', 'wrap'] = 'plain',
    return_type: Any = PydanticUndefined,
    when_used: WhenUsed = 'always',
    check_fields: bool | None = None,
) -> Callable[[_FieldWrapSerializerT], _FieldWrapSerializerT] | Callable[[_FieldPlainSerializerT], _FieldPlainSerializerT]:
    """Decorator that enables custom field serialization.

    Four signatures are supported:

    - `(self, value: Any, info: FieldSerializationInfo)`
    - `(self, value: Any, nxt: SerializerFunctionWrapHandler, info: FieldSerializationInfo)`
    - `(value: Any, info: SerializationInfo)`
    - `(value: Any, nxt: SerializerFunctionWrapHandler, info: SerializationInfo)`

    Args:
        fields: Which field(s) the method should be called on.
        mode: The serialization mode.
            - 'plain' means the function will be called instead of the default serialization logic,
            - 'wrap' means the function will be called with an argument to optionally call the
               default serialization logic.
        return_type: Optional return type for the function, if omitted it will be inferred from the type annotation.
        when_used: Determines the serializer will be used for serialization.
        check_fields: Whether to check that the fields actually exist on the model.

    Returns:
        The decorator function.

    Example:
        ```python
        from pydantic import BaseModel, field_serializer

        class StudentModel(BaseModel):
            name: str = 'Jane'
            courses: set[str]

            @field_serializer('courses', when_used='json')
            def serialize_courses_in_order(self, courses: set[str]):
                return sorted(courses)

        student = StudentModel(courses={'Math', 'Chemistry', 'English'})
        print(student.model_dump_json())
        #> {"name":"Jane","courses":["Chemistry","English","Math"]}
        ```
    """
    ...

# ~~~~~~~~~~~~~~~~~~~~~~~~~ MODEL SERIALIZER ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

if TYPE_CHECKING:
    ModelPlainSerializerWithInfo: TypeAlias = Callable[[Any, SerializationInfo[Any]], Any]
    """A model serializer method with the info argument, in plain mode."""

    ModelPlainSerializerWithoutInfo: TypeAlias = Callable[[Any], Any]
    """A model serializer method without the info argument, in plain mode."""

    ModelPlainSerializer: TypeAlias = 'ModelPlainSerializerWithInfo | ModelPlainSerializerWithoutInfo'
    """A model serializer method in plain mode."""

    ModelWrapSerializerWithInfo: TypeAlias = Callable[[Any, SerializerFunctionWrapHandler, SerializationInfo[Any]], Any]
    """A model serializer method with the info argument, in wrap mode."""

    ModelWrapSerializerWithoutInfo: TypeAlias = Callable[[Any, SerializerFunctionWrapHandler], Any]
    """A model serializer method without the info argument, in wrap mode."""

    ModelWrapSerializer: TypeAlias = 'ModelWrapSerializerWithInfo | ModelWrapSerializerWithoutInfo'
    """A model serializer method in wrap mode."""

    ModelSerializer: TypeAlias = 'ModelPlainSerializer | ModelWrapSerializer'
    """A model serializer method."""

    _ModelPlainSerializerT = TypeVar('_ModelPlainSerializerT', bound=ModelPlainSerializer)
    _ModelWrapSerializerT = TypeVar('_ModelWrapSerializerT', bound=ModelWrapSerializer)

@overload
def model_serializer(f: _ModelPlainSerializerT, /) -> _ModelPlainSerializerT: ...

@overload
def model_serializer(
    *, mode: Literal['wrap'], when_used: WhenUsed = 'always', return_type: Any = ...
) -> Callable[[_ModelWrapSerializerT], _ModelWrapSerializerT]: ...

@overload
def model_serializer(
    *,
    mode: Literal['plain'] = ...,
    when_used: WhenUsed = 'always',
    return_type: Any = ...,
) -> Callable[[_ModelPlainSerializerT], _ModelPlainSerializerT]: ...

def model_serializer(
    f: _ModelPlainSerializerT | _ModelWrapSerializerT | None = None,
    /,
    *,
    mode: Literal['plain', 'wrap'] = 'plain',
    when_used: WhenUsed = 'always',
    return_type: Any = PydanticUndefined,
) -> _ModelPlainSerializerT | Callable[[_ModelWrapSerializerT], _ModelWrapSerializerT] | Callable[[_ModelPlainSerializerT], _ModelPlainSerializerT]:
    """Decorator that enables custom model serialization.

    This is useful when a model need to be serialized in a customized manner, allowing for flexibility beyond just specific fields.

    Two signatures are supported for mode='plain', which is the default:

    - `(self)`
    - `(self, info: SerializationInfo)`

    And two other signatures for mode='wrap':

    - `(self, nxt: SerializerFunctionWrapHandler)`
    - `(self, nxt: SerializerFunctionWrapHandler, info: SerializationInfo)`

    Args:
        f: The function to be decorated.
        mode: The serialization mode.
            - 'plain' means the function will be called instead of the default serialization logic
            - 'wrap' means the function will be called with an argument to optionally call the default
                serialization logic.
        when_used: Determines when this serializer should be used.
        return_type: The return type for the function. If omitted it will be inferred from the type annotation.

    Returns:
        The decorator function.

    Example:
        ```python
        from typing import Literal
        from pydantic import BaseModel, model_serializer

        class TemperatureModel(BaseModel):
            unit: Literal['C', 'F']
            value: int

            @model_serializer()
            def serialize_model(self):
                if self.unit == 'F':
                    return {'unit': 'C', 'value': int((self.value - 32) / 1.8)}
                return {'unit': self.unit, 'value': self.value}

        temperature = TemperatureModel(unit='F', value=212)
        print(temperature.model_dump())
        #> {'unit': 'C', 'value': 100}
        ```
    """
    ...

# ~~~~~~~~~~~~~~~~~~~~~~~~~ SERIALIZE AS ANY ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

AnyType = TypeVar('AnyType')

if TYPE_CHECKING:
    SerializeAsAny = Annotated[AnyType, ...]
    """Annotation used to mark a type as having duck-typing serialization behavior.

    See usage documentation for more details.
    """
else:

    @dataclasses.dataclass
    class SerializeAsAny:
        """Annotation used to mark a type as having duck-typing serialization behavior.

        This allows serialization of instances to behave as if they were of type `Any`,
        which can be useful when working with subclasses or dynamic types.

        Example:
            ```python
            from typing import List
            from pydantic import BaseModel, SerializeAsAny

            class Pet:
                def __init__(self, name: str):
                    self.name = name

            class Dog(Pet):
                def __init__(self, name: str, breed: str):
                    super().__init__(name)
                    self.breed = breed

            class Model(BaseModel):
                pet: SerializeAsAny[Pet]
                pets: List[SerializeAsAny[Pet]]

            dog = Dog(name='Fido', breed='Labrador')
            m = Model(pet=dog, pets=[dog])
            print(m.model_dump())
            #> {'pet': {'name': 'Fido', 'breed': 'Labrador'}, 'pets': [{'name': 'Fido', 'breed': 'Labrador'}]}
            ```
        """

        def __class_getitem__(cls, item: Any) -> Any: ...

        def __get_pydantic_core_schema__(
            self, source_type: Any, handler: GetCoreSchemaHandler
        ) -> core_schema.CoreSchema: ...
