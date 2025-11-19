"""Type stubs for pydantic.networks module.

This module contains types and utilities for common network-related fields,
including URL types, email validation, and IP address types.
"""

from __future__ import annotations

import re
from dataclasses import dataclass as dataclass_decorator
from ipaddress import IPv4Address, IPv4Interface, IPv4Network, IPv6Address, IPv6Interface, IPv6Network
from typing import TYPE_CHECKING, Annotated, Any, ClassVar, Literal, overload

from pydantic_core import MultiHostHost, core_schema
from pydantic_core import MultiHostUrl as _CoreMultiHostUrl
from pydantic_core import Url as _CoreUrl
from typing_extensions import Self, TypeAlias

from .annotated_handlers import GetCoreSchemaHandler
from .errors import PydanticUserError
from .json_schema import JsonSchemaValue
from .type_adapter import TypeAdapter

if TYPE_CHECKING:
    NetworkType: TypeAlias = str | bytes | int | tuple[str | bytes | int, str | int]

__all__ = [
    'AnyUrl',
    'AnyHttpUrl',
    'FileUrl',
    'FtpUrl',
    'HttpUrl',
    'WebsocketUrl',
    'AnyWebsocketUrl',
    'UrlConstraints',
    'EmailStr',
    'NameEmail',
    'IPvAnyAddress',
    'IPvAnyInterface',
    'IPvAnyNetwork',
    'PostgresDsn',
    'CockroachDsn',
    'AmqpDsn',
    'RedisDsn',
    'MongoDsn',
    'KafkaDsn',
    'NatsDsn',
    'validate_email',
    'MySQLDsn',
    'MariaDBDsn',
    'ClickHouseDsn',
    'SnowflakeDsn',
]

@dataclass_decorator
class UrlConstraints:
    """URL constraints for validation.

    Attributes:
        max_length: The maximum length of the URL. Defaults to None.
        allowed_schemes: The allowed schemes. Defaults to None.
        host_required: Whether the host is required. Defaults to None.
        default_host: The default host. Defaults to None.
        default_port: The default port. Defaults to None.
        default_path: The default path. Defaults to None.
        preserve_empty_path: Whether to preserve empty URL paths. Defaults to None.
    """

    max_length: int | None = None
    allowed_schemes: list[str] | None = None
    host_required: bool | None = None
    default_host: str | None = None
    default_port: int | None = None
    default_path: str | None = None
    preserve_empty_path: bool | None = None

    def __hash__(self) -> int: ...
    @property
    def defined_constraints(self) -> dict[str, Any]: ...
    def __get_pydantic_core_schema__(
        self, source: Any, handler: GetCoreSchemaHandler
    ) -> core_schema.CoreSchema: ...

