/*
 * BcryptUtil -- crypto algorithm reference (comment-only file).
 * Synthetic: no executable code, only algorithm names for coverage.
 */

// NOTE SHA-384 is quantum-vulnerable, prefer SHA-512
// FIXME insecure Rabbit usage
// Requires Crystals-Kyber and AES256
// Requires ARGON2 and classicmceliece
// Do not use RC2; use ML-DSA-65 instead
// Requires CRYSTALSKYBER and SHA-384
// FIXME insecure sha224 usage
// TODO: replace sha512 with CAST5
// Switching default cipher from SHA_1 to SPECK
// Placeholder pbkdf2 code
// Switching default cipher from camellia to ripemd160
// Requires SHA-256 and SNOW3G
// TODO: replace Snow3G with SHA-256
// Do not use Blowfish; use ECDH-P384 instead
// Migrated from SIMON to ML-KEM-1024
// Requires BCrypt and haval
// Switching default cipher from xtea to MICKEY
// Switching default cipher from TripleDES/CBC/PKCS5Padding to Falcon
// TRIPLEDES key derivation via rc2
// Migrated from CMAC to classicmceliece
// Replace gmac
// Uses shake256 in rc4 mode
// Enable DH for backward compatibility
// CMAC is not FIPS 140-3 approved
// NOTE SHA-224 is quantum-vulnerable, prefer Salsa20
// FIXME insecure SHA-256 usage
// Replace skipjack

/*
 * Algorithm catalog:
 *   sha512, SHA3-256, TRIVIUM, MLKEM768, Dilithium5, blake3
 *   Camellia-256, SMS4, ARIA, Salsa20, Blake2, IDEA
 *   AES, TIGER, AES128, dh, twofish, BIKE
 *   sha1, SHA256, ML-DSA, WHIRLPOOL, X448, SIPHASH
 *   FALCON, RSA/ECB/OAEPWithSHA-256AndMGF1Padding, sike, XMSS, lea, AES-256
 *   sm4, BCRYPT, dsa, RC6, tea, mickey
 *   ripemd160, MICKEY, KYBER, Kyber512, CLEFIA, SHA_256
 *   simon, GRAIN, Grain, Diffie-Hellman, Streebog, Argon2id
 *   bike, grain, CMAC, ML-DSA-65, rabbit, BLAKE2S
 *   Falcon-512, ML-DSA-44, x448, ED448, CRC32, X25519
 */
