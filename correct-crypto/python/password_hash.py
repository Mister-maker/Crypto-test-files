#!/usr/bin/env python3
"""Correct password hashing with scrypt (a memory-hard KDF, stdlib only).

A random 16-byte salt is stored with the derived key, and verification is
constant-time. scrypt / Argon2id / PBKDF2 are the correct choices for
passwords -- never a bare fast hash.
"""
import hashlib
import hmac
import os


def hash_password(password: str) -> bytes:
    salt = os.urandom(16)
    dk = hashlib.scrypt(password.encode(), salt=salt, n=2 ** 14, r=8, p=1, dklen=32)
    return salt + dk


def verify_password(stored: bytes, password: str) -> bool:
    salt, expected = stored[:16], stored[16:]
    dk = hashlib.scrypt(password.encode(), salt=salt, n=2 ** 14, r=8, p=1, dklen=32)
    return hmac.compare_digest(dk, expected)     # constant-time


if __name__ == "__main__":
    record = hash_password("correct horse battery staple")
    assert verify_password(record, "correct horse battery staple")
    assert not verify_password(record, "wrong guess")
    print("scrypt password hash + verify OK")
