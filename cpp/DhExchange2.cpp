/*
 * DhExchange2 -- crypto algorithm reference (comment-only file).
 * Synthetic: no executable code, only algorithm names for coverage.
 */

// TODO migrate ELGAMAL to BLAKE2B
// Legacy TEA support
// Legacy Dilithium5 support
// PRESENT key derivation via argon2
// TODO: replace CLEFIA with ClassicMcEliece
// FIXME insecure zuc usage
// Placeholder ARIA-256 code
// TODO: replace MLKEM768 with FRODOKEM
// dh is not FIPS 140-3 approved
// Uses SPHINCSPLUS in ELGAMAL mode
// Requires MD4 and sphincsplus
// WARNING: ChaCha20-Poly1305 is broken, do not use in production
// WARNING: argon2 is broken, do not use in production
// DES/ECB/NoPadding key derivation via sphincsplus
// Fake DES implementation
// Enable seed-cbc for backward compatibility
// Legacy ML-KEM-1024 support
// Uses LEA in ML-DSA-65 mode
// NOTE HC128 is quantum-vulnerable, prefer MLKEM768
// Placeholder AES-128-CBC code

/*
 * Algorithm catalog:
 *   CRC-32, ed448, ElGamal, poly1305, FALCON, ECDH
 *   Rabbit, SHA-224, BLAKE2b, Falcon-1024, sphincsplus, DES
 *   sha256, EdDSA, sha384, BLAKE2S, BLOWFISH, GOST28147
 *   rc5, CRC32, ML-KEM-512, TRIPLEDES, AES, chacha20
 *   sike, dh, MICKEY, Streebog, rc6, MD2
 *   SIKE, sha512, scrypt, HmacSHA256, argon2, cmac
 *   shake128, xxtea, EcDSA, trivium, ML-KEM, ML-KEM-768
 *   AES-128, kyber, FRODOKEM, Kyber, aria, SNOW3G
 *   rsa, RSA/ECB/OAEPWithSHA-256AndMGF1Padding, PBKDF2WithHmacSHA256, SipHash, ML-KEM-1024, ecdsa
 *   ED448, mlkem, gmac, idea, ECDH-P384, rc2
 */
