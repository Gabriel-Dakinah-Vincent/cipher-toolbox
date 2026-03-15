"""Tests for the optional MCP server (cipher_tool.mcp_server)."""
from __future__ import annotations

import asyncio
import builtins
import importlib
import importlib.util
import sys

import pytest

# ---------------------------------------------------------------------------
# Skip guard
# ---------------------------------------------------------------------------
fastmcp_available = importlib.util.find_spec("fastmcp") is not None
skip_no_mcp = pytest.mark.skipif(
    not fastmcp_available,
    reason="fastmcp not installed — run: pip install cipher-toolbox[mcp]",
)

# ---------------------------------------------------------------------------
# Guard test (always runs — does not need fastmcp)
# ---------------------------------------------------------------------------

def test_missing_fastmcp_raises_helpful_error(monkeypatch):
    _real_import = builtins.__import__

    def _fake_import(name, *args, **kwargs):
        if name == "fastmcp":
            raise ImportError("no module named 'fastmcp'")
        return _real_import(name, *args, **kwargs)

    mods_to_remove = [k for k in sys.modules if k.startswith("cipher_tool.mcp_server")]
    saved = {k: sys.modules.pop(k) for k in mods_to_remove}

    monkeypatch.setattr(builtins, "__import__", _fake_import)
    try:
        with pytest.raises(ImportError, match=r"pip install cipher-toolbox\[mcp\]"):
            importlib.import_module("cipher_tool.mcp_server")
    finally:
        sys.modules.update(saved)


# ---------------------------------------------------------------------------
# Server bootstrap tests
# ---------------------------------------------------------------------------

@skip_no_mcp
def test_mcp_instance_is_created():
    from cipher_tool.mcp_server.server import mcp as server_mcp
    from fastmcp import FastMCP
    assert isinstance(server_mcp, FastMCP)


@skip_no_mcp
def test_server_name():
    from cipher_tool.mcp_server.server import mcp as server_mcp
    assert server_mcp.name == "Cipher Toolbox"


# ---------------------------------------------------------------------------
# Tool registration tests
# ---------------------------------------------------------------------------

EXPECTED_TOOLS = {
    "encrypt", "decrypt",
    "rsa_keygen", "list_ciphers", "fetch_docs",
}


@skip_no_mcp
def test_all_tools_registered():
    from cipher_tool.mcp_server.server import mcp as server_mcp
    registered = {t.name for t in asyncio.run(server_mcp.list_tools())}
    assert EXPECTED_TOOLS.issubset(registered), (
        f"Missing tools: {EXPECTED_TOOLS - registered}"
    )


@skip_no_mcp
def test_tool_count():
    from cipher_tool.mcp_server.server import mcp as server_mcp
    registered = {t.name for t in asyncio.run(server_mcp.list_tools())}
    assert len(registered) == len(EXPECTED_TOOLS), (
        f"Expected {len(EXPECTED_TOOLS)} tools, got {len(registered)}: {registered}"
    )


# ---------------------------------------------------------------------------
# Resource registration tests
# ---------------------------------------------------------------------------

EXPECTED_RESOURCES = {
    "docs://overview",
    "docs://installation",
    "docs://classical-ciphers",
    "docs://modern-ciphers",
    "docs://security",
    "docs://parameters",
}


@skip_no_mcp
def test_all_resources_registered():
    from cipher_tool.mcp_server.server import mcp as server_mcp
    registered = {str(r.uri) for r in asyncio.run(server_mcp.list_resources())}
    assert EXPECTED_RESOURCES.issubset(registered), (
        f"Missing resources: {EXPECTED_RESOURCES - registered}"
    )


@skip_no_mcp
def test_resources_return_strings():
    from cipher_tool.mcp_server import server as srv
    fns = [
        srv.resource_overview,
        srv.resource_installation,
        srv.resource_classical,
        srv.resource_modern,
        srv.resource_security,
        srv.resource_parameters,
    ]
    for fn in fns:
        result = fn()
        assert isinstance(result, str) and len(result) > 0, f"{fn.__name__} failed"


@skip_no_mcp
def test_resource_template_returns_docs_for_each_cipher():
    from cipher_tool.mcp_server.server import resource_cipher, SUPPORTED_CIPHERS
    for name in SUPPORTED_CIPHERS:
        result = resource_cipher(name)
        assert isinstance(result, str) and len(result) > 0, f"No docs for {name}"
        assert "Unknown cipher" not in result, f"{name} returned unknown cipher"


@skip_no_mcp
def test_resource_template_unknown_cipher():
    from cipher_tool.mcp_server.server import resource_cipher
    result = resource_cipher("nonexistent")
    assert "Unknown cipher" in result


# ---------------------------------------------------------------------------
# Prompt registration tests
# ---------------------------------------------------------------------------

EXPECTED_PROMPTS = {
    "encrypt-message",
    "decrypt-message",
    "explain-cipher",
    "compare-ciphers",
    "brute-force-caesar",
    "cipher-security-audit",
    "encrypt-and-store-workflow",
    "cipher-quiz",
}


@skip_no_mcp
def test_all_prompts_registered():
    from cipher_tool.mcp_server.server import mcp as server_mcp
    registered = {p.name for p in asyncio.run(server_mcp.list_prompts())}
    assert EXPECTED_PROMPTS.issubset(registered), (
        f"Missing prompts: {EXPECTED_PROMPTS - registered}"
    )


