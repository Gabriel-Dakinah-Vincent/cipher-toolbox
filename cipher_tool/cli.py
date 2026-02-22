#!/usr/bin/env python3
"""
Cipher Toolbox CLI
A command-line interface for the cipher toolbox.
"""

import argparse
import sys
from cipher_tool import encrypt, decrypt
from cipher_tool.telemetry import setup_telemetry, send_telemetry


def list_ciphers():
    """List all available ciphers."""
    from cipher_tool.core.registry import CIPHER_REGISTRY

    print("Available ciphers:")
    print("\nClassical Substitution Ciphers:")
    print("  - caesar: Caesar cipher (shift parameter)")
    print("  - atbash: Atbash cipher")
    print("  - affine: Affine cipher (a, b parameters)")

    print("\nClassical Polyalphabetic Ciphers:")
    print("  - vigenere: Vigenère cipher (key parameter)")
    print("  - autokey: Autokey cipher (key parameter)")
    print("  - beaufort: Beaufort cipher (key parameter)")

    print("\nClassical Transposition Ciphers:")
    print("  - railfence: Rail Fence cipher (rails parameter)")
    print("  - columnar: Columnar Transposition (key parameter)")

    print("\nModern Symmetric Ciphers:")
    print("  - xor: XOR cipher (key parameter)")
    print("  - aes: AES cipher (key parameter)")
    print("  - chacha20: ChaCha20 cipher (key parameter)")

    print("\nModern Asymmetric Ciphers:")
    print("  - rsa: RSA cipher (key_size parameter)")


def main():
    parser = argparse.ArgumentParser(
        description="Cipher Toolbox - Educational encryption and decryption tool",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  %(prog)s encrypt caesar "HELLO WORLD" --shift 3
  %(prog)s decrypt caesar "KHOOR ZRUOG" --shift 3
  %(prog)s encrypt vigenere "HELLO WORLD" --key SECRET
  %(prog)s encrypt aes "Hello World" --key mypassword
  %(prog)s list
        """
    )

    subparsers = parser.add_subparsers(dest='command', help='Available commands')

    subparsers.add_parser('list', help='List available ciphers')

    encrypt_parser = subparsers.add_parser('encrypt', help='Encrypt text')
    encrypt_parser.add_argument('cipher', help='Cipher to use')
    encrypt_parser.add_argument('text', help='Text to encrypt')
    encrypt_parser.add_argument('--shift', type=int)
    encrypt_parser.add_argument('--key')
    encrypt_parser.add_argument('--a', type=int)
    encrypt_parser.add_argument('--b', type=int)
    encrypt_parser.add_argument('--rails', type=int)
    encrypt_parser.add_argument('--key-size', type=int)

    decrypt_parser = subparsers.add_parser('decrypt', help='Decrypt text')
    decrypt_parser.add_argument('cipher', help='Cipher to use')
    decrypt_parser.add_argument('text', help='Text to decrypt')
    decrypt_parser.add_argument('--shift', type=int)
    decrypt_parser.add_argument('--key')
    decrypt_parser.add_argument('--a', type=int)
    decrypt_parser.add_argument('--b', type=int)
    decrypt_parser.add_argument('--rails', type=int)
    decrypt_parser.add_argument('--key-size', type=int)

    args = parser.parse_args()

    if not args.command:
        parser.print_help()
        return

    # Setup telemetry (first run only)
    setup_telemetry()

    # Send telemetry for executed command
    send_telemetry(args.command)

    if args.command == 'list':
        list_ciphers()
        return

    params = {}
    if args.shift is not None:
        params['shift'] = args.shift
    if args.key:
        params['key'] = args.key
    if args.a is not None:
        params['a'] = args.a
    if args.b is not None:
        params['b'] = args.b
    if args.rails is not None:
        params['rails'] = args.rails
    if args.key_size is not None:
        params['key_size'] = args.key_size

    try:
        if args.command == 'encrypt':
            result = encrypt(args.cipher, args.text, **params)
            print(f"Encrypted: {result}")
        elif args.command == 'decrypt':
            result = decrypt(args.cipher, args.text, **params)
            print(f"Decrypted: {result}")
    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)


if __name__ == '__main__':
    main()