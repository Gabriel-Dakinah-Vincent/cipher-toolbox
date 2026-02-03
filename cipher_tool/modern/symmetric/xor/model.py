from cipher_tool.core.base import BaseCipher


class XORCipher(BaseCipher):
    """
    XOR cipher implementation.
    """

    def __init__(self, key: str = "SECRET"):
        self.key = key.encode()

    def encrypt(self, text: str) -> str:
        text_bytes = text.encode()
        result = []
        
        for i, byte in enumerate(text_bytes):
            key_byte = self.key[i % len(self.key)]
            result.append(byte ^ key_byte)
        
        return ''.join(f'{b:02x}' for b in result)

    def decrypt(self, text: str) -> str:
        # Convert hex string back to bytes
        try:
            cipher_bytes = bytes.fromhex(text)
        except ValueError:
            raise ValueError("Invalid hex string")
        
        result = []
        for i, byte in enumerate(cipher_bytes):
            key_byte = self.key[i % len(self.key)]
            result.append(byte ^ key_byte)
        
        return bytes(result).decode()