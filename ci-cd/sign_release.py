#!/usr/bin/env python3
"""CI/CD release signing and integrity checks.

Runs in the release pipeline: computes SHA-256 checksums for build artifacts,
signs the checksum manifest with Ed25519, and verifies incoming CI webhooks with
HMAC-SHA-256. All secrets come from the CI environment -- never hardcoded in the
repo. Requires: cryptography (pip install cryptography).
"""
import base64
import hashlib
import hmac
import os
import pathlib


def sha256_checksum(path: pathlib.Path) -> str:
    """SHA-256 of a build artifact, streamed so large files fit in memory."""
    digest = hashlib.sha256()
    with path.open("rb") as fh:
        for chunk in iter(lambda: fh.read(65536), b""):
            digest.update(chunk)
    return digest.hexdigest()


def build_manifest(dist_dir: str) -> str:
    """Produce a SHA256SUMS-style manifest for everything in the dist dir."""
    lines = []
    for artifact in sorted(pathlib.Path(dist_dir).glob("*")):
        if artifact.is_file():
            lines.append(f"{sha256_checksum(artifact)}  {artifact.name}")
    return "\n".join(lines) + "\n"


def sign_manifest(manifest: str) -> str:
    """Sign the checksum manifest with the pipeline's Ed25519 release key."""
    from cryptography.hazmat.primitives.asymmetric.ed25519 import Ed25519PrivateKey

    seed_b64 = os.environ["CI_SIGNING_KEY"]        # 32-byte Ed25519 seed, base64, from CI secrets
    private_key = Ed25519PrivateKey.from_private_bytes(base64.b64decode(seed_b64))
    signature = private_key.sign(manifest.encode())
    return base64.b64encode(signature).decode()


def verify_webhook(payload: bytes, signature_header: str) -> bool:
    """Verify an incoming CI webhook with HMAC-SHA-256 (constant-time compare)."""
    secret = os.environ["CI_WEBHOOK_SECRET"].encode()
    expected = hmac.new(secret, payload, hashlib.sha256).hexdigest()
    return hmac.compare_digest(expected, signature_header)


def main() -> None:
    dist_dir = os.environ.get("DIST_DIR", "dist")
    manifest = build_manifest(dist_dir)
    pathlib.Path("SHA256SUMS").write_text(manifest)
    pathlib.Path("SHA256SUMS.sig").write_text(sign_manifest(manifest))
    print("Signed release manifest with Ed25519 -> SHA256SUMS + SHA256SUMS.sig")


if __name__ == "__main__":
    main()
