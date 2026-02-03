from abc import ABC, abstractmethod


class BaseCipher(ABC):
    """
    Abstract base class for all ciphers.
    """

    @abstractmethod
    def encrypt(self, text: str) -> str:
        pass

    @abstractmethod
    def decrypt(self, text: str) -> str:
        pass

    @staticmethod
    def _shift_char(char: str, shift: int) -> str:
        if not char.isalpha():
            return char

        base = ord('A') if char.isupper() else ord('a')
        return chr((ord(char) - base + shift) % 26 + base)