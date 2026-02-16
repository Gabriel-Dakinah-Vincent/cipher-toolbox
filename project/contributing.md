---
description: >-
  Contributing guidelines for Cipher Toolbox (Python cryptography and cipher
  toolkit). Setup, tests, pull requests, and adding new cipher algorithms.
---

# Contributing to Cipher Toolbox

Contribute to **Cipher Toolbox**, an open-source **Python cipher and cryptography toolkit**. This guide covers local setup, running tests, and submitting pull requests.

Keep changes small and reviewable. Add tests and docs with every change.

### Jump to

* [Development setup](contributing.md#development-setup)
* [How to contribute](contributing.md#how-to-contribute)
* [Adding new ciphers](contributing.md#adding-new-ciphers)
* [Pull request process](contributing.md#pull-request-process)
* [Code of conduct](contributing.md#code-of-conduct)

### Development setup

Set up a Python development environment for the `cipher-toolbox` package. You will run the CLI and the Python API locally.

#### Prerequisites

* Python 3.9+
* Git
* A supported OS (Windows, macOS, or Linux)

{% stepper %}
{% step %}
#### Fork and clone

1. Fork the repository.
2. Clone your fork:

{% code title="Clone the repo" %}
```bash
git clone https://github.com/yourusername/cipher-toolbox.git
cd cipher-toolbox
```
{% endcode %}
{% endstep %}

{% step %}
#### Create and activate a virtualenv

Use a virtual environment for Python dependency isolation.

{% code title="Create a virtualenv" %}
```bash
python -m venv venv
```
{% endcode %}

* Windows: `venv\Scripts\activate`
* macOS/Linux: `source venv/bin/activate`
{% endstep %}

{% step %}
#### Install dependencies

Install the package in editable mode with development dependencies.

{% code title="Install dev dependencies" %}
```bash
python -m pip install -e .[dev]
```
{% endcode %}
{% endstep %}
{% endstepper %}

#### Run tests locally

Run the unit test suite before opening a pull request.

{% code title="Run tests" %}
```bash
# Optional: upgrade pip if you hit install issues
python -m pip install --upgrade pip

# Run tests
pytest tests/ -v

# Run tests with coverage
pytest tests/ --cov=cipher_tool
```
{% endcode %}

### How to contribute

#### Reporting bugs

Report bugs for the Cipher Toolbox CLI and Python API using GitHub issues.

* Include Python version, OS, and the full traceback
* Include the exact cipher name and parameters you used
* Include expected vs actual behavior
* Provide a minimal reproduction snippet or CLI command

#### Reporting security vulnerabilities

Please do not report vulnerabilities in public issues. Use the [Security Policy](security.md).

This follows coordinated vulnerability disclosure best practices.\nIt aligns with ISO/IEC 29147 (disclosure) and ISO/IEC 30111 (handling).

#### Suggesting features

Suggest features via a GitHub issue.

* Describe the use case and expected behavior
* Mention if it is a **classical cipher**, **modern cipher**, or tooling
* Keep it aligned with the educational scope

### Adding new ciphers

Cipher Toolbox includes classical and modern cipher algorithms. New cipher implementations should be easy to read and easy to test.

#### 1) Put it in the right folder

* `cipher_tool/classical/substitution/`
* `cipher_tool/classical/polyalphabetic/`
* `cipher_tool/classical/transposition/`
* `cipher_tool/modern/symmetric/`
* `cipher_tool/modern/asymmetric/`

#### 2) Implement the cipher class

{% code title="Cipher implementation skeleton" %}
```python
# cipher_tool/classical/substitution/mycipher/model.py
from cipher_tool.core.base import BaseCipher

class MyCipher(BaseCipher):
    def __init__(self, key="default"):
        self.key = key

    def encrypt(self, text: str) -> str:
        # Implementation here
        pass

    def decrypt(self, text: str) -> str:
        # Implementation here
        pass
```
{% endcode %}

#### 3) Register the cipher

{% code title="Register the cipher" %}
```python
# cipher_tool/core/registry.py
from cipher_tool.classical.substitution.mycipher.model import MyCipher

CIPHER_REGISTRY = {
    # ... existing ciphers
    "mycipher": MyCipher,
}
```
{% endcode %}

#### 4) Add tests

{% code title="Add tests" %}
```python
# tests/test_ciphers.py
from cipher_tool import encrypt, decrypt

def test_mycipher():
    plaintext = "TEST"
    ciphertext = encrypt("mycipher", plaintext, key="mykey")
    decrypted = decrypt("mycipher", ciphertext, key="mykey")
    assert decrypted == plaintext
```
{% endcode %}

#### Code style

* Follow PEP 8
* Use meaningful variable names
* Add docstrings to classes and methods
* Keep functions focused and small

### Pull request process

Pull requests are reviewed for correctness, tests, and documentation quality.

1. Create a feature branch: `git checkout -b feature/new-cipher`
2. Make your changes
3. Add tests for new functionality
4. Ensure all tests pass: `pytest tests/`
5. Update documentation if needed
6. Commit with clear messages
7. Push and create a pull request

#### Review checklist (recommended)

* Tests cover the change.
* Docs match behavior.
* Examples are copy-paste runnable.
* Public APIs stay backward compatible when possible.

### Code of conduct

Follow the project [Code of Conduct](code-of-conduct.md). It applies to issues, pull requests, and discussions.

### Questions

Feel free to open an issue for questions or join discussions in the repository.
