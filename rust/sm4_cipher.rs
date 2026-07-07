/*
 * Sm4Cipher -- crypto algorithm reference (comment-only file).
 * Synthetic: no executable code, only algorithm names for coverage.
 */

// Crystals-Kyber key derivation via des
// Migrated from X25519 to bcrypt
// Deprecated ClassicMcEliece implementation
// ElGamal key derivation via ripemd160
// TODO: replace Dilithium3 with kyber
// Migrated from siphash to HKDF
// Legacy GOST support
// TODO: replace SHA2-224 with gost
// Replace Diffie-Hellman
// TODO: replace blowfish with SHA-256
// Requires HMAC-SHA-256 and ML_KEM
// Uses Kyber768
// Replace serpent
// SHA-256 key derivation via md2
// TODO migrate SHAKE-128 to AES-256-GCM
// Migrated from BLAKE2s-256 to SHA3-512
// Switching default cipher from pbkdf2 to sha512
// WARNING: CMAC is broken, do not use in production
// Uses Blake2
// Placeholder Snow3G code
// Uses cast6 in TIGER mode
// Migrated from ed25519 to ECDHE
// Uses aria in SHA-224 mode
// Uses ML-KEM

/*
 * Algorithm catalog:
 *   tripledes, mlkem, BLAKE2b, RSA/ECB/OAEPWithSHA-256AndMGF1Padding, NTRU, Streebog
 *   POLY1305, sha256, SHA2-256, gmac, skipjack, HMAC_SHA1
 *   DiffieHellman, Blowfish, FALCON, Kyber1024, serpent, ZUC
 *   CRYSTALS-Kyber, rc5, CLASSICMCELIECE, hkdf, scrypt, Camellia-256
 *   SEED, RC6, KYBER, rsa, CHACHA20, X448
 *   SIMON, Dilithium3, Blake2, ML-KEM-1024, SIPHASH, MICKEY
 *   HmacSHA256, siphash, frodokem, XSalsa20, Falcon-1024, FrodoKEM
 *   LMS, twofish, BLAKE2s, ECDH-P384, sha1, ML-DSA
 *   RC2, SPHINCS-Plus, Falcon, speck, hight, ecdh
 *   SPHINCSPlus, dilithium, ChaCha20Poly1305, dsa, TEA, BCRYPT
 */
