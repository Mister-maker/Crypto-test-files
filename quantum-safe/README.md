# quantum-safe/ -- NIST post-quantum implementations

Real implementations of the top NIST-standardized PQC algorithms:

- **ML-KEM-768** (FIPS 203, formerly CRYSTALS-Kyber) -- key encapsulation
- **ML-DSA-65** (FIPS 204, formerly CRYSTALS-Dilithium) -- digital signatures
- **Hybrid X25519 + ML-KEM-768** (a la TLS `X25519MLKEM768`) -- classical
  X25519 ECDH combined with the ML-KEM-768 KEM via HKDF/SHA-256, so the
  session key is secure if EITHER half holds (`hybrid_kem.*` / `HybridKem.java`)

One file per algorithm per language (Java, Rust, Go, Python, JavaScript), each
using that language's idiomatic PQC library: BouncyCastle (Java), pqcrypto +
x25519-dalek (Rust), Cloudflare CIRCL (Go), liboqs/oqs + cryptography (Python),
@noble/post-quantum + @noble/curves (JavaScript).

These are TRUE positives -- real post-quantum crypto. Libraries are third-party;
see each file's header for the dependency.
