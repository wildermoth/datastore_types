"""
Type stubs for click.core module.

This module contains the core classes for Click's command-line interface framework.
"""

from typing import Any, Callable, Dict, List, Optional, Sequence, Set, Tuple, TypeVar, Union, overload, Mapping, Iterable, IO, Protocol
from types import TracebackType
from click.types import ParamType
from click.formatting import HelpFormatter
from click.parser import OptionParser

_T = TypeVar("_T")
_F = TypeVar("_F", bound=Callable[..., Any])

class Context:
    """
    The context object holds state for the current execution of the CLI.
    It maintains information about the command being executed, parameters,
    and provides access to the parent context.
    """

    parent: Optional[Context]
    command: Command
    info_name: Optional[str]
    params: Dict[str, Any]
    args: List[str]
    protected_args: List[str]
    obj: Any
    default_map: Optional[Dict[str, Any]]
    invoked_subcommand: Optional[str]
    terminal_width: Optional[int]
    max_content_width: Optional[int]
    allow_extra_args: bool
    allow_interspersed_args: bool
    ignore_unknown_options: bool
    help_option_names: List[str]
    token_normalize_func: Optional[Callable[[str], str]]
    resilient_parsing: bool
    auto_envvar_prefix: Optional[str]
    color: Optional[bool]
    _meta: Dict[str, Any]
    _close_callbacks: List[Callable[[], Any]]
    _depth: int

    def __init__(
        self,
        command: Command,
        parent: Optional[Context] = ...,
        info_name: Optional[str] = ...,
        obj: Optional[Any] = ...,
        auto_envvar_prefix: Optional[str] = ...,
        default_map: Optional[Dict[str, Any]] = ...,
        terminal_width: Optional[int] = ...,
        max_content_width: Optional[int] = ...,
        resilient_parsing: bool = ...,
        allow_extra_args: Optional[bool] = ...,
        allow_interspersed_args: Optional[bool] = ...,
        ignore_unknown_options: Optional[bool] = ...,
        help_option_names: Optional[List[str]] = ...,
        token_normalize_func: Optional[Callable[[str], str]] = ...,
        color: Optional[bool] = ...,
        show_default: Optional[bool] = ...,
    ) -> None: ...

    def __enter__(self) -> Context: ...
    def __exit__(
        self,
        exc_type: Optional[type[BaseException]],
        exc_value: Optional[BaseException],
        tb: Optional[TracebackType],
    ) -> None: ...

    @property
    def meta(self) -> Dict[str, Any]: ...

    def scope(self, cleanup: bool = ...) -> Context: ...
    def make_formatter(self) -> HelpFormatter: ...
    def call_on_close(self, f: _F) -> _F: ...
    def close(self) -> None: ...
    def find_root(self) -> Context: ...
    def find_object(self, object_type: type[_T]) -> Optional[_T]: ...
    def ensure_object(self, object_type: type[_T]) -> _T: ...
    def lookup_default(self, name: str, call: bool = ...) -> Any: ...
    def fail(self, message: str) -> None: ...
    def abort(self) -> None: ...
    def exit(self, code: int = ...) -> None: ...
    def get_usage(self) -> str: ...
    def get_help(self) -> str: ...
    def invoke(
        self,
        callback: Union[Command, Callable[..., Any]],
        *args: Any,
        **kwargs: Any,
    ) -> Any: ...
    def forward(
        self,
        callback: Union[Command, Callable[..., Any]],
        *args: Any,
        **kwargs: Any,
    ) -> Any: ...
    def set_parameter_source(self, name: str, source: ParameterSource) -> None: ...
    def get_parameter_source(self, name: str) -> Optional[ParameterSource]: ...


class ParameterSource:
    """Enum-like class representing the source of a parameter value."""
    COMMANDLINE: ParameterSource
    ENVIRONMENT: ParameterSource
    DEFAULT: ParameterSource
    DEFAULT_MAP: ParameterSource


