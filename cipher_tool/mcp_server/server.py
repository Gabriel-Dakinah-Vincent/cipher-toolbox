from __future__ import annotations

import argparse
import urllib.request
from typing import Annotated

from fastmcp import FastMCP
from fastmcp.prompts import Message
from pydantic import Field
from cipher_tool import encrypt as _encrypt, decrypt as _decrypt

GITBOOK_BASE = "https://eadmiral.gitbook.io/cipher-toolbox"

SUPPORTED_CIPHERS = [
    "caesar", "atbash", "affine",
    "vigenere", "beaufort", "autokey",
    "railfence", "columnar",
    "xor", "aes", "chacha20",
    "rsa",
]

mcp = FastMCP(
    name="Cipher Toolbox",
    instructions=(
        "Cipher Toolbox MCP Server — educational cryptography toolkit.\n\n"
        "THREE MCP PRIMITIVES\n"
        "  Tools     — encrypt_text / decrypt_text for all 12 ciphers + 2 utility helpers\n"
        "  Resources — docs:// URIs with offline reference material\n"
        "  Prompts   — guided templates for common cryptography workflows\n\n"
        "CIPHER CATALOGUE\n"
        "  Classical / Substitution   : caesar · atbash · affine\n"
        "  Classical / Polyalphabetic : vigenere · beaufort · autokey\n"
        "  Classical / Transposition  : railfence · columnar\n"
        "  Modern    / Symmetric      : xor · aes · chacha20\n"
        "  Modern    / Asymmetric     : rsa\n\n"
        "PARAMETER GUIDE\n"
        "  caesar    → shift (int)           atbash   → (none)\n"
        "  affine    → a (int), b (int)      vigenere → key (str)\n"
        "  beaufort  → key (str)             autokey  → key (str)\n"
        "  railfence → rails (int)           columnar → key (str)\n"
        "  xor       → key (str)             aes      → key (str, optional)\n"
        "  chacha20  → key (str, optional)   rsa      → key_size (int, default 2048)\n\n"
        "⚠️  Classical ciphers are NOT secure — educational use only."
    ),
)

# 
# PRIMITIVE 1 — Tools (4 total)
# 

@mcp.tool(name="encrypt")
def encrypt_text(
    cipher: Annotated[str, Field(description="Cipher name: caesar, atbash, affine, vigenere, beaufort, autokey, railfence, columnar, xor, aes, chacha20, or rsa")],
    text: Annotated[str, Field(description="Plaintext to encrypt")],
    shift: Annotated[int | None, Field(description="Shift value for caesar cipher (1-25)")] = None,
    key: Annotated[str | None, Field(description="Key for vigenere, beaufort, autokey, columnar, xor, aes, or chacha20")] = None,
    a: Annotated[int | None, Field(description="Multiplier for affine cipher (must be coprime to 26)")] = None,
    b: Annotated[int | None, Field(description="Offset for affine cipher")] = None,
    rails: Annotated[int | None, Field(description="Number of rails for railfence cipher (≥2)")] = None,
    key_size: Annotated[int | None, Field(description="RSA key size in bits (default 2048)")] = None,
) -> str:
    """Encrypt text using any supported cipher. Pass the cipher name and only the parameters relevant to that cipher."""
    params: dict = {}
    if shift is not None:
        params["shift"] = shift
    if key is not None:
        params["key"] = key
    if a is not None:
        params["a"] = a
    if b is not None:
        params["b"] = b
    if rails is not None:
        params["rails"] = rails
    if key_size is not None:
        params["key_size"] = key_size
    return _encrypt(cipher.lower(), text, **params)


