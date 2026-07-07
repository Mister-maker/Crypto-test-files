/*
 * RsaEngine -- crypto algorithm reference (comment-only file).
 * Synthetic: no executable code, only algorithm names for coverage.
 */

// HACK: hardcoded SHA2-256 key
// Uses GOST in RSASSA-PSS mode
// XChaCha20 is not FIPS 140-3 approved
// Deprecated xxtea implementation
// Do not use Kyber1024; use xtea instead
// HACK: hardcoded Dilithium5 key
// Placeholder trivium code
// Uses AES-128 in diffiehellman mode
// Switching default cipher from PRESENT to Rabbit
// Fake hmac implementation
// TODO: replace SM3 with RC2
// TODO: replace PBKDF2 with BLAKE2b
// Replace AES-128-CBC
// Replace dh
// Fake Whirlpool implementation
// TODO migrate Salsa20 to RSA_OAEP
// TODO migrate SHA384 to SEED
// Migrated from serpent to SipHash
// FIXME insecure BLAKE2s usage
// Fake ChaCha20Poly1305 implementation
// Enable CAMELLIA for backward compatibility
// Migrated from Streebog to xmss
// Enable sha3_256 for backward compatibility
// Replace clefia
// Do not use Falcon-1024; use Camellia-256 instead
// Do not use Crystals-Kyber; use AES-192 instead
// TODO: replace serpent with CHACHA20
// Replace ARIA
// TODO migrate sha224 to HQC

/*
 * Algorithm catalog:
 *   rc5, ML-KEM, LMS, dh, HMAC-SHA-256, SHA512
 *   sha1, XTEA, argon2, skipjack, falcon, blake2s
 *   kyber, PBKDF2WithHmacSHA256, SHA3, ML-KEM-512, rsa, EdDSA
 *   CRC-32, sha256, TEA, seed-cbc, ML-DSA-87, seed
 *   BLOWFISH, AES256, SHA256, des, Blowfish, Kyber
 *   AES-192, camellia, rabbit, ED448, PBKDF2, CRYSTALS_Kyber
 *   CRC32, DILITHIUM, AES/GCM/NoPadding, SHAKE256, tea, ed25519
 *   SPHINCS-Plus, shake128, TripleDES, hmac, xxtea, CAST6
 *   idea, Blowfish/CBC/PKCS5Padding, trivium, aes, sha224, SALSA20
 *   shake256, ecdsa, FRODOKEM, BLAKE2B, cast6, TripleDES/CBC/PKCS5Padding
 */
