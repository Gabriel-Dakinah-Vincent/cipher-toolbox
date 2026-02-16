---
description: Supported ciphers, parameters, and format conventions.
---

# Ciphers and parameters

### Supported ciphers

#### Classical

* Substitution: Caesar, Atbash, Affine
* Polyalphabetic: Vigenère, Autokey, Beaufort
* Transposition: Rail Fence, Columnar

#### Modern

* Symmetric: XOR, AES, ChaCha20
* Asymmetric: RSA

### Parameters

| Cipher    | Parameters | Type | Notes             | Example          |
| --------- | ---------- | ---- | ----------------- | ---------------- |
| caesar    | `shift`    | int  | 0–25              | `shift=3`        |
| atbash    | None       | -    | -                 | -                |
| affine    | `a`, `b`   | int  | `a` coprime to 26 | `a=5, b=8`       |
| vigenere  | `key`      | str  | non-empty         | `key="SECRET"`   |
| autokey   | `key`      | str  | non-empty         | `key="KEY"`      |
| beaufort  | `key`      | str  | non-empty         | `key="KEY"`      |
| railfence | `rails`    | int  | >= 2              | `rails=3`        |
| columnar  | `key`      | str  | non-empty         | `key="KEY"`      |
| xor       | `key`      | str  | non-empty         | `key="SECRET"`   |
| aes       | `key`      | str  | password string   | `key="password"` |
| chacha20  | `key`      | str  | password string   | `key="password"` |
| rsa       | `key_size` | int  | 1024/2048/4096    | `key_size=2048`  |

### Input / output conventions

{% hint style="info" %}
Cipher Toolbox is educational. Text handling can vary by cipher. Check results with short known test vectors.
{% endhint %}

* Classical ciphers typically operate on letters.
* Some ciphers may drop or normalize whitespace and punctuation.
* `xor` ciphertext is hex.
* `aes`, `chacha20`, and `rsa` ciphertext is base64.
* AES/ChaCha20/RSA ciphertext varies per run.

### Security

{% hint style="warning" %}
Do not use this package to secure sensitive data. Use production-grade libraries instead.
{% endhint %}
