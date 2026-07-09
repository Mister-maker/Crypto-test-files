#!/usr/bin/env python3
"""Quantum-safe NIST PQC: ML-KEM-768 (FIPS 203) and ML-DSA-65 (FIPS 204).

Uses liboqs via the `oqs` Python binding (pip install liboqs-python). ML-KEM
(formerly CRYSTALS-Kyber) is key encapsulation; ML-DSA (formerly CRYSTALS-
Dilithium) is digital signatures.
"""
import oqs


def mlkem768_kem() -> bool:
    with oqs.KeyEncapsulation("ML-KEM-768") as kem:
        public_key = kem.generate_keypair()
        ciphertext, shared_secret = kem.encap_secret(public_key)
        return kem.decap_secret(ciphertext) == shared_secret


def mldsa65_sign(message: bytes) -> bool:
    with oqs.Signature("ML-DSA-65") as signer:
        public_key = signer.generate_keypair()
        signature = signer.sign(message)
        return signer.verify(message, signature, public_key)


if __name__ == "__main__":
    print("ML-KEM-768 shared-secret match:", mlkem768_kem())
    print("ML-DSA-65 verified:", mldsa65_sign(b"message"))
