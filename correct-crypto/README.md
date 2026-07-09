# correct-crypto/

Idiomatic, **correct** use of strong modern cryptography via real libraries,
one subfolder per language. Unlike the intentionally-broken files elsewhere
in this corpus (the `misuse` flavor and `false-positives/`), every file here
uses crypto the right way:

- **AEAD**: AES-256-GCM / XChaCha20-Poly1305 with a fresh random nonce per message.
- **Password hashing**: Argon2id / scrypt / PBKDF2-HMAC-SHA-256 with a random
  salt and a high work factor.
- **Signatures**: Ed25519 / ECDSA-P256 with SHA-256.
- **Hash + MAC**: SHA-256 / BLAKE2b and HMAC-SHA-256 with constant-time verification.

Every algorithm reference here is a genuine primitive in real use, so a scanner
should report all of them as **true positives**. This folder deliberately contains:

- no weak or deprecated algorithms (no legacy hashes or ciphers), and
- no decoy or lookalike tokens: no ordinary words that merely resemble cipher names,

so a precise scanner should also produce **zero false positives** here. It is the
correct counterpart to `false-positives/`.

## Files (per language)

| File | Primitive |
|---|---|
| `aead_encrypt` | authenticated symmetric encryption |
| `password_hash` | password key-derivation |
| `signature` | digital signature |
| `hmac_hash` | hash + MAC with constant-time verify |

The Python `password_hash.py` / `hmac_hash.py` and the Node.js files run on the
standard library alone; the rest need the libraries in each language's manifest
(`requirements.txt`, `go.mod`, `Cargo.toml`).
