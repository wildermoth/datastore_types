"""Type stubs for pydantic.types module.

This module contains custom types used by Pydantic for validation and serialization.
"""

from __future__ import annotations

import dataclasses as _dataclasses
from collections.abc import Hashable
from datetime import date, datetime
from decimal import Decimal
from pathlib import Path
from re import Pattern
from typing import Annotated, Any, Callable, ClassVar, Literal, TypeVar
from uuid import UUID

import annotated_types
from pydantic_core import CoreSchema

from ._internal import _fields
from .annotated_handlers import GetCoreSchemaHandler, GetJsonSchemaHandler
from .json_schema import JsonSchemaValue

__all__ = (
    'Strict',
    'StrictStr',
    'SocketPath',
    'conbytes',
    'conlist',
    'conset',
    'confrozenset',
    'constr',
    'ImportString',
    'conint',
    'PositiveInt',
    'NegativeInt',
    'NonNegativeInt',
    'NonPositiveInt',
    'confloat',
    'PositiveFloat',
    'NegativeFloat',
    'NonNegativeFloat',
    'NonPositiveFloat',
    'FiniteFloat',
    'condecimal',
    'UUID1',
    'UUID3',
    'UUID4',
    'UUID5',
    'UUID6',
    'UUID7',
    'UUID8',
    'FilePath',
    'DirectoryPath',
    'NewPath',
    'Json',
    'Secret',
    'SecretStr',
    'SecretBytes',
    'StrictBool',
    'StrictBytes',
    'StrictInt',
    'StrictFloat',
    'PaymentCardNumber',
    'ByteSize',
    'PastDate',
    'FutureDate',
    'PastDatetime',
    'FutureDatetime',
    'condate',
    'AwareDatetime',
    'NaiveDatetime',
    'AllowInfNan',
    'EncoderProtocol',
    'EncodedBytes',
    'EncodedStr',
    'Base64Encoder',
    'Base64Bytes',
    'Base64Str',
    'Base64UrlBytes',
    'Base64UrlStr',
    'GetPydanticSchema',
    'StringConstraints',
    'Tag',
    'Discriminator',
    'JsonValue',
    'OnErrorOmit',
    'FailFast',
)

T = TypeVar('T')

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~ METADATA CLASSES ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

@_dataclasses.dataclass
class Strict(_fields.PydanticMetadata, annotated_types.BaseMetadata):
    """A field metadata class to indicate that a field should be validated in strict mode.

    Attributes:
        strict: Whether to validate the field in strict mode.
    """

    strict: bool = True

    def __hash__(self) -> int: ...

@_dataclasses.dataclass
class AllowInfNan(_fields.PydanticMetadata):
    """A field metadata class to indicate that a field should allow -inf, inf, and nan.

    Attributes:
        allow_inf_nan: Whether to allow -inf, inf, and nan.
    """

    allow_inf_nan: bool = True

    def __hash__(self) -> int: ...

@_dataclasses.dataclass(frozen=True)
class StringConstraints(annotated_types.GroupedMetadata):
    """A field metadata class to apply constraints to str types.

    Attributes:
        strip_whitespace: Whether to remove leading and trailing whitespace.
        to_upper: Whether to convert the string to uppercase.
        to_lower: Whether to convert the string to lowercase.
        strict: Whether to validate the string in strict mode.
        min_length: The minimum length of the string.
        max_length: The maximum length of the string.
        pattern: A regex pattern that the string must match.
    """

    strip_whitespace: bool | None = None
    to_upper: bool | None = None
    to_lower: bool | None = None
    strict: bool | None = None
    min_length: int | None = None
    max_length: int | None = None
    pattern: str | Pattern[str] | None = None

@_dataclasses.dataclass
class FailFast(_fields.PydanticMetadata, annotated_types.BaseMetadata):
    """A field metadata class to indicate that validation should stop on the first error.

    Attributes:
        fail_fast: Whether to stop validation on the first error.
    """

    fail_fast: bool = True

    def __hash__(self) -> int: ...

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ BOOLEAN TYPES ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

StrictBool = Annotated[bool, Strict()]
"""A boolean that must be either True or False."""

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ INTEGER TYPES ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

