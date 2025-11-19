"""
Comprehensive type stubs for pydantic v2.

This module provides type hints for the pydantic library, a data validation
library for Python that uses Python type annotations.
"""

from typing import Any, Callable, Dict, Literal, Mapping, Set, TypeVar, Union, overload
from typing_extensions import Self, TypeAlias, dataclass_transform

import pydantic_core
from pydantic_core import ValidationError as ValidationError
from pydantic_core.core_schema import (
    FieldSerializationInfo as FieldSerializationInfo,
    SerializationInfo as SerializationInfo,
    SerializerFunctionWrapHandler as SerializerFunctionWrapHandler,
    ValidationInfo as ValidationInfo,
    ValidatorFunctionWrapHandler as ValidatorFunctionWrapHandler,
)

# Re-exports from submodules
from . import dataclasses as dataclasses
from .aliases import (
    AliasChoices as AliasChoices,
    AliasGenerator as AliasGenerator,
    AliasPath as AliasPath,
)
from .annotated_handlers import (
    GetCoreSchemaHandler as GetCoreSchemaHandler,
    GetJsonSchemaHandler as GetJsonSchemaHandler,
)
from .config import ConfigDict as ConfigDict, with_config as with_config
from .deprecated.class_validators import (
    root_validator as root_validator,
    validator as validator,
)
from .deprecated.config import BaseConfig as BaseConfig, Extra as Extra
from .deprecated.tools import (
    parse_obj_as as parse_obj_as,
    schema_json_of as schema_json_of,
    schema_of as schema_of,
)
from .errors import (
    PydanticErrorCodes as PydanticErrorCodes,
    PydanticForbiddenQualifier as PydanticForbiddenQualifier,
    PydanticImportError as PydanticImportError,
    PydanticInvalidForJsonSchema as PydanticInvalidForJsonSchema,
    PydanticSchemaGenerationError as PydanticSchemaGenerationError,
    PydanticUndefinedAnnotation as PydanticUndefinedAnnotation,
    PydanticUserError as PydanticUserError,
)
from .fields import (
    Field as Field,
    PrivateAttr as PrivateAttr,
    computed_field as computed_field,
)
from .functional_serializers import (
    PlainSerializer as PlainSerializer,
    SerializeAsAny as SerializeAsAny,
    WrapSerializer as WrapSerializer,
    field_serializer as field_serializer,
    model_serializer as model_serializer,
)
from .functional_validators import (
    AfterValidator as AfterValidator,
    BeforeValidator as BeforeValidator,
    InstanceOf as InstanceOf,
    ModelWrapValidatorHandler as ModelWrapValidatorHandler,
    PlainValidator as PlainValidator,
    SkipValidation as SkipValidation,
    ValidateAs as ValidateAs,
    WrapValidator as WrapValidator,
    field_validator as field_validator,
    model_validator as model_validator,
)
from .json_schema import WithJsonSchema as WithJsonSchema
from .main import BaseModel as BaseModel, create_model as create_model
from .networks import (
    AmqpDsn as AmqpDsn,
    AnyHttpUrl as AnyHttpUrl,
    AnyUrl as AnyUrl,
    AnyWebsocketUrl as AnyWebsocketUrl,
    ClickHouseDsn as ClickHouseDsn,
    CockroachDsn as CockroachDsn,
    EmailStr as EmailStr,
    FileUrl as FileUrl,
    FtpUrl as FtpUrl,
    HttpUrl as HttpUrl,
    IPvAnyAddress as IPvAnyAddress,
    IPvAnyInterface as IPvAnyInterface,
    IPvAnyNetwork as IPvAnyNetwork,
    KafkaDsn as KafkaDsn,
    MariaDBDsn as MariaDBDsn,
    MongoDsn as MongoDsn,
    MySQLDsn as MySQLDsn,
    NameEmail as NameEmail,
    NatsDsn as NatsDsn,
    PostgresDsn as PostgresDsn,
    RedisDsn as RedisDsn,
    SnowflakeDsn as SnowflakeDsn,
    UrlConstraints as UrlConstraints,
    WebsocketUrl as WebsocketUrl,
    validate_email as validate_email,
)
from .root_model import RootModel as RootModel
from .type_adapter import TypeAdapter as TypeAdapter
from .types import (
    AllowInfNan as AllowInfNan,
    AwareDatetime as AwareDatetime,
    Base64Bytes as Base64Bytes,
    Base64Encoder as Base64Encoder,
    Base64Str as Base64Str,
    Base64UrlBytes as Base64UrlBytes,
    Base64UrlStr as Base64UrlStr,
    ByteSize as ByteSize,
    Discriminator as Discriminator,
    DirectoryPath as DirectoryPath,
    EncodedBytes as EncodedBytes,
    EncodedStr as EncodedStr,
    EncoderProtocol as EncoderProtocol,
    FailFast as FailFast,
    FilePath as FilePath,
    FiniteFloat as FiniteFloat,
    FutureDate as FutureDate,
    FutureDatetime as FutureDatetime,
    GetPydanticSchema as GetPydanticSchema,
    ImportString as ImportString,
    Json as Json,
    JsonValue as JsonValue,
    NaiveDatetime as NaiveDatetime,
    NegativeFloat as NegativeFloat,
    NegativeInt as NegativeInt,
    NewPath as NewPath,
    NonNegativeFloat as NonNegativeFloat,
    NonNegativeInt as NonNegativeInt,
    NonPositiveFloat as NonPositiveFloat,
    NonPositiveInt as NonPositiveInt,
    OnErrorOmit as OnErrorOmit,
    PastDate as PastDate,
    PastDatetime as PastDatetime,
    PaymentCardNumber as PaymentCardNumber,
    PositiveFloat as PositiveFloat,
    PositiveInt as PositiveInt,
    Secret as Secret,
    SecretBytes as SecretBytes,
    SecretStr as SecretStr,
    SocketPath as SocketPath,
    Strict as Strict,
    StrictBool as StrictBool,
    StrictBytes as StrictBytes,
    StrictFloat as StrictFloat,
    StrictInt as StrictInt,
    StrictStr as StrictStr,
    StringConstraints as StringConstraints,
    Tag as Tag,
    UUID1 as UUID1,
    UUID3 as UUID3,
    UUID4 as UUID4,
    UUID5 as UUID5,
    UUID6 as UUID6,
    UUID7 as UUID7,
    UUID8 as UUID8,
    conbytes as conbytes,
    condate as condate,
    condecimal as condecimal,
    confloat as confloat,
    confrozenset as confrozenset,
    conint as conint,
    conlist as conlist,
    conset as conset,
    constr as constr,
)
from .validate_call_decorator import validate_call as validate_call
from .version import VERSION as VERSION
from .warnings import (
    PydanticDeprecatedSince20 as PydanticDeprecatedSince20,
    PydanticDeprecatedSince26 as PydanticDeprecatedSince26,
    PydanticDeprecatedSince29 as PydanticDeprecatedSince29,
    PydanticDeprecatedSince210 as PydanticDeprecatedSince210,
    PydanticDeprecatedSince211 as PydanticDeprecatedSince211,
    PydanticDeprecatedSince212 as PydanticDeprecatedSince212,
    PydanticDeprecationWarning as PydanticDeprecationWarning,
    PydanticExperimentalWarning as PydanticExperimentalWarning,
)

