"""Type stubs for pydantic.fields module.

This module contains type definitions for field configuration and metadata in Pydantic models.
"""

from __future__ import annotations

import re
import sys
from collections.abc import Callable, Mapping
from dataclasses import Field as DataclassField
from typing import Annotated, Any, ClassVar, Literal, TypeVar, final, overload

import annotated_types
from pydantic_core import PydanticUndefined
from typing_extensions import Self, TypeAlias, TypedDict, Unpack, deprecated

from . import types
from ._internal._namespace_utils import GlobalsNamespace, MappingNamespace
from ._internal._repr import ReprArgs
from .aliases import AliasChoices, AliasGenerator, AliasPath
from .config import JsonDict

if sys.version_info >= (3, 13):
    import warnings
    Deprecated: TypeAlias = warnings.deprecated | deprecated
else:
    Deprecated: TypeAlias = deprecated

__all__ = ('Field', 'FieldInfo', 'PrivateAttr', 'computed_field')

_Unset: Any = PydanticUndefined
_T = TypeVar('_T')

class _FromFieldInfoInputs(TypedDict, total=False):
    """Type checking for **kwargs in FieldInfo.from_field."""
    annotation: type[Any] | None
    default_factory: Callable[[], Any] | Callable[[dict[str, Any]], Any] | None
    alias: str | None
    alias_priority: int | None
    validation_alias: str | AliasPath | AliasChoices | None
    serialization_alias: str | None
    title: str | None
    field_title_generator: Callable[[str, FieldInfo], str] | None
    description: str | None
    examples: list[Any] | None
    exclude: bool | None
    exclude_if: Callable[[Any], bool] | None
    gt: annotated_types.SupportsGt | None
    ge: annotated_types.SupportsGe | None
    lt: annotated_types.SupportsLt | None
    le: annotated_types.SupportsLe | None
    multiple_of: float | None
    strict: bool | None
    min_length: int | None
    max_length: int | None
    pattern: str | re.Pattern[str] | None
    allow_inf_nan: bool | None
    max_digits: int | None
    decimal_places: int | None
    union_mode: Literal['smart', 'left_to_right'] | None
    discriminator: str | types.Discriminator | None
    deprecated: Deprecated | str | bool | None
    json_schema_extra: JsonDict | Callable[[JsonDict], None] | None
    frozen: bool | None
    validate_default: bool | None
    repr: bool
    init: bool | None
    init_var: bool | None
    kw_only: bool | None
    coerce_numbers_to_str: bool | None
    fail_fast: bool | None

class _FieldInfoInputs(_FromFieldInfoInputs, total=False):
    """Type checking for **kwargs in FieldInfo.__init__."""
    default: Any

