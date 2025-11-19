"""Type stubs for pydantic.json_schema module.

This module contains classes and functions to customize how JSON Schema is generated.
"""

from __future__ import annotations as _annotations

import dataclasses
from collections.abc import Hashable, Iterable, Sequence
from enum import Enum
from re import Pattern
from typing import (
    TYPE_CHECKING,
    Annotated,
    Any,
    Callable,
    Literal,
    NewType,
    TypeVar,
    Union,
    cast,
    overload,
)

from pydantic_core import CoreSchema, PydanticOmit, core_schema
from typing_extensions import TypeAlias, deprecated, final

if TYPE_CHECKING:
    from . import ConfigDict
    from ._internal._schema_generation_shared import GetJsonSchemaFunction
    from ._internal._dataclasses import PydanticDataclass
    from .main import BaseModel

__all__ = [
    'GenerateJsonSchema',
    'JsonSchemaValue',
    'JsonSchemaMode',
    'JsonSchemaWarningKind',
    'WithJsonSchema',
    'Examples',
    'SkipJsonSchema',
    'model_json_schema',
    'models_json_schema',
    'DEFAULT_REF_TEMPLATE',
]

# Type aliases for JSON Schema

JsonSchemaValue = dict[str, Any]
"""A type alias for a JSON schema value. This is a dictionary of string keys to arbitrary JSON values."""

JsonSchemaMode = Literal['validation', 'serialization']
"""A type alias that represents the mode of a JSON schema; either 'validation' or 'serialization'."""

JsonSchemaWarningKind = Literal['skipped-choice', 'non-serializable-default', 'skipped-discriminator']
"""A type alias representing the kinds of warnings that can be emitted during JSON schema generation."""

# Reference types

CoreRef = NewType('CoreRef', str)
DefsRef = NewType('DefsRef', str)
JsonRef = NewType('JsonRef', str)

CoreModeRef = tuple[CoreRef, JsonSchemaMode]

# Constants

DEFAULT_REF_TEMPLATE: str
"""The default format string used to generate reference names."""

class PydanticJsonSchemaWarning(UserWarning):
    """This class is used to emit warnings produced during JSON schema generation.

    See the GenerateJsonSchema.emit_warning and GenerateJsonSchema.render_warning_message
    methods for more details; these can be overridden to control warning behavior.
    """

    ...

NoDefault: object
"""A sentinel value used to indicate that no default value should be used when generating a JSON Schema
for a core schema with a default value."""

@dataclasses.dataclass
class _DefinitionsRemapping:
    """Internal class for remapping definitions."""

    defs_remapping: dict[DefsRef, DefsRef]
    json_remapping: dict[JsonRef, JsonRef]

    @staticmethod
    def from_prioritized_choices(
        prioritized_choices: dict[DefsRef, list[DefsRef]],
        defs_to_json: dict[DefsRef, JsonRef],
        definitions: dict[DefsRef, JsonSchemaValue],
    ) -> _DefinitionsRemapping: ...
    def remap_defs_ref(self, ref: DefsRef) -> DefsRef: ...
    def remap_json_ref(self, ref: JsonRef) -> JsonRef: ...
    def remap_json_schema(self, schema: Any) -> Any: ...