__version__: str

__all__ = (
    # dataclasses
    "dataclasses",
    # functional validators
    "field_validator",
    "model_validator",
    "AfterValidator",
    "BeforeValidator",
    "PlainValidator",
    "WrapValidator",
    "SkipValidation",
    "ValidateAs",
    "InstanceOf",
    "ModelWrapValidatorHandler",
    # JSON Schema
    "WithJsonSchema",
    # deprecated V1 functional validators
    "root_validator",
    "validator",
    # functional serializers
    "field_serializer",
    "model_serializer",
    "PlainSerializer",
    "SerializeAsAny",
    "WrapSerializer",
    # config
    "ConfigDict",
    "with_config",
    # deprecated V1 config
    "BaseConfig",
    "Extra",
    # validate_call
    "validate_call",
    # errors
    "PydanticErrorCodes",
    "PydanticUserError",
    "PydanticSchemaGenerationError",
    "PydanticImportError",
    "PydanticUndefinedAnnotation",
    "PydanticInvalidForJsonSchema",
    "PydanticForbiddenQualifier",
    # fields
    "Field",
    "computed_field",
    "PrivateAttr",
    # alias
    "AliasChoices",
    "AliasGenerator",
    "AliasPath",
    # main
    "BaseModel",
    "create_model",
    # network
    "AnyUrl",
    "AnyHttpUrl",
    "FileUrl",
    "HttpUrl",
    "FtpUrl",
    "WebsocketUrl",
    "AnyWebsocketUrl",
    "UrlConstraints",
    "EmailStr",
    "NameEmail",
    "IPvAnyAddress",
    "IPvAnyInterface",
    "IPvAnyNetwork",
    "PostgresDsn",
    "CockroachDsn",
    "AmqpDsn",
    "RedisDsn",
    "MongoDsn",
    "KafkaDsn",
    "NatsDsn",
    "MySQLDsn",
    "MariaDBDsn",
    "ClickHouseDsn",
    "SnowflakeDsn",
    "validate_email",
    # root_model
    "RootModel",
    # deprecated tools
    "parse_obj_as",
    "schema_of",
    "schema_json_of",
    # types
    "Strict",
    "StrictStr",
    "conbytes",
    "conlist",
    "conset",
    "confrozenset",
    "constr",
    "StringConstraints",
    "ImportString",
    "conint",
    "PositiveInt",
    "NegativeInt",
    "NonNegativeInt",
    "NonPositiveInt",
    "confloat",
    "PositiveFloat",
    "NegativeFloat",
    "NonNegativeFloat",
    "NonPositiveFloat",
    "FiniteFloat",
    "condecimal",
    "condate",
    "UUID1",
    "UUID3",
    "UUID4",
    "UUID5",
    "UUID6",
    "UUID7",
    "UUID8",
    "FilePath",
    "DirectoryPath",
    "NewPath",
    "Json",
    "Secret",
    "SecretStr",
    "SecretBytes",
    "SocketPath",
    "StrictBool",
    "StrictBytes",
    "StrictInt",
    "StrictFloat",
    "PaymentCardNumber",
    "ByteSize",
    "PastDate",
    "FutureDate",
    "PastDatetime",
    "FutureDatetime",
    "AwareDatetime",
    "NaiveDatetime",
    "AllowInfNan",
    "EncoderProtocol",
    "EncodedBytes",
    "EncodedStr",
    "Base64Encoder",
    "Base64Bytes",
    "Base64Str",
    "Base64UrlBytes",
    "Base64UrlStr",
    "GetPydanticSchema",
    "Tag",
    "Discriminator",
    "JsonValue",
    "FailFast",
    # type_adapter
    "TypeAdapter",
    # version
    "__version__",
    "VERSION",
    # warnings
    "PydanticDeprecatedSince20",
    "PydanticDeprecatedSince26",
    "PydanticDeprecatedSince29",
    "PydanticDeprecatedSince210",
    "PydanticDeprecatedSince211",
    "PydanticDeprecatedSince212",
    "PydanticDeprecationWarning",
    "PydanticExperimentalWarning",
    # annotated handlers
    "GetCoreSchemaHandler",
    "GetJsonSchemaHandler",
    # pydantic_core
    "ValidationError",
    "ValidationInfo",
    "SerializationInfo",
    "ValidatorFunctionWrapHandler",
    "FieldSerializationInfo",
    "SerializerFunctionWrapHandler",
    "OnErrorOmit",
)