@mcp.tool(name="decrypt")
def decrypt_text(
    cipher: Annotated[str, Field(description="Cipher name: caesar, atbash, affine, vigenere, beaufort, autokey, railfence, columnar, xor, aes, chacha20, or rsa")],
    ciphertext: Annotated[str, Field(description="Ciphertext to decrypt")],
    shift: Annotated[int | None, Field(description="Shift value for caesar cipher (1-25)")] = None,
    key: Annotated[str | None, Field(description="Key for vigenere, beaufort, autokey, columnar, xor, aes, or chacha20")] = None,
    a: Annotated[int | None, Field(description="Multiplier for affine cipher (must be coprime to 26)")] = None,
    b: Annotated[int | None, Field(description="Offset for affine cipher")] = None,
    rails: Annotated[int | None, Field(description="Number of rails for railfence cipher (≥2)")] = None,
    key_size: Annotated[int | None, Field(description="RSA key size in bits (default 2048)")] = None,
) -> str:
    """Decrypt text using any supported cipher. Pass the cipher name and only the parameters relevant to that cipher."""
    params: dict = {}
    if shift is not None:
        params["shift"] = shift
    if key is not None:
        params["key"] = key
    if a is not None:
        params["a"] = a
    if b is not None:
        params["b"] = b
    if rails is not None:
        params["rails"] = rails
    if key_size is not None:
        params["key_size"] = key_size
    return _decrypt(cipher.lower(), ciphertext, **params)


@mcp.tool()
def rsa_keygen(
    key_size: Annotated[int, Field(description="RSA key size in bits (default 2048)")] = 2048,
) -> str:
    """Generate a fresh RSA key pair. Returns public and private keys in PEM format. Resets the server's RSA state so subsequent encrypt/decrypt calls use this new key pair."""
    from cryptography.hazmat.primitives.asymmetric import rsa
    from cryptography.hazmat.primitives import serialization
    from cipher_tool.modern.asymmetric.rsa.model import RSACipher

    private_key = rsa.generate_private_key(
        public_exponent=65537,
        key_size=key_size,
    )
    public_key = private_key.public_key()

    RSACipher._shared_keys = {"private": private_key, "public": public_key}

    priv_pem = private_key.private_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PrivateFormat.PKCS8,
        encryption_algorithm=serialization.NoEncryption(),
    ).decode()

    pub_pem = public_key.public_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PublicFormat.SubjectPublicKeyInfo,
    ).decode()

    return (
        f"RSA {key_size}-bit key pair generated.\n\n"
        f"=== PUBLIC KEY ===\n{pub_pem}\n"
        f"=== PRIVATE KEY ===\n{priv_pem}\n"
        "Save the private key securely. "
        "The server will use this key pair for encrypt/decrypt until restarted or rsa_keygen is called again."
    )


@mcp.tool()
def list_ciphers() -> str:
    """List every supported cipher with its parameters and output format."""
    return (
        "Cipher Toolbox — Supported Ciphers\n"
        "===================================\n\n"
        "Classical / Substitution\n"
        "  caesar      shift: int              → uppercase text\n"
        "  atbash      (none)                  → uppercase text\n"
        "  affine      a: int, b: int          → uppercase text\n\n"
        "Classical / Polyalphabetic\n"
        "  vigenere    key: str                 → uppercase text\n"
        "  beaufort    key: str                 → uppercase text\n"
        "  autokey     key: str                 → uppercase text\n\n"
        "Classical / Transposition\n"
        "  railfence   rails: int               → text\n"
        "  columnar    key: str                 → text\n\n"
        "Modern / Symmetric\n"
        "  xor         key: str                 → hex string\n"
        "  aes         key: str (optional)      → base64\n"
        "  chacha20    key: str (optional)      → base64\n\n"
        "Modern / Asymmetric\n"
        "  rsa         key_size: int (default 2048) → base64\n"
    )


