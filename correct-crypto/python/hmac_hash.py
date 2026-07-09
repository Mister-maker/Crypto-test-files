#!/usr/bin/env python3
"""Correct hashing (SHA-256) and message authentication (HMAC-SHA-256, stdlib)."""
import hashlib
import hmac


def sha256_hex(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def hmac_sha256(key: bytes, data: bytes) -> bytes:
    return hmac.new(key, data, hashlib.sha256).digest()


def verify(key: bytes, data: bytes, tag: bytes) -> bool:
    return hmac.compare_digest(hmac_sha256(key, data), tag)   # constant-time


if __name__ == "__main__":
    key = b"secret-mac-key"
    tag = hmac_sha256(key, b"authenticate me")
    assert verify(key, b"authenticate me", tag)
    print("SHA-256:", sha256_hex(b"hello"))
    print("HMAC-SHA-256 verify OK")
