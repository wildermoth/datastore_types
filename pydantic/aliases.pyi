"""Support for alias configurations stubs."""

from __future__ import annotations

import dataclasses
from typing import Any, Callable, Literal

from pydantic_core import PydanticUndefined

from pydantic._internal import _internal_dataclass

class AliasPath:
    """!!! abstract "Usage Documentation"
        [`AliasPath` and `AliasChoices`](../concepts/alias.md#aliaspath-and-aliaschoices)

    A data class used by `validation_alias` as a convenience to create aliases.

    Attributes:
        path: A list of string or integer aliases.
    """

    path: list[int | str]

    def __init__(self, first_arg: str, *args: str | int) -> None:
        """Initialize an AliasPath with a first argument and optional additional arguments.

        Args:
            first_arg: The first argument in the path.
            *args: Additional string or integer arguments for the path.
        """
        ...

    def convert_to_aliases(self) -> list[str | int]:
        """Converts arguments to a list of string or integer aliases.

        Returns:
            The list of aliases.
        """
        ...

    def search_dict_for_path(self, d: dict) -> Any:
        """Searches a dictionary for the path specified by the alias.

        Args:
            d: The dictionary to search in.

        Returns:
            The value at the specified path, or `PydanticUndefined` if the path is not found.
        """
        ...

class AliasChoices:
    """!!! abstract "Usage Documentation"
        [`AliasPath` and `AliasChoices`](../concepts/alias.md#aliaspath-and-aliaschoices)

    A data class used by `validation_alias` as a convenience to create aliases.

    Attributes:
        choices: A list containing a string or `AliasPath`.
    """

    choices: list[str | AliasPath]

    def __init__(self, first_choice: str | AliasPath, *choices: str | AliasPath) -> None:
        """Initialize AliasChoices with a first choice and optional additional choices.

        Args:
            first_choice: The first choice, either a string or AliasPath.
            *choices: Additional choices, each either a string or AliasPath.
        """
        ...

    def convert_to_aliases(self) -> list[list[str | int]]:
        """Converts arguments to a list of lists containing string or integer aliases.

        Returns:
            The list of aliases.
        """
        ...

class AliasGenerator:
    """!!! abstract "Usage Documentation"
        [Using an `AliasGenerator`](../concepts/alias.md#using-an-aliasgenerator)

    A data class used by `alias_generator` as a convenience to create various aliases.

    Attributes:
        alias: A callable that takes a field name and returns an alias for it.
        validation_alias: A callable that takes a field name and returns a validation alias for it.
        serialization_alias: A callable that takes a field name and returns a serialization alias for it.
    """

    alias: Callable[[str], str] | None
    validation_alias: Callable[[str], str | AliasPath | AliasChoices] | None
    serialization_alias: Callable[[str], str] | None

    def __init__(
        self,
        alias: Callable[[str], str] | None = None,
        validation_alias: Callable[[str], str | AliasPath | AliasChoices] | None = None,
        serialization_alias: Callable[[str], str] | None = None,
    ) -> None:
        """Initialize an AliasGenerator with optional alias generators.

        Args:
            alias: A callable for generating aliases.
            validation_alias: A callable for generating validation aliases.
            serialization_alias: A callable for generating serialization aliases.
        """
        ...

    def _generate_alias(
        self,
        alias_kind: Literal['alias', 'validation_alias', 'serialization_alias'],
        allowed_types: tuple[type[str] | type[AliasPath] | type[AliasChoices], ...],
        field_name: str,
    ) -> str | AliasPath | AliasChoices | None:
        """Generate an alias of the specified kind. Returns None if the alias generator is None.

        Args:
            alias_kind: The kind of alias to generate.
            allowed_types: Tuple of allowed types for the alias.
            field_name: The field name to generate an alias for.

        Returns:
            The generated alias or None.

        Raises:
            TypeError: If the alias generator produces an invalid type.
        """
        ...

    def generate_aliases(self, field_name: str) -> tuple[str | None, str | AliasPath | AliasChoices | None, str | None]:
        """Generate `alias`, `validation_alias`, and `serialization_alias` for a field.

        Args:
            field_name: The field name to generate aliases for.

        Returns:
            A tuple of three aliases - alias, validation_alias, and serialization_alias.
        """
        ...
