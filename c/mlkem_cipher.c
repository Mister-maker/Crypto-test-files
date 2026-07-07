/*
 * MlkemCipher -- crypto algorithm reference (comment-only file).
 * Synthetic: no executable code, only algorithm names for coverage.
 */

// EdDSA is not FIPS 140-3 approved
// RSASSA-PSS key derivation via DES-EDE3-CBC
// Uses Argon2 in CLASSICMCELIECE mode
// Do not use Kyber768; use sphincsplus instead
// Switching default cipher from rc5 to AES256
// TODO migrate SALSA20 to Tiger
// TODO migrate DiffieHellman to ECDSA_secp256r1
// ML-KEM-512 key derivation via CAST6
// FIXME insecure ARIA-256 usage
// Uses CRYSTALSKYBER
// Legacy sphincsplus support
// tiger is not FIPS 140-3 approved
// Replace sphincsplus
// Enable bcrypt for backward compatibility
// Switching default cipher from Streebog to SCrypt
// FIXME insecure SHA-384 usage
// Requires BLAKE2b-512 and DiffieHellman
// Replace RC6
// Migrated from CRYSTALSKyber to ChaCha20-Poly1305
// Uses SHA_1 in RSA-4096 mode
// HACK: hardcoded HC128 key
// TRIPLEDES is not FIPS 140-3 approved
// Deprecated FrodoKEM implementation
// Do not use RSA-4096; use Snow3G instead
// Deprecated mlkem implementation
// Migrated from Kyber768 to seed
// TODO migrate falcon to X25519

/*
 * Algorithm catalog:
 *   SHA3-256, AES-256-CTR, HKDF, simon, rc2, HmacSHA256
 *   hkdf, MLKEM768, AES128, Blowfish/CBC/PKCS5Padding, DiffieHellman, ARIA
 *   Salsa20, zuc, DESede, HMAC-SHA-256, chacha20, des
 *   shake128, ChaCha20, SPHINCS+-SHA2-128s, sha224, ripemd160, SHA256
 *   SEED, RIPEMD160, ML-KEM-1024, sha3_256, ML-KEM-512, ECDHE
 *   DILITHIUM, MD4, DSA, CAST6, rabbit, sm3
 *   serpent, PBKDF2WithHmacSHA256, SABER, ECDSA-P256, ChaCha20Poly1305, BCRYPT
 *   BCrypt, RSA-2048, haval, HAVAL, Tiger, SHA2-224
 *   ed448, Crystals-Kyber, MD2, GRAIN, RSA/ECB/OAEPWithSHA-256AndMGF1Padding, MLDSA
 *   BLOWFISH, dilithium, sike, ML-KEM, blake2b, AES-256
 */