@mcp.tool()
def fetch_docs(
    topic: Annotated[str, Field(description="Topic: overview, installation, quickstart, caesar, atbash, affine, vigenere, beaufort, autokey, railfence, columnar, xor, aes, chacha20, rsa, or security")] = "overview",
) -> str:
    """Fetch documentation for a given topic from the Cipher Toolbox GitBook."""
    page_map = {
        "overview":     "",
        "installation": "getting-started/installation",
        "quickstart":   "getting-started/quick-start",
        "caesar":       "ciphers/classical/substitution/caesar-cipher",
        "atbash":       "ciphers/classical/substitution/atbash-cipher",
        "affine":       "ciphers/classical/substitution/affine-cipher",
        "vigenere":     "ciphers/classical/polyalphabetic/vigenere-cipher",
        "beaufort":     "ciphers/classical/polyalphabetic/beaufort-cipher",
        "autokey":      "ciphers/classical/polyalphabetic/autokey-cipher",
        "railfence":    "ciphers/classical/transposition/rail-fence-cipher",
        "columnar":     "ciphers/classical/transposition/columnar-transposition",
        "xor":          "ciphers/modern/symmetric/xor-cipher",
        "aes":          "ciphers/modern/symmetric/aes-cipher",
        "chacha20":     "ciphers/modern/symmetric/chacha20-cipher",
        "rsa":          "ciphers/modern/asymmetric/rsa-cipher",
        "security":     "security",
    }
    path = page_map.get(topic.lower(), "")
    url = f"{GITBOOK_BASE}/{path}".rstrip("/")
    try:
        urllib.request.urlopen(url, timeout=5)  # noqa: S310
        return f"Documentation for '{topic}': {url}\nVisit the link above for full details."
    except Exception as exc:
        return f"Documentation for '{topic}': {url}\n(Could not fetch page: {exc})"


# 
# PRIMITIVE 2 — Dynamic per-cipher resource template
# 

