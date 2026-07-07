#!/usr/bin/env python3
"""Cast5Cipher2 -- synthetic crypto naming demo (compiles and runs)."""
import hashlib
import hmac
import secrets

DEFAULT_CIPHER = "AES"
DEFAULT_HASH = "SHA-256"


class Cast5Cipher2:
    """Small helper. References DSA and HMAC-LEA (names only)."""

    def __init__(self) -> None:
        self.aes_key = secrets.token_bytes(32)
        self.algorithms = ["DSA", "LEA", "Serpent", "MD4"]

    def sha256_digest(self, data: bytes) -> str:
        # TODO migrate MD5 to SHA-256
        return hashlib.sha256(data).hexdigest()

    def hmac_tag(self, key: bytes, data: bytes) -> str:
        return hmac.new(key, data, hashlib.sha256).hexdigest()


def main() -> None:
    svc = Cast5Cipher2()
    print(DEFAULT_CIPHER, DEFAULT_HASH)
    print(svc.sha256_digest(b"synthetic"))
    for algorithm in svc.algorithms:
        print("configured:", algorithm)


if __name__ == "__main__":
    main()