class GenerateJsonSchema:
    """A class for generating JSON schemas.

    This class generates JSON schemas based on configured parameters. The default schema dialect
    is https://json-schema.org/draft/2020-12/schema. The class uses by_alias to configure how
    fields with multiple names are handled and ref_template to format reference names.

    Attributes:
        schema_dialect: The JSON schema dialect used to generate the schema.
        ignored_warning_kinds: Warnings to ignore when generating the schema.
        by_alias: Whether to use field aliases when generating the schema.
        ref_template: The format string used when generating reference names.
        core_to_json_refs: A mapping of core refs to JSON refs.
        core_to_defs_refs: A mapping of core refs to definition refs.
        defs_to_core_refs: A mapping of definition refs to core refs.
        json_to_defs_refs: A mapping of JSON refs to definition refs.
        definitions: Definitions in the schema.

    Args:
        by_alias: Whether to use field aliases in the generated schemas. Defaults to True.
        ref_template: The format string to use when generating reference names. Defaults to '#/$defs/{model}'.
        union_format: The format to use when combining schemas from unions together. Can be one of:
            - 'any_of': Use the anyOf keyword to combine schemas (the default).
            - 'primitive_type_array': Use the type keyword as an array of strings.
    """

    schema_dialect: str
    ignored_warning_kinds: set[JsonSchemaWarningKind]
    by_alias: bool
    ref_template: str
    union_format: Literal['any_of', 'primitive_type_array']
    core_to_json_refs: dict[CoreModeRef, JsonRef]
    core_to_defs_refs: dict[CoreModeRef, DefsRef]
    defs_to_core_refs: dict[DefsRef, CoreModeRef]
    json_to_defs_refs: dict[JsonRef, DefsRef]
    definitions: dict[DefsRef, JsonSchemaValue]

    def __init__(
        self,
        by_alias: bool = True,
        ref_template: str = DEFAULT_REF_TEMPLATE,
        union_format: Literal['any_of', 'primitive_type_array'] = 'any_of',
    ) -> None:
        """Initialize the GenerateJsonSchema instance.

        Args:
            by_alias: Whether to use field aliases in the generated schemas.
            ref_template: The format string to use when generating reference names.
            union_format: The format to use when combining schemas from unions together.
        """
        ...

    @property
    def mode(self) -> JsonSchemaMode: ...

    def build_schema_type_to_method(
        self,
    ) -> dict[str, Callable[[Any], JsonSchemaValue]]:
        """Builds a dictionary mapping fields to methods for generating JSON schemas.

        Returns:
            A dictionary containing the mapping of CoreSchemaOrFieldType to a handler method.

        Raises:
            TypeError: If no method has been defined for generating a JSON schema for a given pydantic core schema type.
        """
        ...

    def generate_definitions(
        self, inputs: Sequence[tuple[Any, JsonSchemaMode, core_schema.CoreSchema]]
    ) -> tuple[dict[tuple[Any, JsonSchemaMode], JsonSchemaValue], dict[DefsRef, JsonSchemaValue]]:
        """Generates JSON schema definitions from a list of core schemas.

        Args:
            inputs: A sequence of tuples, where:
                - The first element is a JSON schema key type.
                - The second element is the JSON mode: either 'validation' or 'serialization'.
                - The third element is a core schema.

        Returns:
            A tuple where:
                - The first element is a dictionary whose keys are tuples of JSON schema key type and JSON mode.
                - The second element is a dictionary whose keys are definition references.

        Raises:
            PydanticUserError: Raised if the JSON schema generator has already been used.
        """
        ...

    def generate(self, schema: CoreSchema, mode: JsonSchemaMode = 'validation') -> JsonSchemaValue:
        """Generates a JSON schema for a specified schema in a specified mode.

        Args:
            schema: A Pydantic model.
            mode: The mode in which to generate the schema. Defaults to 'validation'.

        Returns:
            A JSON schema representing the specified schema.

        Raises:
            PydanticUserError: If the JSON schema generator has already been used to generate a JSON schema.
        """
        ...

    def generate_inner(self, schema: Any) -> JsonSchemaValue:
        """Generates a JSON schema for a given core schema.

        Args:
            schema: The given core schema.

        Returns:
            The generated JSON schema.
        """
        ...

    def sort(self, value: JsonSchemaValue, parent_key: str | None = None) -> JsonSchemaValue:
        """Sort the keys in the JSON schema.

        Override this method to customize the sorting of the JSON schema (e.g., don't sort at all,
        sort all keys unconditionally, etc.).

        By default, alphabetically sort the keys in the JSON schema, skipping the 'properties'
        and 'default' keys to preserve field definition order. This sort is recursive.

        Args:
            value: The JSON schema to sort.
            parent_key: The parent key (used for recursion).

        Returns:
            The sorted JSON schema.
        """
        ...

    # Schema generation methods

    def invalid_schema(self, schema: core_schema.InvalidSchema) -> JsonSchemaValue: ...
    def any_schema(self, schema: core_schema.AnySchema) -> JsonSchemaValue: ...
    def none_schema(self, schema: core_schema.NoneSchema) -> JsonSchemaValue: ...
    def bool_schema(self, schema: core_schema.BoolSchema) -> JsonSchemaValue: ...
    def int_schema(self, schema: core_schema.IntSchema) -> JsonSchemaValue: ...
    def float_schema(self, schema: core_schema.FloatSchema) -> JsonSchemaValue: ...
    def decimal_schema(self, schema: core_schema.DecimalSchema) -> JsonSchemaValue: ...
    def str_schema(self, schema: core_schema.StringSchema) -> JsonSchemaValue: ...
    def bytes_schema(self, schema: core_schema.BytesSchema) -> JsonSchemaValue: ...
    def date_schema(self, schema: core_schema.DateSchema) -> JsonSchemaValue: ...
    def time_schema(self, schema: core_schema.TimeSchema) -> JsonSchemaValue: ...
    def datetime_schema(self, schema: core_schema.DateTimeSchema) -> JsonSchemaValue: ...
    def timezone_schema(self, schema: core_schema.TimezoneSchema) -> JsonSchemaValue: ...
    def timedelta_schema(self, schema: core_schema.TimeDeltaSchema) -> JsonSchemaValue: ...
    def literal_schema(self, schema: core_schema.LiteralSchema) -> JsonSchemaValue: ...
    def is_instance_schema(self, schema: core_schema.IsInstanceSchema) -> JsonSchemaValue: ...
    def is_subclass_schema(self, schema: core_schema.IsSubclassSchema) -> JsonSchemaValue: ...
    def callable_schema(self, schema: core_schema.CallableSchema) -> JsonSchemaValue: ...
    def list_schema(self, schema: core_schema.ListSchema) -> JsonSchemaValue: ...
    def tuple_schema(self, schema: core_schema.TupleSchema) -> JsonSchemaValue: ...
    def set_schema(self, schema: core_schema.SetSchema) -> JsonSchemaValue: ...
    def frozenset_schema(self, schema: core_schema.FrozenSetSchema) -> JsonSchemaValue: ...
    def generator_schema(self, schema: core_schema.GeneratorSchema) -> JsonSchemaValue: ...
    def dict_schema(self, schema: core_schema.DictSchema) -> JsonSchemaValue: ...
    def function_plain_schema(self, schema: core_schema.FunctionPlainSchema) -> JsonSchemaValue: ...
    def function_wrap_schema(self, schema: core_schema.FunctionWrapSchema) -> JsonSchemaValue: ...
    def default_schema(self, schema: core_schema.WithDefaultSchema) -> JsonSchemaValue: ...
    def nullable_schema(self, schema: core_schema.NullableSchema) -> JsonSchemaValue: ...
    def union_schema(self, schema: core_schema.UnionSchema) -> JsonSchemaValue: ...
    def tagged_union_schema(self, schema: core_schema.TaggedUnionSchema) -> JsonSchemaValue: ...
    def model_schema(self, schema: core_schema.ModelSchema) -> JsonSchemaValue: ...
    def dataclass_schema(self, schema: core_schema.DataclassSchema) -> JsonSchemaValue: ...
    def typed_dict_schema(self, schema: core_schema.TypedDictSchema) -> JsonSchemaValue: ...
    def model_fields_schema(self, schema: core_schema.ModelFieldsSchema) -> JsonSchemaValue: ...
    def model_field(self, schema: core_schema.ModelField) -> JsonSchemaValue: ...
    def dataclass_field(self, schema: core_schema.DataclassField) -> JsonSchemaValue: ...
    def typed_dict_field(self, schema: core_schema.TypedDictField) -> JsonSchemaValue: ...
    def computed_field(self, schema: core_schema.ComputedField) -> JsonSchemaValue: ...
    def url_schema(self, schema: core_schema.UrlSchema) -> JsonSchemaValue: ...
    def multi_host_url_schema(self, schema: core_schema.MultiHostUrlSchema) -> JsonSchemaValue: ...
    def uuid_schema(self, schema: core_schema.UuidSchema) -> JsonSchemaValue: ...
    def json_schema(self, schema: core_schema.JsonSchema) -> JsonSchemaValue: ...

    def emit_warning(
        self,
        kind: JsonSchemaWarningKind,
        message: str,
        schema: Any | None = None,
    ) -> None:
        """Emit a warning during JSON schema generation.

        Args:
            kind: The kind of warning to emit.
            message: The warning message.
            schema: The schema that caused the warning (optional).
        """
        ...

    def render_warning_message(self, kind: JsonSchemaWarningKind, message: str) -> str:
        """Render a warning message.

        Args:
            kind: The kind of warning.
            message: The warning message.

        Returns:
            The rendered warning message.
        """
        ...

    def get_cache_defs_ref_schema(self, core_ref: CoreRef) -> tuple[DefsRef, JsonSchemaValue]: ...
    def get_json_ref_counts(self, json_schema: JsonSchemaValue) -> dict[JsonRef, int]: ...
    def get_schema_from_definitions(self, json_ref: JsonRef) -> JsonSchemaValue | None: ...

    def update_with_validations(
        self, json_schema: dict, handler_override: JsonSchemaValue | None, schema: core_schema.CoreSchema
    ) -> None:
        """Update a JSON schema with validation information.

        Args:
            json_schema: The JSON schema to update.
            handler_override: Override for the handler.
            schema: The core schema.
        """
        ...

    class ValidationsMapping:
        """Mappings of core schema keys to JSON schema keys for validations."""

        numeric: dict[str, str]
        string: dict[str, str]
        bytes: dict[str, str]

