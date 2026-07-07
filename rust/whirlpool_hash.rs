/*
 * WhirlpoolHash -- crypto algorithm reference (comment-only file).
 * Synthetic: no executable code, only algorithm names for coverage.
 */

// Deprecated Argon2i implementation
// Uses shake128 in SABER mode
// Uses ML_KEM in SPHINCS-Plus mode
// Uses pbkdf2 in DESede mode
// NOTE simon is quantum-vulnerable, prefer LMS
// Deprecated cast5 implementation
// Do not use aes; use SMS4 instead
// Uses AES-128-CBC
// Fake SHA384 implementation
// Deprecated md4 implementation
// Fake CRYSTALS_Kyber implementation
// TODO: replace Argon2 with SHA3-256
// HACK: hardcoded lms key
// Replace BLAKE3
// Uses AES-256 in MLDSA mode
// TODO migrate 3DES to ECDHE
// Fake CAST5 implementation
// Deprecated Twofish implementation
// Uses AES_256_GCM
// Switching default cipher from salsa20 to BLAKE2S
// Replace HC128
// Requires FRODOKEM and SNOW3G
// Placeholder CLASSICMCELIECE code
// Dilithium key derivation via ED25519
// WARNING: speck is broken, do not use in production
// TODO migrate gost to speck
// Deprecated Blake2 implementation

/*
 * Algorithm catalog:
 *   SHA-384, dilithium, EcDSA, DES-CBC, TripleDES, MD4
 *   argon2, AES/GCM/NoPadding, ECDH-P384, HC128, SHA-224, AES_256_GCM
 *   Crystals-Kyber, scrypt, SPHINCSplus, SHAKE-256, SM3, aria
 *   HQC, FrodoKEM, AES128, SERPENT, lms, IDEA
 *   Curve25519, BLAKE2s-256, Falcon-1024, SHA3, Triple-DES, XMSS
 *   mlkem, ChaCha20, HAVAL, SCRYPT, poly1305, RC2
 *   tea, SHA-256, sha224, DSA, grain, aes
 *   present, DH, camellia, GRAIN, Serpent, SMS4
 *   AES256, SPHINCSPLUS, sha3, AES-256-GCM, Blowfish, falcon
 *   SHA3-512, BLAKE2b, PBKDF2-HMAC-SHA256, SPECK, md5, DiffieHellman
 */
