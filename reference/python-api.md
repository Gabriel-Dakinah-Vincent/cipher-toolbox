---
description: Programmatic usage via encrypt() and decrypt().
---

# Python API

### Install

```bash
pip install cipher-toolbox
```

### Basic usage

```python
from cipher_tool import encrypt, decrypt

ciphertext = encrypt("caesar", "HELLO WORLD", shift=3)
plaintext = decrypt("caesar", ciphertext, shift=3)

print(ciphertext)  # KHOOR ZRUOG
print(plaintext)   # HELLO WORLD
```

### Input and output formats

* Classical ciphers usually return text.
* `xor` returns **hex**.
* `aes`, `chacha20`, and `rsa` return **base64**.
* For `aes`, `chacha20`, and `rsa`, ciphertext can vary per run.
  * This is expected due to random nonces, IVs, and padding.

### Error handling

```python
from cipher_tool import encrypt

try:
    encrypt("invalid_cipher", "test")
except ValueError as e:
    print(e)
```

<details>

<summary>More examples</summary>

#### Classical

```python
from cipher_tool import encrypt, decrypt

print(encrypt("atbash", "HELLO"))
print(encrypt("affine", "HELLO", a=5, b=8))
print(encrypt("vigenere", "HELLO WORLD", key="SECRET"))
print(encrypt("railfence", "HELLO WORLD", rails=3))
```

#### Modern

```python
from cipher_tool import encrypt

print(encrypt("xor", "HELLO", key="SECRET"))
print(encrypt("aes", "Hello World", key="mypassword"))  # varies per run
print(encrypt("chacha20", "Hello World", key="mypassword"))  # varies per run
print(encrypt("rsa", "HELLO", key_size=2048))  # varies per run
```

#### Batch processing

```python
from cipher_tool import encrypt, decrypt

messages = ["HELLO", "WORLD", "CIPHER", "TOOLBOX"]
key = "SECRET"

encrypted = [encrypt("vigenere", msg, key=key) for msg in messages]
decrypted = [decrypt("vigenere", msg, key=key) for msg in encrypted]

print(encrypted)
print(decrypted)
```

</details>