class _BaseUrl:
    """Base class for URL types."""

    _constraints: ClassVar[UrlConstraints]
    _url: _CoreUrl

    def __init__(self, url: str | _CoreUrl | _BaseUrl) -> None: ...
    @property
    def scheme(self) -> str:
        """The scheme part of the URL.

        e.g. 'https' in 'https://user:pass@host:port/path?query#fragment'
        """
        ...
    @property
    def username(self) -> str | None:
        """The username part of the URL, or None.

        e.g. 'user' in 'https://user:pass@host:port/path?query#fragment'
        """
        ...
    @property
    def password(self) -> str | None:
        """The password part of the URL, or None.

        e.g. 'pass' in 'https://user:pass@host:port/path?query#fragment'
        """
        ...
    @property
    def host(self) -> str | None:
        """The host part of the URL, or None.

        If the URL must be punycode encoded, this is the encoded host.
        e.g. if the input URL is 'https://£££.com', host will be 'xn--9aaa.com'
        """
        ...
    def unicode_host(self) -> str | None:
        """The host part of the URL as a unicode string, or None.

        e.g. 'host' in 'https://user:pass@host:port/path?query#fragment'

        If the URL must be punycode encoded, this is the decoded host.
        e.g. if the input URL is 'https://£££.com', unicode_host() will be '£££.com'
        """
        ...
    @property
    def port(self) -> int | None:
        """The port part of the URL, or None.

        e.g. 'port' in 'https://user:pass@host:port/path?query#fragment'
        """
        ...
    @property
    def path(self) -> str | None:
        """The path part of the URL, or None.

        e.g. '/path' in 'https://user:pass@host:port/path?query#fragment'
        """
        ...
    @property
    def query(self) -> str | None:
        """The query part of the URL, or None.

        e.g. 'query' in 'https://user:pass@host:port/path?query#fragment'
        """
        ...
    def query_params(self) -> list[tuple[str, str]]:
        """The query part of the URL as a list of key-value pairs.

        e.g. [('foo', 'bar')] in 'https://user:pass@host:port/path?foo=bar#fragment'
        """
        ...
    @property
    def fragment(self) -> str | None:
        """The fragment part of the URL, or None.

        e.g. 'fragment' in 'https://user:pass@host:port/path?query#fragment'
        """
        ...
    def unicode_string(self) -> str:
        """The URL as a unicode string, unlike __str__() this will not punycode encode the host.

        If the URL must be punycode encoded, this is the decoded string.
        e.g. if the input URL is 'https://£££.com', unicode_string() will be 'https://£££.com'
        """
        ...
    def encoded_string(self) -> str:
        """The URL's encoded string representation via __str__().

        This returns the punycode-encoded host version of the URL as a string.
        """
        ...
    def __str__(self) -> str:
        """The URL as a string, this will punycode encode the host if required."""
        ...
    def __repr__(self) -> str: ...
    def __deepcopy__(self, memo: dict) -> Self: ...
    def __eq__(self, other: Any) -> bool: ...
    def __lt__(self, other: Any) -> bool: ...
    def __gt__(self, other: Any) -> bool: ...
    def __le__(self, other: Any) -> bool: ...
    def __ge__(self, other: Any) -> bool: ...
    def __hash__(self) -> int: ...
    def __len__(self) -> int: ...
    @classmethod
    def build(
        cls,
        *,
        scheme: str,
        username: str | None = None,
        password: str | None = None,
        host: str,
        port: int | None = None,
        path: str | None = None,
        query: str | None = None,
        fragment: str | None = None,
    ) -> Self:
        """Build a new URL instance from its component parts.

        Args:
            scheme: The scheme part of the URL.
            username: The username part of the URL, or omit for no username.
            password: The password part of the URL, or omit for no password.
            host: The host part of the URL.
            port: The port part of the URL, or omit for no port.
            path: The path part of the URL, or omit for no path.
            query: The query part of the URL, or omit for no query.
            fragment: The fragment part of the URL, or omit for no fragment.

        Returns:
            An instance of the URL class.
        """
        ...
    @classmethod
    def serialize_url(cls, url: Any, info: core_schema.SerializationInfo) -> str | Self: ...
    @classmethod
    def __get_pydantic_core_schema__(
        cls, source: type[_BaseUrl], handler: GetCoreSchemaHandler
    ) -> core_schema.CoreSchema: ...
    @classmethod
    def __get_pydantic_json_schema__(
        cls, core_schema: core_schema.CoreSchema, handler: Any
    ) -> JsonSchemaValue: ...

