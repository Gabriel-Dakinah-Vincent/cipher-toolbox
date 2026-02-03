from cipher_tool.core.base import BaseCipher
from cryptography.hazmat.primitives.asymmetric import rsa, padding
from cryptography.hazmat.primitives import hashes
import base64


class RSACipher(BaseCipher):
    """
    RSA cipher implementation.
    Note: This creates a new key pair for each instance.
    In practice, you'd want to manage keys separately.
    """

    _shared_keys = None  # Class variable to share keys across encrypt/decrypt

    def __init__(self, key_size: int = 2048):
        # Use shared keys if they exist, otherwise create new ones
        if RSACipher._shared_keys is None:
            RSACipher._shared_keys = {
                'private': rsa.generate_private_key(
                    public_exponent=65537,
                    key_size=key_size
                )
            }
            RSACipher._shared_keys['public'] = RSACipher._shared_keys['private'].public_key()
        
        self.private_key = RSACipher._shared_keys['private']
        self.public_key = RSACipher._shared_keys['public']

    def encrypt(self, text: str) -> str:
        text_bytes = text.encode()
        
        # For simplicity, limit text size to what RSA can handle
        max_chunk_size = (self.public_key.key_size // 8) - 2 * (hashes.SHA256().digest_size) - 2
        if len(text_bytes) > max_chunk_size:
            # Split into chunks
            chunks = [text_bytes[i:i + max_chunk_size] for i in range(0, len(text_bytes), max_chunk_size)]
        else:
            chunks = [text_bytes]
        
        encrypted_chunks = []
        for chunk in chunks:
            encrypted_chunk = self.public_key.encrypt(
                chunk,
                padding.OAEP(
                    mgf=padding.MGF1(algorithm=hashes.SHA256()),
                    algorithm=hashes.SHA256(),
                    label=None
                )
            )
            encrypted_chunks.append(encrypted_chunk)
        
        # Store chunk count in the first 4 bytes
        chunk_count = len(encrypted_chunks).to_bytes(4, 'big')
        return base64.b64encode(chunk_count + b''.join(encrypted_chunks)).decode()

    def decrypt(self, text: str) -> str:
        try:
            # Decode from base64
            encrypted_data = base64.b64decode(text.encode())
            
            # Extract chunk count
            chunk_count = int.from_bytes(encrypted_data[:4], 'big')
            encrypted_data = encrypted_data[4:]
            
            # Calculate chunk size
            chunk_size = self.private_key.key_size // 8
            chunks = [encrypted_data[i:i + chunk_size] for i in range(0, len(encrypted_data), chunk_size)]
            
            if len(chunks) != chunk_count:
                raise ValueError("Chunk count mismatch")
            
            decrypted_chunks = []
            for chunk in chunks:
                decrypted_chunk = self.private_key.decrypt(
                    chunk,
                    padding.OAEP(
                        mgf=padding.MGF1(algorithm=hashes.SHA256()),
                        algorithm=hashes.SHA256(),
                        label=None
                    )
                )
                decrypted_chunks.append(decrypted_chunk)
            
            return b''.join(decrypted_chunks).decode()
        except Exception as e:
            raise ValueError(f"Decryption failed: {e}")