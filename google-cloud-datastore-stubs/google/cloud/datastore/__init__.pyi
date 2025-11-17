"""Type stubs for google.cloud.datastore"""

from google.cloud.datastore.batch import Batch as Batch
from google.cloud.datastore.client import Client as Client
from google.cloud.datastore.entity import Entity as Entity
from google.cloud.datastore.key import Key as Key
from google.cloud.datastore.query import Query as Query
from google.cloud.datastore.query_profile import ExplainOptions as ExplainOptions
from google.cloud.datastore.transaction import Transaction as Transaction
from google.cloud.datastore.version import __version__ as __version__

__all__ = [
    "__version__",
    "Batch",
    "Client",
    "Entity",
    "Key",
    "Query",
    "ExplainOptions",
    "Transaction",
]