@skip_no_mcp
def test_prompts_return_message_lists():
    from fastmcp.prompts import Message
    from cipher_tool.mcp_server import server as srv

    calls = [
        srv.prompt_encrypt_message("HELLO"),
        srv.prompt_decrypt_message("KHOOR"),
        srv.prompt_explain_cipher("caesar"),
        srv.prompt_compare_ciphers("caesar", "vigenere"),
        srv.prompt_brute_force_caesar("KHOOR"),
        srv.prompt_cipher_security_audit("aes"),
        srv.prompt_encrypt_and_store_workflow("HELLO"),
        srv.prompt_cipher_quiz(),
    ]
    for result in calls:
        assert isinstance(result, list) and len(result) > 0
        assert all(isinstance(m, Message) for m in result)


# ---------------------------------------------------------------------------
# Tool round-trip smoke tests (all via encrypt_text / decrypt_text)
# ---------------------------------------------------------------------------

@skip_no_mcp
def test_roundtrip_caesar():
    from cipher_tool.mcp_server.server import encrypt_text, decrypt_text
    ct = encrypt_text("caesar", "HELLO", shift=3)
    assert decrypt_text("caesar", ct, shift=3) == "HELLO"


@skip_no_mcp
def test_roundtrip_atbash():
    from cipher_tool.mcp_server.server import encrypt_text, decrypt_text
    ct = encrypt_text("atbash", "HELLO")
    assert decrypt_text("atbash", ct) == "HELLO"


@skip_no_mcp
def test_roundtrip_affine():
    from cipher_tool.mcp_server.server import encrypt_text, decrypt_text
    ct = encrypt_text("affine", "HELLO", a=5, b=8)
    assert decrypt_text("affine", ct, a=5, b=8) == "HELLO"


@skip_no_mcp
def test_roundtrip_vigenere():
    from cipher_tool.mcp_server.server import encrypt_text, decrypt_text
    ct = encrypt_text("vigenere", "HELLO", key="KEY")
    assert decrypt_text("vigenere", ct, key="KEY") == "HELLO"


@skip_no_mcp
def test_roundtrip_beaufort():
    from cipher_tool.mcp_server.server import encrypt_text, decrypt_text
    ct = encrypt_text("beaufort", "HELLO", key="KEY")
    assert decrypt_text("beaufort", ct, key="KEY") == "HELLO"


@skip_no_mcp
def test_roundtrip_autokey():
    from cipher_tool.mcp_server.server import encrypt_text, decrypt_text
    ct = encrypt_text("autokey", "HELLO", key="KEY")
    assert decrypt_text("autokey", ct, key="KEY") == "HELLO"


@skip_no_mcp
def test_roundtrip_railfence():
    from cipher_tool.mcp_server.server import encrypt_text, decrypt_text
    ct = encrypt_text("railfence", "HELLO WORLD", rails=3)
    assert decrypt_text("railfence", ct, rails=3) == "HELLO WORLD"


@skip_no_mcp
def test_roundtrip_columnar():
    from cipher_tool.mcp_server.server import encrypt_text, decrypt_text
    ct = encrypt_text("columnar", "HELLOWORLD", key="KEY")
    assert decrypt_text("columnar", ct, key="KEY") == "HELLOWORLD"


@skip_no_mcp
def test_roundtrip_xor():
    from cipher_tool.mcp_server.server import encrypt_text, decrypt_text
    ct = encrypt_text("xor", "HELLO", key="SECRET")
    assert decrypt_text("xor", ct, key="SECRET") == "HELLO"


@skip_no_mcp
def test_roundtrip_aes():
    from cipher_tool.mcp_server.server import encrypt_text, decrypt_text
    ct = encrypt_text("aes", "HELLO WORLD")
    assert decrypt_text("aes", ct) == "HELLO WORLD"


@skip_no_mcp
def test_roundtrip_chacha20():
    from cipher_tool.mcp_server.server import encrypt_text, decrypt_text
    ct = encrypt_text("chacha20", "HELLO WORLD")
    assert decrypt_text("chacha20", ct) == "HELLO WORLD"


@skip_no_mcp
def test_roundtrip_rsa():
    from cipher_tool.mcp_server.server import encrypt_text, decrypt_text
    ct = encrypt_text("rsa", "HELLO")
    assert decrypt_text("rsa", ct) == "HELLO"


@skip_no_mcp
def test_rsa_keygen_and_roundtrip():
    from cipher_tool.mcp_server.server import rsa_keygen, encrypt_text, decrypt_text
    result = rsa_keygen(2048)
    assert "PUBLIC KEY" in result
    assert "PRIVATE KEY" in result
    ct = encrypt_text("rsa", "HELLO")
    assert decrypt_text("rsa", ct) == "HELLO"


@skip_no_mcp
def test_list_ciphers():
    from cipher_tool.mcp_server.server import list_ciphers
    result = list_ciphers()
    assert isinstance(result, str) and len(result) > 0
    for name in ("caesar", "aes", "rsa", "columnar"):
        assert name in result, f"'{name}' not found in list_ciphers output"
