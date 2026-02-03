from cipher_tool.core.base import BaseCipher


class AffineCipher(BaseCipher):
    """
    Affine cipher implementation.
    """

    def __init__(self, a: int = 5, b: int = 8):
        if self._gcd(a, 26) != 1:
            raise ValueError("'a' must be coprime to 26")
        self.a = a
        self.b = b
        self.a_inv = self._mod_inverse(a, 26)

    def encrypt(self, text: str) -> str:
        result = []
        for char in text:
            if char.isalpha():
                base = ord('A') if char.isupper() else ord('a')
                x = ord(char) - base
                encrypted = (self.a * x + self.b) % 26
                result.append(chr(encrypted + base))
            else:
                result.append(char)
        return ''.join(result)

    def decrypt(self, text: str) -> str:
        result = []
        for char in text:
            if char.isalpha():
                base = ord('A') if char.isupper() else ord('a')
                y = ord(char) - base
                decrypted = (self.a_inv * (y - self.b)) % 26
                result.append(chr(decrypted + base))
            else:
                result.append(char)
        return ''.join(result)

    def _gcd(self, a: int, b: int) -> int:
        while b:
            a, b = b, a % b
        return a

    def _mod_inverse(self, a: int, m: int) -> int:
        for i in range(1, m):
            if (a * i) % m == 1:
                return i
        raise ValueError(f"No modular inverse for {a} mod {m}")