@final
class FieldInfo:
    """This class holds information about a field.

    `FieldInfo` is used for any field definition regardless of whether the Field()
    function is explicitly used. This class should generally not be instantiated directly;
    instead, use the `Field` function or one of the constructor classmethods.

    Attributes:
        annotation: The type annotation of the field.
        default: The default value of the field. Set to PydanticUndefined if no default is provided.
        default_factory: A callable to generate the default value. The callable can either take 0 arguments
            (in which case it is called as is) or a single argument containing the already validated data.
        alias: The alias name of the field.
        alias_priority: The priority of the field's alias.
        validation_alias: The validation alias of the field (used only for validation, not serialization).
        serialization_alias: The serialization alias of the field (used only for serialization, not validation).
        title: The title of the field.
        field_title_generator: A callable that takes a field name and FieldInfo instance and returns title for it.
        description: The description of the field.
        examples: List of examples of the field.
        exclude: Whether to exclude the field from the model serialization.
        exclude_if: A callable that determines whether to exclude a field during serialization based on its value.
        discriminator: Field name or Discriminator for discriminating the type in a tagged union.
        deprecated: A deprecation message, an instance of `warnings.deprecated` or the `typing_extensions.deprecated` backport,
            or a boolean. If `True`, a default deprecation message will be emitted when accessing the field.
        json_schema_extra: A dict or callable to provide extra JSON schema properties.
        frozen: Whether the field is frozen. If true, attempts to change the value on an instance will raise an error.
        validate_default: Whether to validate the default value of the field.
        repr: Whether to include the field in representation of the model.
        init: Whether the field should be included in the constructor of the dataclass.
        init_var: Whether the field should _only_ be included in the constructor of the dataclass, and not stored.
        kw_only: Whether the field should be a keyword-only argument in the constructor of the dataclass.
        metadata: The metadata list. Contains all the data that isn't expressed as direct `FieldInfo` attributes.
    """

    annotation: type[Any] | None
    default: Any
    default_factory: Callable[[], Any] | Callable[[dict[str, Any]], Any] | None
    alias: str | None
    alias_priority: int | None
    validation_alias: str | AliasPath | AliasChoices | None
    serialization_alias: str | None
    title: str | None
    field_title_generator: Callable[[str, FieldInfo], str] | None
    description: str | None
    examples: list[Any] | None
    exclude: bool | None
    exclude_if: Callable[[Any], bool] | None
    discriminator: str | types.Discriminator | None
    deprecated: Deprecated | str | bool | None
    json_schema_extra: JsonDict | Callable[[JsonDict], None] | None
    frozen: bool | None
    validate_default: bool | None
    repr: bool
    init: bool | None
    init_var: bool | None
    kw_only: bool | None
    metadata: list[Any]

    metadata_lookup: ClassVar[dict[str, Callable[[Any], Any] | None]]
    """A mapping of constraint names to metadata classes that implement those constraints."""

    def __init__(self, **kwargs: Unpack[_FieldInfoInputs]) -> None:
        """Initialize FieldInfo.

        Args:
            **kwargs: Field configuration parameters.
        """
        ...

    @staticmethod
    def from_field(default: Any = PydanticUndefined, **kwargs: Unpack[_FromFieldInfoInputs]) -> FieldInfo:
        """Create a new FieldInfo object with the Field function.

        Args:
            default: The default value for the field.
            **kwargs: Additional arguments dictionary.

        Returns:
            A new FieldInfo object with the given parameters.

        Raises:
            TypeError: If 'annotation' is passed as a keyword argument.
        """
        ...

    @staticmethod
    def from_annotation(annotation: type[Any], *, _source: Any = ...) -> FieldInfo:
        """Create a FieldInfo instance from a bare annotation.

        Args:
            annotation: An annotation object.

        Returns:
            An instance of the field metadata.
        """
        ...

    @staticmethod
    def from_annotated_attribute(annotation: type[Any], default: Any, *, _source: Any = ...) -> FieldInfo:
        """Create FieldInfo from an annotation with a default value.

        Args:
            annotation: The type annotation of the field.
            default: The default value of the field.

        Returns:
            A field object with the passed values.
        """
        ...

    @property
    def deprecation_message(self) -> str | None:
        """The deprecation message to be emitted, or None if not set."""
        ...

    @property
    def default_factory_takes_validated_data(self) -> bool | None:
        """Whether the provided default factory callable has a validated data parameter."""
        ...

    @overload
    def get_default(
        self, *, call_default_factory: Literal[True], validated_data: dict[str, Any] | None = None
    ) -> Any: ...

    @overload
    def get_default(self, *, call_default_factory: Literal[False] = ...) -> Any: ...

    def get_default(self, *, call_default_factory: bool = False, validated_data: dict[str, Any] | None = None) -> Any:
        """Get the default value.

        Args:
            call_default_factory: Whether to call the default factory or not.
            validated_data: The already validated data to be passed to the default factory.

        Returns:
            The default value.
        """
        ...

    def is_required(self) -> bool:
        """Check if the field is required.

        Returns:
            True if the field is required, False otherwise.
        """
        ...

    def rebuild_annotation(self) -> Any:
        """Rebuild the original annotation for use in function signatures.

        Returns:
            The rebuilt annotation.
        """
        ...

    def apply_typevars_map(
        self,
        typevars_map: Mapping[TypeVar, Any] | None,
        globalns: GlobalsNamespace | None = None,
        localns: MappingNamespace | None = None,
    ) -> None:
        """Apply a typevars_map to the annotation.

        This method is used when analyzing parametrized generic types to replace typevars with their concrete types.
        This method applies the `typevars_map` to the annotation in place.

        Args:
            typevars_map: A dictionary mapping type variables to their concrete types.
            globalns: The globals namespace to use during type annotation evaluation.
            localns: The locals namespace to use during type annotation evaluation.
        """
        ...

    def asdict(self) -> dict[str, Any]:
        """Return a dictionary representation of the `FieldInfo` instance.

        The returned value is a dictionary with three items:

        * `annotation`: The type annotation of the field.
        * `metadata`: The metadata list.
        * `attributes`: A mapping of the remaining `FieldInfo` attributes to their values.

        Returns:
            A dictionary with keys 'annotation', 'metadata', and 'attributes'.
        """
        ...

    def __repr_args__(self) -> ReprArgs: ...

