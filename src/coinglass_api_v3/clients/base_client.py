"""Coinglass API Base Client
=======================

This module provides the base client functionality for the Coinglass API.
"""

import requests
from typing import Dict, Optional, Any
from ..exceptions import CoinglassAPIError


class BaseClient:
    """Base client implementation for Coinglass API.

    Handles request session setup and basic request execution.
    """

    BASE_URL = "https://open-api-v3.coinglass.com"

    def __init__(self, api_key: str) -> None:
        """Initializes the base client.

        Args:
            api_key: Your Coinglass API key.
        """
        self.api_key = api_key
        self.session = requests.Session()
        self.session.headers.update(
            {"CG-API-KEY": api_key, "Accept": "application/json"}
        )

    def _request(
        self, method: str, endpoint: str, params: Optional[Dict[str, Any]] = None
    ) -> Dict[str, Any]:
        """Executes an API request.

        Args:
            method: HTTP method ('GET', 'POST', etc.).
            endpoint: API endpoint (e.g., '/api/futures/supported-coins').
            params: Request parameters.

        Returns:
            The API response as a dictionary.

        Raises:
            CoinglassAPIError: If an API error occurs or the request fails.
        """
        url = f"{self.BASE_URL}{endpoint}"

        try:
            response = self.session.request(method, url, params=params)
            response.raise_for_status()
            data = response.json()

            if data.get("code") != "0":
                raise CoinglassAPIError(
                    f"API error [{data.get('code')}]: {data.get('msg')}",
                    code=data.get("code"),
                    response=data,
                )

            return data
        except requests.exceptions.HTTPError as http_err:
            raise CoinglassAPIError(
                f"HTTP error occurred: {http_err}", response=http_err.response
            )
        except requests.exceptions.RequestException as req_err:
            raise CoinglassAPIError(f"Request failed: {req_err}")
        except ValueError as json_err:
            raise CoinglassAPIError(f"Failed to decode JSON response: {json_err}")
