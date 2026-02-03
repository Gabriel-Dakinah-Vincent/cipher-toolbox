from cipher_tool.core.base import BaseCipher
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
import os
import base64


class ChaCha20Cipher(BaseCipher):
    """
    ChaCha20 cipher implementation.
    """

    def __init__(self, key: str = "01234567890123456789012345678901"):
        # Ensure key is 32 bytes
        self.key = key.encode()[:32].ljust(32, b'0')

    def encrypt(self, text: str) -> str:
        # Generate random nonce
        nonce = os.urandom(16)
        
        # Create cipher
        cipher = Cipher(algorithms.ChaCha20(self.key, nonce), mode=None)
        encryptor = cipher.encryptor()
        
        # Encrypt
        ciphertext = encryptor.update(text.encode()) + encryptor.finalize()
        
        # Return nonce + ciphertext as base64
        return base64.b64encode(nonce + ciphertext).decode()

    def decrypt(self, text: str) -> str:
        try:
            # Decode from base64
            data = base64.b64decode(text.encode())
            
            # Extract nonce and ciphertext
            nonce = data[:16]
            ciphertext = data[16:]
            
            # Create cipher
            cipher = Cipher(algorithms.ChaCha20(self.key, nonce), mode=None)
            decryptor = cipher.decryptor()
            
            # Decrypt
            plaintext = decryptor.update(ciphertext) + decryptor.finalize()
            
            return plaintext.decode()
        except Exception as e:
            raise ValueError(f"Decryption failed: {e}")