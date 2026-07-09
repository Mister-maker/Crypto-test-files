#!/usr/bin/env python3
"""Hybrid PQC KEM: X25519 + ML-KEM-768 (a la TLS X25519MLKEM768).

Combines a classical X25519 ECDH shared secret with an ML-KEM-768 (FIPS 203)
encapsulated shared secret via HKDF, so the session key stays secure if EITHER
the classical or the post-quantum half holds. Requires: cryptography, oqs.
"""
import oqs
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric.x25519 import X25519PrivateKey
from cryptography.hazmat.primitives.kdf.hkdf import HKDF


def _combine(ss_pq: bytes, ss_classical: bytes) -> bytes:
    return HKDF(algorithm=hashes.SHA256(), length=32, salt=None,
                info=b"X25519MLKEM768").derive(ss_pq + ss_classical)


def demo() -> bool:
    with oqs.KeyEncapsulation("ML-KEM-768") as kem:
        mlkem_pub = kem.generate_keypair()
        recipient_x = X25519PrivateKey.generate()

        # sender: ML-KEM-768 encapsulate + ephemeral X25519 ECDH
        eph = X25519PrivateKey.generate()
        mlkem_ct, ss_pq_send = kem.encap_secret(mlkem_pub)
        ss_classical_send = eph.exchange(recipient_x.public_key())
        sender_secret = _combine(ss_pq_send, ss_classical_send)

        # recipient: ML-KEM-768 decapsulate + X25519 ECDH
        ss_pq_recv = kem.decap_secret(mlkem_ct)
        ss_classical_recv = recipient_x.exchange(eph.public_key())
        recipient_secret = _combine(ss_pq_recv, ss_classical_recv)
        return sender_secret == recipient_secret


if __name__ == "__main__":
    print("X25519 + ML-KEM-768 hybrid secret match:", demo())