# Field function overloads
@overload
def Field(
    default: type[...],  # ellipsis type
    *,
    alias: str | None = ...,
    alias_priority: int | None = ...,
    validation_alias: str | AliasPath | AliasChoices | None = ...,
    serialization_alias: str | None = ...,
    title: str | None = ...,
    field_title_generator: Callable[[str, FieldInfo], str] | None = ...,
    description: str | None = ...,
    examples: list[Any] | None = ...,
    exclude: bool | None = ...,
    exclude_if: Callable[[Any], bool] | None = ...,
    discriminator: str | types.Discriminator | None = ...,
    deprecated: Deprecated | str | bool | None = ...,
    json_schema_extra: JsonDict | Callable[[JsonDict], None] | None = ...,
    frozen: bool | None = ...,
    validate_default: bool | None = ...,
    repr: bool = ...,
    init: bool | None = ...,
    init_var: bool | None = ...,
    kw_only: bool | None = ...,
    pattern: str | re.Pattern[str] | None = ...,
    strict: bool | None = ...,
    coerce_numbers_to_str: bool | None = ...,
    gt: annotated_types.SupportsGt | None = ...,
    ge: annotated_types.SupportsGe | None = ...,
    lt: annotated_types.SupportsLt | None = ...,
    le: annotated_types.SupportsLe | None = ...,
    multiple_of: float | None = ...,
    allow_inf_nan: bool | None = ...,
    max_digits: int | None = ...,
    decimal_places: int | None = ...,
    min_length: int | None = ...,
    max_length: int | None = ...,
    union_mode: Literal['smart', 'left_to_right'] = ...,
    fail_fast: bool | None = ...,
) -> Any: ...

@overload
def Field(
    default: Any,
    *,
    alias: str | None = ...,
    alias_priority: int | None = ...,
    validation_alias: str | AliasPath | AliasChoices | None = ...,
    serialization_alias: str | None = ...,
    title: str | None = ...,
    field_title_generator: Callable[[str, FieldInfo], str] | None = ...,
    description: str | None = ...,
    examples: list[Any] | None = ...,
    exclude: bool | None = ...,
    exclude_if: Callable[[Any], bool] | None = ...,
    discriminator: str | types.Discriminator | None = ...,
    deprecated: Deprecated | str | bool | None = ...,
    json_schema_extra: JsonDict | Callable[[JsonDict], None] | None = ...,
    frozen: bool | None = ...,
    validate_default: Literal[True],
    repr: bool = ...,
    init: bool | None = ...,
    init_var: bool | None = ...,
    kw_only: bool | None = ...,
    pattern: str | re.Pattern[str] | None = ...,
    strict: bool | None = ...,
    coerce_numbers_to_str: bool | None = ...,
    gt: annotated_types.SupportsGt | None = ...,
    ge: annotated_types.SupportsGe | None = ...,
    lt: annotated_types.SupportsLt | None = ...,
    le: annotated_types.SupportsLe | None = ...,
    multiple_of: float | None = ...,
    allow_inf_nan: bool | None = ...,
    max_digits: int | None = ...,
    decimal_places: int | None = ...,
    min_length: int | None = ...,
    max_length: int | None = ...,
    union_mode: Literal['smart', 'left_to_right'] = ...,
    fail_fast: bool | None = ...,
) -> Any: ...

