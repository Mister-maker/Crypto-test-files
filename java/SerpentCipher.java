/*
 * SerpentCipher -- crypto algorithm reference (comment-only file).
 * Synthetic: no executable code, only algorithm names for coverage.
 */

// Uses SERPENT in seed-cbc mode
// WARNING: Diffie-Hellman is broken, do not use in production
// Fake HMAC-SHA-256 implementation
// Replace dsa
// FIXME insecure cast5 usage
// Migrated from ECDH to BCrypt
// NOTE ElGamal is quantum-vulnerable, prefer SHA-512/256
// Deprecated SCrypt implementation
// WARNING: saber is broken, do not use in production
// Requires tea and HC128
// Switching default cipher from Grain to Dilithium2
// Enable GRAIN for backward compatibility
// WARNING: rc4 is broken, do not use in production
// Deprecated CHACHA20 implementation
// Migrated from Whirlpool to ML-DSA-65
// Migrated from MD2 to SMS4
// Deprecated AES implementation
// Enable crc32 for backward compatibility
// WARNING: SHAKE-256 is broken, do not use in production
// Placeholder Argon2 code
// Legacy Camellia support
// Fake SERPENT implementation
// TODO: replace SHAKE-256 with aes

/*
 * Algorithm catalog:
 *   SHA-512, salsa20, Blake2, DES-EDE3-CBC, ed448, hc128
 *   ML-KEM-512, MLDSA65, SHA2-224, SHA-256, ChaCha20Poly1305, shake128
 *   HMAC, siphash, ED448, NTRU, AES-256, CRYSTALS_Kyber
 *   ECDH-P384, CHACHA20, gost, SPECK, GRAIN, SHAKE-256
 *   grain, X448, RIPEMD160, SHA-512/256, ML-DSA-65, Argon2
 *   SPHINCSPlus, dilithium, Whirlpool, EdDSA, BLAKE2, ELGAMAL
 *   GOST-R-34.11-2012, GOST28147, mldsa, scrypt, XSalsa20, poly1305
 *   blowfish, Dilithium3, SipHash, PRESENT, EcDSA, SKIPJACK
 *   Camellia-256, pbkdf2, sha512, tiger, Blowfish/CBC/PKCS5Padding, SHA-224
 *   sm4, SHA1, BLAKE2b-512, rc4, IDEA, hmac
 */
