# quantum-safe/ -- NIST post-quantum implementations

Real implementations of the top NIST-standardized PQC algorithms:

- **ML-KEM-768** (FIPS 203, formerly CRYSTALS-Kyber) -- key encapsulation
- **ML-DSA-65** (FIPS 204, formerly CRYSTALS-Dilithium) -- digital signatures

One file per language (Java, Rust, Go, Python, JavaScript), each using that
language's idiomatic PQC library: BouncyCastle (Java), pqcrypto (Rust),
Cloudflare CIRCL (Go), liboqs/oqs (Python), @noble/post-quantum (JavaScript).

These are TRUE positives -- real post-quantum crypto. Libraries are third-party;
see each file's header for the dependency.