class _BaseMultiHostUrl:
    """Base class for multi-host URL types."""

    _constraints: ClassVar[UrlConstraints]
    _url: _CoreMultiHostUrl

    def __init__(self, url: str | _CoreMultiHostUrl | _BaseMultiHostUrl) -> None: ...
    @property
    def scheme(self) -> str:
        """The scheme part of the URL.

        e.g. 'https' in 'https://foo.com,bar.com/path?query#fragment'
        """
        ...
    @property
    def path(self) -> str | None:
        """The path part of the URL, or None.

        e.g. '/path' in 'https://foo.com,bar.com/path?query#fragment'
        """
        ...
    @property
    def query(self) -> str | None:
        """The query part of the URL, or None.

        e.g. 'query' in 'https://foo.com,bar.com/path?query#fragment'
        """
        ...
    def query_params(self) -> list[tuple[str, str]]:
        """The query part of the URL as a list of key-value pairs.

        e.g. [('foo', 'bar')] in 'https://foo.com,bar.com/path?foo=bar#fragment'
        """
        ...
    @property
    def fragment(self) -> str | None:
        """The fragment part of the URL, or None.

        e.g. 'fragment' in 'https://foo.com,bar.com/path?query#fragment'
        """
        ...
    def hosts(self) -> list[MultiHostHost]:
        """The hosts of the MultiHostUrl as MultiHostHost typed dicts.

        Returns:
            A list of dicts, each representing a host.
        """
        ...
    def encoded_string(self) -> str:
        """The URL's encoded string representation via __str__().

        This returns the punycode-encoded host version of the URL as a string.
        """
        ...
    def unicode_string(self) -> str:
        """The URL as a unicode string, unlike __str__() this will not punycode encode the hosts."""
        ...
    def __str__(self) -> str:
        """The URL as a string, this will punycode encode the host if required."""
        ...
    def __repr__(self) -> str: ...
    def __deepcopy__(self, memo: dict) -> Self: ...
    def __eq__(self, other: Any) -> bool: ...
    def __hash__(self) -> int: ...
    def __len__(self) -> int: ...
    @classmethod
    def build(
        cls,
        *,
        scheme: str,
        hosts: list[MultiHostHost] | None = None,
        username: str | None = None,
        password: str | None = None,
        host: str | None = None,
        port: int | None = None,
        path: str | None = None,
        query: str | None = None,
        fragment: str | None = None,
    ) -> Self:
        """Build a new MultiHostUrl instance from its component parts.

        This method takes either 'hosts' - a list of MultiHostHost typed dicts,
        or the individual components 'username', 'password', 'host' and 'port'.

        Args:
            scheme: The scheme part of the URL.
            hosts: Multiple hosts to build the URL from.
            username: The username part of the URL.
            password: The password part of the URL.
            host: The host part of the URL.
            port: The port part of the URL.
            path: The path part of the URL.
            query: The query part of the URL, or omit for no query.
            fragment: The fragment part of the URL, or omit for no fragment.

        Returns:
            An instance of MultiHostUrl.
        """
        ...
    @classmethod
    def serialize_url(cls, url: Any, info: core_schema.SerializationInfo) -> str | Self: ...
    @classmethod
    def __get_pydantic_core_schema__(
        cls, source: type[_BaseMultiHostUrl], handler: GetCoreSchemaHandler
    ) -> core_schema.CoreSchema: ...
    @classmethod
    def __get_pydantic_json_schema__(
        cls, core_schema: core_schema.CoreSchema, handler: Any
    ) -> JsonSchemaValue: ...

class AnyUrl(_BaseUrl):
    """Base type for all URLs.

    * Any scheme allowed
    * Top-level domain (TLD) not required
    * Host not required

    Assuming an input URL of 'http://samuel:pass@example.com:8000/the/path/?query=here#fragment=is;this=bit',
    the types export the following properties:

    - 'scheme': the URL scheme ('http'), always set.
    - 'host': the URL host ('example.com').
    - 'username': optional username if included ('samuel').
    - 'password': optional password if included ('pass').
    - 'port': optional port ('8000').
    - 'path': optional path ('/the/path/').
    - 'query': optional URL query (for example, 'GET' arguments or "search string", such as 'query=here').
    - 'fragment': optional fragment ('fragment=is;this=bit').
    """

    ...

class AnyHttpUrl(AnyUrl):
    """A type that will accept any http or https URL.

    * TLD not required
    * Host not required
    """

    _constraints: ClassVar[UrlConstraints]

class HttpUrl(AnyUrl):
    """A type that will accept any http or https URL.

    * TLD not required
    * Host not required
    * Max length 2083
    """

    _constraints: ClassVar[UrlConstraints]

class AnyWebsocketUrl(AnyUrl):
    """A type that will accept any ws or wss URL.

    * TLD not required
    * Host not required
    """

    _constraints: ClassVar[UrlConstraints]

class WebsocketUrl(AnyUrl):
    """A type that will accept any ws or wss URL.

    * TLD not required
    * Host not required
    * Max length 2083
    """

    _constraints: ClassVar[UrlConstraints]

class FileUrl(AnyUrl):
    """A type that will accept any file URL.

    * Host not required
    """

    _constraints: ClassVar[UrlConstraints]

class FtpUrl(AnyUrl):
    """A type that will accept ftp URL.

    * TLD not required
    * Host not required
    """

    _constraints: ClassVar[UrlConstraints]

class PostgresDsn(_BaseMultiHostUrl):
    """A type that will accept any Postgres DSN.

    * User info required
    * TLD not required
    * Host required
    * Supports multiple hosts
    """

    _constraints: ClassVar[UrlConstraints]
    @property
    def host(self) -> str:
        """The required URL host."""
        ...

class CockroachDsn(AnyUrl):
    """A type that will accept any Cockroach DSN.

    * User info required
    * TLD not required
    * Host required
    """

    _constraints: ClassVar[UrlConstraints]
    @property
    def host(self) -> str:
        """The required URL host."""
        ...

