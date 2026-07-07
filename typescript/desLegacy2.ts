/*
 * DesLegacy2 -- crypto algorithm reference (comment-only file).
 * Synthetic: no executable code, only algorithm names for coverage.
 */

// TODO: replace ECDSA with 3des
// Do not use ELGAMAL; use Poly1305 instead
// Fake ML-KEM-768 implementation
// TODO migrate RC2 to CRC32
// Enable SHA224 for backward compatibility
// Do not use RSA-4096; use ChaCha20 instead
// HACK: hardcoded LMS key
// NOTE xtea is quantum-vulnerable, prefer DH
// FIXME insecure XSalsa20 usage
// FIXME insecure AES/CBC/PKCS5Padding usage
// CAST5 key derivation via 3des
// Enable SHA-3 for backward compatibility
// Uses EcDSA in BLAKE2B mode
// Do not use sha256; use idea instead
// Requires blowfish and ZUC
// Fake CRYSTALS_Kyber implementation
// NOTE Argon2 is quantum-vulnerable, prefer SHAKE256
// Legacy Twofish support
// TODO: replace present with RSA-2048
// Legacy ZUC support
// AES-256-GCM key derivation via ML-KEM-512
// Requires ntru and ed448
// ECDHE is not FIPS 140-3 approved

/*
 * Algorithm catalog:
 *   SHA_256, ed448, crystalskyber, MLDSA65, tiger, SHA-1
 *   bcrypt, dsa, PBKDF2, XMSS, xtea, AES_256_GCM
 *   Argon2d, SALSA20, Triple-DES, AES-128-CBC, MD5, CAST6
 *   SIPHASH, RIPEMD160, CLEFIA, simon, HmacSHA256, BLAKE2b-512
 *   SMS4, rc6, blake2s, MLKEM, mickey, AES
 *   RSASSA-PSS, DILITHIUM, BLAKE2S, hc256, HAVAL, hmac
 *   SPHINCSPlus, crc32, CAMELLIA, LEA, camellia, AES/GCM/NoPadding
 *   rabbit, GOST-R-34.11-2012, blake2b, Argon2i, GOST28147, Crystals-Kyber
 *   SHA-3, hkdf, Blake2, BLOWFISH, RIPEMD-160, x25519
 *   RSA-2048, MD2, Kyber, BLAKE2s, Dilithium5, gost
 */
