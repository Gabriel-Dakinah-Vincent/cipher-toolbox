from cipher_tool.core.base import BaseCipher


class CaesarCipher(BaseCipher):
    """
    Caesar cipher implementation.
    """

    def __init__(self, shift: int = 3):
        self.shift = shift % 26

    def encrypt(self, text: str) -> str:
        return "".join(self._shift_char(c, self.shift) for c in text)

    def decrypt(self, text: str) -> str:
        return "".join(self._shift_char(c, -self.shift) for c in text)