def model_json_schema(
    cls: type[BaseModel] | type[PydanticDataclass],
    by_alias: bool = True,
    ref_template: str = DEFAULT_REF_TEMPLATE,
    union_format: Literal['any_of', 'primitive_type_array'] = 'any_of',
    schema_generator: type[GenerateJsonSchema] = GenerateJsonSchema,
    mode: JsonSchemaMode = 'validation',
) -> dict[str, Any]:
    """Utility function to generate a JSON Schema for a model.

    Args:
        cls: The model class to generate a JSON Schema for.
        by_alias: If True (the default), fields will be serialized according to their alias.
            If False, fields will be serialized according to their attribute name.
        ref_template: The template to use for generating JSON Schema references.
        union_format: The format to use when combining schemas from unions together. Can be one of:
            - 'any_of': Use the anyOf keyword to combine schemas (the default).
            - 'primitive_type_array': Use the type keyword as an array of strings.
        schema_generator: The class to use for generating the JSON Schema.
        mode: The mode to use for generating the JSON Schema. It can be one of:
            - 'validation': Generate a JSON Schema for validating data.
            - 'serialization': Generate a JSON Schema for serializing data.

    Returns:
        The generated JSON Schema.

    Raises:
        AttributeError: If called on the BaseModel class itself rather than a subclass.
    """
    ...