def conint(
    *,
    strict: bool | None = None,
    gt: int | None = None,
    ge: int | None = None,
    lt: int | None = None,
    le: int | None = None,
    multiple_of: int | None = None,
) -> type[int]:
    """A wrapper around int that allows for additional constraints.

    Args:
        strict: Whether to validate the integer in strict mode.
        gt: The value must be greater than this.
        ge: The value must be greater than or equal to this.
        lt: The value must be less than this.
        le: The value must be less than or equal to this.
        multiple_of: The value must be a multiple of this.

    Returns:
        The wrapped integer type.
    """
    ...

PositiveInt = Annotated[int, annotated_types.Gt(0)]
"""An integer that must be greater than zero."""

NegativeInt = Annotated[int, annotated_types.Lt(0)]
"""An integer that must be less than zero."""

NonPositiveInt = Annotated[int, annotated_types.Le(0)]
"""An integer that must be less than or equal to zero."""

NonNegativeInt = Annotated[int, annotated_types.Ge(0)]
"""An integer that must be greater than or equal to zero."""

StrictInt = Annotated[int, Strict()]
"""An integer that must be validated in strict mode."""

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ FLOAT TYPES ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

def confloat(
    *,
    strict: bool | None = None,
    gt: float | None = None,
    ge: float | None = None,
    lt: float | None = None,
    le: float | None = None,
    multiple_of: float | None = None,
    allow_inf_nan: bool | None = None,
) -> type[float]:
    """A wrapper around float that allows for additional constraints.

    Args:
        strict: Whether to validate the float in strict mode.
        gt: The value must be greater than this.
        ge: The value must be greater than or equal to this.
        lt: The value must be less than this.
        le: The value must be less than or equal to this.
        multiple_of: The value must be a multiple of this.
        allow_inf_nan: Whether to allow -inf, inf, and nan.

    Returns:
        The wrapped float type.
    """
    ...

PositiveFloat = Annotated[float, annotated_types.Gt(0)]
"""A float that must be greater than zero."""

NegativeFloat = Annotated[float, annotated_types.Lt(0)]
"""A float that must be less than zero."""

NonPositiveFloat = Annotated[float, annotated_types.Le(0)]
"""A float that must be less than or equal to zero."""

NonNegativeFloat = Annotated[float, annotated_types.Ge(0)]
"""A float that must be greater than or equal to zero."""

StrictFloat = Annotated[float, Strict(True)]
"""A float that must be validated in strict mode."""

FiniteFloat = Annotated[float, AllowInfNan(False)]
"""A float that must be finite (not -inf, inf, or nan)."""

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ BYTES TYPES ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

def conbytes(
    *,
    min_length: int | None = None,
    max_length: int | None = None,
    strict: bool | None = None,
) -> type[bytes]:
    """A wrapper around bytes that allows for additional constraints.

    Args:
        min_length: The minimum length of the bytes.
        max_length: The maximum length of the bytes.
        strict: Whether to validate the bytes in strict mode.

    Returns:
        The wrapped bytes type.
    """
    ...

StrictBytes = Annotated[bytes, Strict()]
"""A bytes that must be validated in strict mode."""

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ STRING TYPES ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

def constr(
    *,
    strip_whitespace: bool | None = None,
    to_upper: bool | None = None,
    to_lower: bool | None = None,
    strict: bool | None = None,
    min_length: int | None = None,
    max_length: int | None = None,
    pattern: str | Pattern[str] | None = None,
) -> type[str]:
    """A wrapper around str that allows for additional constraints.

    Args:
        strip_whitespace: Whether to remove leading and trailing whitespace.
        to_upper: Whether to turn all characters to uppercase.
        to_lower: Whether to turn all characters to lowercase.
        strict: Whether to validate the string in strict mode.
        min_length: The minimum length of the string.
        max_length: The maximum length of the string.
        pattern: A regex pattern to validate the string against.

    Returns:
        The wrapped string type.
    """
    ...

StrictStr = Annotated[str, Strict()]
"""A string that must be validated in strict mode."""

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~ COLLECTION TYPES ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

HashableItemType = TypeVar('HashableItemType', bound=Hashable)
AnyItemType = TypeVar('AnyItemType')

def conset(
    item_type: type[HashableItemType], *, min_length: int | None = None, max_length: int | None = None
) -> type[set[HashableItemType]]:
    """A wrapper around typing.Set that allows for additional constraints.

    Args:
        item_type: The type of the items in the set.
        min_length: The minimum length of the set.
        max_length: The maximum length of the set.

    Returns:
        The wrapped set type.
    """
    ...

