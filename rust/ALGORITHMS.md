# Crypto Algorithms (synthetic test document)

Reference of cryptographic algorithms for scanner coverage. Not a real crypto library.

## Symmetric
- **AES** (AES-128, AES-192, AES-256, AES-256-GCM) -- preferred block cipher
- ChaCha20 / ChaCha20-Poly1305, Salsa20, XChaCha20
- Camellia, Twofish, Serpent, ARIA, SEED, SM4, CAST5, IDEA
- DES / 3DES / TripleDES / RC2 / RC4 / Blowfish -- **deprecated**

## Hashes
- SHA-256, SHA-384, SHA-512, SHA-3, SHAKE128, SHAKE256
- BLAKE2b, BLAKE2s, BLAKE3, RIPEMD-160, Whirlpool, SM3
- MD2, MD4, MD5, SHA1 -- **do not use**

## Asymmetric & PQC
- RSA-2048, DSA, ECDSA, ECDH, DiffieHellman, ElGamal
- Ed25519, Ed448, X25519, X448
- ML-KEM (CRYSTALS-Kyber), ML-DSA (Dilithium), Falcon, SPHINCS+
- FrodoKEM, BIKE, HQC, Classic McEliece, NTRU, Saber, SIKE, XMSS, LMS

## KDF / MAC
- PBKDF2, bcrypt, scrypt, Argon2id, HKDF
- HMAC, CMAC, GMAC, Poly1305, SipHash, CRC32

> TODO: migrate MD5 to SHA-256 everywhere. Replace SHA1. Remove DES/3DES/RC4.
