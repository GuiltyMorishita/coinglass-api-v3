"""
Coinglass API Exception Module
============================

Defines custom exception classes for Coinglass API interactions.
"""

from typing import Optional, Dict, Any, Type, ClassVar


class CoinglassAPIError(Exception):
    """
    Custom exception class for Coinglass API errors.

    Represents errors that occur during API request processing.
    """

    CODE: ClassVar[Optional[str]] = None

    def __init__(
        self,
        message: str,
        code: Optional[str] = None,
        response: Optional[Dict[str, Any]] = None,
    ) -> None:
        """
        Initializes the CoinglassAPIError.

        Args:
            message: The error message.
            code: The error code returned by the API (if available).
            response: The full API response (if available).
        """
        self.message = message
        self.code = code if code is not None else self.CODE
        self.response = response
        super().__init__(self._format_message())

    def _format_message(self) -> str:
        """Formats the exception message including the code if available."""
        if self.code:
            return f"[Code: {self.code}] {self.message}"
        return self.message

    def __str__(self) -> str:
        """Returns the formatted string representation of the exception."""
        return self._format_message()

    @classmethod
    def from_response(cls, response: Dict[str, Any]) -> "CoinglassAPIError":
        """
        Creates an appropriate error instance from an API response.

        Args:
            response: The API response dictionary.

        Returns:
            An instance of the appropriate CoinglassAPIError subclass.
        """
        code = str(response.get("code", "")) if response.get("code") is not None else ""
        message = response.get("msg", "") or "Unknown API error"

        # Find the appropriate error class based on the code
        error_class = ERROR_CODE_MAP.get(code, cls)
        return error_class(message=message, code=code, response=response)


class APIKeyMissingError(CoinglassAPIError):
    """Exception raised when the API key is missing."""

    CODE = "30001"


class RateLimitExceededError(CoinglassAPIError):
    """Exception raised when the rate limit is exceeded."""

    CODE = "50001"


class RequestError(CoinglassAPIError):
    """Exception raised for general request errors."""

    CODE = "40001"


# Mapping of error codes to exception classes
ERROR_CODE_MAP: Dict[str, Type[CoinglassAPIError]] = {
    "30001": APIKeyMissingError,
    "50001": RateLimitExceededError,
    "40001": RequestError,
}
