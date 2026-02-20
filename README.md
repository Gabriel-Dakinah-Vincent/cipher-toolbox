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
{% code title="CLI quick start" %}
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
{% endcode %}
{% endtab %}

{% tab title="Python" %}
{% code title="Python quick start" %}
```python
from cipher_tool import encrypt, decrypt

ciphertext = encrypt("caesar", "HELLO WORLD", shift=3)
plaintext = decrypt("caesar", ciphertext, shift=3)

print(ciphertext)  # KHOOR ZRUOG
print(plaintext)   # HELLO WORLD
```
{% endcode %}
{% endtab %}
{% endtabs %}

### What’s included

* A CLI: `cipher-tool`.
* A small Python API: `encrypt()` and `decrypt()`.
* Classical ciphers for learning and test vectors.
* A few modern primitives for demos.

See [Ciphers and parameters](reference/ciphers-and-parameters.md) for supported algorithms.

### Docs

<table data-view="cards"><thead><tr><th>Title</th><th data-card-target data-type="content-ref">Target</th><th data-type="rating" data-max="5"></th><th data-hidden data-card-cover data-type="image">Cover image</th></tr></thead><tbody><tr><td>CLI reference</td><td><a href="reference/cli-reference.md">cli-reference.md</a></td><td>null</td><td><a href="https://images.unsplash.com/photo-1762242298589-582f5f6c3fb1?crop=entropy&#x26;cs=srgb&#x26;fm=jpg&#x26;ixid=M3wxOTcwMjR8MHwxfHNlYXJjaHwxfHxDT01NQU5EJTIwTElORXxlbnwwfHx8fDE3NzE1ODU2ODh8MA&#x26;ixlib=rb-4.1.0&#x26;q=85">https://images.unsplash.com/photo-1762242298589-582f5f6c3fb1?crop=entropy&#x26;cs=srgb&#x26;fm=jpg&#x26;ixid=M3wxOTcwMjR8MHwxfHNlYXJjaHwxfHxDT01NQU5EJTIwTElORXxlbnwwfHx8fDE3NzE1ODU2ODh8MA&#x26;ixlib=rb-4.1.0&#x26;q=85</a></td></tr><tr><td>Python API</td><td><a href="reference/python-api.md">python-api.md</a></td><td>null</td><td><a href="https://images.unsplash.com/photo-1658204191944-374e8115a2de?crop=entropy&#x26;cs=srgb&#x26;fm=jpg&#x26;ixid=M3wxOTcwMjR8MHwxfHNlYXJjaHw1fHxhcGl8ZW58MHx8fHwxNzcxNTg1Njk3fDA&#x26;ixlib=rb-4.1.0&#x26;q=85">https://images.unsplash.com/photo-1658204191944-374e8115a2de?crop=entropy&#x26;cs=srgb&#x26;fm=jpg&#x26;ixid=M3wxOTcwMjR8MHwxfHNlYXJjaHw1fHxhcGl8ZW58MHx8fHwxNzcxNTg1Njk3fDA&#x26;ixlib=rb-4.1.0&#x26;q=85</a></td></tr><tr><td>Ciphers and parameters</td><td><a href="reference/ciphers-and-parameters.md">ciphers-and-parameters.md</a></td><td>null</td><td><a href="https://images.unsplash.com/photo-1677602686233-23ac18fad0de?crop=entropy&#x26;cs=srgb&#x26;fm=jpg&#x26;ixid=M3wxOTcwMjR8MHwxfHNlYXJjaHw2fHxDaXBoZXJ8ZW58MHx8fHwxNzcxNTg1NzM1fDA&#x26;ixlib=rb-4.1.0&#x26;q=85">https://images.unsplash.com/photo-1677602686233-23ac18fad0de?crop=entropy&#x26;cs=srgb&#x26;fm=jpg&#x26;ixid=M3wxOTcwMjR8MHwxfHNlYXJjaHw2fHxDaXBoZXJ8ZW58MHx8fHwxNzcxNTg1NzM1fDA&#x26;ixlib=rb-4.1.0&#x26;q=85</a></td></tr><tr><td>Contributing</td><td><a href="project/contributing.md">contributing.md</a></td><td>null</td><td><a href="https://images.unsplash.com/photo-1730531678444-6a754099570f?crop=entropy&#x26;cs=srgb&#x26;fm=jpg&#x26;ixid=M3wxOTcwMjR8MHwxfHNlYXJjaHw5fHxDb250cmlidXRlfGVufDB8fHx8MTc3MTU4NTc3MXww&#x26;ixlib=rb-4.1.0&#x26;q=85">https://images.unsplash.com/photo-1730531678444-6a754099570f?crop=entropy&#x26;cs=srgb&#x26;fm=jpg&#x26;ixid=M3wxOTcwMjR8MHwxfHNlYXJjaHw5fHxDb250cmlidXRlfGVufDB8fHx8MTc3MTU4NTc3MXww&#x26;ixlib=rb-4.1.0&#x26;q=85</a></td></tr><tr><td>Security policy</td><td><a href="project/security.md">security.md</a></td><td>null</td><td><a href="https://images.unsplash.com/photo-1523961131990-5ea7c61b2107?crop=entropy&#x26;cs=srgb&#x26;fm=jpg&#x26;ixid=M3wxOTcwMjR8MHwxfHNlYXJjaHw3fHxTZWN1cml0eXxlbnwwfHx8fDE3NzE1ODU3OTJ8MA&#x26;ixlib=rb-4.1.0&#x26;q=85">https://images.unsplash.com/photo-1523961131990-5ea7c61b2107?crop=entropy&#x26;cs=srgb&#x26;fm=jpg&#x26;ixid=M3wxOTcwMjR8MHwxfHNlYXJjaHw3fHxTZWN1cml0eXxlbnwwfHx8fDE3NzE1ODU3OTJ8MA&#x26;ixlib=rb-4.1.0&#x26;q=85</a></td></tr><tr><td>Changelog</td><td><a href="project/changelog.md">changelog.md</a></td><td>null</td><td><a href="https://images.unsplash.com/photo-1499244571948-7ccddb3583f1?crop=entropy&#x26;cs=srgb&#x26;fm=jpg&#x26;ixid=M3wxOTcwMjR8MHwxfHNlYXJjaHwxfHxjaGFuZ2V8ZW58MHx8fHwxNzcxNTg1ODI4fDA&#x26;ixlib=rb-4.1.0&#x26;q=85">https://images.unsplash.com/photo-1499244571948-7ccddb3583f1?crop=entropy&#x26;cs=srgb&#x26;fm=jpg&#x26;ixid=M3wxOTcwMjR8MHwxfHNlYXJjaHwxfHxjaGFuZ2V8ZW58MHx8fHwxNzcxNTg1ODI4fDA&#x26;ixlib=rb-4.1.0&#x26;q=85</a></td></tr></tbody></table>

### Security notice

{% hint style="warning" %}
Cipher Toolbox is for education and experimentation.

Do not use it for sensitive or regulated data.

Use production-grade libraries for real security.
{% endhint %}

See [Security Policy](project/security.md) for reporting.

### License

MIT licensed. See [LICENSE](LICENSE/).
