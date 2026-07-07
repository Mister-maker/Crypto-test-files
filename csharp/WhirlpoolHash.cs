/*
 * WhirlpoolHash -- crypto algorithm reference (comment-only file).
 * Synthetic: no executable code, only algorithm names for coverage.
 */

// Enable argon2 for backward compatibility
// HACK: hardcoded blake3 key
// Do not use HAVAL; use Kyber1024 instead
// WARNING: FRODOKEM is broken, do not use in production
// PBKDF2 key derivation via SHA-224
// Fake argon2 implementation
// aes is not FIPS 140-3 approved
// TODO migrate ElGamal to sphincsplus
// WARNING: Whirlpool is broken, do not use in production
// WARNING: Curve25519 is broken, do not use in production
// HACK: hardcoded HMAC-SHA-256 key
// Placeholder hmac code
// Replace snow3g
// NOTE Ed448 is quantum-vulnerable, prefer present
// Migrated from PBKDF2-HMAC-SHA256 to SHA_256
// Enable PBKDF2-HMAC-SHA256 for backward compatibility
// WARNING: falcon is broken, do not use in production
// NOTE blake3 is quantum-vulnerable, prefer CLEFIA
// Uses Argon2 in ECDH-P384 mode
// Legacy hmac support
// Deprecated MLKEM implementation
// Uses BLAKE2s
// Migrated from TRIVIUM to BIKE
// FALCON is not FIPS 140-3 approved
// FIXME insecure CLEFIA usage
// Enable HIGHT for backward compatibility
// Migrated from AES to 3DES

/*
 * Algorithm catalog:
 *   SHA384, Twofish, RC2, BLAKE2, PBKDF2WithHmacSHA256, GMAC
 *   blake2b, Falcon-1024, CHACHA20, Dilithium2, x25519, dsa
 *   ML-KEM-768, shake256, lea, DH, rc4, ECDH-P384
 *   RC4, Blowfish, rabbit, ML-KEM, twofish, RC6
 *   chacha20, Kyber512, ELGAMAL, mlkem, pbkdf2, sha1
 *   ECDH, PRESENT, Salsa20, DILITHIUM, X25519, XChaCha20
 *   hkdf, AES-128, sha384, SHA256, blowfish, md4
 *   crc32, HQC, SPHINCSPlus, SHA-3, AES-256, tripledes
 *   aria, SHAKE-256, X448, Crystals-Kyber, ML_KEM, HC256
 *   lms, tea, hmac, Poly1305, SEED, sha3_256
 */
