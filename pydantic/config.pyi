"""Type stubs for pydantic.config module.

This module contains type definitions for configuring Pydantic models.
"""

from __future__ import annotations

from re import Pattern
from typing import TYPE_CHECKING, Any, Callable, Literal, TypeVar, Union, overload

from typing_extensions import TypeAlias, TypedDict, Unpack, deprecated

from .aliases import AliasGenerator

if TYPE_CHECKING:
    from ._internal._generate_schema import GenerateSchema as _GenerateSchema
    from .fields import ComputedFieldInfo, FieldInfo

__all__ = ('ConfigDict', 'with_config')

# JSON-related type aliases
JsonValue: TypeAlias = Union[int, float, str, bool, None, list['JsonValue'], 'JsonDict']
"""Type alias for JSON values."""

JsonDict: TypeAlias = dict[str, JsonValue]
"""Type alias for JSON dictionaries."""

JsonEncoder = Callable[[Any], Any]
"""A callable that encodes a value to JSON."""

JsonSchemaExtraCallable: TypeAlias = Union[
    Callable[[JsonDict], None],
    Callable[[JsonDict, type[Any]], None],
]
"""A callable that provides extra JSON schema properties."""

ExtraValues = Literal['allow', 'ignore', 'forbid']
"""Literal type for extra values configuration."""

