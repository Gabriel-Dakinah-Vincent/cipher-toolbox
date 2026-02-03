# Cipher Toolbox

A comprehensive educational cipher toolbox for encryption and decryption, featuring both classical and modern cryptographic algorithms.

## Features

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

## Installation

```bash
# Clone the repository
git clone https://github.com/Gabriel-Dakinah-Vincent/cipher-toolbox.git
cd cipher-toolbox

# Install dependencies
pip install cryptography

# Install the package
pip install -e .
```

## Usage

### Python API

```python
from cipher_tool import encrypt, decrypt

# Caesar cipher
ciphertext = encrypt("caesar", "HELLO WORLD", shift=3)
plaintext = decrypt("caesar", ciphertext, shift=3)

# Vigenère cipher
ciphertext = encrypt("vigenere", "HELLO WORLD", key="SECRET")
plaintext = decrypt("vigenere", ciphertext, key="SECRET")

# AES encryption
ciphertext = encrypt("aes", "Hello World", key="mypassword")
plaintext = decrypt("aes", ciphertext, key="mypassword")
```

### Command Line Interface

```bash
# List available ciphers
python cli.py list

# Encrypt with Caesar cipher
python cli.py encrypt caesar "HELLO WORLD" --shift 3

# Decrypt with Caesar cipher
python cli.py decrypt caesar "KHOOR ZRUOG" --shift 3

# Encrypt with Vigenère cipher
python cli.py encrypt vigenere "HELLO WORLD" --key SECRET

# Encrypt with AES
python cli.py encrypt aes "Hello World" --key mypassword
```

## Cipher Parameters

| Cipher | Parameters | Example |
|--------|------------|---------|
| caesar | `shift` (int) | `shift=3` |
| atbash | None | - |
| affine | `a` (int), `b` (int) | `a=5, b=8` |
| vigenere | `key` (str) | `key="SECRET"` |
| autokey | `key` (str) | `key="KEY"` |
| beaufort | `key` (str) | `key="KEY"` |
| railfence | `rails` (int) | `rails=3` |
| columnar | `key` (str) | `key="KEY"` |
| xor | `key` (str) | `key="SECRET"` |
| aes | `key` (str) | `key="password"` |
| chacha20 | `key` (str) | `key="password"` |
| rsa | `key_size` (int) | `key_size=2048` |

## Testing

```bash
# Run all tests
python -m pytest tests/ -v

# Run specific test
python -m pytest tests/test_ciphers.py::test_caesar_cipher -v
```

## Project Structure

```
cipher-toolbox/
├── cipher_tool/
│   ├── classical/
│   │   ├── substitution/
│   │   │   ├── caesar/
│   │   │   ├── atbash/
│   │   │   └── affine/
│   │   ├── polyalphabetic/
│   │   │   ├── vigenere/
│   │   │   ├── autokey/
│   │   │   └── beaufort/
│   │   └── transposition/
│   │       ├── rail_fence/
│   │       └── columnar_transposition/
│   ├── modern/
│   │   ├── symmetric/
│   │   │   ├── xor/
│   │   │   ├── aes/
│   │   │   └── chacha20/
│   │   └── asymmetric/
│   │       └── rsa/
│   └── core/
│       ├── base.py
│       └── registry.py
├── tests/
├── cli.py
└── README.md
```

## Educational Purpose

This toolbox is designed for educational purposes to help understand:
- Classical cryptographic techniques
- Modern encryption algorithms
- Cryptographic principles and concepts
- Implementation differences between cipher types

## Security Notice

⚠️ **Warning**: This implementation is for educational purposes only. Do not use these implementations for securing sensitive data in production environments. Use well-tested, production-ready cryptographic libraries instead.

## Contributing

1. Fork the repository
2. Create a feature branch
3. Add tests for new ciphers
4. Ensure all tests pass
5. Submit a pull request

## Publishing to PyPI

### Prerequisites
```bash
pip install build twine
```

### Build the Package
```bash
# Clean previous builds
rm -rf build/ dist/ *.egg-info/

# Build source and wheel distributions
python -m build
```

### Test on PyPI Test Repository
```bash
# Upload to Test PyPI first
twine upload --repository testpypi dist/*

# Test installation from Test PyPI
pip install --index-url https://test.pypi.org/simple/ cipher-toolbox
```

### Publish to PyPI
```bash
# Upload to production PyPI
twine upload dist/*

# Verify installation
pip install cipher-toolbox
```

### Version Management
Update version in `pyproject.toml` before publishing:
```toml
version = "0.1.1"  # Increment version
```

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Author

Gabriel Dakinah Vincent