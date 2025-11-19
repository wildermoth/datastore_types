"""RootModel class and type definitions stubs."""

from __future__ import annotations as _annotations

from copy import copy, deepcopy
from typing import TYPE_CHECKING, Any, Generic, Literal, TypeVar

from pydantic_core import PydanticUndefined
from typing_extensions import Self, dataclass_transform

from pydantic import PydanticUserError
from pydantic._internal import _model_construction, _repr
from pydantic.main import BaseModel, _object_setattr

if TYPE_CHECKING:
    from pydantic.fields import Field as PydanticModelField
    from pydantic.fields import PrivateAttr as PydanticModelPrivateAttr

    @dataclass_transform(kw_only_default=False, field_specifiers=(PydanticModelField, PydanticModelPrivateAttr))
    class _RootModelMetaclass(_model_construction.ModelMetaclass): ...
else:
    _RootModelMetaclass = _model_construction.ModelMetaclass

RootModelRootType = TypeVar('RootModelRootType')

class RootModel(BaseModel, Generic[RootModelRootType], metaclass=_RootModelMetaclass):
    """!!! abstract "Usage Documentation"
        [`RootModel` and Custom Root Types](../concepts/models.md#rootmodel-and-custom-root-types)

    A Pydantic `BaseModel` for the root object of the model.

    Attributes:
        root: The root object of the model.
        __pydantic_root_model__: Whether the model is a RootModel.
        __pydantic_private__: Private fields in the model.
        __pydantic_extra__: Extra fields in the model.
    """

    __pydantic_root_model__: bool
    __pydantic_private__: None
    __pydantic_extra__: None

    root: RootModelRootType

    def __init_subclass__(cls, **kwargs: Any) -> None: ...

    def __init__(self, /, root: RootModelRootType = PydanticUndefined, **data: Any) -> None: ...

    @classmethod
    def model_construct(cls, root: RootModelRootType, _fields_set: set[str] | None = None) -> Self:
        """Create a new model using the provided root object and update fields set.

        Args:
            root: The root object of the model.
            _fields_set: The set of fields to be updated.

        Returns:
            The new model.

        Raises:
            NotImplemented: If the model is not a subclass of `RootModel`.
        """
        ...

    def __getstate__(self) -> dict[Any, Any]: ...

    def __setstate__(self, state: dict[Any, Any]) -> None: ...

    def __copy__(self) -> Self:
        """Returns a shallow copy of the model."""
        ...

    def __deepcopy__(self, memo: dict[int, Any] | None = None) -> Self:
        """Returns a deep copy of the model."""
        ...

    if TYPE_CHECKING:
        def model_dump(  # type: ignore
            self,
            *,
            mode: Literal['json', 'python'] | str = 'python',
            include: Any = None,
            exclude: Any = None,
            context: dict[str, Any] | None = None,
            by_alias: bool | None = None,
            exclude_unset: bool = False,
            exclude_defaults: bool = False,
            exclude_none: bool = False,
            exclude_computed_fields: bool = False,
            round_trip: bool = False,
            warnings: bool | Literal['none', 'warn', 'error'] = True,
            serialize_as_any: bool = False,
        ) -> Any:
            """This method is included just to get a more accurate return type for type checkers.
            It is included in this `if TYPE_CHECKING:` block since no override is actually necessary.

            See the documentation of `BaseModel.model_dump` for more details about the arguments.

            Generally, this method will have a return type of `RootModelRootType`, assuming that `RootModelRootType` is
            not a `BaseModel` subclass. If `RootModelRootType` is a `BaseModel` subclass, then the return
            type will likely be `dict[str, Any]`, as `model_dump` calls are recursive. The return type could
            even be something different, in the case of a custom serializer.
            Thus, `Any` is used here to catch all of these cases.
            """
            ...

    def __eq__(self, other: Any) -> bool: ...

    def __repr_args__(self) -> _repr.ReprArgs: ...
