---
description: Command-line usage, formats, and examples.
---

# CLI reference

### Install

{% code title="Install (CLI)" %}
```bash
pip install cipher-toolbox
```
{% endcode %}

### Commands

{% code title="Core commands" %}
```bash
cipher-tool list
cipher-tool encrypt --help
cipher-tool decrypt --help
```
{% endcode %}

### Input and output formats

* Classical ciphers usually output text.
* `xor` outputs **hex**.
* `aes`, `chacha20`, and `rsa` output **base64**.
* For `aes`, `chacha20`, and `rsa`, ciphertext can vary per run.
  * This is expected due to nonces, IVs, and padding.

### Common examples

{% code title="Common examples" %}
```bash
# Caesar
cipher-tool encrypt caesar "HELLO WORLD" --shift 3
cipher-tool decrypt caesar "KHOOR ZRUOG" --shift 3

# List what’s available
cipher-tool list
```
{% endcode %}

<details>

<summary>All CLI examples (by cipher)</summary>

#### Classical substitution

**Caesar**

{% code title="Caesar" %}
```bash
cipher-tool encrypt caesar "HELLO WORLD" --shift 3
cipher-tool decrypt caesar "KHOOR ZRUOG" --shift 3
```
{% endcode %}

**Atbash**

{% code title="Atbash" %}
```bash
cipher-tool encrypt atbash "HELLO WORLD"
cipher-tool decrypt atbash "SVOOL DLIOW"
```
{% endcode %}

**Affine**

{% code title="Affine" %}
```bash
cipher-tool encrypt affine "HELLO" --a 5 --b 8
cipher-tool decrypt affine "RCLLA" --a 5 --b 8
```
{% endcode %}

#### Classical polyalphabetic

**Vigenère**

{% code title="Vigenère" %}
```bash
cipher-tool encrypt vigenere "HELLO WORLD" --key "SECRET"
cipher-tool decrypt vigenere "ZINCS KCVNH" --key "SECRET"
```
{% endcode %}

**Autokey**

{% code title="Autokey" %}
```bash
cipher-tool encrypt autokey "HELLO" --key "KEY"
cipher-tool decrypt autokey "RIJSS" --key "KEY"
```
{% endcode %}

**Beaufort**

{% code title="Beaufort" %}
```bash
cipher-tool encrypt beaufort "HELLO" --key "KEY"
cipher-tool decrypt beaufort "DANZQ" --key "KEY"
```
{% endcode %}

#### Classical transposition

**Rail fence**

{% code title="Rail fence" %}
```bash
cipher-tool encrypt railfence "HELLO WORLD" --rails 3
cipher-tool decrypt railfence "HOREL OLLWD" --rails 3
```
{% endcode %}

**Columnar**

{% code title="Columnar" %}
```bash
cipher-tool encrypt columnar "HELLO WORLD" --key "KEY"
cipher-tool decrypt columnar "EHLOLWLORD" --key "KEY"
```
{% endcode %}

#### Modern symmetric

{% hint style="info" %}
AES and ChaCha20 outputs vary per run. That’s expected.
{% endhint %}

**XOR**

{% code title="XOR" %}
```bash
cipher-tool encrypt xor "HELLO" --key "SECRET"
cipher-tool decrypt xor "1b0a001a1c" --key "SECRET"
```
{% endcode %}

**AES**

{% code title="AES" %}
```bash
cipher-tool encrypt aes "Hello World" --key "mypassword"
cipher-tool decrypt aes "base64-string" --key "mypassword"
```
{% endcode %}

**ChaCha20**

{% code title="ChaCha20" %}
```bash
cipher-tool encrypt chacha20 "Hello World" --key "mypassword"
cipher-tool decrypt chacha20 "base64-string" --key "mypassword"
```
{% endcode %}

#### Modern asymmetric

{% hint style="info" %}
RSA output varies per run due to padding. That’s expected.
{% endhint %}

**RSA**

{% code title="RSA" %}
```bash
cipher-tool encrypt rsa "HELLO"
cipher-tool decrypt rsa "base64-string"
```
{% endcode %}

</details>