CIPHER_DOCS = {
    "caesar": (
        "# Caesar Cipher\n\n"
        "**Family:** Classical / Substitution\n\n"
        "Shifts each letter by a fixed number of positions in the alphabet.\n\n"
        "## Parameters\n- `shift` (int): Number of positions to shift (1-25)\n\n"
        "## Example\n```python\nencrypt('caesar', 'HELLO', shift=3)  # KHOOR\ndecrypt('caesar', 'KHOOR', shift=3)  # HELLO\n```\n\n"
        "## Security\n- Key space: 25\n- Trivially broken by brute force\n- Educational use only\n"
    ),
    "atbash": (
        "# Atbash Cipher\n\n"
        "**Family:** Classical / Substitution\n\n"
        "Reverses the alphabet: A\u2194Z, B\u2194Y, C\u2194X, etc. No key required.\n\n"
        "## Parameters\nNone\n\n"
        "## Example\n```python\nencrypt('atbash', 'HELLO')  # SVOOL\ndecrypt('atbash', 'SVOOL')  # HELLO\n```\n\n"
        "## Security\n- Key space: 1 (fixed mapping)\n- Instantly breakable\n- Educational use only\n"
    ),
    "affine": (
        "# Affine Cipher\n\n"
        "**Family:** Classical / Substitution\n\n"
        "Encrypts using E(x) = (a\u00b7x + b) mod 26. `a` must be coprime to 26.\n\n"
        "## Parameters\n- `a` (int): Multiplier, must be coprime to 26 (valid: 1,3,5,7,9,11,15,17,19,21,23,25)\n"
        "- `b` (int): Offset (0-25)\n\n"
        "## Example\n```python\nencrypt('affine', 'HELLO', a=5, b=8)  # RCLLA\ndecrypt('affine', 'RCLLA', a=5, b=8)  # HELLO\n```\n\n"
        "## Security\n- Key space: 312\n- Vulnerable to frequency analysis\n- Educational use only\n"
    ),
    "vigenere": (
        "# Vigenere Cipher\n\n"
        "**Family:** Classical / Polyalphabetic\n\n"
        "Uses a repeating keyword to shift each letter by a different amount.\n\n"
        "## Parameters\n- `key` (str): Keyword for encryption\n\n"
        "## Example\n```python\nencrypt('vigenere', 'HELLO WORLD', key='KEY')  # RIJVS UYVJN\ndecrypt('vigenere', 'RIJVS UYVJN', key='KEY')  # HELLO WORLD\n```\n\n"
        "## Security\n- Key space: variable (depends on key length)\n- Vulnerable to Kasiski examination and Friedman analysis\n- Educational use only\n"
    ),
    "beaufort": (
        "# Beaufort Cipher\n\n"
        "**Family:** Classical / Polyalphabetic\n\n"
        "Variant of Vigenere where the plaintext is subtracted from the key.\n"
        "Encryption and decryption are the same operation.\n\n"
        "## Parameters\n- `key` (str): Keyword for encryption\n\n"
        "## Example\n```python\nencrypt('beaufort', 'HELLO', key='KEY')\ndecrypt('beaufort', ct, key='KEY')  # HELLO\n```\n\n"
        "## Security\n- Same weaknesses as Vigenere\n- Educational use only\n"
    ),
    "autokey": (
        "# Autokey Cipher\n\n"
        "**Family:** Classical / Polyalphabetic\n\n"
        "Like Vigenere, but extends the key with the plaintext itself.\n\n"
        "## Parameters\n- `key` (str): Initial keyword\n\n"
        "## Example\n```python\nencrypt('autokey', 'HELLO', key='KEY')\ndecrypt('autokey', ct, key='KEY')  # HELLO\n```\n\n"
        "## Security\n- Stronger than Vigenere but still vulnerable to known-plaintext attacks\n- Educational use only\n"
    ),
    "railfence": (
        "# Rail Fence Cipher\n\n"
        "**Family:** Classical / Transposition\n\n"
        "Writes text in a zigzag pattern across N rails, then reads row by row.\n\n"
        "## Parameters\n- `rails` (int): Number of rails (>=2)\n\n"
        "## Example\n```python\nencrypt('railfence', 'HELLO WORLD', rails=3)\ndecrypt('railfence', ct, rails=3)  # HELLO WORLD\n```\n\n"
        "## Security\n- Key space: n-2 (tiny)\n- Trivially broken by trying all rail counts\n- Educational use only\n"
    ),
    "columnar": (
        "# Columnar Transposition\n\n"
        "**Family:** Classical / Transposition\n\n"
        "Arranges text in a grid and reads columns in keyword-sorted order.\n\n"
        "## Parameters\n- `key` (str): Keyword that determines column order\n\n"
        "## Example\n```python\nencrypt('columnar', 'HELLO WORLD', key='KEY')\ndecrypt('columnar', ct, key='KEY')\n```\n\n"
        "## Security\n- Key space: k! (factorial of key length)\n- Vulnerable to anagramming attacks\n- Educational use only\n"
    ),
    "xor": (
        "# XOR Cipher\n\n"
        "**Family:** Modern / Symmetric\n\n"
        "Byte-wise XOR with a repeating key. Output is a hex string.\n\n"
        "## Parameters\n- `key` (str): Key for XOR operation\n\n"
        "## Example\n```python\nencrypt('xor', 'HELLO', key='SECRET')  # hex string\ndecrypt('xor', hex_ct, key='SECRET')   # HELLO\n```\n\n"
        "## Security\n- Only secure with a truly random one-time key as long as the message\n- Repeating keys are trivially broken\n"
    ),
    "aes": (
        "# AES (Advanced Encryption Standard)\n\n"
        "**Family:** Modern / Symmetric\n\n"
        "256-bit block cipher using CBC mode with PKCS7 padding. Output is base64 (IV + ciphertext).\n\n"
        "## Parameters\n- `key` (str, optional): Password padded/truncated to 32 bytes. Uses default if omitted.\n\n"
        "## Example\n```python\nencrypt('aes', 'HELLO WORLD')              # base64 string\nencrypt('aes', 'HELLO WORLD', key='mykey')  # base64 string\n```\n\n"
        "## Security\n- Key space: 2^256\n- Cryptographically secure when used properly\n"
    ),
    "chacha20": (
        "# ChaCha20\n\n"
        "**Family:** Modern / Symmetric\n\n"
        "Stream cipher alternative to AES. Output is base64 (nonce + ciphertext).\n\n"
        "## Parameters\n- `key` (str, optional): Password padded/truncated to 32 bytes. Uses default if omitted.\n\n"
        "## Example\n```python\nencrypt('chacha20', 'HELLO WORLD')              # base64 string\nencrypt('chacha20', 'HELLO WORLD', key='mykey')  # base64 string\n```\n\n"
        "## Security\n- Key space: 2^256\n- Cryptographically secure, fast in software\n- Modern alternative to AES\n"
    ),
    "rsa": (
        "# RSA\n\n"
        "**Family:** Modern / Asymmetric\n\n"
        "Public-key encryption using OAEP padding with SHA-256. Output is base64.\n\n"
        "## Parameters\n- `key_size` (int, optional): Key size in bits (default 2048)\n\n"
        "## Example\n```python\nencrypt('rsa', 'HELLO')                    # base64 string\nencrypt('rsa', 'HELLO', key_size=4096)     # base64 string\n```\n\n"
        "## Security\n- Key space: 2^2048+\n- Cryptographically secure with >=2048-bit keys\n"
        "- Note: Key pair is generated per server session\n"
    ),
}