def confrozenset(
    item_type: type[HashableItemType], *, min_length: int | None = None, max_length: int | None = None
) -> type[frozenset[HashableItemType]]:
    """A wrapper around typing.FrozenSet that allows for additional constraints.

    Args:
        item_type: The type of the items in the frozenset.
        min_length: The minimum length of the frozenset.
        max_length: The maximum length of the frozenset.

    Returns:
        The wrapped frozenset type.
    """
    ...

def conlist(
    item_type: type[AnyItemType],
    *,
    min_length: int | None = None,
    max_length: int | None = None,
    unique_items: bool | None = None,
) -> type[list[AnyItemType]]:
    """A wrapper around list that adds validation.

    Args:
        item_type: The type of the items in the list.
        min_length: The minimum length of the list.
        max_length: The maximum length of the list.
        unique_items: Whether the items in the list must be unique. (Deprecated)

    Returns:
        The wrapped list type.
    """
    ...

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~ DECIMAL TYPES ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

def condecimal(
    *,
    strict: bool | None = None,
    gt: Decimal | None = None,
    ge: Decimal | None = None,
    lt: Decimal | None = None,
    le: Decimal | None = None,
    multiple_of: Decimal | None = None,
    max_digits: int | None = None,
    decimal_places: int | None = None,
    allow_inf_nan: bool | None = None,
) -> type[Decimal]:
    """A wrapper around Decimal that allows for additional constraints.

    Args:
        strict: Whether to validate the decimal in strict mode.
        gt: The value must be greater than this.
        ge: The value must be greater than or equal to this.
        lt: The value must be less than this.
        le: The value must be less than or equal to this.
        multiple_of: The value must be a multiple of this.
        max_digits: The maximum number of digits.
        decimal_places: The maximum number of decimal places.
        allow_inf_nan: Whether to allow -inf, inf, and nan.

    Returns:
        The wrapped Decimal type.
    """
    ...

# ~~~~~~~~~~~~~~~~~~~~~~~~~~ IMPORT STRING TYPE ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

AnyType = TypeVar('AnyType')

class ImportString:
    """A type that can be used to import a Python object from a string.

    ImportString expects a string and loads the Python object importable at that dotted path.
    """

    @classmethod
    def __class_getitem__(cls, item: AnyType) -> AnyType: ...

    @classmethod
    def __get_pydantic_core_schema__(
        cls, source: type[Any], handler: GetCoreSchemaHandler
    ) -> CoreSchema: ...

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ UUID TYPES ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

@_dataclasses.dataclass
class UuidVersion(_fields.PydanticMetadata):
    """A field metadata class to indicate a UUID version.

    Use this class as an annotation via Annotated to specify which UUID version is expected.

    Attributes:
        uuid_version: The version of the UUID. Must be one of 1, 3, 4, 5, 6, 7 or 8.

    Example:
        ```python
        from typing import Annotated
        from uuid import UUID
        from pydantic.types import UuidVersion

        UUID1 = Annotated[UUID, UuidVersion(1)]
        ```
    """

    uuid_version: Literal[1, 3, 4, 5, 6, 7, 8]

    def __get_pydantic_json_schema__(
        self, core_schema: CoreSchema, handler: GetJsonSchemaHandler
    ) -> JsonSchemaValue: ...

    def __get_pydantic_core_schema__(self, source: Any, handler: GetCoreSchemaHandler) -> CoreSchema: ...

    def __hash__(self) -> int: ...

UUID1 = Annotated[UUID, UuidVersion(1)]
"""A UUID that must be version 1.

Example:
    ```python
    import uuid
    from pydantic import UUID1, BaseModel

    class Model(BaseModel):
        uuid1: UUID1

    Model(uuid1=uuid.uuid1())
    ```
"""

UUID3 = Annotated[UUID, UuidVersion(3)]
"""A UUID that must be version 3.

Example:
    ```python
    import uuid
    from pydantic import UUID3, BaseModel

    class Model(BaseModel):
        uuid3: UUID3

    Model(uuid3=uuid.uuid3(uuid.NAMESPACE_DNS, 'pydantic.org'))
    ```
"""

UUID4 = Annotated[UUID, UuidVersion(4)]
"""A UUID that must be version 4.

Example:
    ```python
    import uuid
    from pydantic import UUID4, BaseModel

    class Model(BaseModel):
        uuid4: UUID4

    Model(uuid4=uuid.uuid4())
    ```
"""

