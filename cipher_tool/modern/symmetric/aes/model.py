from cipher_tool.core.base import BaseCipher
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives import padding
import os
import base64


class AESCipher(BaseCipher):
    """
    AES cipher implementation.
    """

    def __init__(self, key: str = "0123456789abcdef0123456789abcdef"):
        # Ensure key is 32 bytes (256-bit)
        self.key = key.encode()[:32].ljust(32, b'0')

    def encrypt(self, text: str) -> str:
        # Generate random IV
        iv = os.urandom(16)
        
        # Create cipher
        cipher = Cipher(algorithms.AES(self.key), modes.CBC(iv))
        encryptor = cipher.encryptor()
        
        # Pad the text
        padder = padding.PKCS7(128).padder()
        padded_data = padder.update(text.encode()) + padder.finalize()
        
        # Encrypt
        ciphertext = encryptor.update(padded_data) + encryptor.finalize()
        
        # Return IV + ciphertext as base64
        return base64.b64encode(iv + ciphertext).decode()

    def decrypt(self, text: str) -> str:
        try:
            # Decode from base64
            data = base64.b64decode(text.encode())
            
            # Extract IV and ciphertext
            iv = data[:16]
            ciphertext = data[16:]
            
            # Create cipher
            cipher = Cipher(algorithms.AES(self.key), modes.CBC(iv))
            decryptor = cipher.decryptor()
            
            # Decrypt
            padded_plaintext = decryptor.update(ciphertext) + decryptor.finalize()
            
            # Unpad
            unpadder = padding.PKCS7(128).unpadder()
            plaintext = unpadder.update(padded_plaintext) + unpadder.finalize()
            
            return plaintext.decode()
        except Exception as e:
            raise ValueError(f"Decryption failed: {e}")