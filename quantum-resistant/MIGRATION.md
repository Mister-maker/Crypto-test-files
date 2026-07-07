# PQC Migration Notes (synthetic)

**Harvest now, decrypt later**: adversaries can record RSA/ECDH-protected
traffic today and decrypt it once a cryptographically-relevant quantum
computer exists.

| Legacy (quantum-vulnerable) | Replace with (PQC) |
|---|---|
| RSA-2048 / RSA-4096 key transport | ML-KEM-768 (Kyber) |
| ECDH / X25519 key agreement | X25519MLKEM768 hybrid |
| RSA-PSS / ECDSA / Ed25519 signatures | ML-DSA-65 or SLH-DSA |
| Long-lived firmware signing | LMS / XMSS (stateful hash-based) |

TODO: inventory all RSA, DH, ECDH, ECDSA, EdDSA usage and stage the
migration to ML-KEM, ML-DSA, Falcon and SLH-DSA (FIPS 203/204/205).
