#!/usr/bin/env python3
"""Correct authenticated encryption with AES-256-GCM (AEAD).

A fresh random 96-bit nonce is generated per message and never reused; GCM
provides both confidentiality and integrity, and the associated data is
authenticated but not encrypted.
"""
import os
from cryptography.hazmat.primitives.ciphers.aead import AESGCM


def encrypt(key: bytes, plaintext: bytes, aad: bytes = b"") -> bytes:
    nonce = os.urandom(12)                       # unique per message
    ciphertext = AESGCM(key).encrypt(nonce, plaintext, aad)
    return nonce + ciphertext                    # prepend nonce for the receiver


def decrypt(key: bytes, blob: bytes, aad: bytes = b"") -> bytes:
    nonce, ciphertext = blob[:12], blob[12:]
    return AESGCM(key).decrypt(nonce, ciphertext, aad)


if __name__ == "__main__":
    key = AESGCM.generate_key(bit_length=256)
    blob = encrypt(key, b"correct and secure", b"header")
    assert decrypt(key, blob, b"header") == b"correct and secure"
    print("AES-256-GCM round-trip OK")