class BaseCommand:
    """Base class for all command objects."""

    name: Optional[str]
    context_settings: Dict[str, Any]

    def __init__(self, name: Optional[str] = ..., context_settings: Optional[Dict[str, Any]] = ...) -> None: ...

    def get_usage(self, ctx: Context) -> str: ...
    def get_help(self, ctx: Context) -> str: ...
    def make_context(
        self,
        info_name: Optional[str],
        args: List[str],
        parent: Optional[Context] = ...,
        **extra: Any,
    ) -> Context: ...
    def parse_args(self, ctx: Context, args: List[str]) -> List[str]: ...
    def invoke(self, ctx: Context) -> Any: ...
    def main(
        self,
        args: Optional[Sequence[str]] = ...,
        prog_name: Optional[str] = ...,
        complete_var: Optional[str] = ...,
        standalone_mode: bool = ...,
        windows_expand_args: bool = ...,
        **extra: Any,
    ) -> Any: ...
    def __call__(self, *args: Any, **kwargs: Any) -> Any: ...


class Command(BaseCommand):
    """
    Commands are the basic building blocks of command line interfaces in Click.
    A command encapsulates a function and its parameters.
    """

    callback: Optional[Callable[..., Any]]
    params: List[Parameter]
    help: Optional[str]
    epilog: Optional[str]
    short_help: Optional[str]
    options_metavar: str
    add_help_option: bool
    no_args_is_help: bool
    hidden: bool
    deprecated: bool

    def __init__(
        self,
        name: Optional[str] = ...,
        callback: Optional[Callable[..., Any]] = ...,
        params: Optional[List[Parameter]] = ...,
        help: Optional[str] = ...,
        epilog: Optional[str] = ...,
        short_help: Optional[str] = ...,
        options_metavar: str = ...,
        add_help_option: bool = ...,
        no_args_is_help: bool = ...,
        hidden: bool = ...,
        deprecated: bool = ...,
        context_settings: Optional[Dict[str, Any]] = ...,
    ) -> None: ...

    def get_params(self, ctx: Context) -> List[Parameter]: ...
    def format_help(self, ctx: Context, formatter: HelpFormatter) -> None: ...
    def format_help_text(self, ctx: Context, formatter: HelpFormatter) -> None: ...
    def format_options(self, ctx: Context, formatter: HelpFormatter) -> None: ...
    def format_epilog(self, ctx: Context, formatter: HelpFormatter) -> None: ...
    def format_usage(self, ctx: Context, formatter: HelpFormatter) -> None: ...
    def get_short_help_str(self, limit: int = ...) -> str: ...


class MultiCommand(Command):
    """
    A multi command is the basic implementation of a command that
    dispatches to subcommands.
    """

    no_args_is_help: bool
    invoke_without_command: bool
    subcommand_metavar: Optional[str]
    chain: bool
    result_callback: Optional[Callable[..., Any]]

    def __init__(
        self,
        name: Optional[str] = ...,
        invoke_without_command: bool = ...,
        no_args_is_help: Optional[bool] = ...,
        subcommand_metavar: Optional[str] = ...,
        chain: bool = ...,
        result_callback: Optional[Callable[..., Any]] = ...,
        **attrs: Any,
    ) -> None: ...

    def result_processor(self, f: _F) -> _F: ...
    def format_commands(self, ctx: Context, formatter: HelpFormatter) -> None: ...
    def resolve_command(self, ctx: Context, args: List[str]) -> Tuple[Optional[str], Optional[Command], List[str]]: ...
    def get_command(self, ctx: Context, cmd_name: str) -> Optional[Command]: ...
    def list_commands(self, ctx: Context) -> List[str]: ...


class Group(MultiCommand):
    """
    A group allows to attach commands to it. The most important
    use case is for organizing commands into logical groups.
    """

    commands: Dict[str, Command]

    def __init__(
        self,
        name: Optional[str] = ...,
        commands: Optional[Dict[str, Command]] = ...,
        **attrs: Any,
    ) -> None: ...

    def add_command(self, cmd: Command, name: Optional[str] = ...) -> None: ...
    def command(self, *args: Any, **kwargs: Any) -> Callable[[Callable[..., Any]], Command]: ...
    def group(self, *args: Any, **kwargs: Any) -> Callable[[Callable[..., Any]], Group]: ...