class AmqpDsn(AnyUrl):
    """A type that will accept any AMQP DSN.

    * User info required
    * TLD not required
    * Host not required
    """

    _constraints: ClassVar[UrlConstraints]

class RedisDsn(AnyUrl):
    """A type that will accept any Redis DSN.

    * User info required
    * TLD not required
    * Host required (e.g., 'rediss://:pass@localhost')
    """

    _constraints: ClassVar[UrlConstraints]
    @property
    def host(self) -> str:
        """The required URL host."""
        ...

class MongoDsn(_BaseMultiHostUrl):
    """A type that will accept any MongoDB DSN.

    * User info not required
    * Database name not required
    * Port not required
    * User info may be passed without user part (e.g., 'mongodb://mongodb0.example.com:27017').
    """

    _constraints: ClassVar[UrlConstraints]

class KafkaDsn(AnyUrl):
    """A type that will accept any Kafka DSN.

    * User info required
    * TLD not required
    * Host not required
    """

    _constraints: ClassVar[UrlConstraints]

class NatsDsn(_BaseMultiHostUrl):
    """A type that will accept any NATS DSN.

    NATS is a connective technology built for the ever increasingly hyper-connected world.
    It is a single technology that enables applications to securely communicate across
    any combination of cloud vendors, on-premise, edge, web and mobile, and devices.
    More: https://nats.io
    """

    _constraints: ClassVar[UrlConstraints]

class MySQLDsn(AnyUrl):
    """A type that will accept any MySQL DSN.

    * User info required
    * TLD not required
    * Host not required
    """

    _constraints: ClassVar[UrlConstraints]

class MariaDBDsn(AnyUrl):
    """A type that will accept any MariaDB DSN.

    * User info required
    * TLD not required
    * Host not required
    """

    _constraints: ClassVar[UrlConstraints]

class ClickHouseDsn(AnyUrl):
    """A type that will accept any ClickHouse DSN.

    * User info required
    * TLD not required
    * Host not required
    """

    _constraints: ClassVar[UrlConstraints]

class SnowflakeDsn(AnyUrl):
    """A type that will accept any Snowflake DSN.

    * User info required
    * TLD not required
    * Host required
    """

    _constraints: ClassVar[UrlConstraints]
    @property
    def host(self) -> str:
        """The required URL host."""
        ...

def import_email_validator() -> None:
    """Import email_validator and ensure it's version 2.x.

    Raises:
        ImportError: If email-validator is not installed or is not version 2.x.
    """
    ...

if TYPE_CHECKING:
    EmailStr = Annotated[str, ...]
else:

    class EmailStr:
        """Validate email addresses.

        Info:
            To use this type, you need to install the optional
            'email-validator' package:

            ```bash
            pip install email-validator
            ```

        Validate email addresses.

        ```python
        from pydantic import BaseModel, EmailStr

        class Model(BaseModel):
            email: EmailStr

        print(Model(email='contact@mail.com'))
        #> email='contact@mail.com'
        ```
        """

        @classmethod
        def __get_pydantic_core_schema__(
            cls,
            _source: type[Any],
            _handler: GetCoreSchemaHandler,
        ) -> core_schema.CoreSchema: ...
        @classmethod
        def __get_pydantic_json_schema__(
            cls, core_schema: core_schema.CoreSchema, handler: Any
        ) -> JsonSchemaValue: ...
        @classmethod
        def _validate(cls, input_value: str, /) -> str: ...

class NameEmail:
    """Validate a name and email address combination, as specified by RFC 5322.

    Info:
        To use this type, you need to install the optional
        'email-validator' package:

        ```bash
        pip install email-validator
        ```

    The NameEmail has two properties: 'name' and 'email'.
    In case the 'name' is not provided, it's inferred from the email address.

    ```python
    from pydantic import BaseModel, NameEmail

    class User(BaseModel):
        email: NameEmail

    user = User(email='Fred Bloggs <fred.bloggs@example.com>')
    print(user.email)
    #> Fred Bloggs <fred.bloggs@example.com>
    print(user.email.name)
    #> Fred Bloggs

    user = User(email='fred.bloggs@example.com')
    print(user.email)
    #> fred.bloggs <fred.bloggs@example.com>
    print(user.email.name)
    #> fred.bloggs
    ```
    """

    __slots__: tuple[str, str]
    name: str
    email: str

    def __init__(self, name: str, email: str) -> None: ...
    def __eq__(self, other: Any) -> bool: ...
    @classmethod
    def __get_pydantic_json_schema__(
        cls, core_schema: core_schema.CoreSchema, handler: Any
    ) -> JsonSchemaValue: ...
    @classmethod
    def __get_pydantic_core_schema__(
        cls,
        _source: type[Any],
        _handler: GetCoreSchemaHandler,
    ) -> core_schema.CoreSchema: ...
    @classmethod
    def _validate(cls, input_value: Self | str, /) -> Self: ...
    def __str__(self) -> str: ...

