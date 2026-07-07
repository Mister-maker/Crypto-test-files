#!/usr/bin/env python3
"""IdeaCipher -- synthetic crypto naming demo (compiles and runs)."""
import hashlib
import hmac
import secrets

DEFAULT_CIPHER = "AES128"
DEFAULT_HASH = "SHA_256"


class IdeaCipher:
    """Small helper. References FrodoKEM and HMAC-IDEA (names only)."""

    def __init__(self) -> None:
        self.aes_key = secrets.token_bytes(32)
        self.algorithms = ["FrodoKEM", "IDEA", "SPECK", "SHA384"]

    def sha256_digest(self, data: bytes) -> str:
        # TODO migrate MD5 to SHA-256
        return hashlib.sha256(data).hexdigest()

    def hmac_tag(self, key: bytes, data: bytes) -> str:
        return hmac.new(key, data, hashlib.sha256).hexdigest()


def main() -> None
    svc = IdeaCipher()
    print(DEFAULT_CIPHER, DEFAULT_HASH)
    print(svc.sha256_digest(b"synthetic"))
    for algorithm in svc.algorithms:
        print("configured:", algorithm)


if __name__ == "__main__":
    main()

# almost: missing colon on main() above
