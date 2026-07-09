#!/usr/bin/env python3
"""Correct digital signatures with Ed25519."""
from cryptography.exceptions import InvalidSignature
from cryptography.hazmat.primitives.asymmetric.ed25519 import Ed25519PrivateKey


def demo() -> None:
    private_key = Ed25519PrivateKey.generate()
    public_key = private_key.public_key()
    message = b"sign me"
    signature = private_key.sign(message)
    try:
        public_key.verify(signature, message)    # raises if tampered
        print("Ed25519 signature verified")
    except InvalidSignature:
        print("Ed25519 verification failed")


if __name__ == "__main__":
    demo()