@mcp.resource("docs://cipher/{name}")
def resource_cipher(name: str) -> str:
    """Dynamic documentation for a specific cipher."""
    key = name.lower()
    if key in CIPHER_DOCS:
        return CIPHER_DOCS[key]
    available = ", ".join(sorted(CIPHER_DOCS.keys()))
    return f"# Unknown cipher: {name}\n\nAvailable ciphers: {available}\n"


# 
# PRIMITIVE 2 (continued) — Resources (6 total)
# 

@mcp.resource("docs://overview")
def resource_overview() -> str:
    """Project overview, cipher catalogue, and quick API example."""
    return (
        "# Cipher Toolbox — Overview\n\n"
        "An educational Python library covering 12 ciphers across four families:\n\n"
        "- **Classical / Substitution**: caesar, atbash, affine\n"
        "- **Classical / Polyalphabetic**: vigenere, beaufort, autokey\n"
        "- **Classical / Transposition**: railfence, columnar\n"
        "- **Modern / Symmetric**: xor, aes, chacha20\n"
        "- **Modern / Asymmetric**: rsa\n\n"
        "## Quick API Example\n\n"
        "```python\n"
        "from cipher_tool import encrypt, decrypt\n\n"
        "ct = encrypt('caesar', 'HELLO', shift=3)   # 'KHOOR'\n"
        "pt = decrypt('caesar', ct, shift=3)         # 'HELLO'\n"
        "```\n"
    )


@mcp.resource("docs://installation")
def resource_installation() -> str:
    """Installation instructions and Claude Desktop configuration."""
    return (
        "# Installation\n\n"
        "```bash\n"
        "pip install cipher-toolbox          # core library\n"
        "pip install cipher-toolbox[mcp]     # with MCP server\n"
        "```\n\n"
        "## Claude Desktop Configuration\n\n"
        "Add to `claude_desktop_config.json`:\n\n"
        "```json\n"
        '{\n'
        '  "mcpServers": {\n'
        '    "cipher-toolbox": {\n'
        '      "command": "cipher-mcp",\n'
        '      "args": ["--transport", "stdio"]\n'
        '    }\n'
        '  }\n'
        '}\n'
        "```\n"
    )


