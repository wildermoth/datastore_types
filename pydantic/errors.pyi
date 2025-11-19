"""Type stubs for pydantic.errors module.

This module contains Pydantic-specific error classes and error code types.
"""

from __future__ import annotations as _annotations

import re
from typing import Any, ClassVar, Literal

from typing_extensions import Self
from typing_inspection.introspection import Qualifier

__all__ = (
    'PydanticUserError',
    'PydanticUndefinedAnnotation',
    'PydanticImportError',
    'PydanticSchemaGenerationError',
    'PydanticInvalidForJsonSchema',
    'PydanticForbiddenQualifier',
    'PydanticErrorCodes',
)

PydanticErrorCodes = Literal[
    'class-not-fully-defined',
    'custom-json-schema',
    'decorator-missing-field',
    'discriminator-no-field',
    'discriminator-alias-type',
    'discriminator-needs-literal',
    'discriminator-alias',
    'discriminator-validator',
    'callable-discriminator-no-tag',
    'typed-dict-version',
    'model-field-overridden',
    'model-field-missing-annotation',
    'config-both',
    'removed-kwargs',
    'circular-reference-schema',
    'invalid-for-json-schema',
    'json-schema-already-used',
    'base-model-instantiated',
    'undefined-annotation',
    'schema-for-unknown-type',
    'import-error',
    'create-model-field-definitions',
    'validator-no-fields',
    'validator-invalid-fields',
    'validator-instance-method',
    'validator-input-type',
    'root-validator-pre-skip',
    'model-serializer-instance-method',
    'validator-field-config-info',
    'validator-v1-signature',
    'validator-signature',
    'field-serializer-signature',
    'model-serializer-signature',
    'multiple-field-serializers',
    'invalid-annotated-type',
    'type-adapter-config-unused',
    'root-model-extra',
    'unevaluable-type-annotation',
    'dataclass-init-false-extra-allow',
    'clashing-init-and-init-var',
    'model-config-invalid-field-name',
    'with-config-on-model',
    'dataclass-on-model',
    'validate-call-type',
    'unpack-typed-dict',
    'overlapping-unpack-typed-dict',
    'invalid-self-type',
    'validate-by-alias-and-name-false',
]

DEV_ERROR_DOCS_URL: str
"""Base URL for Pydantic error documentation."""

class PydanticErrorMixin:
    """A mixin class for common functionality shared by all Pydantic-specific errors.

    Attributes:
        message: A message describing the error.
        code: An optional error code from PydanticErrorCodes enum.
    """

    message: str
    code: PydanticErrorCodes | None

    def __init__(self, message: str, *, code: PydanticErrorCodes | None) -> None:
        """Initialize the error with a message and optional code.

        Args:
            message: A message describing the error.
            code: An optional error code from PydanticErrorCodes enum.
        """
        ...
    def __str__(self) -> str: ...

class PydanticUserError(PydanticErrorMixin, TypeError):
    """An error raised due to incorrect use of Pydantic.

    This is a TypeError subclass that provides Pydantic-specific error information.
    """

    ...

class PydanticUndefinedAnnotation(PydanticErrorMixin, NameError):
    """A subclass of NameError raised when handling undefined annotations during CoreSchema generation.

    Attributes:
        name: Name of the error.
        message: Description of the error.
    """

    name: str

    def __init__(self, name: str, message: str) -> None:
        """Initialize the error with a name and message.

        Args:
            name: Name of the undefined annotation.
            message: Description of the error.
        """
        ...
    @classmethod
    def from_name_error(cls, name_error: NameError) -> Self:
        """Convert a NameError to a PydanticUndefinedAnnotation error.

        Args:
            name_error: NameError to be converted.

        Returns:
            Converted PydanticUndefinedAnnotation error.
        """
        ...

class PydanticImportError(PydanticErrorMixin, ImportError):
    """An error raised when an import fails due to module changes between V1 and V2.

    Attributes:
        message: Description of the error.
    """

    def __init__(self, message: str) -> None:
        """Initialize the error with a message.

        Args:
            message: Description of the error.
        """
        ...

class PydanticSchemaGenerationError(PydanticUserError):
    """An error raised during failures to generate a CoreSchema for some type.

    Attributes:
        message: Description of the error.
    """

    def __init__(self, message: str) -> None:
        """Initialize the error with a message.

        Args:
            message: Description of the error.
        """
        ...

class PydanticInvalidForJsonSchema(PydanticUserError):
    """An error raised during failures to generate a JSON schema for some CoreSchema.

    Attributes:
        message: Description of the error.
    """

    def __init__(self, message: str) -> None:
        """Initialize the error with a message.

        Args:
            message: Description of the error.
        """
        ...

class PydanticForbiddenQualifier(PydanticUserError):
    """An error raised if a forbidden type qualifier is found in a type annotation.

    This error is raised when a type annotation uses a forbidden qualifier like
    Required, NotRequired, ReadOnly, ClassVar, InitVar, or Final.
    """

    _qualifier_repr_map: ClassVar[dict[Qualifier, str]]

    def __init__(self, qualifier: Qualifier, annotation: Any) -> None:
        """Initialize the error with a qualifier and annotation.

        Args:
            qualifier: The forbidden type qualifier.
            annotation: The annotation that contains the forbidden qualifier.
        """
        ...