UUID5 = Annotated[UUID, UuidVersion(5)]
"""A UUID that must be version 5.

Example:
    ```python
    import uuid
    from pydantic import UUID5, BaseModel

    class Model(BaseModel):
        uuid5: UUID5

    Model(uuid5=uuid.uuid5(uuid.NAMESPACE_DNS, 'pydantic.org'))
    ```
"""

UUID6 = Annotated[UUID, UuidVersion(6)]
"""A UUID that must be version 6."""

UUID7 = Annotated[UUID, UuidVersion(7)]
"""A UUID that must be version 7."""

UUID8 = Annotated[UUID, UuidVersion(8)]
"""A UUID that must be version 8."""

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ PATH TYPES ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

FilePath = Annotated[Path, ...]
"""A path that must be a file."""

DirectoryPath = Annotated[Path, ...]
"""A path that must be a directory."""

NewPath = Annotated[Path, ...]
"""A path that must not exist."""

SocketPath = Annotated[Path, ...]
"""A path that must be a socket."""

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ JSON TYPE ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

class Json:
    """A type that can be used to parse JSON strings into Python objects.

    When used as a type annotation, the field will accept JSON strings and parse them
    into the specified type.
    """

    @classmethod
    def __class_getitem__(cls, item: type[T]) -> type[T]: ...

    @classmethod
    def __get_pydantic_core_schema__(
        cls, source: type[Any], handler: GetCoreSchemaHandler
    ) -> CoreSchema: ...

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ SECRET TYPES ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

SecretType = TypeVar('SecretType', str, bytes)

class Secret:
    """Base class for secret types that hide their values when displayed.

    This is a generic class that can be used with str or bytes.
    """

    def __init__(self, secret_value: SecretType) -> None:
        """Initialize a secret.

        Args:
            secret_value: The secret value to hide.
        """
        ...

    def get_secret_value(self) -> SecretType:
        """Get the secret value.

        Returns:
            The secret value.
        """
        ...

class SecretStr(Secret[str]):
    """A string that will be hidden when displayed."""

    def __init__(self, secret_value: str) -> None:
        """Initialize a secret string.

        Args:
            secret_value: The secret string value.
        """
        ...

    def get_secret_value(self) -> str:
        """Get the secret string value.

        Returns:
            The secret string.
        """
        ...

class SecretBytes(Secret[bytes]):
    """Bytes that will be hidden when displayed."""

    def __init__(self, secret_value: bytes) -> None:
        """Initialize secret bytes.

        Args:
            secret_value: The secret bytes value.
        """
        ...

    def get_secret_value(self) -> bytes:
        """Get the secret bytes value.

        Returns:
            The secret bytes.
        """
        ...

# ~~~~~~~~~~~~~~~~~~~~~~~~~ PAYMENT CARD NUMBER ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

class PaymentCardNumber(str):
    """A payment card number that will be validated and masked."""

    def __init__(self, card_number: str) -> None:
        """Initialize a payment card number.

        Args:
            card_number: The card number string.
        """
        ...

    @property
    def masked(self) -> str:
        """Get the masked card number.

        Returns:
            The masked card number.
        """
        ...

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ BYTESIZE TYPE ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

class ByteSize(int):
    """A type that represents a size in bytes, with human-readable formatting."""

    @classmethod
    def __get_pydantic_core_schema__(
        cls, source: type[Any], handler: GetCoreSchemaHandler
    ) -> CoreSchema: ...

    def human_readable(self, decimal: bool = False) -> str:
        """Get a human-readable representation of the byte size.

        Args:
            decimal: Whether to use decimal (1000) or binary (1024) units.

        Returns:
            A human-readable string representation.
        """
        ...

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ DATE TYPES ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

def condate(
    *,
    strict: bool | None = None,
    gt: date | None = None,
    ge: date | None = None,
    lt: date | None = None,
    le: date | None = None,
) -> type[date]:
    """A wrapper around date that allows for additional constraints.

    Args:
        strict: Whether to validate the date in strict mode.
        gt: The value must be greater than this.
        ge: The value must be greater than or equal to this.
        lt: The value must be less than this.
        le: The value must be less than or equal to this.

    Returns:
        The wrapped date type.
    """
    ...

class PastDate:
    """A date that must be in the past."""

    @classmethod
    def __class_getitem__(cls, item: Any) -> Any: ...

    @classmethod
    def __get_pydantic_core_schema__(
        cls, source: type[Any], handler: GetCoreSchemaHandler
    ) -> CoreSchema: ...

