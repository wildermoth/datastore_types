"""Type stubs for google.cloud.datastore.client"""

from typing import Any, Dict, Iterable, List, Optional, Sequence, Tuple, Union
import datetime

from google.auth.credentials import Credentials
from google.api_core import retry as retry_module
from google.api_core.client_options import ClientOptions
from google.cloud.client import ClientWithProject

from google.cloud.datastore.batch import Batch
from google.cloud.datastore.entity import Entity
from google.cloud.datastore.key import Key
from google.cloud.datastore.query import Query
from google.cloud.datastore.aggregation import AggregationQuery
from google.cloud.datastore.transaction import Transaction

DATASTORE_EMULATOR_HOST: str
DATASTORE_DATASET: str
DISABLE_GRPC: str

class Client(ClientWithProject):
    """Convenience wrapper for invoking APIs/factories w/ a project."""

    SCOPE: Tuple[str, ...]

    namespace: Optional[str]
    _client_info: Any
    _client_options: Optional[Union[ClientOptions, Dict[str, Any]]]
    _batch_stack: Any
    _datastore_api_internal: Optional[Any]
    _database: Optional[str]
    _use_grpc: bool
    _base_url: str

    def __init__(
        self,
        project: Optional[str] = ...,
        namespace: Optional[str] = ...,
        credentials: Optional[Credentials] = ...,
        client_info: Optional[Any] = ...,
        client_options: Optional[Union[ClientOptions, Dict[str, Any]]] = ...,
        database: Optional[str] = ...,
        _http: Optional[Any] = ...,
        _use_grpc: Optional[bool] = ...
    ) -> None: ...

    @staticmethod
    def _determine_default(project: Optional[str]) -> Optional[str]: ...

    @property
    def base_url(self) -> str: ...

    @base_url.setter
    def base_url(self, value: str) -> None: ...

    @property
    def database(self) -> Optional[str]: ...

    @property
    def _datastore_api(self) -> Any: ...

    def _push_batch(self, batch: Batch) -> None: ...
    def _pop_batch(self) -> Batch: ...

    @property
    def current_batch(self) -> Optional[Batch]: ...

    @property
    def current_transaction(self) -> Optional[Transaction]: ...

    def get(
        self,
        key: Key,
        missing: Optional[List[Entity]] = ...,
        deferred: Optional[List[Key]] = ...,
        transaction: Optional[Transaction] = ...,
        eventual: bool = ...,
        retry: Optional[retry_module.Retry] = ...,
        timeout: Optional[float] = ...,
        read_time: Optional[datetime.datetime] = ...
    ) -> Optional[Entity]: ...

    def get_multi(
        self,
        keys: Sequence[Key],
        missing: Optional[List[Entity]] = ...,
        deferred: Optional[List[Key]] = ...,
        transaction: Optional[Transaction] = ...,
        eventual: bool = ...,
        retry: Optional[retry_module.Retry] = ...,
        timeout: Optional[float] = ...,
        read_time: Optional[datetime.datetime] = ...
    ) -> List[Entity]: ...

    def put(
        self,
        entity: Entity,
        retry: Optional[retry_module.Retry] = ...,
        timeout: Optional[float] = ...
    ) -> None: ...

    def put_multi(
        self,
        entities: Iterable[Entity],
        retry: Optional[retry_module.Retry] = ...,
        timeout: Optional[float] = ...
    ) -> None: ...

    def delete(
        self,
        key: Union[Key, Entity],
        retry: Optional[retry_module.Retry] = ...,
        timeout: Optional[float] = ...
    ) -> None: ...

    def delete_multi(
        self,
        keys: Sequence[Union[Key, Entity]],
        retry: Optional[retry_module.Retry] = ...,
        timeout: Optional[float] = ...
    ) -> None: ...

    def allocate_ids(
        self,
        incomplete_key: Key,
        num_ids: int,
        retry: Optional[retry_module.Retry] = ...,
        timeout: Optional[float] = ...
    ) -> List[Key]: ...

    def key(
        self,
        *path_args: Union[str, int],
        namespace: Optional[str] = ...,
        **kwargs: Any
    ) -> Key: ...

    def entity(
        self,
        key: Optional[Key] = ...,
        exclude_from_indexes: Union[Tuple[str, ...], Iterable[str]] = ...
    ) -> Entity: ...

    def batch(self) -> Batch: ...

    def transaction(self, **kwargs: Any) -> Transaction: ...

    def query(self, **kwargs: Any) -> Query: ...

    def aggregation_query(self, query: Query, **kwargs: Any) -> AggregationQuery: ...

    def reserve_ids_sequential(
        self,
        complete_key: Key,
        num_ids: int,
        retry: Optional[retry_module.Retry] = ...,
        timeout: Optional[float] = ...
    ) -> None: ...

    def reserve_ids(
        self,
        complete_key: Key,
        num_ids: int,
        retry: Optional[retry_module.Retry] = ...,
        timeout: Optional[float] = ...
    ) -> None: ...

    def reserve_ids_multi(
        self,
        complete_keys: List[Key],
        retry: Optional[retry_module.Retry] = ...,
        timeout: Optional[float] = ...
    ) -> None: ...

def _get_gcd_project() -> Optional[str]: ...
def _determine_default_project(project: Optional[str] = ...) -> Optional[str]: ...
def _make_retry_timeout_kwargs(
    retry: Optional[retry_module.Retry],
    timeout: Optional[float]
) -> Dict[str, Any]: ...
def _extended_lookup(
    datastore_api: Any,
    project: str,
    key_pbs: List[Any],
    missing: Optional[List[Any]] = ...,
    deferred: Optional[List[Any]] = ...,
    eventual: bool = ...,
    transaction: Optional[Transaction] = ...,
    retry: Optional[retry_module.Retry] = ...,
    timeout: Optional[float] = ...,
    read_time: Optional[datetime.datetime] = ...,
    database: Optional[str] = ...
) -> List[Any]: ...
