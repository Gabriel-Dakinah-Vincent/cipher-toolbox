# Security Policy

### Supported versions

The following versions of **Cipher Toolbox** are currently supported with security updates:

| Version        | Supported |
| -------------- | --------- |
| Latest release | ✅ Yes     |
| Older releases | ❌ No      |

Users are strongly encouraged to upgrade to the **latest version** to receive security fixes and improvements.

***

### Reporting a vulnerability

If you discover a security vulnerability in this project, **please do not open a public issue**.

Instead, report it responsibly by following the steps below.

#### How to report

* Send a detailed report via **private communication** to the project maintainer
* Include:
  * A clear description of the vulnerability
  * Steps to reproduce (if applicable)
  * Potential impact
  * Affected versions
  * Any proof-of-concept code (if available)

> Reports will be acknowledged as soon as possible.

***

### Response timeline

Once a vulnerability is reported:

* **Acknowledgement:** within 48 hours
* **Initial assessment:** within 5–7 days
* **Fix or mitigation:** as soon as reasonably possible
* **Public disclosure:** coordinated after a fix is released

***

### Scope

This project includes both **classical** and **modern** cryptographic algorithms.

#### Important notes

* **Classical ciphers** (e.g. Caesar, Vigenère, Rail Fence) are:
  * Included for **educational purposes only**
  * **Not secure** for real-world use
* **Modern cryptography** implementations:
  * Use well-established libraries where possible
  * Are provided with care but **should be reviewed before production use**

The maintainers do **not** recommend using this library for protecting sensitive or regulated data without independent security review.

***

### Dependencies

Cipher Toolbox relies on third-party libraries (e.g. `cryptography`).

Security updates to dependencies should be applied promptly.\
Known vulnerabilities in dependencies should be reported if they impact this project.

***

### Responsible disclosure

We value responsible disclosure and collaboration with the security community.

* Please allow time for fixes before public disclosure
* Credit will be given where appropriate (unless anonymity is requested)

***

### Disclaimer

This project is provided **as-is**, without warranty of any kind.\
It is primarily intended for **learning, experimentation, and educational use**.

Use at your own risk.

***

### Thank you

Thank you for helping keep **Cipher Toolbox** and its users safe.
