import requests
import os
import aiohttp
import asyncio


class VidHiveClient:
    """
    A Python client for interacting with the Vid-Hive API.

    Attributes:
        api_key (str): The API key for authenticating with the Vid-Hive API.
        base_url (str): The base URL of the Vid-Hive API.
    """

    def __init__(self, api_key: str, base_url: str):
        """
        Initialize the VidHiveClient.

        Args:
            api_key (str): The API key for authentication.
            base_url (str): The base URL of the Vid-Hive API.
        """
        self.api_key = api_key
        self.base_url = base_url

    def get_signed_url(self, filename: str, same_vpc: bool = True):
        """
        Get a signed URL for uploading a file.

        Args:
            filename (str): The name of the file to upload.
            same_vpc (bool): Whether the upload is from the same VPC. Defaults to True.

        Returns:
            dict: A dictionary containing the signed URL and storage key.
        """
        url = f"{self.base_url}/api/v1/upload/sign-url"
        headers = {
            "X-API-KEY": self.api_key,
            "Content-Type": "application/json"
        }
        payload = {
            "filename": filename,
            "sameVpc": same_vpc
        }
        response = requests.post(url, json=payload, headers=headers)
        response.raise_for_status()
        return response.json()

    def upload_file(self, filename: str, file_path: str, same_vpc: bool = True):
        """
        Upload a file to the Vid-Hive storage.

        Args:
            filename (str): The name of the file to upload.
            file_path (str): The local path to the file.
            same_vpc (bool): Whether the upload is from the same VPC. Defaults to True.

        Returns:
            str: The storage key of the uploaded file.

        Raises:
            FileNotFoundError: If the file does not exist at the specified path.
        """
        if not os.path.exists(file_path):
            raise FileNotFoundError(f"File not found at path: {file_path}")

        signed_url_data = self.get_signed_url(filename, same_vpc)
        signed_url = signed_url_data.get("signedUrl")
        storage_key = signed_url_data.get("storageKey")

        with open(file_path, "rb") as file:
            files = {"file": file}
            upload_response = requests.post(signed_url, files=files)
            upload_response.raise_for_status()

        return storage_key


class AsyncVidHiveClient:
    """
    An asynchronous Python client for interacting with the Vid-Hive API.

    Attributes:
        api_key (str): The API key for authenticating with the Vid-Hive API.
        base_url (str): The base URL of the Vid-Hive API.
    """

    def __init__(self, api_key: str, base_url: str):
        """
        Initialize the AsyncVidHiveClient.

        Args:
            api_key (str): The API key for authentication.
            base_url (str): The base URL of the Vid-Hive API.
        """
        self.api_key = api_key
        self.base_url = base_url

    async def get_signed_url(self, filename: str, same_vpc: bool = True):
        """
        Get a signed URL for uploading a file.

        Args:
            filename (str): The name of the file to upload.
            same_vpc (bool): Whether the upload is from the same VPC. Defaults to True.

        Returns:
            dict: A dictionary containing the signed URL and storage key.
        """
        url = f"{self.base_url}/api/v1/upload/sign-url"
        headers = {
            "X-API-KEY": self.api_key,
            "Content-Type": "application/json"
        }
        payload = {
            "filename": filename,
            "sameVpc": same_vpc
        }

        async with aiohttp.ClientSession() as session:
            async with session.post(url, json=payload, headers=headers) as response:
                response.raise_for_status()
                return await response.json()

    async def upload_file(self, filename: str, file_path: str, same_vpc: bool = True):
        """
        Upload a file to the Vid-Hive storage.

        Args:
            filename (str): The name of the file to upload.
            file_path (str): The local path to the file.
            same_vpc (bool): Whether the upload is from the same VPC. Defaults to True.

        Returns:
            str: The storage key of the uploaded file.

        Raises:
            FileNotFoundError: If the file does not exist at the specified path.
        """
        if not os.path.exists(file_path):
            raise FileNotFoundError(f"File not found at path: {file_path}")

        signed_url_data = await self.get_signed_url(filename, same_vpc)
        signed_url = signed_url_data.get("signedUrl")
        storage_key = signed_url_data.get("storageKey")

        async with aiohttp.ClientSession() as session:
            with open(file_path, "rb") as file:
                files = {"file": file.read()}
                async with session.post(signed_url, data=files) as upload_response:
                    upload_response.raise_for_status()

        return storage_key