def models_json_schema(
    models: Sequence[tuple[type[BaseModel] | type[PydanticDataclass], JsonSchemaMode]],
    *,
    by_alias: bool = True,
    title: str | None = None,
    description: str | None = None,
    ref_template: str = DEFAULT_REF_TEMPLATE,
    union_format: Literal['any_of', 'primitive_type_array'] = 'any_of',
    schema_generator: type[GenerateJsonSchema] = GenerateJsonSchema,
) -> tuple[dict[tuple[type[BaseModel] | type[PydanticDataclass], JsonSchemaMode], JsonSchemaValue], JsonSchemaValue]:
    """Utility function to generate a JSON Schema for multiple models.

    Args:
        models: A sequence of tuples of the form (model, mode).
        by_alias: Whether field aliases should be used as keys in the generated JSON Schema.
        title: The title of the generated JSON Schema.
        description: The description of the generated JSON Schema.
        ref_template: The reference template to use for generating JSON Schema references.
        union_format: The format to use when combining schemas from unions together. Can be one of:
            - 'any_of': Use the anyOf keyword to combine schemas (the default).
            - 'primitive_type_array': Use the type keyword as an array of strings.
        schema_generator: The schema generator to use for generating the JSON Schema.

    Returns:
        A tuple where:
            - The first element is a dictionary whose keys are tuples of (model, mode).
            - The second element is a JSON schema containing all definitions.
    """
    ...