@mcp.resource("docs://classical-ciphers")
def resource_classical() -> str:
    """Reference for all 8 classical ciphers with code examples."""
    return (
        "# Classical Ciphers\n\n"
        "## Substitution\n\n"
        "### Caesar Cipher\n"
        "Shifts each letter by a fixed amount.\n"
        "```python\nencrypt('caesar', 'HELLO', shift=3)  # KHOOR\n```\n\n"
        "### Atbash Cipher\n"
        "Reverses the alphabet (A↔Z, B↔Y, …).\n"
        "```python\nencrypt('atbash', 'HELLO')  # SVOOL\n```\n\n"
        "### Affine Cipher\n"
        "Applies E(x) = (a·x + b) mod 26. *a* must be coprime with 26.\n"
        "```python\nencrypt('affine', 'HELLO', a=5, b=8)\n```\n\n"
        "## Polyalphabetic\n\n"
        "### Vigenère Cipher\n"
        "Uses a repeating keyword to shift each letter.\n"
        "```python\nencrypt('vigenere', 'HELLO', key='KEY')  # RIJVS\n```\n\n"
        "### Beaufort Cipher\n"
        "Like Vigenère but subtracts plaintext from key.\n"
        "```python\nencrypt('beaufort', 'HELLO', key='KEY')\n```\n\n"
        "### Autokey Cipher\n"
        "Extends the key with the plaintext itself.\n"
        "```python\nencrypt('autokey', 'HELLO', key='KEY')\n```\n\n"
        "## Transposition\n\n"
        "### Rail Fence Cipher\n"
        "Writes text in a zigzag across *n* rails, then reads row by row.\n"
        "```python\nencrypt('railfence', 'HELLO WORLD', rails=3)\n```\n\n"
        "### Columnar Transposition\n"
        "Arranges text in columns ordered by a keyword.\n"
        "```python\nencrypt('columnar', 'HELLO WORLD', key='KEY')\n```\n"
    )


@mcp.resource("docs://modern-ciphers")
def resource_modern() -> str:
    """Reference for modern ciphers: XOR, AES, ChaCha20, RSA."""
    return (
        "# Modern Ciphers\n\n"
        "## Symmetric\n\n"
        "### XOR Cipher\n"
        "Byte-wise XOR with a repeating key. Output is a hex string.\n"
        "```python\nencrypt('xor', 'HELLO', key='SECRET')\n```\n\n"
        "### AES (Advanced Encryption Standard)\n"
        "256-bit symmetric encryption. Output is base64. "
        "A random key is generated if none is provided.\n"
        "```python\nencrypt('aes', 'HELLO WORLD')\n```\n\n"
        "### ChaCha20\n"
        "Stream cipher alternative to AES. Output is base64.\n"
        "```python\nencrypt('chacha20', 'HELLO WORLD')\n```\n\n"
        "## Asymmetric\n\n"
        "### RSA\n"
        "Public-key encryption. Default key size is 2048 bits. Output is base64.\n"
        "```python\nencrypt('rsa', 'HELLO')\n```\n"
    )


@mcp.resource("docs://security")
def resource_security() -> str:
    """Security considerations and weakness table."""
    return (
        "# Security Considerations\n\n"
        "| Cipher     | Key Space       | Known Weakness              |\n"
        "|------------|-----------------|-----------------------------||\n"
        "| caesar     | 25              | Trivial brute-force         |\n"
        "| atbash     | 1               | Fixed mapping               |\n"
        "| affine     | 312             | Small key space             |\n"
        "| vigenere   | variable        | Kasiski / Friedman attacks  |\n"
        "| beaufort   | variable        | Same as Vigenère            |\n"
        "| autokey    | variable        | Known-plaintext attacks     |\n"
        "| railfence  | n-2             | Tiny key space              |\n"
        "| columnar   | k!              | Anagramming attacks         |\n"
        "| xor        | variable        | Repeating-key analysis      |\n"
        "| aes        | 2^256           | Secure (use ≥256-bit key)   |\n"
        "| chacha20   | 2^256           | Secure                      |\n"
        "| rsa        | 2^2048+         | Secure (use ≥2048-bit key)  |\n\n"
        "## What This Library Does NOT Provide\n\n"
        "- Authenticated encryption (no AEAD modes)\n"
        "- Secure key management or storage\n"
        "- Protection against side-channel attacks\n"
        "- Production-grade cryptographic guarantees\n"
    )


