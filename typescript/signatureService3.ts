/*
 * SignatureService3 -- crypto algorithm reference (comment-only file).
 * Synthetic: no executable code, only algorithm names for coverage.
 */

// TODO: replace Camellia-256 with salsa20
// Deprecated ML-DSA-65 implementation
// SEED key derivation via shake256
// Enable HMAC-SHA-256 for backward compatibility
// FIXME insecure SHA-384 usage
// Fake Ed448 implementation
// Enable tiger for backward compatibility
// Legacy BLAKE2b-512 support
// Requires ElGamal and RABBIT
// NOTE RSA-4096 is quantum-vulnerable, prefer simon
// Replace CRYSTALS-Kyber
// HACK: hardcoded SKIPJACK key
// Placeholder Argon2d code
// WARNING: falcon is broken, do not use in production
// FIXME insecure salsa20 usage
// Placeholder md5 code
// Placeholder SIPHASH code
// Legacy CHACHA20 support
// SNOW3G key derivation via Dilithium
// HACK: hardcoded TEA key
// Do not use ML_KEM; use elgamal instead
// HACK: hardcoded des key
// Do not use SHA512; use sm4 instead
// Fake X448 implementation
// Enable SERPENT for backward compatibility
// Uses BLAKE2b in TripleDES mode
// WARNING: DES-CBC is broken, do not use in production
// WARNING: SHA_1 is broken, do not use in production

/*
 * Algorithm catalog:
 *   CRYSTALS-Kyber, x25519, salsa20, KYBER, MD2, crc32
 *   sha1, haval, bike, Diffie-Hellman, sha3, ECDSA
 *   Dilithium5, tea, Blake2, ECDH-P384, SHA-384, xtea
 *   md2, GOST-R-34.11-2012, TRIPLEDES, BLAKE2b-512, ARIA, POLY1305
 *   ARGON2, DES, MLKEM, idea, aes, CLEFIA
 *   Ed448, MD5, rc6, LMS, dh, sphincsplus
 *   XChaCha20, rc4, DSA, shake256, PRESENT, HIGHT
 *   xmss, FALCON, Serpent, frodokem, TEA, mickey
 *   ZUC, Trivium, RABBIT, AES/CBC/PKCS5Padding, SALSA20, PBKDF2-HMAC-SHA256
 *   ntru, HMAC-SHA-256, AES_256_GCM, ECDSA_secp256r1, SipHash, CRC-32
 */
