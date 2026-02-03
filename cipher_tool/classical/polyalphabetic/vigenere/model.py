from cipher_tool.core.base import BaseCipher


class VigenereCipher(BaseCipher):
    """
    Vigenère cipher implementation.
    """

    def __init__(self, key: str = "KEY"):
        self.key = key.upper()

    def encrypt(self, text: str) -> str:
        return self._vigenere_transform(text, encrypt=True)

    def decrypt(self, text: str) -> str:
        return self._vigenere_transform(text, encrypt=False)

    def _vigenere_transform(self, text: str, encrypt: bool) -> str:
        result = []
        key_index = 0
        
        for char in text:
            if char.isalpha():
                base = ord('A') if char.isupper() else ord('a')
                char_pos = ord(char) - base
                key_pos = ord(self.key[key_index % len(self.key)]) - ord('A')
                
                if encrypt:
                    new_pos = (char_pos + key_pos) % 26
                else:
                    new_pos = (char_pos - key_pos) % 26
                
                result.append(chr(new_pos + base))
                key_index += 1
            else:
                result.append(char)
        
        return ''.join(result)