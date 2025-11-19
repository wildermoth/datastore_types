"""The `version` module holds the version information for Pydantic stubs."""

from __future__ import annotations as _annotations

import sys

from pydantic_core import __version__ as __pydantic_core_version__

VERSION: str
"""The version of Pydantic.

This version specifier is guaranteed to be compliant with the [specification],
introduced by [PEP 440].

[specification]: https://packaging.python.org/en/latest/specifications/version-specifiers/
[PEP 440]: https://peps.python.org/pep-0440/
"""

def version_short() -> str:
    """Return the `major.minor` part of Pydantic version.

    It returns '2.1' if Pydantic version is '2.1.1'.

    Returns:
        The short version string in 'major.minor' format.
    """
    ...

def version_info() -> str:
    """Return complete version information for Pydantic and its dependencies.

    Returns:
        A string containing detailed version information about Pydantic, pydantic-core,
        Python, platform, related packages, and git commit information.
    """
    ...

def check_pydantic_core_version() -> bool:
    """Check that the installed `pydantic-core` dependency is compatible.

    Returns:
        True if the pydantic-core version is compatible with the current pydantic version,
        False otherwise.
    """
    ...

def parse_mypy_version(version: str) -> tuple[int, int, int]:
    """Parse `mypy` string version to a 3-tuple of ints.

    It parses normal version like `1.11.0` and extra info followed by a `+` sign
    like `1.11.0+dev.d6d9d8cd4f27c52edac1f537e236ec48a01e54cb.dirty`.

    Args:
        version: The mypy version string.

    Returns:
        A triple of ints, e.g. `(1, 11, 0)`.
    """
    ...
