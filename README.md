# Vid Hive Python Client

This is the Python client library for interacting with the Vid Hive API. It provides convenient methods to communicate with the Vid Hive service.

## Installation

To install the `vid-hive-py-client` package, use the following command:

```bash
pip install git+https://github.com/ngovanxuanduc-atech/vid-hive-py-client.git
```

## Example Usage

Here is an example of how to use the `vid-hive-py-client` library to upload a file:

```python
from vid_hive_client.client import VidHiveClient

# Initialize the client
client = VidHiveClient(api_key="your_api_key", base_url="https://api.vid-hive.com")

# Upload a file
file_path = "path/to/your/file.txt"
storage_key = client.upload_file(filename="file.txt", file_path=file_path)
print(f"File uploaded successfully. Storage key: {storage_key}")
```

### Async Example

If you prefer to use the library in an asynchronous context, here is an example:

```python
import asyncio
from vid_hive_client.client import AsyncVidHiveClient

async def main():
    # Initialize the client
    client = AsyncVidHiveClient(api_key="your_api_key", base_url="https://api.vid-hive.com")

    # Upload a file asynchronously
    file_path = "path/to/your/file.txt"
    storage_key = await client.upload_file(filename="file.txt", file_path=file_path)
    print(f"File uploaded successfully. Storage key: {storage_key}")

# Run the async function
asyncio.run(main())
```
