"""
Type stubs for the Click library.

Click is a Python package for creating beautiful command-line interfaces
with as little code as necessary. It's highly configurable and comes with
sensible defaults out of the box.

This stub file provides type annotations for all public APIs in Click.
"""

from typing import Any, Callable, Dict, IO, Iterable, List, Optional, Sequence, Tuple, TypeVar, Union, overload, Type
import sys

# Version info
__version__: str

# Re-export core classes
from click.core import (
    Context as Context,
    BaseCommand as BaseCommand,
    Command as Command,
    MultiCommand as MultiCommand,
    Group as Group,
    CommandCollection as CommandCollection,
    Parameter as Parameter,
    Option as Option,
    Argument as Argument,
    ParameterSource as ParameterSource,
)

# Re-export decorators
from click.decorators import (
    command as command,
    group as group,
    argument as argument,
    option as option,
    password_option as password_option,
    confirmation_option as confirmation_option,
    version_option as version_option,
    help_option as help_option,
    pass_context as pass_context,
    pass_obj as pass_obj,
    make_pass_decorator as make_pass_decorator,
    pass_meta_key as pass_meta_key,
)

# Re-export types
from click.types import (
    ParamType as ParamType,
    CompositeParamType as CompositeParamType,
    FuncParamType as FuncParamType,
    UnprocessedParamType as UnprocessedParamType,
    StringParamType as StringParamType,
    Choice as Choice,
    DateTime as DateTime,
    IntParamType as IntParamType,
    IntRange as IntRange,
    FloatParamType as FloatParamType,
    FloatRange as FloatRange,
    BoolParamType as BoolParamType,
    UUIDParameterType as UUIDParameterType,
    File as File,
    Path as Path,
    Tuple as Tuple,
    STRING as STRING,
    INT as INT,
    FLOAT as FLOAT,
    BOOL as BOOL,
    UUID as UUID,
    UNPROCESSED as UNPROCESSED,
)

# Re-export exceptions
from click.exceptions import (
    ClickException as ClickException,
    UsageError as UsageError,
    BadParameter as BadParameter,
    MissingParameter as MissingParameter,
    NoSuchOption as NoSuchOption,
    BadOptionUsage as BadOptionUsage,
    BadArgumentUsage as BadArgumentUsage,
    FileError as FileError,
    Abort as Abort,
    Exit as Exit,
)

# Re-export testing utilities
from click.testing import (
    CliRunner as CliRunner,
    Result as Result,
)

# Re-export formatting
from click.formatting import (
    HelpFormatter as HelpFormatter,
    wrap_text as wrap_text,
)

# Re-export termui functions
from click.termui import (
    echo as echo,
    echo_via_pager as echo_via_pager,
    prompt as prompt,
    confirm as confirm,
    get_terminal_size as get_terminal_size,
    progressbar as progressbar,
    clear as clear,
    style as style,
    unstyle as unstyle,
    secho as secho,
    edit as edit,
    launch as launch,
    getchar as getchar,
    raw_terminal as raw_terminal,
    pause as pause,
)

# Re-export utilities
from click.utils import (
    get_app_dir as get_app_dir,
    get_os_args as get_os_args,
    format_filename as format_filename,
    LazyFile as LazyFile,
    KeepOpenFile as KeepOpenFile,
)

# Re-export parser
from click.parser import (
    OptionParser as OptionParser,
    split_arg_string as split_arg_string,
)

# Re-export shell completion
from click.shell_completion import (
    CompletionItem as CompletionItem,
    ShellComplete as ShellComplete,
    BashComplete as BashComplete,
    ZshComplete as ZshComplete,
    FishComplete as FishComplete,
)

# Additional utility functions

def get_current_context(silent: bool = ...) -> Optional[Context]:
    """
    Get the current execution context.

    Args:
        silent: If True, return None if no context is available
                If False, raise RuntimeError if no context is available
    """
    ...


def get_text_stderr() -> IO[str]:
    """Get the text stream for stderr."""
    ...


def get_text_stdout() -> IO[str]:
    """Get the text stream for stdout."""
    ...


def get_binary_stderr() -> IO[bytes]:
    """Get the binary stream for stderr."""
    ...


def get_binary_stdout() -> IO[bytes]:
    """Get the binary stream for stdout."""
    ...


def open_file(
    filename: str,
    mode: str = ...,
    encoding: Optional[str] = ...,
    errors: str = ...,
    lazy: bool = ...,
    atomic: bool = ...,
) -> IO[Any]:
    """
    Open a file, intelligently handling special filenames like '-' for stdin/stdout.
    """
    ...


def format_filename(
    filename: Union[str, bytes],
    shorten: bool = ...,
) -> str:
    """
    Format a filename for display."""
    ...


# Type aliases for common patterns
_AnyCallable = Callable[..., Any]
_Decorator = Callable[[_AnyCallable], _AnyCallable]
