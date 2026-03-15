# Cipher Toolbox

A comprehensive educational cipher toolbox for encryption and decryption, featuring both classical and modern cryptographic algorithms — now with a built-in **MCP (Model Context Protocol) server** for AI assistant integration.

[![PyPI version](https://badge.fury.io/py/cipher-toolbox.svg)](https://badge.fury.io/py/cipher-toolbox)
[![Python 3.9+](https://img.shields.io/badge/python-3.9+-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![CI](https://github.com/Gabriel-Dakinah-Vincent/cipher-toolbox/workflows/CI/badge.svg)](https://github.com/Gabriel-Dakinah-Vincent/cipher-toolbox/actions)
[![MCP](https://img.shields.io/badge/MCP-Compatible-green.svg)](https://modelcontextprotocol.io)

## 🚀 Quick Start

```bash
# Install from PyPI
pip install cipher-toolbox

# List available ciphers
cipher-tool list

# Encrypt with Caesar cipher
cipher-tool encrypt caesar "HELLO WORLD" --shift 3
# Output: KHOOR ZRUOG

# Decrypt with Caesar cipher
cipher-tool decrypt caesar "KHOOR ZRUOG" --shift 3
# Output: HELLO WORLD
```

## 📚 Features

### Classical Ciphers

**Substitution Ciphers:**
- **Caesar Cipher**: Simple shift cipher
- **Atbash Cipher**: Alphabet reversal cipher
- **Affine Cipher**: Mathematical substitution cipher

**Polyalphabetic Ciphers:**
- **Vigenère Cipher**: Keyword-based polyalphabetic substitution
- **Autokey Cipher**: Uses plaintext as part of the key
- **Beaufort Cipher**: Variant of Vigenère cipher

**Transposition Ciphers:**
- **Rail Fence Cipher**: Zigzag pattern transposition
- **Columnar Transposition**: Column-based rearrangement

### Modern Ciphers

**Symmetric Ciphers:**
- **XOR Cipher**: Simple bitwise XOR encryption
- **AES**: Advanced Encryption Standard (256-bit)
- **ChaCha20**: Modern stream cipher

**Asymmetric Ciphers:**
- **RSA**: Public-key cryptography

## 🛠 Installation

### From PyPI (Recommended)

```bash
# Core library only
pip install cipher-toolbox

# With MCP server support (for Claude Desktop / AI assistants)
pip install cipher-toolbox[mcp]

# Everything — dev tools + MCP (for contributors)
pip install cipher-toolbox[all]
```

### From Source

```bash
git clone https://github.com/Gabriel-Dakinah-Vincent/cipher-toolbox.git
cd cipher-toolbox
pip install -e .
```

### With MCP Server (From Source)

```bash
git clone https://github.com/Gabriel-Dakinah-Vincent/cipher-toolbox.git
cd cipher-toolbox
pip install -e .[mcp]
```

### Development Installation

```bash
git clone https://github.com/Gabriel-Dakinah-Vincent/cipher-toolbox.git
cd cipher-toolbox
pip install -e .[dev]
```

## 💻 Command Line Interface

### Basic Commands

```bash
# List all available ciphers
cipher-tool list

# Get help
cipher-tool --help
cipher-tool encrypt --help
cipher-tool decrypt --help
```

### Classical Substitution Ciphers

#### Caesar Cipher
```bash
# Encrypt
cipher-tool encrypt caesar "HELLO WORLD" --shift 3
# Output: KHOOR ZRUOG

# Decrypt
cipher-tool decrypt caesar "KHOOR ZRUOG" --shift 3
# Output: HELLO WORLD

# Different shift values
cipher-tool encrypt caesar "ATTACK AT DAWN" --shift 13
# Output: NGGNPX NG QNJA
```

#### Atbash Cipher
```bash
# Encrypt (A->Z, B->Y, etc.)
cipher-tool encrypt atbash "HELLO WORLD"
# Output: SVOOL DLIOW

# Decrypt (same operation)
cipher-tool decrypt atbash "SVOOL DLIOW"
# Output: HELLO WORLD
```

#### Affine Cipher
```bash
# Encrypt with parameters a=5, b=8
cipher-tool encrypt affine "HELLO" --a 5 --b 8
# Output: RCLLA

# Decrypt with same parameters
cipher-tool decrypt affine "RCLLA" --a 5 --b 8
# Output: HELLO

# Different parameters
cipher-tool encrypt affine "CRYPTOGRAPHY" --a 7 --b 3
```

### Classical Polyalphabetic Ciphers

#### Vigenère Cipher
```bash
# Encrypt with keyword
cipher-tool encrypt vigenere "HELLO WORLD" --key "SECRET"
# Output: ZINCS KCVNH

# Decrypt with same keyword
cipher-tool decrypt vigenere "ZINCS KCVNH" --key "SECRET"
# Output: HELLO WORLD

# Longer messages
cipher-tool encrypt vigenere "ATTACK AT DAWN" --key "LEMON"
# Output: LXFOPV EF RNHR
```

#### Autokey Cipher
```bash
# Encrypt (key extends with plaintext)
cipher-tool encrypt autokey "HELLO" --key "KEY"
# Output: RIJSS

# Decrypt
cipher-tool decrypt autokey "RIJSS" --key "KEY"
# Output: HELLO

# Longer key
cipher-tool encrypt autokey "CRYPTOGRAPHY" --key "SECRET"
```

#### Beaufort Cipher
```bash
# Encrypt
cipher-tool encrypt beaufort "HELLO" --key "KEY"
# Output: DANZQ

# Decrypt (same operation)
cipher-tool decrypt beaufort "DANZQ" --key "KEY"
# Output: HELLO
```

### Classical Transposition Ciphers

#### Rail Fence Cipher
```bash
# Encrypt with 3 rails
cipher-tool encrypt railfence "HELLO WORLD" --rails 3
# Output: HOREL OLLWD

# Decrypt with same rail count
cipher-tool decrypt railfence "HOREL OLLWD" --rails 3
# Output: HELLO WORLD

# Different rail counts
cipher-tool encrypt railfence "WE ARE DISCOVERED FLEE AT ONCE" --rails 4
# Output: WECRLTEERDSOEEFEAOCAIVDEN
```

#### Columnar Transposition
```bash
# Encrypt with keyword
cipher-tool encrypt columnar "HELLO WORLD" --key "KEY"
# Output: EHLOLWLORD

# Decrypt with same keyword
cipher-tool decrypt columnar "EHLOLWLORD" --key "KEY"
# Output: HELLOWORLDX (padded with X)

# Longer messages
cipher-tool encrypt columnar "ATTACK AT DAWN" --key "ZEBRA"
```

### Modern Symmetric Ciphers

#### XOR Cipher
```bash
# Encrypt (returns hex)
cipher-tool encrypt xor "HELLO" --key "SECRET"
# Output: 1b0a001a1c

# Decrypt from hex
cipher-tool decrypt xor "1b0a001a1c" --key "SECRET"
# Output: HELLO

# Longer messages
cipher-tool encrypt xor "This is a secret message" --key "PASSWORD"
```

#### AES Cipher
```bash
# Encrypt (returns base64)
cipher-tool encrypt aes "Hello World" --key "mypassword"
# Output: base64-encoded-string

# Decrypt from base64
cipher-tool decrypt aes "base64-string" --key "mypassword"
# Output: Hello World

# Secure messages
cipher-tool encrypt aes "Sensitive data here" --key "supersecretkey123"
```

#### ChaCha20 Cipher
```bash
# Encrypt (returns base64)
cipher-tool encrypt chacha20 "Hello World" --key "mypassword"
# Output: base64-encoded-string

# Decrypt from base64
cipher-tool decrypt chacha20 "base64-string" --key "mypassword"
# Output: Hello World
```

### Modern Asymmetric Ciphers

#### RSA Cipher
```bash
# Encrypt with default 2048-bit key
cipher-tool encrypt rsa "HELLO"
# Output: base64-encoded-string

# Decrypt (uses same key pair)
cipher-tool decrypt rsa "base64-string"
# Output: HELLO

# Different key sizes
cipher-tool encrypt rsa "TEST" --key-size 1024
cipher-tool encrypt rsa "MESSAGE" --key-size 4096
```

## 🐍 Python API

### Basic Usage

```python
from cipher_tool import encrypt, decrypt

# Caesar cipher
ciphertext = encrypt("caesar", "HELLO WORLD", shift=3)
print(ciphertext)  # KHOOR ZRUOG

plaintext = decrypt("caesar", ciphertext, shift=3)
print(plaintext)   # HELLO WORLD
```

### Classical Ciphers Examples

```python
from cipher_tool import encrypt, decrypt

# Substitution ciphers
result = encrypt("atbash", "HELLO")
print(result)  # SVOOL

result = encrypt("affine", "HELLO", a=5, b=8)
print(result)  # RCLLA

# Polyalphabetic ciphers
result = encrypt("vigenere", "HELLO WORLD", key="SECRET")
print(result)  # ZINCS KCVNH

result = encrypt("autokey", "HELLO", key="KEY")
print(result)  # RIJSS

# Transposition ciphers
result = encrypt("railfence", "HELLO WORLD", rails=3)
print(result)  # HOREL OLLWD

result = encrypt("columnar", "HELLO WORLD", key="KEY")
print(result)  # EHLOLWLORD
```

### Modern Ciphers Examples

```python
from cipher_tool import encrypt, decrypt

# Symmetric ciphers
result = encrypt("xor", "HELLO", key="SECRET")
print(result)  # 1b0a001a1c (hex)

result = encrypt("aes", "Hello World", key="mypassword")
print(result)  # base64-encoded string

result = encrypt("chacha20", "Hello World", key="mypassword")
print(result)  # base64-encoded string

# Asymmetric cipher
result = encrypt("rsa", "HELLO", key_size=2048)
print(result)  # base64-encoded string
```

### Error Handling

```python
from cipher_tool import encrypt, decrypt

try:
    # Invalid cipher name
    result = encrypt("invalid_cipher", "test")
except ValueError as e:
    print(f"Error: {e}")  # Error: Unsupported cipher: invalid_cipher

try:
    # Invalid parameters for Affine cipher
    result = encrypt("affine", "test", a=2, b=3)  # a=2 is not coprime to 26
except ValueError as e:
    print(f"Error: {e}")  # Error: 'a' must be coprime to 26
```

### Batch Processing

```python
from cipher_tool import encrypt, decrypt

# Process multiple messages
messages = ["HELLO", "WORLD", "CIPHER", "TOOLBOX"]
key = "SECRET"

# Encrypt all messages
encrypted = [encrypt("vigenere", msg, key=key) for msg in messages]
print(encrypted)  # ['ZINCS', 'KCVNH', 'KBDPEV', 'MCRQFCZ']

# Decrypt all messages
decrypted = [decrypt("vigenere", msg, key=key) for msg in encrypted]
print(decrypted)  # ['HELLO', 'WORLD', 'CIPHER', 'TOOLBOX']
```

## 📖 Cipher Parameters Reference

| Cipher | Parameters | Type | Description | Example |
|--------|------------|------|-------------|----------|
| caesar | `shift` | int | Number of positions to shift (0-25) | `shift=3` |
| atbash | None | - | No parameters needed | - |
| affine | `a`, `b` | int | `a` must be coprime to 26, `b` is offset | `a=5, b=8` |
| vigenere | `key` | str | Keyword for encryption | `key="SECRET"` |
| autokey | `key` | str | Initial key (extends with plaintext) | `key="KEY"` |
| beaufort | `key` | str | Keyword for encryption | `key="KEY"` |
| railfence | `rails` | int | Number of rails (≥2) | `rails=3` |
| columnar | `key` | str | Keyword for column ordering | `key="KEY"` |
| xor | `key` | str | Key for XOR operation | `key="SECRET"` |
| aes | `key` | str | Password (truncated/padded to 32 bytes) | `key="password"` |
| chacha20 | `key` | str | Password (truncated/padded to 32 bytes) | `key="password"` |
| rsa | `key_size` | int | Key size in bits (1024, 2048, 4096) | `key_size=2048` |

## 🎓 Educational Use Cases

### Cryptography Learning

```python
# Compare different cipher strengths
plaintext = "ATTACK AT DAWN"

# Classical ciphers (easily breakable)
caesar_result = encrypt("caesar", plaintext, shift=3)
print(f"Caesar: {caesar_result}")  # Frequency analysis vulnerable

vigenere_result = encrypt("vigenere", plaintext, key="SHORT")
print(f"Vigenère: {vigenere_result}")  # Stronger but still breakable

# Modern ciphers (cryptographically secure)
aes_result = encrypt("aes", plaintext, key="strongpassword")
print(f"AES: {aes_result}")  # Cryptographically secure
```

### Historical Cipher Analysis

```python
# Demonstrate Caesar cipher weakness
for shift in range(26):
    result = decrypt("caesar", "KHOOR ZRUOG", shift=shift)
    print(f"Shift {shift:2d}: {result}")
    # Only shift=3 produces meaningful text: "HELLO WORLD"
```

### Security Demonstrations

```python
# Show why short keys are weak in Vigenère
plaintext = "THE QUICK BROWN FOX JUMPS OVER THE LAZY DOG" * 3

# Short key (vulnerable to frequency analysis)
weak = encrypt("vigenere", plaintext, key="KEY")
print(f"Short key result: {weak[:50]}...")

# Long key (stronger)
strong = encrypt("vigenere", plaintext, key="VERYLONGKEYWORD")
print(f"Long key result: {strong[:50]}...")
```

## 🔒 Security Best Practices

### ⚠️ Important Security Notice

**This implementation is for educational purposes only.** Do not use these implementations for securing sensitive data in production environments. Use well-tested, production-ready cryptographic libraries instead.

### Classical Ciphers

- **Caesar Cipher**: Extremely weak, only 25 possible keys
- **Atbash Cipher**: No key, easily recognizable pattern
- **Affine Cipher**: Limited keyspace, vulnerable to frequency analysis
- **Vigenère Cipher**: Vulnerable to Kasiski examination and frequency analysis
- **Transposition Ciphers**: Preserve letter frequencies, vulnerable to analysis

### Modern Ciphers

- **XOR Cipher**: Only secure with truly random, one-time keys
- **AES**: Cryptographically secure when used properly
- **ChaCha20**: Modern, secure stream cipher
- **RSA**: Secure for small messages, use OAEP padding in production

### Recommendations

```python
# ❌ DON'T use for production security
password = encrypt("caesar", "mypassword", shift=3)

# ✅ DO use for education and learning
demonstration = encrypt("caesar", "EXAMPLE", shift=3)
print(f"Educational example: {demonstration}")

# ✅ DO use proper libraries for production
# from cryptography.fernet import Fernet  # Use this instead
```

## 🤖 MCP Server — AI Assistant Integration

Cipher Toolbox includes a built-in **Model Context Protocol (MCP)** server that lets AI assistants like Claude use all 12 ciphers as tools. The MCP server exposes all three MCP primitives: **Tools**, **Resources**, and **Prompts**.

### What is MCP?

The [Model Context Protocol](https://modelcontextprotocol.io) is an open standard that lets AI assistants connect to external tools and data sources. With the Cipher Toolbox MCP server, Claude can encrypt, decrypt, explain ciphers, and run guided cryptography workflows — all directly in your conversation.

### Step 1 — Install with MCP Support

```bash
pip install cipher-toolbox[mcp]
```

This installs the core library plus [FastMCP](https://github.com/jlowin/fastmcp), which powers the MCP server.

### Step 2 — Verify the Installation

```bash
# Check that the cipher-toolbox-mcp command is available
cipher-toolbox-mcp --help
```

You should see:

```
usage: cipher-toolbox-mcp [-h] [--transport {stdio,http}] [--host HOST] [--port PORT]

Cipher Toolbox MCP Server — Tools, Resources, and Prompts.

options:
  -h, --help            show this help message and exit
  --transport {stdio,http}
                        Transport mode (default: stdio)
  --host HOST
  --port PORT
```

### Step 3 — Configure Claude Desktop

Locate your Claude Desktop configuration file:

| OS | Path |
|----|------|
| **Windows** | `%APPDATA%\Claude\claude_desktop_config.json` |
| **macOS** | `~/Library/Application Support/Claude/claude_desktop_config.json` |
| **Linux** | `~/.config/Claude/claude_desktop_config.json` |

Open the file (create it if it doesn't exist) and add the `cipher-toolbox` MCP server:

#### Option A — Using the cipher-toolbox-mcp executable (recommended)

First, find the full path:

```bash
# Windows
where cipher-toolbox-mcp

# macOS / Linux
which cipher-toolbox-mcp
```

Then add it to your config:

```json
{
  "mcpServers": {
    "cipher-toolbox": {
      "command": "C:\\Users\\YOUR_USERNAME\\AppData\\Local\\Programs\\Python\\Python313\\Scripts\\cipher-toolbox-mcp.exe",
      "args": ["--transport", "stdio"]
    }
  }
}
```

> **Replace** the `command` path with the actual output from `where cipher-toolbox-mcp` / `which cipher-toolbox-mcp`.

#### Option B — Using Python directly

If Option A doesn't work, point directly to your Python interpreter:

```json
{
  "mcpServers": {
    "cipher-toolbox": {
      "command": "C:\\Users\\YOUR_USERNAME\\AppData\\Local\\Programs\\Python\\Python313\\python.exe",
      "args": ["-m", "cipher_tool.mcp_server.server", "--transport", "stdio"]
    }
  }
}
```

> **Important:** Make sure `cipher-toolbox[mcp]` is installed in the same Python environment you reference here.

#### If you already have other MCP servers

Just add `"cipher-toolbox"` inside your existing `mcpServers` object — don't overwrite the others:

```json
{
  "mcpServers": {
    "some-other-server": { "..." : "..." },
    "cipher-toolbox": {
      "command": "/path/to/cipher-toolbox-mcp",
      "args": ["--transport", "stdio"]
    }
  }
}
```

### Step 4 — Restart Claude Desktop

You must fully quit and reopen Claude Desktop for the config to take effect.

```powershell
# Windows — kill from PowerShell then reopen
Get-Process *claude* | Stop-Process -Force
```

On macOS: **Claude → Quit Claude** (or `Cmd+Q`), then reopen.

### Step 5 — Verify the Connection

Once Claude Desktop reopens:

1. Look for the **tools icon** (🔨 hammer) in the chat input area
2. Click it — you should see the Cipher Toolbox tools listed
3. Try a test prompt: **"Encrypt HELLO WORLD using Caesar cipher with shift 3"**

If Claude responds with `KHOOR ZRUOG`, everything is working!

---

### 📋 MCP Primitives Reference

The MCP server exposes **three types of primitives**:

#### Primitive 1 — Tools (26 total)

Tools are functions Claude can call directly. Every cipher has an encrypt and decrypt tool.

**Classical / Substitution (6 tools)**

| Tool | What it does | Parameters |
|------|-------------|------------|
| `caesar_encrypt` | Encrypt with Caesar cipher | `text`, `shift` |
| `caesar_decrypt` | Decrypt with Caesar cipher | `ciphertext`, `shift` |
| `atbash_encrypt` | Encrypt with Atbash cipher | `text` |
| `atbash_decrypt` | Decrypt with Atbash cipher | `ciphertext` |
| `affine_encrypt` | Encrypt with Affine cipher | `text`, `a`, `b` |
| `affine_decrypt` | Decrypt with Affine cipher | `ciphertext`, `a`, `b` |

**Classical / Polyalphabetic (6 tools)**

| Tool | What it does | Parameters |
|------|-------------|------------|
| `vigenere_encrypt` | Encrypt with Vigenère cipher | `text`, `key` |
| `vigenere_decrypt` | Decrypt with Vigenère cipher | `ciphertext`, `key` |
| `beaufort_encrypt` | Encrypt with Beaufort cipher | `text`, `key` |
| `beaufort_decrypt` | Decrypt with Beaufort cipher | `ciphertext`, `key` |
| `autokey_encrypt` | Encrypt with Autokey cipher | `text`, `key` |
| `autokey_decrypt` | Decrypt with Autokey cipher | `ciphertext`, `key` |

**Classical / Transposition (4 tools)**

| Tool | What it does | Parameters |
|------|-------------|------------|
| `railfence_encrypt` | Encrypt with Rail Fence cipher | `text`, `rails` |
| `railfence_decrypt` | Decrypt with Rail Fence cipher | `ciphertext`, `rails` |
| `columnar_encrypt` | Encrypt with Columnar Transposition | `text`, `key` |
| `columnar_decrypt` | Decrypt with Columnar Transposition | `ciphertext`, `key` |

**Modern / Symmetric (6 tools)**

| Tool | What it does | Parameters | Output |
|------|-------------|------------|--------|
| `xor_encrypt` | Encrypt with XOR | `text`, `key` | hex string |
| `xor_decrypt` | Decrypt with XOR | `ciphertext`, `key` | plain text |
| `aes_encrypt` | Encrypt with AES-256 | `text`, `key` (optional) | base64 |
| `aes_decrypt` | Decrypt with AES-256 | `ciphertext`, `key` (optional) | plain text |
| `chacha20_encrypt` | Encrypt with ChaCha20 | `text`, `key` (optional) | base64 |
| `chacha20_decrypt` | Decrypt with ChaCha20 | `ciphertext`, `key` (optional) | plain text |

**Modern / Asymmetric (2 tools)**

| Tool | What it does | Parameters | Output |
|------|-------------|------------|--------|
| `rsa_encrypt` | Encrypt with RSA | `text`, `key_size` (default 2048) | base64 |
| `rsa_decrypt` | Decrypt with RSA | `ciphertext`, `key_size` (default 2048) | plain text |

**Utility (2 tools)**

| Tool | What it does | Parameters |
|------|-------------|------------|
| `list_ciphers` | List all supported ciphers with parameters | (none) |
| `fetch_docs` | Fetch documentation for a topic | `topic` (default: "overview") |

#### Primitive 2 — Resources (6 total)

Resources are read-only reference documents Claude can access via `docs://` URIs.

| URI | Content |
|-----|--------|
| `docs://overview` | Project summary, cipher catalogue, quick API example |
| `docs://installation` | pip install steps, Claude Desktop JSON config |
| `docs://classical-ciphers` | All 8 classical ciphers with code examples |
| `docs://modern-ciphers` | XOR, AES, ChaCha20, RSA — formats and key handling |
| `docs://security` | Weakness table, what the library doesn't provide |
| `docs://parameters` | Table of every cipher's parameters and output format |

#### Primitive 3 — Prompts (8 total)

Prompts are guided workflow templates. In Claude Desktop, you can access them from the **prompt selector** (slash `/` or 📎 icon).

| Prompt | Parameters | What it does |
|--------|-----------|-------------|
| `encrypt-message` | `plaintext`, `cipher`, `key_or_params` | Encrypt text, explain the transformation, verify round-trip |
| `decrypt-message` | `ciphertext`, `cipher`, `key_or_params` | Decrypt text, explain the reversal algorithm |
| `explain-cipher` | `cipher` | History, algorithm, worked example, strengths, weaknesses |
| `compare-ciphers` | `cipher_a`, `cipher_b`, `sample_text` | Encrypt with both, comparison table, recommendation |
| `brute-force-caesar` | `ciphertext` | Try all 25 shifts, identify readable result, explain weakness |
| `cipher-security-audit` | `cipher` | Classification, key space, known attacks, verdict, alternatives |
| `encrypt-and-store-workflow` | `plaintext`, `cipher`, `key` | Full encrypt→store→decrypt walkthrough with key management |
| `cipher-quiz` | `difficulty`, `topic` | 5 scored questions, validated with cipher tools |

---

### 💬 Example Prompts for Claude Desktop

Once the MCP server is connected, try these prompts in Claude Desktop:

#### Basic Encryption & Decryption

```
Encrypt "HELLO WORLD" using Caesar cipher with shift 3
```

```
Decrypt "KHOOR ZRUOG" using Caesar cipher with shift 3
```

```
Encrypt "SECRET MESSAGE" with AES
```

```
Encrypt "HELLO" with Vigenere cipher using key "KEY"
```

```
Encrypt "HELLO" using Atbash cipher
```

```
Encrypt "HELLO" with Affine cipher using a=5 and b=8
```

```
Encrypt "HELLO WORLD" with Rail Fence cipher using 3 rails
```

```
Encrypt "HELLO" with XOR cipher using key "SECRET"
```

```
Encrypt "HELLO" with RSA
```

```
List all available ciphers
```

```
Fetch the documentation for the Caesar cipher
```

#### Using Resources

```
Read the overview documentation
```

```
Show me the installation guide
```

```
What classical ciphers are available?
```

```
Show me the security considerations for all ciphers
```

```
What parameters does each cipher need?
```

#### Using Prompt Templates

These trigger the built-in guided workflows:

```
Use the brute-force-caesar prompt with ciphertext "KHOOR"
```

```
Use the explain-cipher prompt for "vigenere"
```

```
Use the compare-ciphers prompt to compare caesar and aes
```

```
Give me a medium difficulty cipher quiz
```

```
Do a security audit of the Caesar cipher
```

```
Walk me through encrypting and storing a secret with AES
```

#### Fun Combo Prompts

```
Encrypt "ATTACK AT DAWN" with Caesar shift 7, then show me all 25 brute force attempts to crack it
```

```
Encrypt the same message with Caesar, Vigenere, and AES — then compare the results
```

```
Is the Atbash cipher secure? Do a full security audit
```

```
Create a spy scenario: encrypt a secret message with Vigenere, then try to break it
```

```
Show me the difference between classical and modern encryption by encrypting "TOP SECRET" with every available cipher
```

---

### 🔧 Running the MCP Server Manually

#### stdio mode (default — for Claude Desktop)

```bash
cipher-toolbox-mcp
# or explicitly:
cipher-toolbox-mcp --transport stdio
```

#### HTTP mode (for web-based MCP clients)

```bash
cipher-toolbox-mcp --transport http --host 0.0.0.0 --port 8000
```

#### As a Python module

```bash
python -m cipher_tool.mcp_server.server --transport stdio
```

---

### 🐛 MCP Troubleshooting

#### "cipher-toolbox-mcp" is not recognized

Make sure you installed with the `[mcp]` extra:

```bash
pip install cipher-toolbox[mcp]
```

Then verify:

```bash
# Windows
where cipher-toolbox-mcp

# macOS / Linux
which cipher-toolbox-mcp
```

#### Claude Desktop doesn't show the tools

1. **Check the config path** — make sure `claude_desktop_config.json` is a file, not a directory
2. **Check the command path** — run the exact `command` from your config in a terminal to see if it errors
3. **Check the logs** — Claude Desktop logs are at:
   - Windows: `%APPDATA%\Claude\logs\mcp*.log`
   - macOS: `~/Library/Logs/Claude/mcp*.log`
4. **Restart fully** — make sure Claude Desktop is completely quit (check system tray on Windows)

#### ImportError: fastmcp not found

The MCP server requires `fastmcp`. Make sure it's installed in the **same Python environment** that Claude Desktop uses:

```bash
# Check which Python Claude Desktop will use
python -c "import fastmcp; print(fastmcp.__version__)"
```

If you have multiple Python versions, install in the correct one:

```bash
# Example for Python 3.13 on Windows
py -3.13 -m pip install cipher-toolbox[mcp]
```

#### Server starts but Claude can't connect

Try the alternative config using Python directly:

```json
{
  "mcpServers": {
    "cipher-toolbox": {
      "command": "python",
      "args": ["-m", "cipher_tool.mcp_server.server", "--transport", "stdio"]
    }
  }
}
```

---

## 🧪 Testing

```bash
# Run all tests (cipher tests + MCP tests)
pytest tests/ -v

# Run only cipher tests
pytest tests/test_ciphers.py -v

# Run only MCP server tests (requires fastmcp)
pytest tests/test_mcp_server.py -v

# Run tests with coverage
pytest tests/ --cov=cipher_tool

# Run specific cipher tests
pytest tests/test_ciphers.py::test_caesar_cipher -v
```

> **Note:** MCP tests are automatically skipped if `fastmcp` is not installed. Install with `pip install cipher-toolbox[mcp]` to run them.

## 🤝 Contributing

We welcome contributions! Please see [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines.

### Quick Contribution Guide

1. Fork the repository
2. Create a feature branch: `git checkout -b feature/new-cipher`
3. Add your cipher implementation
4. Add tests for your cipher
5. Ensure all tests pass: `pytest tests/`
6. Submit a pull request

### Adding New Ciphers

See [CONTRIBUTING.md](CONTRIBUTING.md) for detailed instructions on adding new cipher implementations.

## 📊 Project Stats

- **12 Cipher Implementations**: Classical and modern algorithms
- **MCP Server**: 26 tools, 6 resources, 8 prompts for AI assistant integration
- **100% Test Coverage**: All ciphers and MCP primitives thoroughly tested
- **Cross-Platform**: Works on Windows, macOS, and Linux
- **Python 3.9+**: Modern Python support
- **CLI + API + MCP**: Command-line, programmatic, and AI assistant interfaces

## 🔗 Related Projects

- [cryptography](https://cryptography.io/) - Production-ready cryptographic library
- [PyCrypto](https://www.dlitz.net/software/pycrypto/) - Python cryptography toolkit
- [hashlib](https://docs.python.org/3/library/hashlib.html) - Built-in hashing algorithms

## 📚 References

- Schneier, B. (1996). Applied Cryptography. John Wiley & Sons.
- Katz, J., & Lindell, Y. (2014). Introduction to Modern Cryptography. CRC Press.
- [NIST Cryptographic Standards](https://csrc.nist.gov/projects/cryptographic-standards-and-guidelines)
- [RFC 7539 - ChaCha20 and Poly1305](https://tools.ietf.org/html/rfc7539)

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 👨💻 Author

**Gabriel Dakinah Vincent**
- GitHub: [@Gabriel-Dakinah-Vincent](https://github.com/Gabriel-Dakinah-Vincent)
- Project: [cipher-toolbox](https://github.com/Gabriel-Dakinah-Vincent/cipher-toolbox)

## 🌟 Contributors

- [Gabriel Dakinah Vincent](https://github.com/Gabriel-Dakinah-Vincent) - Creator

---

⭐ **Star this repository if you find it useful!** ⭐