@mcp.resource("docs://parameters")
def resource_parameters() -> str:
    """Complete parameter and output format reference for every cipher."""
    return (
        "# Cipher Parameters Reference\n\n"
        "| Cipher    | Parameters              | Output Format   |\n"
        "|-----------|-------------------------|-----------------|\n"
        "| caesar    | shift: int              | uppercase text  |\n"
        "| atbash    | (none)                  | uppercase text  |\n"
        "| affine    | a: int, b: int          | uppercase text  |\n"
        "| vigenere  | key: str                | uppercase text  |\n"
        "| beaufort  | key: str                | uppercase text  |\n"
        "| autokey   | key: str                | uppercase text  |\n"
        "| railfence | rails: int              | text            |\n"
        "| columnar  | key: str                | text            |\n"
        "| xor       | key: str                | hex string      |\n"
        "| aes       | key: str (optional)     | base64          |\n"
        "| chacha20  | key: str (optional)     | base64          |\n"
        "| rsa       | key_size: int (def 2048)| base64          |\n"
    )


# 
# PRIMITIVE 3 — Prompts (8 total)
# 

@mcp.prompt(name="encrypt-message")
def prompt_encrypt_message(
    plaintext: str, cipher: str = "caesar", key_or_params: str = ""
) -> list[Message]:
    """Encrypt a message, explain the transformation, and verify round-trip."""
    return [Message(role="user", content=(
        f"Encrypt the following plaintext using the **{cipher}** cipher.\n\n"
        f"Plaintext: `{plaintext}`\n"
        f"Key / Parameters: `{key_or_params or '(defaults)'}`\n\n"
        "Steps:\n"
        f"1. Call the `encrypt_text` tool with cipher='{cipher}' and the given parameters.\n"
        "2. Show the resulting ciphertext.\n"
        "3. Explain how the cipher transformed the plaintext.\n"
        f"4. Call `decrypt_text` on the ciphertext to verify round-trip recovery.\n"
        "5. Confirm the original plaintext is recovered."
    ))]


@mcp.prompt(name="decrypt-message")
def prompt_decrypt_message(
    ciphertext: str, cipher: str = "caesar", key_or_params: str = ""
) -> list[Message]:
    """Decrypt a message and explain the reversal algorithm."""
    return [Message(role="user", content=(
        f"Decrypt the following ciphertext using the **{cipher}** cipher.\n\n"
        f"Ciphertext: `{ciphertext}`\n"
        f"Key / Parameters: `{key_or_params or '(defaults)'}`\n\n"
        "Steps:\n"
        f"1. Call the `decrypt_text` tool with cipher='{cipher}' and the given parameters.\n"
        "2. Show the recovered plaintext.\n"
        "3. Explain how the decryption algorithm reverses the encryption."
    ))]


@mcp.prompt(name="explain-cipher")
def prompt_explain_cipher(cipher: str) -> list[Message]:
    """Deep-dive explanation of a cipher."""
    return [Message(role="user", content=(
        f"Give a comprehensive explanation of the **{cipher}** cipher.\n\n"
        "Cover the following:\n"
        "1. **History** — who invented it and when.\n"
        "2. **Algorithm** — step-by-step encryption and decryption process.\n"
        "3. **Worked example** — encrypt a short sample by hand.\n"
        "4. **Strengths** — what it does well.\n"
        "5. **Weaknesses** — known attacks and limitations.\n"
        "6. **Modern verdict** — is it safe for real-world use today?"
    ))]


@mcp.prompt(name="compare-ciphers")
def prompt_compare_ciphers(
    cipher_a: str, cipher_b: str, sample_text: str = "HELLO WORLD"
) -> list[Message]:
    """Side-by-side comparison of two ciphers."""
    return [Message(role="user", content=(
        f"Compare **{cipher_a}** and **{cipher_b}** using the sample text "
        f"`{sample_text}`.\n\n"
        "Steps:\n"
        f"1. Encrypt the sample with `encrypt_text` using cipher='{cipher_a}' (use sensible defaults).\n"
        f"2. Encrypt the sample with `encrypt_text` using cipher='{cipher_b}' (use sensible defaults).\n"
        "3. Show both ciphertexts side by side.\n"
        "4. Build a comparison table covering: key type, key space, speed, "
        "security level, and best use case.\n"
        "5. Give a recommendation on which to prefer and why."
    ))]


