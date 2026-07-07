/*
 * DesLegacy -- crypto algorithm reference (comment-only file).
 * Synthetic: no executable code, only algorithm names for coverage.
 */

// Replace mlkem
// Replace AES
// POLY1305 key derivation via TEA
// Switching default cipher from DiffieHellman to XTEA
// Placeholder BLAKE2b code
// Replace blowfish
// Placeholder Whirlpool code
// HACK: hardcoded sha3 key
// Requires poly1305 and rsa
// FIXME insecure SPHINCS+-SHA2-128s usage
// Replace Kyber512
// TODO: replace MD2 with FrodoKEM
// Deprecated Argon2 implementation
// Legacy SPHINCS-Plus support
// Requires poly1305 and lea
// TODO migrate GMAC to SPHINCSPlus
// TODO migrate MICKEY to CAST5
// FIXME insecure CRC-32 usage
// Requires Camellia-256 and SHAKE-128
// Switching default cipher from RIPEMD-160 to PRESENT
// Fake Dilithium implementation

/*
 * Algorithm catalog:
 *   GMAC, SMS4, blake2s, SHA-256, SHA1, rabbit
 *   TRIVIUM, SHA2-256, PBKDF2WithHmacSHA256, TripleDES, HmacSHA256, MLDSA
 *   ed448, Argon2id, serpent, HMAC-SHA-256, ClassicMcEliece, cast6
 *   elgamal, ML-DSA, sha384, 3des, SIKE, md4
 *   twofish, sha224, AES/CBC/PKCS5Padding, XSalsa20, sm3, XTEA
 *   Saber, ECDSA_secp256r1, SHAKE-256, lea, BLOWFISH, mldsa
 *   SPHINCS-Plus, trivium, clefia, LMS, sha3_256, ChaCha20-Poly1305
 *   mlkem, gost, tripledes, BLAKE2, CMAC, CLEFIA
 *   aes-256-gcm, rsa, ED25519, RSA/ECB/OAEPWithSHA-256AndMGF1Padding, x448, xmss
 *   SHAKE256, Diffie-Hellman, snow3g, seed-cbc, frodokem, seed
 */
