from typing import Dict, Type
from cipher_tool.core.base import BaseCipher

# Classical ciphers
from cipher_tool.classical.substitution.caesar.model import CaesarCipher
from cipher_tool.classical.substitution.atbash.model import AtbashCipher
from cipher_tool.classical.substitution.affine.model import AffineCipher
from cipher_tool.classical.polyalphabetic.vigenere.model import VigenereCipher
from cipher_tool.classical.polyalphabetic.autokey.model import AutokeyCipher
from cipher_tool.classical.polyalphabetic.beaufort.model import BeaufortCipher
from cipher_tool.classical.transposition.rail_fence.model import RailFenceCipher
from cipher_tool.classical.transposition.columnar_transposition.model import ColumnarTranspositionCipher

# Modern ciphers
from cipher_tool.modern.symmetric.xor.model import XORCipher
from cipher_tool.modern.symmetric.aes.model import AESCipher
from cipher_tool.modern.symmetric.chacha20.model import ChaCha20Cipher
from cipher_tool.modern.asymmetric.rsa.model import RSACipher

CIPHER_REGISTRY: Dict[str, Type[BaseCipher]] = {
    # Classical substitution ciphers
    "caesar": CaesarCipher,
    "atbash": AtbashCipher,
    "affine": AffineCipher,
    
    # Classical polyalphabetic ciphers
    "vigenere": VigenereCipher,
    "autokey": AutokeyCipher,
    "beaufort": BeaufortCipher,
    
    # Classical transposition ciphers
    "railfence": RailFenceCipher,
    "columnar": ColumnarTranspositionCipher,
    
    # Modern symmetric ciphers
    "xor": XORCipher,
    "aes": AESCipher,
    "chacha20": ChaCha20Cipher,
    
    # Modern asymmetric ciphers
    "rsa": RSACipher,
}