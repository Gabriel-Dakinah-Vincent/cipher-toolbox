---
description: Educational cipher toolkit with a CLI and Python API.
icon: key
---

# Cipher Toolbox

A practical cipher toolbox for learning encryption and decryption.

[![PyPI](https://img.shields.io/pypi/v/cipher-toolbox)](https://pypi.org/project/cipher-toolbox/) [![Python versions](https://img.shields.io/pypi/pyversions/cipher-toolbox)](https://pypi.org/project/cipher-toolbox/) [![Downloads](https://img.shields.io/pypi/dm/cipher-toolbox)](https://pypi.org/project/cipher-toolbox/) [![License](https://img.shields.io/pypi/l/cipher-toolbox)](https://opensource.org/licenses/MIT) [![CI](https://github.com/Gabriel-Dakinah-Vincent/cipher-toolbox/workflows/CI/badge.svg)](https://github.com/Gabriel-Dakinah-Vincent/cipher-toolbox/actions) [![Open issues](https://img.shields.io/github/issues/Gabriel-Dakinah-Vincent/cipher-toolbox)](https://github.com/Gabriel-Dakinah-Vincent/cipher-toolbox/issues) [![Last commit](https://img.shields.io/github/last-commit/Gabriel-Dakinah-Vincent/cipher-toolbox)](https://github.com/Gabriel-Dakinah-Vincent/cipher-toolbox/commits/main)

### Quick start

{% tabs %}
{% tab title="CLI" %}
```bash
# Install from PyPI
pip install cipher-toolbox

# List available ciphers
cipher-tool list

# Encrypt with Caesar
cipher-tool encrypt caesar "HELLO WORLD" --shift 3
# KHOOR ZRUOG

# Decrypt with Caesar
cipher-tool decrypt caesar "KHOOR ZRUOG" --shift 3
# HELLO WORLD
```
{% endtab %}

{% tab title="Python" %}
```python
from cipher_tool import encrypt, decrypt

ciphertext = encrypt("caesar", "HELLO WORLD", shift=3)
plaintext = decrypt("caesar", ciphertext, shift=3)

print(ciphertext)  # KHOOR ZRUOG
print(plaintext)   # HELLO WORLD
```
{% endtab %}
{% endtabs %}

### What’s included

* A CLI: `cipher-tool`.
* A small Python API: `encrypt()` and `decrypt()`.
* Classical ciphers for learning and test vectors.
* A few modern primitives for demos.

See [Ciphers and parameters](reference/ciphers-and-parameters.md) for supported algorithms.

### Docs

<table data-view="cards"><thead><tr><th>Title</th><th data-card-target data-type="content-ref">Target</th></tr></thead><tbody><tr><td>CLI reference</td><td><a href="reference/cli-reference.md">cli-reference.md</a></td></tr><tr><td>Python API</td><td><a href="reference/python-api.md">python-api.md</a></td></tr><tr><td>Ciphers and parameters</td><td><a href="reference/ciphers-and-parameters.md">ciphers-and-parameters.md</a></td></tr><tr><td>Contributing</td><td><a href="project/contributing.md">contributing.md</a></td></tr><tr><td>Security policy</td><td><a href="project/security.md">security.md</a></td></tr><tr><td>Changelog</td><td><a href="project/changelog.md">changelog.md</a></td></tr></tbody></table>

### Security notice

{% hint style="warning" %}
Cipher Toolbox is for education and experimentation.

Do not use it for sensitive or regulated data.

Use production-grade libraries for real security.
{% endhint %}

See [Security Policy](project/security.md) for reporting.

### License

MIT licensed. See [LICENSE](LICENSE/).
