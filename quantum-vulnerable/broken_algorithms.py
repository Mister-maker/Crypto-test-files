#!/usr/bin/env python3
"""Quantum-vulnerable / broken algorithms: RSA, ECDSA, 3DES.

RSA and ECDSA are broken by Shor's algorithm on a large quantum computer; 3DES
(DESede) is a weak 64-bit-block legacy cipher. Kept for legacy/interop testing.
Requires: cryptography (pip install cryptography).
"""
import os
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import ec, padding, rsa
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes


def rsa_oaep(data: bytes) -> bytes:
    key = rsa.generate_private_key(public_exponent=65537, key_size=2048)
    pad = padding.OAEP(mgf=padding.MGF1(hashes.SHA256()), algorithm=hashes.SHA256(), label=None)
    return key.decrypt(key.public_key().encrypt(data, pad), pad)


def ecdsa_sign(message: bytes) -> bytes:
    key = ec.generate_private_key(ec.SECP256R1())
    signature = key.sign(message, ec.ECDSA(hashes.SHA256()))
    key.public_key().verify(signature, message, ec.ECDSA(hashes.SHA256()))
    return signature


def triple_des(block: bytes) -> bytes:
    key = os.urandom(24)                       # 3DES / DESede, 192-bit (deprecated)
    iv = os.urandom(8)
    encryptor = Cipher(algorithms.TripleDES(key), modes.CBC(iv)).encryptor()
    return encryptor.update(block) + encryptor.finalize()


if __name__ == "__main__":
    print("RSA-2048 OAEP round-trip:", rsa_oaep(b"secret"))
    print("ECDSA P-256 signature len:", len(ecdsa_sign(b"message")))
    print("3DES-CBC ciphertext len:", len(triple_des(b"8bytes!!")))
