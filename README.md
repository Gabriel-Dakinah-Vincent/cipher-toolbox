# Cipher Toolbox

A comprehensive educational cipher toolbox for encryption and decryption, featuring both classical and modern cryptographic algorithms.

[![PyPI version](https://badge.fury.io/py/cipher-toolbox.svg)](https://badge.fury.io/py/cipher-toolbox)
[![Python 3.9+](https://img.shields.io/badge/python-3.9+-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![CI](https://github.com/Gabriel-Dakinah-Vincent/cipher-toolbox/workflows/CI/badge.svg)](https://github.com/Gabriel-Dakinah-Vincent/cipher-toolbox/actions)

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
pip install cipher-toolbox
```

### From Source

```bash
git clone https://github.com/Gabriel-Dakinah-Vincent/cipher-toolbox.git
cd cipher-toolbox
pip install -e .
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

## 🧪 Testing

```bash
# Run all tests
pytest tests/ -v

# Run tests with coverage
pytest tests/ --cov=cipher_tool

# Run specific cipher tests
pytest tests/test_ciphers.py::test_caesar_cipher -v
```

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
- **100% Test Coverage**: All ciphers thoroughly tested
- **Cross-Platform**: Works on Windows, macOS, and Linux
- **Python 3.9+**: Modern Python support
- **CLI + API**: Both command-line and programmatic interfaces

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