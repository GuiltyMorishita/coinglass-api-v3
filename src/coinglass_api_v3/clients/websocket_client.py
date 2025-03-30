"""
Coinglass WebSocket Client
==========================

This module implements a client for accessing the Coinglass WebSocket API.
"""

import json
import logging
import threading
import time
from typing import Dict, List, Optional, Any, Callable, TypeVar

from websocket import WebSocketApp, enableTrace

T = TypeVar("T")
WebSocketDataHandler = Callable[[Any], None]

logger = logging.getLogger(__name__)


class CoinglassWebSocketClient:
    """Coinglass WebSocket client."""

    WS_URL = "wss://open-ws.coinglass.com/ws-api"
    PING_INTERVAL = 20  # Ping interval in seconds

    def __init__(self, api_key: str, debug: bool = False) -> None:
        """
        Initializes the Coinglass WebSocket client.

        Args:
            api_key: Coinglass API key.
            debug: Whether to enable debug mode.
        """
        self.api_key = api_key
        self.debug = debug
        self.ws: Optional[WebSocketApp] = None
        self.is_connected = False
        self.is_authenticated = False
        self.subscribed_channels: Dict[str, List[str]] = {}
        self.handlers: Dict[str, List[WebSocketDataHandler]] = {}
        self.reconnect_interval = 5  # Reconnect interval in seconds
        self.max_reconnect_attempts = 5  # Maximum reconnect attempts
        self.reconnect_attempts = 0
        self.running = False
        self.connect_lock = threading.Lock()
        self._ping_thread: Optional[threading.Thread] = None
        self._ws_thread: Optional[threading.Thread] = None

        if debug:
            enableTrace(True)
            logging.basicConfig(level=logging.DEBUG)

    def _send_message(self, message: Dict[str, Any]) -> None:
        """Sends a message over the WebSocket."""
        if self.ws and self.is_connected:
            try:
                msg_str = json.dumps(message)
                self.ws.send(msg_str)
                logger.debug(f"Sent message: {msg_str}")
            except Exception as e:
                logger.error(f"Error sending message: {e}")
        else:
            logger.warning("WebSocket is not connected. Cannot send message.")

    def _send_ping(self) -> None:
        """Periodically sends a ping message."""
        while self.running and self.is_connected:
            try:
                ping_message = {"op": "ping"}
                self._send_message(ping_message)
                logger.debug("Sent ping")
                time.sleep(self.PING_INTERVAL)
            except Exception as e:
                logger.error(f"Error in ping thread: {e}")
                break

    def _on_message(self, ws: WebSocketApp, message: str) -> None:
        """
        Callback for when a message is received.

        Args:
            ws: The WebSocketApp instance.
            message: The received message.
        """
        try:
            data = json.loads(message)
            logger.debug(f"Received message: {data}")

            if isinstance(data, dict) and data.get("op") == "pong":
                logger.debug("Received pong")
                return

            if isinstance(data, dict) and data.get("op") == "auth":
                success = data.get("success", False)
                self.is_authenticated = success
                if success:
                    logger.info("Authentication successful")
                    self._resubscribe_channels()
                else:
                    logger.error(
                        f"Authentication failed: {data.get('message', 'Unknown error')}"
                    )
                return

            if isinstance(data, dict) and "channel" in data and "data" in data:
                channel = data["channel"]
                channel_data = data["data"]

                if channel in self.handlers:
                    for handler in self.handlers[channel]:
                        try:
                            handler(channel_data)
                        except Exception as e:
                            logger.error(f"Error in handler for channel {channel}: {e}")
                else:
                    logger.debug(f"No handler registered for channel: {channel}")
            elif isinstance(data, dict) and data.get("event") == "error":
                logger.error(
                    f"Received error message from server: {data.get('message', 'Unknown error')}"
                )

        except json.JSONDecodeError:
            logger.error(f"Failed to parse message: {message}")
        except Exception as e:
            logger.error(f"Error processing message: {e}")

    def _on_error(self, ws: WebSocketApp, error: Exception) -> None:
        """
        Callback for when an error occurs.

        Args:
            ws: The WebSocketApp instance.
            error: The error that occurred.
        """
        logger.error(f"WebSocket error: {error}")
        self.is_connected = False
        self.is_authenticated = False

    def _on_close(
        self,
        ws: WebSocketApp,
        close_status_code: Optional[int],
        close_msg: Optional[str],
    ) -> None:
        """
        Callback for when the connection is closed.

        Args:
            ws: The WebSocketApp instance.
            close_status_code: The close status code.
            close_msg: The close message.
        """
        logger.info(
            f"WebSocket connection closed: Status={close_status_code}, Msg={close_msg}"
        )
        self.is_connected = False
        self.is_authenticated = False

        if self.running:
            logger.warning("Connection closed unexpectedly. Attempting to reconnect...")
            self._attempt_reconnect()
        else:
            logger.info("WebSocket closed intentionally.")

    def _on_open(self, ws: WebSocketApp) -> None:
        """
        Callback for when the connection is opened.

        Args:
            ws: The WebSocketApp instance.
        """
        logger.info("WebSocket connection opened")
        self.is_connected = True
        self.reconnect_attempts = 0

        auth_message_dict = {"op": "auth", "args": [{"apiKey": self.api_key}]}
        self._send_message(auth_message_dict)

        self._ping_thread = threading.Thread(target=self._send_ping, daemon=True)
        self._ping_thread.start()

    def connect(self) -> None:
        """Connects to the WebSocket."""
        with self.connect_lock:
            if self.running:
                logger.warning("WebSocket client is already running or connecting.")
                return

            self.running = True
            self._start_ws_thread()

    def _start_ws_thread(self) -> None:
        """Starts the thread for WebSocket connection and execution."""
        if self._ws_thread and self._ws_thread.is_alive():
            logger.warning("WebSocket thread is already running.")
            return

        logger.info(f"Connecting to {self.WS_URL}...")
        self.ws = WebSocketApp(
            self.WS_URL,
            on_open=self._on_open,
            on_message=self._on_message,
            on_error=self._on_error,
            on_close=self._on_close,
        )
        self._ws_thread = threading.Thread(target=self.ws.run_forever, daemon=True)
        self._ws_thread.start()

    def disconnect(self) -> None:
        """Disconnects from the WebSocket."""
        with self.connect_lock:
            if not self.running:
                logger.warning("WebSocket client is not running.")
                return

            logger.info("Disconnecting WebSocket...")
            self.running = False

            if self.ws:
                try:
                    self.ws.close()
                except Exception as e:
                    logger.error(f"Error closing WebSocket: {e}")

            if self._ws_thread and self._ws_thread.is_alive():
                logger.debug("Waiting for WebSocket thread to terminate...")
                self._ws_thread.join(timeout=5)
                if self._ws_thread.is_alive():
                    logger.warning("WebSocket thread did not terminate gracefully.")
                else:
                    logger.debug("WebSocket thread terminated.")

            self.ws = None
            self._ws_thread = None
            self._ping_thread = None
            self.is_connected = False
            self.is_authenticated = False
            logger.info("WebSocket disconnected.")

    def _attempt_reconnect(self) -> None:
        """Attempts to reconnect."""
        if not self.running:
            logger.info("Reconnect attempt aborted as the client is not running.")
            return

        if self.reconnect_attempts < self.max_reconnect_attempts:
            self.reconnect_attempts += 1
            wait_time = self.reconnect_interval * (2 ** (self.reconnect_attempts - 1))
            logger.info(
                f"Attempting reconnect {self.reconnect_attempts}/{self.max_reconnect_attempts} "
                f"in {wait_time} seconds..."
            )
            time.sleep(wait_time)
            # Close the existing WebSocket instance if it exists
            if self.ws:
                try:
                    self.ws.close()
                except Exception as e:
                    logger.error(f"Error closing WebSocket before reconnect: {e}")
            self._start_ws_thread()
        else:
            logger.error("Max reconnect attempts reached. Giving up.")
            self.running = False  # Stop trying to reconnect

    def _resubscribe_channels(self) -> None:
        """Resubscribes to all previously subscribed channels after reconnection."""
        if not self.is_connected or not self.is_authenticated:
            logger.warning("Cannot resubscribe: Not connected or authenticated.")
            return

        logger.info("Resubscribing to channels...")
        for channel, params_list in list(self.subscribed_channels.items()):
            # Create a copy of the params list to avoid modification issues during iteration
            current_params = list(params_list)
            if current_params:
                # Combine parameters into a single args list for subscription
                args = [f"{channel}:{param}" for param in current_params]
                sub_message = {"op": "subscribe", "args": args}
                self._send_message(sub_message)
                logger.info(
                    f"Resubscribed to channel {channel} with params: {current_params}"
                )
            else:
                logger.warning(
                    f"No parameters found for channel {channel} during resubscribe."
                )

    def subscribe(
        self, channel: str, params: List[str], handler: WebSocketDataHandler
    ) -> None:
        """
        Subscribes to a WebSocket channel.

        Args:
            channel: The channel name (e.g., "liquidation", "trade").
            params: A list of parameters for the channel (e.g., ["BTC", "ETH"] or ["BTCUSDT:Binance"]).
            handler: The callback function to handle data received on this channel.

        Subscription Format Examples:
            - Liquidation for BTC & ETH: channel="liquidation", params=["BTC", "ETH"]
            - Trades for BTCUSDT on Binance: channel="trade", params=["BTCUSDT:Binance"]
            - All liquidations: channel="liquidation", params=["all"]
        """
        if not channel or not params:
            logger.error("Channel and params cannot be empty for subscription.")
            return

        if channel not in self.handlers:
            self.handlers[channel] = []
        if handler not in self.handlers[channel]:
            self.handlers[channel].append(handler)
            logger.info(f"Handler added for channel: {channel}")

        if channel not in self.subscribed_channels:
            self.subscribed_channels[channel] = []

        new_params_to_subscribe = []
        for p in params:
            if p not in self.subscribed_channels[channel]:
                self.subscribed_channels[channel].append(p)
                new_params_to_subscribe.append(p)

        if new_params_to_subscribe:
            if self.is_connected and self.is_authenticated:
                # Format args for subscription message
                args = [f"{channel}:{param}" for param in new_params_to_subscribe]
                sub_message = {"op": "subscribe", "args": args}
                self._send_message(sub_message)
                logger.info(
                    f"Subscribed to channel {channel} with new params: {new_params_to_subscribe}"
                )
            else:
                logger.warning(
                    f"WebSocket not ready. Subscription for {channel} with params "
                    f"{new_params_to_subscribe} will be attempted upon connection/authentication."
                )
        else:
            logger.info(
                f"Already subscribed to channel {channel} with params: {params}"
            )

    def unsubscribe(
        self,
        channel: str,
        params: List[str],
        handler: Optional[WebSocketDataHandler] = None,
    ) -> None:
        """
        Unsubscribes from a WebSocket channel.

        Args:
            channel: The channel name.
            params: A list of parameters to unsubscribe from.
            handler: If provided, only removes this specific handler for the channel.
                     If None, removes all handlers and unsubscribes from the server.
        """
        if channel not in self.subscribed_channels:
            logger.warning(f"Not subscribed to channel: {channel}")
            return

        params_to_unsubscribe = []
        remaining_params = list(self.subscribed_channels.get(channel, []))

        for p in params:
            if p in remaining_params:
                params_to_unsubscribe.append(p)
                remaining_params.remove(p)

        if not params_to_unsubscribe:
            logger.warning(
                f"Not currently subscribed to channel {channel} with params: {params}"
            )
            return

        # Update subscribed channels list
        if not remaining_params:
            del self.subscribed_channels[channel]
        else:
            self.subscribed_channels[channel] = remaining_params

        # Send unsubscribe message to server only if we are connected and authenticated
        if self.is_connected and self.is_authenticated:
            args = [f"{channel}:{param}" for param in params_to_unsubscribe]
            unsub_message = {"op": "unsubscribe", "args": args}
            self._send_message(unsub_message)
            logger.info(
                f"Unsubscribed from channel {channel} with params: {params_to_unsubscribe}"
            )
        else:
            logger.warning(
                "WebSocket not ready. Unsubscription message will not be sent to the server, "
                "but internal state is updated."
            )

        # Remove handler(s)
        if channel in self.handlers:
            if handler:
                if handler in self.handlers[channel]:
                    self.handlers[channel].remove(handler)
                    logger.info(f"Removed specific handler for channel: {channel}")
                else:
                    logger.warning(f"Handler not found for channel: {channel}")
            elif not remaining_params:  # Remove all handlers only if no params are left
                del self.handlers[channel]
                logger.info(f"Removed all handlers for channel: {channel}")