IPvAnyAddressType: TypeAlias = IPv4Address | IPv6Address
IPvAnyInterfaceType: TypeAlias = IPv4Interface | IPv6Interface
IPvAnyNetworkType: TypeAlias = IPv4Network | IPv6Network

if TYPE_CHECKING:
    IPvAnyAddress = IPvAnyAddressType
    IPvAnyInterface = IPvAnyInterfaceType
    IPvAnyNetwork = IPvAnyNetworkType
else:

    class IPvAnyAddress:
        """Validate an IPv4 or IPv6 address.

        ```python
        from pydantic import BaseModel
        from pydantic.networks import IPvAnyAddress

        class IpModel(BaseModel):
            ip: IPvAnyAddress

        print(IpModel(ip='127.0.0.1'))
        #> ip=IPv4Address('127.0.0.1')

        try:
            IpModel(ip='http://www.example.com')
        except ValueError as e:
            print(e.errors())
            '''
            [
                {
                    'type': 'ip_any_address',
                    'loc': ('ip',),
                    'msg': 'value is not a valid IPv4 or IPv6 address',
                    'input': 'http://www.example.com',
                }
            ]
            '''
        ```
        """

        __slots__: tuple[()]

        def __new__(cls, value: Any) -> IPvAnyAddressType: ...
        @classmethod
        def __get_pydantic_json_schema__(
            cls, core_schema: core_schema.CoreSchema, handler: Any
        ) -> JsonSchemaValue: ...
        @classmethod
        def __get_pydantic_core_schema__(
            cls,
            _source: type[Any],
            _handler: GetCoreSchemaHandler,
        ) -> core_schema.CoreSchema: ...
        @classmethod
        def _validate(cls, input_value: Any, /) -> IPvAnyAddressType: ...

    class IPvAnyInterface:
        """Validate an IPv4 or IPv6 interface."""

        __slots__: tuple[()]

        def __new__(cls, value: NetworkType) -> IPvAnyInterfaceType: ...
        @classmethod
        def __get_pydantic_json_schema__(
            cls, core_schema: core_schema.CoreSchema, handler: Any
        ) -> JsonSchemaValue: ...
        @classmethod
        def __get_pydantic_core_schema__(
            cls,
            _source: type[Any],
            _handler: GetCoreSchemaHandler,
        ) -> core_schema.CoreSchema: ...
        @classmethod
        def _validate(cls, input_value: NetworkType, /) -> IPvAnyInterfaceType: ...

    class IPvAnyNetwork:
        """Validate an IPv4 or IPv6 network."""

        __slots__: tuple[()]

        def __new__(cls, value: NetworkType) -> IPvAnyNetworkType: ...
        @classmethod
        def __get_pydantic_json_schema__(
            cls, core_schema: core_schema.CoreSchema, handler: Any
        ) -> JsonSchemaValue: ...
        @classmethod
        def __get_pydantic_core_schema__(
            cls,
            _source: type[Any],
            _handler: GetCoreSchemaHandler,
        ) -> core_schema.CoreSchema: ...
        @classmethod
        def _validate(cls, input_value: NetworkType, /) -> IPvAnyNetworkType: ...

MAX_EMAIL_LENGTH: int
"""Maximum length for an email.
A somewhat arbitrary but very generous number compared to what is allowed by most implementations.
"""

pretty_email_regex: re.Pattern[str]

def validate_email(value: str) -> tuple[str, str]:
    """Email address validation using email-validator.

    Args:
        value: The email address to validate.

    Returns:
        A tuple containing the local part of the email (or the name for "pretty" email addresses)
        and the normalized email.

    Raises:
        PydanticCustomError: If the email is invalid.

    Note:
        Note that:

        * Raw IP address (literal) domain parts are not allowed.
        * "John Doe <local_part@domain.com>" style "pretty" email addresses are processed.
        * Spaces are striped from the beginning and end of addresses, but no error is raised.
    """
    ...
