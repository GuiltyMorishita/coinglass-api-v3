"""
Tests for the exceptions module.
"""

from typing import Dict, Any, TYPE_CHECKING
import pytest

from coinglass_api_v3.exceptions import (
    CoinglassAPIError,
    APIKeyMissingError,
    RateLimitExceededError,
    RequestError,
)

if TYPE_CHECKING:
    from _pytest.capture import CaptureFixture
    from _pytest.fixtures import FixtureRequest
    from _pytest.logging import LogCaptureFixture
    from _pytest.monkeypatch import MonkeyPatch
    from pytest_mock.plugin import MockerFixture


class TestCoinglassAPIError:
    """Tests for the CoinglassAPIError class."""

    def test_init_with_message_only(self) -> None:
        """Test initializing with only a message."""
        error = CoinglassAPIError("Test error message")
        assert error.message == "Test error message"
        assert error.code is None
        assert error.response is None
        assert str(error) == "Test error message"

    def test_init_with_code(self) -> None:
        """Test initializing with a message and code."""
        error = CoinglassAPIError("Test error message", code="1000")
        assert error.message == "Test error message"
        assert error.code == "1000"
        assert error.response is None
        assert str(error) == "[Code: 1000] Test error message"

    def test_init_with_response(self) -> None:
        """Test initializing with a message, code, and response."""
        response: Dict[str, Any] = {"code": "1000", "msg": "API error"}
        error = CoinglassAPIError("Test error message", code="1000", response=response)
        assert error.message == "Test error message"
        assert error.code == "1000"
        assert error.response == response
        assert str(error) == "[Code: 1000] Test error message"

    def test_format_message_with_code(self) -> None:
        """Test formatting message with a code."""
        error = CoinglassAPIError("Test error", code="1000")
        assert error._format_message() == "[Code: 1000] Test error"

    def test_format_message_without_code(self) -> None:
        """Test formatting message without a code."""
        error = CoinglassAPIError("Test error")
        assert error._format_message() == "Test error"


class TestAPIKeyMissingError:
    """Tests for the APIKeyMissingError class."""

    def test_default_code(self) -> None:
        """Test that the default code is set correctly."""
        error = APIKeyMissingError("API key is missing")
        assert error.code == "30001"
        assert str(error) == "[Code: 30001] API key is missing"

    def test_override_code(self) -> None:
        """Test that the code can be overridden."""
        error = APIKeyMissingError("API key is missing", code="9999")
        assert error.code == "9999"
        assert str(error) == "[Code: 9999] API key is missing"


class TestRateLimitExceededError:
    """Tests for the RateLimitExceededError class."""

    def test_default_code(self) -> None:
        """Test that the default code is set correctly."""
        error = RateLimitExceededError("Rate limit exceeded")
        assert error.code == "50001"
        assert str(error) == "[Code: 50001] Rate limit exceeded"


class TestRequestError:
    """Tests for the RequestError class."""

    def test_default_code(self) -> None:
        """Test that the default code is set correctly."""
        error = RequestError("Request error")
        assert error.code == "40001"
        assert str(error) == "[Code: 40001] Request error"


class TestFromResponse:
    """Tests for the from_response class method."""

    def test_from_response_api_key_missing(self) -> None:
        """Test creating an APIKeyMissingError from a response."""
        response: Dict[str, Any] = {
            "code": "30001",
            "msg": "API key is required",
            "success": False,
        }
        error = CoinglassAPIError.from_response(response)

        assert isinstance(error, APIKeyMissingError)
        assert error.message == "API key is required"
        assert error.code == "30001"
        assert error.response == response

    def test_from_response_rate_limit(self) -> None:
        """Test creating a RateLimitExceededError from a response."""
        response: Dict[str, Any] = {
            "code": "50001",
            "msg": "Rate limit exceeded",
            "success": False,
        }
        error = CoinglassAPIError.from_response(response)

        assert isinstance(error, RateLimitExceededError)
        assert error.message == "Rate limit exceeded"
        assert error.code == "50001"
        assert error.response == response

    def test_from_response_request_error(self) -> None:
        """Test creating a RequestError from a response."""
        response: Dict[str, Any] = {
            "code": "40001",
            "msg": "Invalid request",
            "success": False,
        }
        error = CoinglassAPIError.from_response(response)

        assert isinstance(error, RequestError)
        assert error.message == "Invalid request"
        assert error.code == "40001"
        assert error.response == response

    def test_from_response_unknown_code(self) -> None:
        """Test creating a generic CoinglassAPIError for an unknown code."""
        response: Dict[str, Any] = {
            "code": "99999",
            "msg": "Unknown error",
            "success": False,
        }
        error = CoinglassAPIError.from_response(response)

        assert isinstance(error, CoinglassAPIError)
        assert not isinstance(
            error, (APIKeyMissingError, RateLimitExceededError, RequestError)
        )
        assert error.message == "Unknown error"
        assert error.code == "99999"
        assert error.response == response

    def test_from_response_missing_msg(self) -> None:
        """Test creating an error from a response with a missing msg field."""
        response: Dict[str, Any] = {"code": "30001", "success": False}
        error = CoinglassAPIError.from_response(response)

        assert isinstance(error, APIKeyMissingError)
        assert error.message == "Unknown API error"
        assert error.code == "30001"
        assert error.response == response

    def test_from_response_missing_code(self) -> None:
        """Test creating an error from a response with a missing code field."""
        response: Dict[str, Any] = {"msg": "Some error", "success": False}
        error = CoinglassAPIError.from_response(response)

        assert isinstance(error, CoinglassAPIError)
        assert error.message == "Some error"
        assert error.code == ""
        assert error.response == response
