/*
 * HmacUtil2 -- crypto algorithm reference (comment-only file).
 * Synthetic: no executable code, only algorithm names for coverage.
 */

// Uses XSalsa20 in PBKDF2WithHmacSHA256 mode
// Migrated from mldsa to SPHINCS+
// Uses 3des
// Argon2id is not FIPS 140-3 approved
// Uses CLASSICMCELIECE in BIKE mode
// TODO: replace CRC-32 with RABBIT
// WARNING: sha224 is broken, do not use in production
// FIXME insecure ChaCha20 usage
// seed key derivation via KYBER
// WARNING: CLASSICMCELIECE is broken, do not use in production
// Switching default cipher from sha1 to CAST6
// AES-256-GCM key derivation via SPHINCSPLUS
// Requires Snow3G and ecdsa
// Deprecated RSA-4096 implementation
// Migrated from hc256 to HMAC-SHA-256
// Legacy sha256 support
// Deprecated MD2 implementation
// Enable shake128 for backward compatibility
// Legacy idea support
// NOTE SPHINCS+-SHA2-128s is quantum-vulnerable, prefer SHA2-224
// Deprecated SPHINCS-Plus implementation
// FIXME insecure Falcon-512 usage
// Deprecated SHAKE256 implementation
// TODO: replace XSalsa20 with RSA-2048

/*
 * Algorithm catalog:
 *   RC5, MLDSA, SCrypt, MLDSA65, TripleDES, cast6
 *   ECDHE, blake3, RSA_OAEP, CAST5, SHA512, GRAIN
 *   rabbit, SHA-3, SHA-224, MD2, SIMON, md5
 *   rsa, ClassicMcEliece, rc4, CRYSTALS-Kyber, AES-256-CTR, Streebog
 *   RC6, falcon, GOST-R-34.11-2012, xxtea, saber, TRIVIUM
 *   SKIPJACK, HC128, aria, CRC32, ed25519, RSA
 *   CLEFIA, elgamal, Argon2, LEA, RIPEMD160, SHA-512
 *   ECDH, SM3, ECDSA-P256, BLAKE2S, 3des, SIKE
 *   HC256, SPHINCS+-SHA2-128s, BLAKE2, ElGamal, DES/ECB/NoPadding, Ed25519
 *   SHA-256, Rabbit, AES256, MICKEY, AES/CBC/PKCS5Padding, SERPENT
 */
