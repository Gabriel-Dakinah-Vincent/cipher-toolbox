# Contributing to Cipher Toolbox

Thank you for your interest in contributing to Cipher Toolbox! This document provides guidelines for contributing to the project.

## Getting Started

1. Fork the repository
2. Clone your fork: `git clone https://github.com/yourusername/cipher-toolbox.git`
3. Create a virtual environment: `python -m venv venv`
4. Activate it: `venv\Scripts\activate` (Windows) or `source venv/bin/activate` (Unix)
5. Install dependencies: `pip install -e .[dev]`

## Development Setup

```bash
# Install development dependencies
pip install pytest pytest-cov cryptography

# Run tests
pytest tests/ -v

# Run tests with coverage
pytest tests/ --cov=cipher_tool
```

## How to Contribute

### Reporting Bugs
- Use the GitHub issue tracker
- Include Python version, OS, and error messages
- Provide minimal code to reproduce the issue

### Suggesting Features
- Open an issue with the `enhancement` label
- Describe the use case and expected behavior
- Consider if it fits the educational scope of the project

### Adding New Ciphers

1. Create a new directory under the appropriate category:
   - `cipher_tool/classical/substitution/`
   - `cipher_tool/classical/polyalphabetic/`
   - `cipher_tool/classical/transposition/`
   - `cipher_tool/modern/symmetric/`
   - `cipher_tool/modern/asymmetric/`

2. Implement your cipher:
   ```python
   # cipher_tool/classical/substitution/myccipher/model.py
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

3. Add to registry:
   ```python
   # cipher_tool/core/registry.py
   from cipher_tool.classical.substitution.myciper.model import MyCipher
   
   CIPHER_REGISTRY = {
       # ... existing ciphers
       "myciper": MyCipher,
   }
   ```

4. Add tests:
   ```python
   # tests/test_ciphers.py
   def test_myciper():
       plaintext = "TEST"
       ciphertext = encrypt("myciper", plaintext, key="mykey")
       decrypted = decrypt("myciper", ciphertext, key="mykey")
       assert decrypted == plaintext
   ```

### Code Style
- Follow PEP 8
- Use meaningful variable names
- Add docstrings to classes and methods
- Keep functions focused and small

### Pull Request Process
1. Create a feature branch: `git checkout -b feature/new-cipher`
2. Make your changes
3. Add tests for new functionality
4. Ensure all tests pass: `pytest tests/`
5. Update documentation if needed
6. Commit with clear messages
7. Push and create a pull request

## Code of Conduct

- Be respectful and inclusive
- Focus on constructive feedback
- Help newcomers learn
- Keep discussions on-topic

## Questions?

Feel free to open an issue for questions or join discussions in the repository.