class CommandCollection(MultiCommand):
    """
    A command collection allows combining multiple multi commands into one.
    """

    sources: List[MultiCommand]

    def __init__(
        self,
        name: Optional[str] = ...,
        sources: Optional[List[MultiCommand]] = ...,
        **attrs: Any,
    ) -> None: ...


class Parameter:
    """
    A parameter to a command, either an Option or Argument.
    """

    name: Optional[str]
    opts: List[str]
    secondary_opts: List[str]
    type: ParamType
    required: bool
    callback: Optional[Callable[[Context, Parameter, Any], Any]]
    nargs: int
    multiple: bool
    expose_value: bool
    is_eager: bool
    metavar: Optional[str]
    envvar: Optional[Union[str, List[str]]]
    autocompletion: Optional[Callable[[Context, List[str], str], List[Union[str, Tuple[str, str]]]]]

    def __init__(
        self,
        param_decls: Optional[Sequence[str]] = ...,
        type: Optional[Union[type[Any], ParamType]] = ...,
        required: bool = ...,
        default: Optional[Any] = ...,
        callback: Optional[Callable[[Context, Parameter, Any], Any]] = ...,
        nargs: Optional[int] = ...,
        metavar: Optional[str] = ...,
        expose_value: bool = ...,
        is_eager: bool = ...,
        envvar: Optional[Union[str, List[str]]] = ...,
        shell_complete: Optional[Callable[[Context, Parameter, str], List[Union[str, Tuple[str, str]]]]] = ...,
    ) -> None: ...

    @property
    def human_readable_name(self) -> str: ...

    def make_metavar(self) -> str: ...
    def get_default(self, ctx: Context, call: bool = ...) -> Any: ...
    def add_to_parser(self, parser: OptionParser, ctx: Context) -> None: ...
    def consume_value(self, ctx: Context, opts: Dict[str, Any]) -> Tuple[Any, List[str]]: ...
    def type_cast_value(self, ctx: Context, value: Any) -> Any: ...
    def process_value(self, ctx: Context, value: Any) -> Any: ...
    def value_is_missing(self, value: Any) -> bool: ...
    def full_process_value(self, ctx: Context, value: Any) -> Any: ...
    def resolve_envvar_value(self, ctx: Context) -> Optional[str]: ...
    def get_help_record(self, ctx: Context) -> Optional[Tuple[str, str]]: ...
    def get_usage_pieces(self, ctx: Context) -> List[str]: ...
    def get_error_hint(self, ctx: Context) -> str: ...


class Option(Parameter):
    """
    Options are optional parameters, usually triggered by flags like --flag.
    """

    prompt: Optional[Union[str, bool]]
    confirmation_prompt: Union[bool, str]
    prompt_required: bool
    hide_input: bool
    is_flag: bool
    flag_value: Any
    is_bool_flag: bool
    count: bool
    allow_from_autoenv: bool
    help: Optional[str]
    hidden: bool
    show_default: Union[bool, str]
    show_choices: bool
    show_envvar: bool

    def __init__(
        self,
        param_decls: Optional[Sequence[str]] = ...,
        show_default: Union[bool, str] = ...,
        prompt: Optional[Union[bool, str]] = ...,
        confirmation_prompt: Union[bool, str] = ...,
        prompt_required: bool = ...,
        hide_input: bool = ...,
        is_flag: Optional[bool] = ...,
        flag_value: Optional[Any] = ...,
        multiple: bool = ...,
        count: bool = ...,
        allow_from_autoenv: bool = ...,
        type: Optional[Union[type[Any], ParamType]] = ...,
        help: Optional[str] = ...,
        hidden: bool = ...,
        show_choices: bool = ...,
        show_envvar: bool = ...,
        **attrs: Any,
    ) -> None: ...

    def prompt_for_value(self, ctx: Context) -> Any: ...


class Argument(Parameter):
    """
    Arguments are positional parameters to a command.
    """

    def __init__(
        self,
        param_decls: Sequence[str],
        required: Optional[bool] = ...,
        **attrs: Any,
    ) -> None: ...