@overload
def Field(
    default: _T,
    *,
    alias: str | None = ...,
    alias_priority: int | None = ...,
    validation_alias: str | AliasPath | AliasChoices | None = ...,
    serialization_alias: str | None = ...,
    title: str | None = ...,
    field_title_generator: Callable[[str, FieldInfo], str] | None = ...,
    description: str | None = ...,
    examples: list[Any] | None = ...,
    exclude: bool | None = ...,
    exclude_if: Callable[[Any], bool] | None = ...,
    discriminator: str | types.Discriminator | None = ...,
    deprecated: Deprecated | str | bool | None = ...,
    json_schema_extra: JsonDict | Callable[[JsonDict], None] | None = ...,
    frozen: bool | None = ...,
    validate_default: Literal[False] = ...,
    repr: bool = ...,
    init: bool | None = ...,
    init_var: bool | None = ...,
    kw_only: bool | None = ...,
    pattern: str | re.Pattern[str] | None = ...,
    strict: bool | None = ...,
    coerce_numbers_to_str: bool | None = ...,
    gt: annotated_types.SupportsGt | None = ...,
    ge: annotated_types.SupportsGe | None = ...,
    lt: annotated_types.SupportsLt | None = ...,
    le: annotated_types.SupportsLe | None = ...,
    multiple_of: float | None = ...,
    allow_inf_nan: bool | None = ...,
    max_digits: int | None = ...,
    decimal_places: int | None = ...,
    min_length: int | None = ...,
    max_length: int | None = ...,
    union_mode: Literal['smart', 'left_to_right'] = ...,
    fail_fast: bool | None = ...,
) -> _T: ...

@overload
def Field(
    *,
    default_factory: Callable[[], Any] | Callable[[dict[str, Any]], Any],
    alias: str | None = ...,
    alias_priority: int | None = ...,
    validation_alias: str | AliasPath | AliasChoices | None = ...,
    serialization_alias: str | None = ...,
    title: str | None = ...,
    field_title_generator: Callable[[str, FieldInfo], str] | None = ...,
    description: str | None = ...,
    examples: list[Any] | None = ...,
    exclude: bool | None = ...,
    exclude_if: Callable[[Any], bool] | None = ...,
    discriminator: str | types.Discriminator | None = ...,
    deprecated: Deprecated | str | bool | None = ...,
    json_schema_extra: JsonDict | Callable[[JsonDict], None] | None = ...,
    frozen: bool | None = ...,
    validate_default: Literal[True],
    repr: bool = ...,
    init: bool | None = ...,
    init_var: bool | None = ...,
    kw_only: bool | None = ...,
    pattern: str | re.Pattern[str] | None = ...,
    strict: bool | None = ...,
    coerce_numbers_to_str: bool | None = ...,
    gt: annotated_types.SupportsGt | None = ...,
    ge: annotated_types.SupportsGe | None = ...,
    lt: annotated_types.SupportsLt | None = ...,
    le: annotated_types.SupportsLe | None = ...,
    multiple_of: float | None = ...,
    allow_inf_nan: bool | None = ...,
    max_digits: int | None = ...,
    decimal_places: int | None = ...,
    min_length: int | None = ...,
    max_length: int | None = ...,
    union_mode: Literal['smart', 'left_to_right'] = ...,
    fail_fast: bool | None = ...,
) -> Any: ...

@overload
def Field(
    *,
    default_factory: Callable[[], _T] | Callable[[dict[str, Any]], _T],
    alias: str | None = ...,
    alias_priority: int | None = ...,
    validation_alias: str | AliasPath | AliasChoices | None = ...,
    serialization_alias: str | None = ...,
    title: str | None = ...,
    field_title_generator: Callable[[str, FieldInfo], str] | None = ...,
    description: str | None = ...,
    examples: list[Any] | None = ...,
    exclude: bool | None = ...,
    exclude_if: Callable[[Any], bool] | None = ...,
    discriminator: str | types.Discriminator | None = ...,
    deprecated: Deprecated | str | bool | None = ...,
    json_schema_extra: JsonDict | Callable[[JsonDict], None] | None = ...,
    frozen: bool | None = ...,
    validate_default: Literal[False] | None = ...,
    repr: bool = ...,
    init: bool | None = ...,
    init_var: bool | None = ...,
    kw_only: bool | None = ...,
    pattern: str | re.Pattern[str] | None = ...,
    strict: bool | None = ...,
    coerce_numbers_to_str: bool | None = ...,
    gt: annotated_types.SupportsGt | None = ...,
    ge: annotated_types.SupportsGe | None = ...,
    lt: annotated_types.SupportsLt | None = ...,
    le: annotated_types.SupportsLe | None = ...,
    multiple_of: float | None = ...,
    allow_inf_nan: bool | None = ...,
    max_digits: int | None = ...,
    decimal_places: int | None = ...,
    min_length: int | None = ...,
    max_length: int | None = ...,
    union_mode: Literal['smart', 'left_to_right'] = ...,
    fail_fast: bool | None = ...,
) -> _T: ...

