#!/usr/bin/env python3
"""Quantum-resistant symmetric primitives: AES-256-GCM, SHA-512, HMAC-SHA-256.

Symmetric crypto is only weakened by Grover's algorithm (effective security
halved), so 256-bit keys and >=384-bit hashes stay quantum-resistant.
AES-256-GCM needs `cryptography`; SHA-512 and HMAC are standard library.
"""
import hashlib
import hmac
import os
from cryptography.hazmat.primitives.ciphers.aead import AESGCM


def aes256_gcm(plaintext: bytes) -> bytes:
    key = AESGCM.generate_key(bit_length=256)
    nonce = os.urandom(12)
    return nonce + AESGCM(key).encrypt(nonce, plaintext, None)


def sha512(data: bytes) -> str:
    return hashlib.sha512(data).hexdigest()


def hmac_sha256(key: bytes, data: bytes) -> str:
    return hmac.new(key, data, hashlib.sha256).hexdigest()


if __name__ == "__main__":
    print("AES-256-GCM output len:", len(aes256_gcm(b"quantum-resistant")))
    print("SHA-512:", sha512(b"data")[:32])
    print("HMAC-SHA-256:", hmac_sha256(b"key", b"data")[:32])
