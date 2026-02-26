import os
import platform
import requests

API_URL = "https://cipher-tool-telemetry.onrender.com/telemetry"


def send_telemetry(command: str, version: str):
    """
    Sends anonymous usage telemetry.
    Fails silently if any error occurs.
    """
    # Try environment variable first
    api_key = (
        os.getenv("CIPHER_API_KEY")
        or os.getenv("CIPHER_TOOL_API_KEY")
    )
    # Fallback to bundled key if env var not set
    if not api_key:
        try:
            from .key import API_KEY
            api_key = API_KEY
        except Exception:
            api_key = None
    if not api_key:
        return  # No key set → do nothing
    payload = {
        "tool": "cipher-tool",
        "version": version,
        "command": command,
        "python": platform.python_version(),
        "os": platform.system(),
    }
    try:
        requests.post(
            API_URL,
            json=payload,
            headers={"X-API-Key": api_key},
            timeout=3,
        )
    except Exception:
        # Never break CLI if telemetry fails
        pass