# quantum-resistant/ -- symmetric (quantum-resistant) implementations

In this corpus's taxonomy, **quantum-resistant = symmetric** primitives that stay
secure against quantum attacks at adequate sizes (only weakened by Grover's
algorithm, so use 256-bit keys / >=384-bit hashes):

- **AES-256-GCM** -- authenticated encryption
- **SHA-512** -- hashing
- **HMAC-SHA-256** -- message authentication

Correct, idiomatic implementations, one file per language:

| File | Language |
|---|---|
| `SymmetricPrimitives.java` | Java (JCA) |
| `symmetric_primitives.py` | Python (cryptography + stdlib) |
| `symmetric_primitives.go` | Go (crypto/*) |
| `symmetric_primitives.rs` | Rust (aes-gcm, sha2, hmac) |
| `symmetricPrimitives.js` | JavaScript (node:crypto) |

All real crypto -> a scanner should detect every algorithm here as a true positive.
