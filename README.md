# Google Cloud Datastore Type Stubs

This repository contains comprehensive type stubs (`.pyi` files) for the `google-cloud-datastore` library to enable better type checking and IDE support.

## Installation

To use these type stubs with your LSP, you can add them to your project's Python path or install them as a package.

### Option 1: Add to Python Path

Add the `google-cloud-datastore-stubs` directory to your PYTHONPATH or place it in your project directory.

### Option 2: Local Installation

```bash
pip install -e google-cloud-datastore-stubs/
```

## Usage

Once installed, your LSP (Language Server Protocol) and type checkers like mypy will automatically discover and use these type stubs when working with the `google-cloud-datastore` library.

## Coverage

The type stubs cover the following modules:

- `google.cloud.datastore` - Main module with exports
- `google.cloud.datastore.client` - Client class for Datastore operations
- `google.cloud.datastore.entity` - Entity class representing datastore rows
- `google.cloud.datastore.key` - Key class for entity identification
- `google.cloud.datastore.query` - Query classes for data retrieval
- `google.cloud.datastore.aggregation` - Aggregation query support
- `google.cloud.datastore.batch` - Batch operations
- `google.cloud.datastore.transaction` - Transaction support
- `google.cloud.datastore.helpers` - Helper functions and GeoPoint class
- `google.cloud.datastore.query_profile` - Query profiling and explain options

## Example

```python
from google.cloud import datastore

# Your LSP will now provide full type hints and autocompletion
client = datastore.Client()
key = client.key('Task', 'sampleTask')
entity = datastore.Entity(key=key)
entity['description'] = 'Buy milk'
client.put(entity)

# Query with type hints
query = client.query(kind='Task')
results = list(query.fetch())
```

## Compatibility

These stubs are compatible with `google-cloud-datastore` version 2.21.0 and should work with similar versions.

## Contributing

If you find any issues or missing type annotations, feel free to submit a pull request or open an issue.

## License

These type stubs follow the same Apache 2.0 license as the `google-cloud-datastore` library.