"""
cipher_tool.mcp_server
======================
Optional MCP server for Cipher Toolbox.

Only usable when the [mcp] extra is installed:
    pip install cipher-toolbox[mcp]
"""

try:
    import fastmcp  # noqa: F401
except ImportError as _exc:
    raise ImportError(
        "The cipher-toolbox MCP server requires the 'mcp' optional extra.\n"
        "Install it with:\n\n"
        "    pip install cipher-toolbox[mcp]\n"
    ) from _exc

from cipher_tool.mcp_server.server import mcp, cli_main  # noqa: E402

__all__ = ["mcp", "cli_main"]
