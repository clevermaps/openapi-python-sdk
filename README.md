# OpenAPI Python SDK

This project is a Python client generated using the OpenAPI Generator (`Python Pydantic V1` client). It provides an easy-to-use interface to interact with an API defined by an OpenAPI specification. 
Additionally, there is implemented a **wrapper** to simplify the usage of the generated low-level OpenAPI client.

## Generated OpenAPI Client

The OpenAPI client was generated using **OpenAPI Generator**. For detailed information about the client itself (e.g., endpoints, data models, and configuration), refer to the [generated_client/README.md](generated_client/README.md) file.

---

## Simple Wrapper

To simplify working with the generated OpenAPI client, there is implemented a **high-level wrapper** (see `metadata_wrapper.py`). This wrapper abstracts away the complexity of handling tokens, and low-level API calls. It is designed to make interactions with the API more concise and accessible for users.

### Key Features of the Wrapper
- Automatically manages authentication, including access tokens and token expiry logic.
- Provides high-level methods that correspond to common API actions (e.g., `get_all_views`, `create_view`, `update_view`).
- Hides the complexity of interacting directly with the OpenAPI client's lower-level methods.

---

## How to Use

### Installation

```
pip install -r requirements.txt
```

### Configuration

To get started, initialize a configuration object with your base API URL and refresh token:
```python
from config import Config

config = Config(
    base_url="https://staging.dev.clevermaps.io/rest",
    refresh_token="<REFRESH_TOKEN>"
)
```

## Examples

### High-Level Wrapper Usage

The `demo.py` file demonstrates how to use the wrapper for common actions. Here are some examples:

1. **Print All Views in a Project**:
   ```python
   metadata_wrapper = MetadataWrapper(config)
   
   views = metadata_wrapper.get_all_views(project_id)
   ids = [view.id for view in views.content]
   print("View IDs:", ", ".join(ids))
   ```
   
2. **Create a New View**:
   ```python
   metadata_wrapper = MetadataWrapper(config)
   
   view = metadata_wrapper.create_view(project_id, view_object)
   print(f"View Created with ID: {view.id}")
   ```
   
More information about `views` can be found in official documentation [here](https://docs.clevermaps.io/docs/views).

### Running the Examples

To try the examples provided in the `demo.py` file, ensure your setup is complete and run the following command:
```bash
python demo.py
```