class ConfigDict(TypedDict, total=False):
    """A TypedDict for configuring Pydantic behaviour.

    All configuration options are optional and have sensible defaults.
    """

    title: str | None
    """The title for the generated JSON schema, defaults to the model's name."""

    model_title_generator: Callable[[type], str] | None
    """A callable that takes a model class and returns the title for it."""

    field_title_generator: Callable[[str, FieldInfo | ComputedFieldInfo], str] | None
    """A callable that takes a field's name and info and returns title for it."""

    str_to_lower: bool
    """Whether to convert all characters to lowercase for str types."""

    str_to_upper: bool
    """Whether to convert all characters to uppercase for str types."""

    str_strip_whitespace: bool
    """Whether to strip leading and trailing whitespace for str types."""

    str_min_length: int
    """The minimum length for str types."""

    str_max_length: int | None
    """The maximum length for str types."""

    extra: ExtraValues | None
    """Whether to ignore, allow, or forbid extra data during model initialization."""

    frozen: bool
    """Whether models are faux-immutable."""

    populate_by_name: bool
    """Whether an aliased field may be populated by its name as given by the model attribute.

    This setting is deprecated in v2.11+. Use validate_by_name and validate_by_alias instead.
    """

    use_enum_values: bool
    """Whether to populate models with the value property of enums."""

    validate_assignment: bool
    """Whether to validate the data when the model is changed."""

    arbitrary_types_allowed: bool
    """Whether arbitrary types are allowed for field types."""

    from_attributes: bool
    """Whether to build models and look up discriminators of tagged unions using python object attributes."""

    loc_by_alias: bool
    """Whether to use the actual key provided in the data (e.g. alias) for error locs rather than the field's name."""

    alias_generator: Callable[[str], str] | AliasGenerator | None
    """A callable that takes a field name and returns an alias for it or an instance of AliasGenerator."""

    ignored_types: tuple[type, ...]
    """A tuple of types that may occur as values of class attributes without annotations."""

    allow_inf_nan: bool
    """Whether to allow infinity and NaN values to float and decimal fields."""

    json_schema_extra: JsonDict | JsonSchemaExtraCallable | None
    """A dict or callable to provide extra JSON schema properties."""

    json_encoders: dict[type[object], JsonEncoder] | None
    """A dict of custom JSON encoders for specific types. (Deprecated)"""

    strict: bool
    """If True, strict validation is applied to all fields on the model."""

    revalidate_instances: Literal['always', 'never', 'subclass-instances']
    """When and how to revalidate models and dataclasses during validation."""

    ser_json_timedelta: Literal['iso8601', 'float']
    """The format of JSON serialized timedeltas.

    Deprecated in v2.12, use ser_json_temporal instead.
    """

    ser_json_temporal: Literal['iso8601', 'seconds', 'milliseconds']
    """The format of JSON serialized temporal types from the datetime module."""

    val_temporal_unit: Literal['seconds', 'milliseconds', 'infer']
    """The unit to assume for validating numeric input for datetime-like types."""

    ser_json_bytes: Literal['utf8', 'base64', 'hex']
    """The encoding of JSON serialized bytes."""

    val_json_bytes: Literal['utf8', 'base64', 'hex']
    """The encoding of JSON serialized bytes to decode."""

    ser_json_inf_nan: Literal['null', 'constants', 'strings']
    """The encoding of JSON serialized infinity and NaN float values."""

    validate_default: bool
    """Whether to validate default values during validation."""

    validate_return: bool
    """Whether to validate the return value from call validators."""

    protected_namespaces: tuple[str | Pattern[str], ...]
    """A tuple of strings and/or patterns that prevent models from having fields with names that conflict with them."""

    hide_input_in_errors: bool
    """Whether to hide inputs when printing errors."""

    defer_build: bool
    """Whether to defer model validator and serializer construction until the first model validation."""

    plugin_settings: dict[str, object] | None
    """A dict of settings for plugins."""

    schema_generator: type[_GenerateSchema] | None
    """DEPRECATED in v2.10. A custom schema generator class."""

    json_schema_serialization_defaults_required: bool
    """Whether fields with default values should be marked as required in the serialization schema."""

    json_schema_mode_override: Literal['validation', 'serialization', None]
    """If not None, the specified mode will be used to generate the JSON schema."""

    coerce_numbers_to_str: bool
    """If True, enables automatic coercion of any Number type to str in lax mode."""

    regex_engine: Literal['rust-regex', 'python-re']
    """The regex engine to be used for pattern validation."""

    validation_error_cause: bool
    """If True, Python exceptions that were part of a validation failure will be shown as an exception group."""

    use_attribute_docstrings: bool
    """Whether docstrings of attributes should be used for field descriptions."""

    cache_strings: bool | Literal['all', 'keys', 'none']
    """Whether to cache strings to avoid constructing new Python objects."""

    validate_by_alias: bool
    """Whether an aliased field may be populated by its alias."""

    validate_by_name: bool
    """Whether an aliased field may be populated by its name as given by the model attribute."""

    serialize_by_alias: bool
    """Whether an aliased field should be serialized by its alias."""

    url_preserve_empty_path: bool
    """Whether to preserve empty URL paths when validating values for a URL type."""

_TypeT = TypeVar('_TypeT', bound=type)

@overload
@deprecated('Passing `config` as a keyword argument is deprecated. Pass `config` as a positional argument instead.')
def with_config(*, config: ConfigDict) -> Callable[[_TypeT], _TypeT]: ...

@overload
def with_config(config: ConfigDict, /) -> Callable[[_TypeT], _TypeT]: ...

@overload
def with_config(**config: Unpack[ConfigDict]) -> Callable[[_TypeT], _TypeT]: ...

def with_config(config: ConfigDict | None = None, /, **kwargs: Any) -> Callable[[_TypeT], _TypeT]:
    """A convenience decorator to set a Pydantic configuration on a TypedDict or a dataclass.

    This is particularly useful for TypedDict where setting __pydantic_config__ doesn't play well
    with type checkers.

    Args:
        config: The configuration dictionary to apply.
        **kwargs: Alternative way to specify configuration options.

    Returns:
        A decorator function that applies the configuration to a class.

    Example:
        ```python
        from typing_extensions import TypedDict
        from pydantic import ConfigDict, with_config

        @with_config(ConfigDict(str_to_lower=True))
        class TD(TypedDict):
            x: str
        ```
    """
    ...
