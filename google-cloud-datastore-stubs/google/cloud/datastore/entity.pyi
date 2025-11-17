"""Type stubs for google.cloud.datastore.entity"""

from typing import Any, Dict, Iterable, Optional, Set, Tuple, Union

from google.cloud.datastore.key import Key

class Entity(Dict[str, Any]):
    """Entities are akin to rows in a relational database."""

    key: Optional[Key]
    exclude_from_indexes: Set[str]
    _meanings: Dict[str, Tuple[Any, Any]]

    def __init__(
        self,
        key: Optional[Key] = ...,
        exclude_from_indexes: Union[Tuple[str, ...], Iterable[str]] = ...
    ) -> None: ...

    def __eq__(self, other: object) -> bool: ...
    def __ne__(self, other: object) -> bool: ...
    def __repr__(self) -> str: ...

    @property
    def kind(self) -> Optional[str]: ...

    @property
    def id(self) -> Optional[int]: ...