@dataclasses.dataclass
class WithJsonSchema:
    """Add a custom JSON schema that overrides the default JSON schema for a field.

    This provides a way to set a JSON schema for types that would otherwise raise errors
    when producing a JSON schema, such as Callable, without needing to create a custom
    subclass of GenerateJsonSchema.

    Note that any modifications to the schema that would normally be made (such as setting
    the title for model fields) will still be performed.

    If mode is set this will only apply to that schema generation mode, allowing you
    to set different json schemas for validation and serialization.

    Attributes:
        json_schema: The custom JSON schema. If None, the schema will be skipped.
        mode: The JSON schema generation mode this applies to. If None, applies to both modes.

    Example:
        ```python
        from typing import Annotated
        from pydantic import BaseModel
        from pydantic.json_schema import WithJsonSchema

        class Model(BaseModel):
            # custom JSON schema for a Callable field
            callback: Annotated[Callable[[int], str], WithJsonSchema({'type': 'string'})]
        ```
    """

    json_schema: JsonSchemaValue | None
    mode: Literal['validation', 'serialization'] | None = None

    def __get_pydantic_json_schema__(
        self, core_schema: core_schema.CoreSchema, handler: Any
    ) -> JsonSchemaValue: ...
    def __hash__(self) -> int: ...

class Examples:
    """Add examples to a JSON schema.

    If the JSON Schema already contains examples, the provided examples will be appended.

    If mode is set this will only apply to that schema generation mode, allowing you
    to add different examples for validation and serialization.

    Args:
        examples: The examples to add. Can be a list or dict (deprecated).
        mode: The JSON schema generation mode this applies to. If None, applies to both modes.
    """

    examples: dict[str, Any] | list[Any]
    mode: Literal['validation', 'serialization'] | None

    @overload
    @deprecated('Using a dict for examples is deprecated since v2.9 and will be removed in v3.0. Use a list instead.')
    def __init__(
        self, examples: dict[str, Any], mode: Literal['validation', 'serialization'] | None = None
    ) -> None: ...
    @overload
    def __init__(self, examples: list[Any], mode: Literal['validation', 'serialization'] | None = None) -> None: ...
    def __init__(
        self, examples: dict[str, Any] | list[Any], mode: Literal['validation', 'serialization'] | None = None
    ) -> None:
        """Initialize Examples with a list or dict of examples.

        Args:
            examples: The examples to add.
            mode: The JSON schema generation mode this applies to.
        """
        ...
    def __get_pydantic_json_schema__(
        self, core_schema: core_schema.CoreSchema, handler: Any
    ) -> JsonSchemaValue: ...
    def __hash__(self) -> int: ...

AnyType = TypeVar('AnyType')

if TYPE_CHECKING:
    SkipJsonSchema = Annotated[AnyType, ...]
else:

    @dataclasses.dataclass
    class SkipJsonSchema:
        """Skip generating a JSON schema for a field.

        Add this as an annotation on a field to skip generating a JSON schema for that field.

        Example:
            ```python
            from typing import Annotated
            from pydantic import BaseModel
            from pydantic.json_schema import SkipJsonSchema

            class Model(BaseModel):
                # This field will not appear in the JSON schema
                internal_id: Annotated[int, SkipJsonSchema()]
            ```
        """

        def __get_pydantic_json_schema__(
            self, core_schema: core_schema.CoreSchema, handler: Any
        ) -> JsonSchemaValue: ...
