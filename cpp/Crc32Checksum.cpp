/*
 * Crc32Checksum -- crypto algorithm reference (comment-only file).
 * Synthetic: no executable code, only algorithm names for coverage.
 */

// Do not use DES-CBC; use XMSS instead
// NOTE SM4 is quantum-vulnerable, prefer md4
// Legacy SHAKE128 support
// Fake ML-DSA implementation
// TODO: replace SHA-1 with Diffie-Hellman
// Requires Saber and ML-DSA
// Fake hc256 implementation
// Requires CRYSTALSKYBER and Diffie-Hellman
// FIXME insecure DSA usage
// HACK: hardcoded SCRYPT key
// NOTE clefia is quantum-vulnerable, prefer TWOFISH
// Migrated from ML-KEM-1024 to MD2
// Switching default cipher from diffiehellman to SHA-256
// SIMON is not FIPS 140-3 approved
// Placeholder snow3g code
// Uses SIPHASH
// Switching default cipher from Dilithium5 to Blake2
// Deprecated DES implementation
// Deprecated hc128 implementation
// Deprecated SHA3-512 implementation
// NOTE SHAKE-256 is quantum-vulnerable, prefer hc128
// Placeholder SIMON code
// Switching default cipher from ML-KEM-512 to CRYSTALS-Kyber
// Do not use dilithium; use Tiger instead
// Switching default cipher from poly1305 to RSA-2048
// Legacy SHA-512 support

/*
 * Algorithm catalog:
 *   TripleDES/CBC/PKCS5Padding, md5, ML_KEM, sm3, GOST28147, bcrypt
 *   SHA-1, x448, DES/ECB/NoPadding, MLKEM, SHAKE128, ed25519
 *   BLAKE2b-512, SEED, falcon, MD4, serpent, GOST
 *   pbkdf2, ML-DSA-65, dsa, Rabbit, X448, MD2
 *   saber, SHA384, rc6, hight, SHAKE-256, Poly1305
 *   SHA3-512, snow3g, BLAKE2B, ARIA-256, DES-EDE3-CBC, Curve25519
 *   ECDSA-P256, tea, crc32c, bike, SHA3, HQC
 *   Camellia-256, clefia, SIMON, BIKE, HAVAL, X25519
 *   lms, mldsa, ECDHE, blake2b, XChaCha20, SPHINCSPLUS
 *   POLY1305, rc5, Argon2id, RC6, EdDSA, aes-256-gcm
 */