@overload
def Field(
    *,
    alias: str | None = ...,
    alias_priority: int | None = ...,
    validation_alias: str | AliasPath | AliasChoices | None = ...,
    serialization_alias: str | None = ...,
    title: str | None = ...,
    field_title_generator: Callable[[str, FieldInfo], str] | None = ...,
    description: str | None = ...,
    examples: list[Any] | None = ...,
    exclude: bool | None = ...,
    exclude_if: Callable[[Any], bool] | None = ...,
    discriminator: str | types.Discriminator | None = ...,
    deprecated: Deprecated | str | bool | None = ...,
    json_schema_extra: JsonDict | Callable[[JsonDict], None] | None = ...,
    frozen: bool | None = ...,
    validate_default: bool | None = ...,
    repr: bool = ...,
    init: bool | None = ...,
    init_var: bool | None = ...,
    kw_only: bool | None = ...,
    pattern: str | re.Pattern[str] | None = ...,
    strict: bool | None = ...,
    coerce_numbers_to_str: bool | None = ...,
    gt: annotated_types.SupportsGt | None = ...,
    ge: annotated_types.SupportsGe | None = ...,
    lt: annotated_types.SupportsLt | None = ...,
    le: annotated_types.SupportsLe | None = ...,
    multiple_of: float | None = ...,
    allow_inf_nan: bool | None = ...,
    max_digits: int | None = ...,
    decimal_places: int | None = ...,
    min_length: int | None = ...,
    max_length: int | None = ...,
    union_mode: Literal['smart', 'left_to_right'] = ...,
    fail_fast: bool | None = ...,
) -> Any: ...

