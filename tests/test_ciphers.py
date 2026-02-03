from cipher_tool import encrypt, decrypt
import pytest


def test_caesar_cipher():
    plaintext = "HELLO WORLD"
    ciphertext = encrypt("caesar", plaintext, shift=3)
    decrypted = decrypt("caesar", ciphertext, shift=3)
    assert ciphertext == "KHOOR ZRUOG"
    assert decrypted == plaintext


def test_atbash_cipher():
    plaintext = "HELLO WORLD"
    ciphertext = encrypt("atbash", plaintext)
    decrypted = decrypt("atbash", ciphertext)
    assert ciphertext == "SVOOL DLIOW"
    assert decrypted == plaintext


def test_affine_cipher():
    plaintext = "HELLO"
    ciphertext = encrypt("affine", plaintext, a=5, b=8)
    decrypted = decrypt("affine", ciphertext, a=5, b=8)
    assert decrypted == plaintext


def test_vigenere_cipher():
    plaintext = "HELLO WORLD"
    ciphertext = encrypt("vigenere", plaintext, key="KEY")
    decrypted = decrypt("vigenere", ciphertext, key="KEY")
    assert ciphertext == "RIJVS UYVJN"
    assert decrypted == plaintext


def test_autokey_cipher():
    plaintext = "HELLO"
    ciphertext = encrypt("autokey", plaintext, key="KEY")
    decrypted = decrypt("autokey", ciphertext, key="KEY")
    assert decrypted == plaintext


def test_beaufort_cipher():
    plaintext = "HELLO"
    ciphertext = encrypt("beaufort", plaintext, key="KEY")
    decrypted = decrypt("beaufort", ciphertext, key="KEY")
    assert decrypted == plaintext


def test_railfence_cipher():
    plaintext = "HELLO WORLD"
    ciphertext = encrypt("railfence", plaintext, rails=3)
    decrypted = decrypt("railfence", ciphertext, rails=3)
    assert decrypted == plaintext


def test_columnar_cipher():
    plaintext = "HELLO WORLD"
    ciphertext = encrypt("columnar", plaintext, key="KEY")
    decrypted = decrypt("columnar", ciphertext, key="KEY")
    assert decrypted == "HELLOWORLD"


def test_xor_cipher():
    plaintext = "HELLO"
    ciphertext = encrypt("xor", plaintext, key="SECRET")
    decrypted = decrypt("xor", ciphertext, key="SECRET")
    assert decrypted == plaintext


@pytest.mark.skipif(False, reason="Requires cryptography library")
def test_aes_cipher():
    plaintext = "HELLO WORLD"
    ciphertext = encrypt("aes", plaintext)
    decrypted = decrypt("aes", ciphertext)
    assert decrypted == plaintext


@pytest.mark.skipif(False, reason="Requires cryptography library")
def test_chacha20_cipher():
    plaintext = "HELLO WORLD"
    ciphertext = encrypt("chacha20", plaintext)
    decrypted = decrypt("chacha20", ciphertext)
    assert decrypted == plaintext


@pytest.mark.skipif(False, reason="Requires cryptography library")
def test_rsa_cipher():
    plaintext = "HELLO"
    ciphertext = encrypt("rsa", plaintext)
    decrypted = decrypt("rsa", ciphertext)
    assert decrypted == plaintext