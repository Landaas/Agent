#Sending a GET request
"""
Set the environment variable:

# macOS/Linux
export API_KEY="your-secret-key"

# Windows PowerShell
$env:API_KEY = "your-secret-key"
"""

import os
import requests

class APIClient:
    def __init__(self, base_url: str, token: str):
        self.base_url = base_url.rstrip("/")
        self.session = requests.Session()
        self.session.headers.update({
            "Authorization": f"Bearer {token}",
            "Accept": "application/json",
        })

    def get(self, url, params=None, headers=None):
        """
        Send an HTTP GET request and return the decoded JSON response.
        Args:    
            url: The URL to send the GET request to.
            params: (Optional) Dictionary of query string parameters to include in the request. parameters are data sent to specify or filter the exact content you want,
        typically placed directly inside the URL.
            headers: (Optional) Dictionary of HTTP headers to include in the request. Headers act as invisible "envelopes" that carry technical metadata, authentication 
            or instructions about the request itself, without being visible in the URL
        Returns:
            The decoded JSON response, or None if the request fails.

        Raises:
            ValueError: If the response body does not contain valid JSON.
        """


        try:
            response = requests.get(url, params=params, timeout=10)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            print(f"An error occurred: {e}")
            return None

    def post(self, url, data=None, headers=None):
        """
        Send an HTTP POST request and return the decoded JSON response.
        Args:
            url: The URL to send the POST request to.
            data: (Optional) Dictionary of data to include in the request body. This is typically used to send form data or JSON payloads.
            headers: (Optional) Dictionary of HTTP headers to include in the request.
        Returns:
            The decoded JSON response, or None if the request fails.
        """
        
        try:
            response = requests.post(url, json=data, headers=headers, timeout=10)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            print(f"An error occurred: {e}")
            return None

    def put(self, url, data=None, headers=None):
        """
        Send an HTTP PUT request and return the decoded JSON response.
        Args:
            url: The URL to send the PUT request to.
            data: (Optional) Dictionary of data to include in the request body. This is typically used to update existing resources.
            headers: (Optional) Dictionary of HTTP headers to include in the request.
        Returns:
            The decoded JSON response, or None if the request fails.
        """

        try:
            response = requests.put(url, json=data, headers=headers, timeout=10)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            print(f"An error occurred: {e}")
            return None

    def delete(self, url, headers=None):
        """
        Send an HTTP DELETE request and return the decoded JSON response.
        Args:
            url: The URL to send the DELETE request to.
            headers: (Optional) Dictionary of HTTP headers to include in the request.
        Returns:
            The decoded JSON response, or None if the request fails.
        """

        try:
            response = requests.delete(url, headers=headers, timeout=10)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            print(f"An error occurred: {e}")
            return None

    def patch(self, url, data=None, headers=None):
        """
        Send an HTTP PATCH request and return the decoded JSON response.
        Args:
            url: The URL to send the PATCH request to.
            data: (Optional) Dictionary of data to include in the request body. This is typically used to partially update existing resources.
            headers: (Optional) Dictionary of HTTP headers to include in the request.
        Returns:
            The decoded JSON response, or None if the request fails.
        """

        try:
            response = requests.patch(url, json=data, headers=headers, timeout=10)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            print(f"An error occurred: {e}")
            return None