@mcp.prompt(name="brute-force-caesar")
def prompt_brute_force_caesar(ciphertext: str) -> list[Message]:
    """Brute-force all 25 Caesar shifts to find the plaintext."""
    return [Message(role="user", content=(
        f"Brute-force the following Caesar ciphertext: `{ciphertext}`\n\n"
        "Steps:\n"
        "1. For each shift from 1 to 25, call `decrypt_text` with cipher='caesar' and that shift.\n"
        "2. Display all 25 results in a numbered list.\n"
        "3. Identify which shift produces readable English.\n"
        "4. Explain why Caesar cipher is vulnerable to brute-force attacks."
    ))]


@mcp.prompt(name="cipher-security-audit")
def prompt_cipher_security_audit(cipher: str) -> list[Message]:
    """Structured security audit report for a cipher."""
    return [Message(role="user", content=(
        f"Perform a security audit of the **{cipher}** cipher.\n\n"
        "Produce a structured report with these sections:\n"
        "1. **Classification** — family, type, era.\n"
        "2. **Key space** — total number of possible keys.\n"
        "3. **Known attacks** — list each attack with complexity.\n"
        "4. **Verdict** — safe / unsafe for production use.\n"
        "5. **Alternatives** — recommend stronger replacements."
    ))]


@mcp.prompt(name="encrypt-and-store-workflow")
def prompt_encrypt_and_store_workflow(
    plaintext: str, cipher: str = "aes", key: str = ""
) -> list[Message]:
    """Full encrypt → store → decrypt walkthrough with key management guidance."""
    return [Message(role="user", content=(
        f"Walk me through a complete encrypt-store-decrypt workflow.\n\n"
        f"Plaintext: `{plaintext}`\n"
        f"Cipher: **{cipher}**\n"
        f"Key: `{key or '(auto-generate)'}`\n\n"
        "Steps:\n"
        f"1. Call `encrypt_text` with cipher='{cipher}' to encrypt the plaintext.\n"
        "2. Show the ciphertext and explain its format (hex / base64).\n"
        "3. Explain how to securely store the ciphertext and the key separately.\n"
        f"4. Call `decrypt_text` with cipher='{cipher}' to recover the plaintext.\n"
        "5. Confirm round-trip success.\n"
        "6. Provide key management best practices (rotation, storage, access control)."
    ))]


@mcp.prompt(name="cipher-quiz")
def prompt_cipher_quiz(
    difficulty: str = "medium", topic: str = "all"
) -> list[Message]:
    """Generate a 5-question scored cipher quiz."""
    return [Message(role="user", content=(
        f"Generate a **{difficulty}**-difficulty quiz about "
        f"{'all ciphers' if topic == 'all' else 'the ' + topic + ' cipher'}.\n\n"
        "Rules:\n"
        "1. Ask exactly 5 questions, one at a time.\n"
        "2. Wait for the user's answer before proceeding.\n"
        "3. Use the `encrypt_text` and `decrypt_text` tools to "
        "validate answers where applicable.\n"
        "4. After all 5 questions, show the final score out of 5.\n"
        "5. Provide brief explanations for any incorrect answers."
    ))]


# 
# Entry point
# 

def cli_main() -> None:
    """Console-script entry point registered as `cipher-mcp`."""
    parser = argparse.ArgumentParser(
        prog="cipher-toolbox-mcp",
        description="Cipher Toolbox MCP Server — Tools, Resources, and Prompts.",
    )
    parser.add_argument(
        "--transport", choices=["stdio", "http"], default="stdio",
        help="Transport mode (default: stdio)",
    )
    parser.add_argument("--host", default="0.0.0.0")
    parser.add_argument("--port", type=int, default=8000)
    args = parser.parse_args()

    if args.transport == "stdio":
        mcp.run(transport="stdio")
    else:
        mcp.run(transport="http", host=args.host, port=args.port)


if __name__ == "__main__":
    cli_main()
