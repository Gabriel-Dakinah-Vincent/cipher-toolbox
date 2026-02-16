# Cipher Toolbox

A comprehensive, educational cipher toolbox for encryption and decryption.

[![PyPI version](https://badge.fury.io/py/cipher-toolbox.svg)](https://badge.fury.io/py/cipher-toolbox) [![Python 3.9+](https://img.shields.io/badge/python-3.9+-blue.svg)](https://www.python.org/downloads/) [![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT) [![CI](https://github.com/Gabriel-Dakinah-Vincent/cipher-toolbox/workflows/CI/badge.svg)](https://github.com/Gabriel-Dakinah-Vincent/cipher-toolbox/actions)

### Quick start

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

### Docs

<table data-view="cards"><thead><tr><th>Title</th><th data-card-target data-type="content-ref">Target</th></tr></thead><tbody><tr><td>CLI reference</td><td><a href="reference/cli-reference.md">cli-reference.md</a></td></tr><tr><td>Python API</td><td><a href="reference/python-api.md">python-api.md</a></td></tr><tr><td>Ciphers and parameters</td><td><a href="reference/ciphers-and-parameters.md">ciphers-and-parameters.md</a></td></tr><tr><td>Contributing</td><td><a href="project/contributing.md">contributing.md</a></td></tr><tr><td>Security policy</td><td><a href="project/security.md">security.md</a></td></tr><tr><td>Changelog</td><td><a href="project/changelog.md">changelog.md</a></td></tr></tbody></table>

### What this is

Cipher Toolbox is built for learning and demos. It includes classical ciphers and a few modern primitives.

Use it to explore parameters, failure modes, and patterns. Do not use it to protect real secrets.

### Security notice

{% hint style="warning" %}
Cipher Toolbox is for education and experimentation. Do not use it to secure sensitive or regulated data. Use production-grade libraries instead.
{% endhint %}

See the full [Security Policy](project/security.md).

### License

MIT licensed. See [LICENSE](LICENSE/).
