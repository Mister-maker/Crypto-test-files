# quantum-vulnerable/ -- broken / weak algorithm implementations

Algorithms broken by a quantum computer (Shor's algorithm) or already weak /
deprecated:

- **RSA-2048 (OAEP)** -- broken by Shor
- **ECDSA (P-256)** -- broken by Shor
- **3DES (DESede)** -- weak 64-bit-block legacy cipher

Correct, idiomatic implementations, one file per language:

| File | Language |
|---|---|
| `BrokenAlgorithms.java` | Java (JCA) |
| `broken_algorithms.py` | Python (cryptography) |
| `broken_algorithms.go` | Go (crypto/*) |
| `broken_algorithms.rs` | Rust (rsa, p256, des) |
| `brokenAlgorithms.js` | JavaScript (node:crypto) |

Real (if insecure/legacy) crypto -> a scanner should detect every algorithm here
as a true positive, and ideally flag them as quantum-vulnerable / deprecated.
