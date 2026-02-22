import os
import json
import platform
from pathlib import Path
from importlib.metadata import version, PackageNotFoundError

import requests

CONFIG_PATH = Path.home() / ".cipher_tool_config.json"
TELEMETRY_URL = "https://yourdomain.com/telemetry"  # ← Replace with your real server


def _get_package_version():
    try:
        return version("cipher-toolbox")
    except PackageNotFoundError:
        return "unknown"


def telemetry_enabled():
    # Enterprise kill switch
    if os.getenv("CIPHER_TOOL_TELEMETRY_DISABLED") == "1":
        return False

    if not CONFIG_PATH.exists():
        return False

    try:
        config = json.loads(CONFIG_PATH.read_text())
        return config.get("telemetry", False)
    except Exception:
        return False


def setup_telemetry():
    """
    Runs once on first CLI execution.
    Stores explicit user consent.
    """
    if CONFIG_PATH.exists():
        return

    print(
        "\nCipher Toolbox supports anonymous usage analytics.\n"
        "No personal data is collected.\n"
        "You can disable this anytime with:\n"
        "  export CIPHER_TOOL_TELEMETRY_DISABLED=1\n"
    )

    choice = input("Enable anonymous analytics? (y/N): ").strip().lower()

    config = {
        "telemetry": choice == "y"
    }

    try:
        CONFIG_PATH.write_text(json.dumps(config))
    except Exception:
        pass  # Never break CLI


def send_telemetry(command_name: str):
    """
    Sends minimal anonymous execution metadata.
    Never interrupts tool execution.
    """
    if not telemetry_enabled():
        return

    payload = {
        "tool": "cipher-toolbox",
        "version": _get_package_version(),
        "command": command_name,
        "python": platform.python_version(),
        "os": platform.system(),
    }

    try:
        requests.post(TELEMETRY_URL, json=payload, timeout=2)
    except Exception:
        pass  # Silent fail