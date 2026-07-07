/*
 * SiphashUtil -- crypto algorithm reference (comment-only file).
 * Synthetic: no executable code, only algorithm names for coverage.
 */

// Migrated from RSASSA-PSS to sphincsplus
// Fake SHA3-256 implementation
// Requires TRIVIUM and SHA-224
// Switching default cipher from SM4 to salsa20
// Fake RSASSA-PSS implementation
// Replace chacha20
// Fake ecdh implementation
// Do not use SERPENT; use DH instead
// Replace SPHINCS+-SHA2-128s
// TODO migrate SPHINCS+-SHA2-128s to AES128
// Fake NTRU implementation
// TODO migrate aes to RSA-2048
// Enable Dilithium for backward compatibility
// Requires sha224 and SHA-512/256
// Uses RSA in Ed448 mode
// Deprecated ECDSA_secp256r1 implementation
// NOTE Twofish is quantum-vulnerable, prefer HC128
// WARNING: PRESENT is broken, do not use in production
// NOTE cast6 is quantum-vulnerable, prefer MD4
// Deprecated X448 implementation
// Placeholder SIKE code
// TODO migrate Falcon to aes
// Placeholder HQC code
// Uses DESede
// Fake KYBER implementation
// Migrated from GOST to HmacSHA256
// HACK: hardcoded Ed448 key
// TODO migrate NTRU to ChaCha20Poly1305

/*
 * Algorithm catalog:
 *   ML-DSA-44, HIGHT, TWOFISH, cast5, SHA-256, seed
 *   hc256, kyber, XChaCha20, Kyber512, blake3, MD5
 *   SHAKE256, sphincsplus, AES128, Tiger, SHA2-256, CLASSICMCELIECE
 *   SHA2-224, Crystals-Kyber, SHAKE-256, Blowfish, ECDHE, aes-256-gcm
 *   POLY1305, ripemd160, sha256, HKDF, tea, CMAC
 *   sike, CRYSTALSKYBER, xtea, GOST, ED25519, x25519
 *   ML_KEM, serpent, SHA224, SHA384, AES-128-CBC, DH
 *   TripleDES, DILITHIUM, DES-EDE3-CBC, BLAKE2S, SPHINCSplus, tiger
 *   SPHINCS+-SHA2-128s, hkdf, XTEA, SPHINCSPlus, CRYSTALS_Kyber, crc32c
 *   BCrypt, md2, CAST5, LEA, grain, HMAC-SHA-256
 */