def Field(
    default: Any = PydanticUndefined,
    *,
    default_factory: Callable[[], Any] | Callable[[dict[str, Any]], Any] | None = ...,
    alias: str | None = ...,
    alias_priority: int | None = ...,
    validation_alias: str | AliasPath | AliasChoices | None = ...,
    serialization_alias: str | None = ...,
    title: str | None = ...,
    field_title_generator: Callable[[str, FieldInfo], str] | None = ...,
    description: str | None = ...,
    examples: list[Any] | None = ...,
    exclude: bool | None = ...,
    exclude_if: Callable[[Any], bool] | None = ...,
    discriminator: str | types.Discriminator | None = ...,
    deprecated: Deprecated | str | bool | None = ...,
    json_schema_extra: JsonDict | Callable[[JsonDict], None] | None = ...,
    frozen: bool | None = ...,
    validate_default: bool | None = ...,
    repr: bool = ...,
    init: bool | None = ...,
    init_var: bool | None = ...,
    kw_only: bool | None = ...,
    pattern: str | re.Pattern[str] | None = ...,
    strict: bool | None = ...,
    coerce_numbers_to_str: bool | None = ...,
    gt: annotated_types.SupportsGt | None = ...,
    ge: annotated_types.SupportsGe | None = ...,
    lt: annotated_types.SupportsLt | None = ...,
    le: annotated_types.SupportsLe | None = ...,
    multiple_of: float | None = ...,
    allow_inf_nan: bool | None = ...,
    max_digits: int | None = ...,
    decimal_places: int | None = ...,
    min_length: int | None = ...,
    max_length: int | None = ...,
    union_mode: Literal['smart', 'left_to_right'] = ...,
    fail_fast: bool | None = ...,
) -> Any:
    """Create a field for objects that can be configured.

    Used to provide extra information about a field, either for the model schema or complex validation.

    Args:
        default: Default value if the field is not set.
        default_factory: A callable to generate the default value.
        alias: The name to use for the attribute when validating or serializing by alias.
        alias_priority: Priority of the alias.
        validation_alias: Like alias, but only affects validation, not serialization.
        serialization_alias: Like alias, but only affects serialization, not validation.
        title: Human-readable title.
        field_title_generator: A callable that takes a field name and returns title for it.
        description: Human-readable description.
        examples: Example values for this field.
        exclude: Whether to exclude the field from the model serialization.
        exclude_if: A callable that determines whether to exclude a field during serialization.
        discriminator: Field name or Discriminator for discriminating the type in a tagged union.
        deprecated: A deprecation message or boolean.
        json_schema_extra: A dict or callable to provide extra JSON schema properties.
        frozen: Whether the field is frozen.
        validate_default: If True, apply validation to the default value.
        repr: A boolean indicating whether to include the field in the __repr__ output.
        init: Whether the field should be included in the constructor of the dataclass.
        init_var: Whether the field should only be included in the constructor of the dataclass.
        kw_only: Whether the field should be a keyword-only argument in the constructor.
        pattern: Pattern for strings (a regular expression).
        strict: If True, strict validation is applied to the field.
        coerce_numbers_to_str: Whether to enable coercion of any Number type to str.
        gt: Greater than. Only applicable to numbers.
        ge: Greater than or equal. Only applicable to numbers.
        lt: Less than. Only applicable to numbers.
        le: Less than or equal. Only applicable to numbers.
        multiple_of: Value must be a multiple of this. Only applicable to numbers.
        allow_inf_nan: Allow inf, -inf, nan. Only applicable to numbers.
        max_digits: Maximum number of allow digits for strings.
        decimal_places: Maximum number of decimal places allowed for numbers.
        min_length: Minimum length for iterables.
        max_length: Maximum length for iterables.
        union_mode: The strategy to apply when validating a union.
        fail_fast: If True, validation will stop on the first error.

    Returns:
        A new FieldInfo instance.
    """
    ...

class ModelPrivateAttr:
    """A descriptor for private attributes in class models.

    You generally shouldn't be creating `ModelPrivateAttr` instances directly; instead, use
    `PrivateAttr`. This is similar to the relationship between `FieldInfo` and `Field`.

    Attributes:
        default: The default value of the attribute if not provided.
        default_factory: A callable function that generates the default value of the attribute if not provided.
    """

    default: Any
    default_factory: Callable[[], Any] | None

    def __init__(self, default: Any = PydanticUndefined, *, default_factory: Callable[[], Any] | None = None) -> None:
        """Initialize ModelPrivateAttr.

        Indicates that an attribute is intended for private use and not handled during normal validation/serialization.

        Args:
            default: The default value of the attribute if not provided. Defaults to Undefined.
            default_factory: A callable function that generates the default value of the attribute if not provided.
                If both `default` and `default_factory` are set, an error will be raised.
        """
        ...

    def __set_name__(self, cls: type[Any], name: str) -> None:
        """Set the name of the private attribute.

        This implements the descriptor protocol to preserve `__set_name__` defined in PEP 487.

        Args:
            cls: The class that owns this descriptor.
            name: The name of the attribute.
        """
        ...

    def get_default(self) -> Any:
        """Retrieve the default value of the object.

        If `self.default_factory` is `None`, the method will return a deep copy of the `self.default` object.
        If `self.default_factory` is not `None`, it will call `self.default_factory` and return the value returned.

        Returns:
            The default value of the object.
        """
        ...

    def __eq__(self, other: Any) -> bool:
        """Check equality between two ModelPrivateAttr instances.

        Args:
            other: The other object to compare with.

        Returns:
            True if both instances have the same default and default_factory, False otherwise.
        """
        ...

# PrivateAttr function overloads
@overload
def PrivateAttr(
    default: _T,
    *,
    init: Literal[False] = False,
) -> _T: ...

@overload
def PrivateAttr(
    *,
    default_factory: Callable[[], _T],
    init: Literal[False] = False,
) -> _T: ...

