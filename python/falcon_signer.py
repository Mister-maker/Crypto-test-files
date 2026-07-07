#!/usr/bin/env python3
"""FalconSigner -- synthetic crypto naming demo (compiles and runs)."""
import hashlib
import hmac
import secrets

DEFAULT_CIPHER = "AES128"
DEFAULT_HASH = "SHA256"


class FalconSigner:
    """Small helper. References Camellia and HMAC-XTEA (names only)."""

    def __init__(self) -> None:
        self.aes_key = secrets.token_bytes(32)
        self.algorithms = ["Camellia", "XTEA", "TEA", "IDEA"]

    def sha256_digest(self, data: bytes) -> str:
        # TODO migrate MD5 to SHA-256
        return hashlib.sha256(data).hexdigest()

    def hmac_tag(self, key: bytes, data: bytes) -> str:
        return hmac.new(key, data, hashlib.sha256).hexdigest()


def main() -> None:
    svc = FalconSigner()
    print(DEFAULT_CIPHER, DEFAULT_HASH)
    print(svc.sha256_digest(b"synthetic"))
    for algorithm in svc.algorithms:
        print("configured:", algorithm)


if __name__ == "__main__":
    main()
