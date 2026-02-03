from cipher_tool.core.registry import CIPHER_REGISTRY


def decrypt(cipher_name: str, text: str, **params) -> str:
    cipher_name = cipher_name.lower()

    if cipher_name not in CIPHER_REGISTRY:
        raise ValueError(f"Unsupported cipher: {cipher_name}")

    cipher = CIPHER_REGISTRY[cipher_name](**params)
    return cipher.decrypt(text)