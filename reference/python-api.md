---
description: Programmatic usage via encrypt() and decrypt().
---

# Python API

### Install

{% code title="Install (Python)" %}
```bash
pip install cipher-toolbox
```
{% endcode %}

### Basic usage

{% code title="Basic usage" %}
```python
from cipher_tool import encrypt, decrypt

ciphertext = encrypt("caesar", "HELLO WORLD", shift=3)
plaintext = decrypt("caesar", ciphertext, shift=3)

print(ciphertext)  # KHOOR ZRUOG
print(plaintext)   # HELLO WORLD
```
{% endcode %}

### Input and output formats

* Classical ciphers usually return text.
* `xor` returns **hex**.
* `aes`, `chacha20`, and `rsa` return **base64**.
* For `aes`, `chacha20`, and `rsa`, ciphertext can vary per run.
  * This is expected due to random nonces, IVs, and padding.

### Error handling

{% code title="Error handling" %}
```python
from cipher_tool import encrypt

try:
    encrypt("invalid_cipher", "test")
except ValueError as e:
    print(e)
```
{% endcode %}

<details>

<summary>More examples</summary>

#### Classical

{% code title="Classical ciphers" %}
```python
from cipher_tool import encrypt, decrypt

print(encrypt("atbash", "HELLO"))
print(encrypt("affine", "HELLO", a=5, b=8))
print(encrypt("vigenere", "HELLO WORLD", key="SECRET"))
print(encrypt("railfence", "HELLO WORLD", rails=3))
```
{% endcode %}

#### Modern

{% code title="Modern primitives" %}
```python
from cipher_tool import encrypt

print(encrypt("xor", "HELLO", key="SECRET"))
print(encrypt("aes", "Hello World", key="mypassword"))  # varies per run
print(encrypt("chacha20", "Hello World", key="mypassword"))  # varies per run
print(encrypt("rsa", "HELLO", key_size=2048))  # varies per run
```
{% endcode %}

#### Batch processing

{% code title="Batch processing" %}
```python
from cipher_tool import encrypt, decrypt

messages = ["HELLO", "WORLD", "CIPHER", "TOOLBOX"]
key = "SECRET"

encrypted = [encrypt("vigenere", msg, key=key) for msg in messages]
decrypted = [decrypt("vigenere", msg, key=key) for msg in encrypted]

print(encrypted)
print(decrypted)
```
{% endcode %}

</details>