class FutureDate:
    """A date that must be in the future."""

    @classmethod
    def __class_getitem__(cls, item: Any) -> Any: ...

    @classmethod
    def __get_pydantic_core_schema__(
        cls, source: type[Any], handler: GetCoreSchemaHandler
    ) -> CoreSchema: ...

# ~~~~~~~~~~~~~~~~~~~~~~~~~ DATETIME TYPES ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

class AwareDatetime:
    """A datetime that must be timezone-aware."""

    @classmethod
    def __class_getitem__(cls, item: Any) -> Any: ...

    @classmethod
    def __get_pydantic_core_schema__(
        cls, source: type[Any], handler: GetCoreSchemaHandler
    ) -> CoreSchema: ...

class NaiveDatetime:
    """A datetime that must be timezone-naive."""

    @classmethod
    def __class_getitem__(cls, item: Any) -> Any: ...

    @classmethod
    def __get_pydantic_core_schema__(
        cls, source: type[Any], handler: GetCoreSchemaHandler
    ) -> CoreSchema: ...

class PastDatetime:
    """A datetime that must be in the past."""

    @classmethod
    def __class_getitem__(cls, item: Any) -> Any: ...

    @classmethod
    def __get_pydantic_core_schema__(
        cls, source: type[Any], handler: GetCoreSchemaHandler
    ) -> CoreSchema: ...

class FutureDatetime:
    """A datetime that must be in the future."""

    @classmethod
    def __class_getitem__(cls, item: Any) -> Any: ...

    @classmethod
    def __get_pydantic_core_schema__(
        cls, source: type[Any], handler: GetCoreSchemaHandler
    ) -> CoreSchema: ...

# ~~~~~~~~~~~~~~~~~~~~~~~~~ ENCODED TYPES ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

class EncoderProtocol:
    """Protocol for encoding and decoding bytes/strings."""

    @classmethod
    def decode(cls, data: bytes) -> bytes:
        """Decode bytes.

        Args:
            data: The bytes to decode.

        Returns:
            The decoded bytes.
        """
        ...

    @classmethod
    def encode(cls, value: bytes) -> bytes:
        """Encode bytes.

        Args:
            value: The bytes to encode.

        Returns:
            The encoded bytes.
        """
        ...

    @classmethod
    def get_json_format(cls) -> str:
        """Get the JSON format string.

        Returns:
            The JSON format identifier.
        """
        ...

class Base64Encoder(EncoderProtocol):
    """Standard (non-URL-safe) Base64 encoder.

    This encoder uses standard base64 encoding/decoding with alphabet A-Za-z0-9+/.
    """

    @classmethod
    def decode(cls, data: bytes) -> bytes:
        """Decode base64-encoded bytes to original bytes.

        Args:
            data: The base64-encoded bytes to decode.

        Returns:
            The decoded bytes.

        Raises:
            PydanticCustomError: If the base64 decoding fails.
        """
        ...

    @classmethod
    def encode(cls, value: bytes) -> bytes:
        """Encode bytes to base64-encoded bytes.

        Args:
            value: The bytes to encode.

        Returns:
            The base64-encoded bytes.
        """
        ...

    @classmethod
    def get_json_format(cls) -> Literal['base64']:
        """Get the JSON format for the encoded data.

        Returns:
            The literal string 'base64'.
        """
        ...

class Base64UrlEncoder(EncoderProtocol):
    """URL-safe Base64 encoder.

    This encoder uses URL-safe base64 encoding/decoding with alphabet A-Za-z0-9-_.
    """

    @classmethod
    def decode(cls, data: bytes) -> bytes:
        """Decode URL-safe base64-encoded bytes to original bytes.

        Args:
            data: The URL-safe base64-encoded bytes to decode.

        Returns:
            The decoded bytes.

        Raises:
            PydanticCustomError: If the base64 decoding fails.
        """
        ...

    @classmethod
    def encode(cls, value: bytes) -> bytes:
        """Encode bytes to URL-safe base64-encoded bytes.

        Args:
            value: The bytes to encode.

        Returns:
            The URL-safe base64-encoded bytes.
        """
        ...

    @classmethod
    def get_json_format(cls) -> Literal['base64url']:
        """Get the JSON format for the encoded data.

        Returns:
            The literal string 'base64url'.
        """
        ...

class EncodedBytes:
    """Bytes that are encoded/decoded using a specified encoder."""

    def __init__(self, *, encoder: type[EncoderProtocol]) -> None:
        """Initialize encoded bytes.

        Args:
            encoder: The encoder class to use.
        """
        ...

    @classmethod
    def __get_pydantic_core_schema__(
        cls, source: type[Any], handler: GetCoreSchemaHandler
    ) -> CoreSchema: ...

