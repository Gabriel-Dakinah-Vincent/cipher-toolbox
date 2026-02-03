from cipher_tool.core.base import BaseCipher


class BeaufortCipher(BaseCipher):
    """
    Beaufort cipher implementation.
    """

    def __init__(self, key: str = "KEY"):
        self.key = key.upper()

    def encrypt(self, text: str) -> str:
        return self._beaufort_transform(text)

    def decrypt(self, text: str) -> str:
        return self._beaufort_transform(text)

    def _beaufort_transform(self, text: str) -> str:
        result = []
        key_index = 0
        
        for char in text:
            if char.isalpha():
                base = ord('A') if char.isupper() else ord('a')
                char_pos = ord(char) - base
                key_pos = ord(self.key[key_index % len(self.key)]) - ord('A')
                
                new_pos = (key_pos - char_pos) % 26
                result.append(chr(new_pos + base))
                key_index += 1
            else:
                result.append(char)
        
        return ''.join(result)