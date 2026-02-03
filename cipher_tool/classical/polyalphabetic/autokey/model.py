from cipher_tool.core.base import BaseCipher


class AutokeyCipher(BaseCipher):
    """
    Autokey cipher implementation.
    """

    def __init__(self, key: str = "KEY"):
        self.key = key.upper()

    def encrypt(self, text: str) -> str:
        result = []
        key_stream = self.key
        
        for i, char in enumerate(text):
            if char.isalpha():
                # Extend key stream with plaintext character BEFORE encryption
                if i >= len(self.key):
                    key_stream += text[i - len(self.key)].upper()
                
                base = ord('A') if char.isupper() else ord('a')
                char_pos = ord(char.upper()) - ord('A')
                key_pos = ord(key_stream[i]) - ord('A')
                
                new_pos = (char_pos + key_pos) % 26
                encrypted_char = chr(new_pos + ord('A'))
                
                # Preserve original case
                if char.islower():
                    encrypted_char = encrypted_char.lower()
                
                result.append(encrypted_char)
            else:
                result.append(char)
        
        return ''.join(result)

    def decrypt(self, text: str) -> str:
        result = []
        key_stream = self.key
        key_index = 0
        
        for char in text:
            if char.isalpha():
                base = ord('A') if char.isupper() else ord('a')
                char_pos = ord(char.upper()) - ord('A')
                key_pos = ord(key_stream[key_index]) - ord('A')
                
                new_pos = (char_pos - key_pos) % 26
                decrypted_char = chr(new_pos + ord('A'))
                
                # Preserve original case
                if char.islower():
                    decrypted_char = decrypted_char.lower()
                
                result.append(decrypted_char)
                
                # Add the decrypted character to key stream for next iteration
                key_stream += decrypted_char.upper()
                key_index += 1
            else:
                result.append(char)
        
        return ''.join(result)