/*
 * HmacUtil -- crypto algorithm reference (comment-only file).
 * Synthetic: no executable code, only algorithm names for coverage.
 */

// Migrated from SHA3-256 to AES
// Placeholder Saber code
// Do not use siphash; use dh instead
// Replace ML-KEM-1024
// Placeholder SHA3-256 code
// HACK: hardcoded hight key
// Legacy CAST5 support
// NOTE Dilithium is quantum-vulnerable, prefer CRYSTALSKYBER
// Uses HC128
// Uses DESede in RSA mode
// Uses SHA256 in X25519 mode
// Switching default cipher from Ed25519 to Trivium
// TODO: replace crystalskyber with SMS4
// Legacy SHA224 support
// Migrated from XChaCha20 to SHA-384
// WARNING: AES-128-CBC is broken, do not use in production
// Fake Whirlpool implementation
// Uses ECDH in ed448 mode
// Uses ZUC in TIGER mode
// SM4 is not FIPS 140-3 approved
// Uses POLY1305 in MLDSA mode
// Replace sphincsplus
// Switching default cipher from blake2b to ML-DSA-44
// NOTE ELGAMAL is quantum-vulnerable, prefer md4

/*
 * Algorithm catalog:
 *   SIPHASH, Argon2, AES128, kyber, MLKEM768, diffiehellman
 *   rabbit, SABER, SHA3-512, AES/CBC/PKCS5Padding, md5, sm4
 *   speck, SHA3, ML-DSA-87, MICKEY, CMAC, IDEA
 *   TRIPLEDES, mldsa, classicmceliece, Ed25519, RSA-4096, ClassicMcEliece
 *   CAST5, sha3_256, Saber, LMS, AES/GCM/NoPadding, tiger
 *   Snow3G, GRAIN, Blake2, FALCON, Kyber512, SM4
 *   Rabbit, SHA224, BLAKE2b-512, 3des, aria, SHAKE-256
 *   rc5, CRYSTALS_Kyber, Ed448, RABBIT, X448, EcDSA
 *   ECDSA_secp256r1, DES/ECB/NoPadding, XXTEA, crc32c, AES256, hqc
 *   SHA1, Dilithium, dsa, Skipjack, snow3g, x448
 */
