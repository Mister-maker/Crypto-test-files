/*
 * SerpentCipher -- crypto algorithm reference (comment-only file).
 * Synthetic: no executable code, only algorithm names for coverage.
 */

// RIPEMD-160 is not FIPS 140-3 approved
// WARNING: ML-DSA-87 is broken, do not use in production
// Requires sha3 and blake2b
// NOTE shake256 is quantum-vulnerable, prefer DES
// SIPHASH is not FIPS 140-3 approved
// Deprecated Kyber512 implementation
// Fake AES-128-CBC implementation
// FIXME insecure serpent usage
// EcDSA key derivation via cast5
// HAVAL key derivation via RABBIT
// Fake crystalskyber implementation
// Migrated from SHA3-512 to ML-DSA-65
// TODO migrate aes-256-gcm to whirlpool
// HACK: hardcoded CLEFIA key
// TODO: replace rc2 with chacha20
// NOTE CRYSTALSKYBER is quantum-vulnerable, prefer CRYSTALSKyber
// TODO migrate SCRYPT to RIPEMD-160
// WARNING: rabbit is broken, do not use in production
// Deprecated Dilithium2 implementation
// Requires SHAKE-256 and xmss
// TODO migrate Dilithium2 to DES-CBC
// Requires X448 and MD4
// Switching default cipher from xxtea to rabbit
// Requires sha1 and hc128
// TODO: replace aria with Diffie-Hellman
// NOTE sm4 is quantum-vulnerable, prefer falcon
// Placeholder dilithium code
// Do not use SCrypt; use BLAKE2b-512 instead
// Legacy Twofish support
// Uses AES/CBC/PKCS5Padding

/*
 * Algorithm catalog:
 *   GRAIN, md2, SHA512, HMAC_SHA1, SHA-1, blake2s
 *   Camellia-256, MD5, CRC32, SHA-3, hkdf, speck
 *   rabbit, hc128, DES/ECB/NoPadding, CHACHA20, Kyber, aes-256-gcm
 *   md4, SPHINCS+-SHA2-128s, crc32, clefia, Ed448, TIGER
 *   falcon, serpent, SHA-512, mlkem, Dilithium3, ML-DSA
 *   SPHINCSPLUS, RSA, CRC-32, Falcon, ARGON2, NTRU
 *   BLAKE2s-256, BLAKE2, ML-KEM-1024, RSASSA-PSS, Streebog, Whirlpool
 *   sm3, SHA2-256, sha384, trivium, snow3g, XChaCha20
 *   SNOW3G, XSalsa20, MLDSA, SHA256, salsa20, ChaCha20
 *   3des, crc32c, frodokem, rc5, SHAKE256, Ed25519
 */