class EncodedStr:
    """A string that is encoded/decoded using a specified encoder."""

    def __init__(self, *, encoder: type[EncoderProtocol]) -> None:
        """Initialize encoded string.

        Args:
            encoder: The encoder class to use.
        """
        ...

    @classmethod
    def __get_pydantic_core_schema__(
        cls, source: type[Any], handler: GetCoreSchemaHandler
    ) -> CoreSchema: ...

Base64Bytes = Annotated[bytes, EncodedBytes(encoder=Base64Encoder)]
"""Bytes that are base64 encoded.

When used as a type annotation, the field will accept base64-encoded bytes and decode them
into raw bytes automatically.

Example:
    ```python
    from pydantic import BaseModel
    from pydantic.types import Base64Bytes

    class Model(BaseModel):
        data: Base64Bytes

    m = Model(data=b'SGVsbG8gV29ybGQ=')  # decoded to b'Hello World'
    ```
"""

Base64Str = Annotated[str, EncodedStr(encoder=Base64Encoder)]
"""A string that is base64 encoded.

When used as a type annotation, the field will accept base64-encoded strings and decode them
into regular strings automatically.

Example:
    ```python
    from pydantic import BaseModel
    from pydantic.types import Base64Str

    class Model(BaseModel):
        data: Base64Str

    m = Model(data='SGVsbG8gV29ybGQ=')  # decoded to 'Hello World'
    ```
"""

Base64UrlBytes = Annotated[bytes, EncodedBytes(encoder=Base64UrlEncoder)]
"""Bytes that are URL-safe base64 encoded.

When used as a type annotation, the field will accept URL-safe base64-encoded bytes and decode them
into raw bytes automatically.

Example:
    ```python
    from pydantic import BaseModel
    from pydantic.types import Base64UrlBytes

    class Model(BaseModel):
        data: Base64UrlBytes
    ```
"""

Base64UrlStr = Annotated[str, EncodedStr(encoder=Base64UrlEncoder)]
"""A string that is URL-safe base64 encoded.

When used as a type annotation, the field will accept URL-safe base64-encoded strings and decode them
into regular strings automatically.

Example:
    ```python
    from pydantic import BaseModel
    from pydantic.types import Base64UrlStr

    class Model(BaseModel):
        data: Base64UrlStr
    ```
"""

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~ DISCRIMINATOR TYPES ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

class Tag:
    """A tag for use with discriminated unions.

    This can be used to tag a type in a discriminated union.
    """

    def __init__(self, tag: str) -> None:
        """Initialize a tag.

        Args:
            tag: The tag string.
        """
        ...

    @classmethod
    def __get_pydantic_core_schema__(
        cls, source: type[Any], handler: GetCoreSchemaHandler
    ) -> CoreSchema: ...

class Discriminator:
    """Specify a discriminator for a union type.

    This allows you to specify how to discriminate between different types in a union.
    """

    def __init__(
        self,
        discriminator: str | Callable[[Any], str | None],
        *,
        custom_error_type: str | None = None,
        custom_error_message: str | None = None,
        custom_error_context: dict[str, Any] | None = None,
    ) -> None:
        """Initialize a discriminator.

        Args:
            discriminator: The discriminator field name or callable.
            custom_error_type: Custom error type for discrimination failures.
            custom_error_message: Custom error message for discrimination failures.
            custom_error_context: Custom error context for discrimination failures.
        """
        ...

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~ UTILITY TYPES ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

class GetPydanticSchema:
    """A class that allows custom schema generation.

    This can be used as metadata to provide a custom schema generation function.
    """

    def __init__(
        self,
        get_pydantic_core_schema: Callable[[Any, GetCoreSchemaHandler], CoreSchema],
        *,
        get_json_schema: Callable[[CoreSchema, GetJsonSchemaHandler], JsonSchemaValue] | None = None,
    ) -> None:
        """Initialize GetPydanticSchema.

        Args:
            get_pydantic_core_schema: Function to generate core schema.
            get_json_schema: Optional function to generate JSON schema.
        """
        ...

class OnErrorOmit:
    """When used as metadata, causes validation errors to be omitted from the output."""

    @classmethod
    def __class_getitem__(cls, item: type[T]) -> type[T]: ...

JsonValue = Any
"""Type alias for JSON-serializable values."""
