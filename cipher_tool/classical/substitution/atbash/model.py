from cipher_tool.core.base import BaseCipher


class AtbashCipher(BaseCipher):
    """
    Atbash cipher implementation.
    """

    def encrypt(self, text: str) -> str:
        return self._atbash_transform(text)

    def decrypt(self, text: str) -> str:
        return self._atbash_transform(text)

    def _atbash_transform(self, text: str) -> str:
        result = []
        for char in text:
            if char.isalpha():
                if char.isupper():
                    result.append(chr(ord('Z') - (ord(char) - ord('A'))))
                else:
                    result.append(chr(ord('z') - (ord(char) - ord('a'))))
            else:
                result.append(char)
        return ''.join(result)