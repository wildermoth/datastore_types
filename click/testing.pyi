"""
Type stubs for click.testing module.

This module provides utilities for testing Click applications.
The CliRunner allows running commands in isolation for testing purposes.
"""

from typing import Any, Callable, Dict, IO, List, Optional, Sequence, Tuple, Union
from click.core import BaseCommand, Context
import sys

class Result:
    """
    Holds the result of a CLI invocation from CliRunner.
    """

    runner: CliRunner
    stdout_bytes: bytes
    stderr_bytes: Optional[bytes]
    exit_code: int
    exception: Optional[BaseException]
    exc_info: Optional[Tuple[type[BaseException], BaseException, Any]]

    @property
    def output(self) -> str:
        """The terminal output as a string."""
        ...

    @property
    def stdout(self) -> str:
        """The standard output as a string."""
        ...

    @property
    def stderr(self) -> str:
        """The standard error as a string."""
        ...

    def __init__(
        self,
        runner: CliRunner,
        stdout_bytes: bytes,
        stderr_bytes: Optional[bytes],
        exit_code: int,
        exception: Optional[BaseException],
        exc_info: Optional[Tuple[type[BaseException], BaseException, Any]] = ...,
    ) -> None: ...


class CliRunner:
    """
    A test runner for Click applications that allows running commands
    in isolation with captured output.

    Example:
        runner = CliRunner()
        result = runner.invoke(cli, ['--help'])
        assert result.exit_code == 0
    """

    charset: str
    env: Dict[str, str]
    echo_stdin: bool
    mix_stderr: bool

    def __init__(
        self,
        charset: str = ...,
        env: Optional[Dict[str, str]] = ...,
        echo_stdin: bool = ...,
        mix_stderr: bool = ...,
    ) -> None: ...

    def get_default_prog_name(self, cli: BaseCommand) -> str: ...

    def make_env(self, overrides: Optional[Dict[str, str]] = ...) -> Dict[str, str]: ...

    def isolation(
        self,
        input: Optional[Union[str, bytes, IO[Any]]] = ...,
        env: Optional[Dict[str, str]] = ...,
        color: bool = ...,
    ) -> Any: ...

    def invoke(
        self,
        cli: BaseCommand,
        args: Optional[Union[str, Sequence[str]]] = ...,
        input: Optional[Union[str, bytes, IO[Any]]] = ...,
        env: Optional[Dict[str, str]] = ...,
        catch_exceptions: bool = ...,
        color: bool = ...,
        **extra: Any,
    ) -> Result:
        """
        Invokes a command in isolated environment.

        Args:
            cli: The command to invoke
            args: Arguments to pass to the command
            input: Input data to provide to stdin
            env: Environment variables to set
            catch_exceptions: Whether to catch exceptions or let them propagate
            color: Whether to enable color output
            **extra: Additional keyword arguments passed to the command

        Returns:
            Result object containing output and exit code
        """
        ...

    def isolated_filesystem(
        self,
        temp_dir: Optional[Union[str, bytes]] = ...,
    ) -> Any:
        """
        Context manager that creates a temporary directory and changes
        the current working directory to it for isolated filesystem tests.
        """
        ...