@overload
def PrivateAttr(
    *,
    init: Literal[False] = False,
) -> Any: ...

def PrivateAttr(
    default: Any = PydanticUndefined,
    *,
    default_factory: Callable[[], Any] | None = None,
    init: Literal[False] = False,
) -> Any:
    """Indicate that an attribute is intended for private use.

    Private attributes are not validated by Pydantic.

    Args:
        default: The attribute's default value.
        default_factory: Callable that will be called when a default value is needed.
        init: Whether the attribute should be included in the constructor. Always False.

    Returns:
        An instance of ModelPrivateAttr class.

    Raises:
        TypeError: If both default and default_factory are set.
    """
    ...

class ComputedFieldInfo:
    """A container for data from `@computed_field` decorator so that we can access it while building the pydantic-core schema.

    Attributes:
        decorator_repr: A class variable representing the decorator string, '@computed_field'.
        wrapped_property: The wrapped computed field property.
        return_type: The type of the computed field property's return value.
        alias: The alias of the property to be used during serialization.
        alias_priority: The priority of the alias. This affects whether an alias generator is used.
        title: Title of the computed field to include in the serialization JSON schema.
        field_title_generator: A callable that takes a field name and returns title for it.
        description: Description of the computed field to include in the serialization JSON schema.
        deprecated: A deprecation message, an instance of `warnings.deprecated` or the `typing_extensions.deprecated` backport,
            or a boolean. If `True`, a default deprecation message will be emitted when accessing the field.
        examples: Example values of the computed field to include in the serialization JSON schema.
        json_schema_extra: A dict or callable to provide extra JSON schema properties.
        repr: A boolean indicating whether to include the field in the __repr__ output.
    """

    decorator_repr: ClassVar[str]
    wrapped_property: property
    return_type: Any
    alias: str | None
    alias_priority: int | None
    title: str | None
    field_title_generator: Callable[[str, ComputedFieldInfo], str] | None
    description: str | None
    deprecated: Deprecated | str | bool | None
    examples: list[Any] | None
    json_schema_extra: JsonDict | Callable[[JsonDict], None] | None
    repr: bool

    @property
    def deprecation_message(self) -> str | None:
        """The deprecation message to be emitted, or `None` if not set."""
        ...

PropertyT = TypeVar('PropertyT')

@overload
def computed_field(func: PropertyT, /) -> PropertyT: ...

@overload
def computed_field(
    *,
    alias: str | None = None,
    alias_priority: int | None = None,
    title: str | None = None,
    field_title_generator: Callable[[str, ComputedFieldInfo], str] | None = None,
    description: str | None = None,
    deprecated: Deprecated | str | bool | None = None,
    examples: list[Any] | None = None,
    json_schema_extra: JsonDict | Callable[[JsonDict], None] | None = None,
    repr: bool = True,
    return_type: Any = PydanticUndefined,
) -> Callable[[PropertyT], PropertyT]: ...

def computed_field(
    func: PropertyT | None = None,
    /,
    *,
    alias: str | None = None,
    alias_priority: int | None = None,
    title: str | None = None,
    field_title_generator: Callable[[str, ComputedFieldInfo], str] | None = None,
    description: str | None = None,
    deprecated: Deprecated | str | bool | None = None,
    examples: list[Any] | None = None,
    json_schema_extra: JsonDict | Callable[[JsonDict], None] | None = None,
    repr: bool | None = None,
    return_type: Any = PydanticUndefined,
) -> PropertyT | Callable[[PropertyT], PropertyT]:
    """Decorator to include property and cached_property when serializing models or dataclasses.

    Args:
        func: The function to wrap.
        alias: Alias to use when serializing this computed field.
        alias_priority: Priority of the alias.
        title: Title to use when including this computed field in JSON Schema.
        field_title_generator: A callable that takes a field name and returns title for it.
        description: Description to use when including this computed field in JSON Schema.
        deprecated: A deprecation message or boolean.
        examples: Example values to use when including this computed field in JSON Schema.
        json_schema_extra: A dict or callable to provide extra JSON schema properties.
        repr: Whether to include this computed field in model repr.
        return_type: Optional return type for serialization logic.

    Returns:
        A proxy wrapper for the property.
    """
    ...
