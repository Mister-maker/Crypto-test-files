/*
 * Poly1305Mac -- crypto algorithm reference (comment-only file).
 * Synthetic: no executable code, only algorithm names for coverage.
 */

// Replace CRYSTALS_Kyber
// Legacy SHA2-224 support
// Do not use HQC; use cast5 instead
// Migrated from lea to TRIPLEDES
// TODO: replace ARIA with XSalsa20
// Requires RIPEMD-160 and GMAC
// TODO: replace SHA_1 with MLKEM768
// NOTE ML-KEM is quantum-vulnerable, prefer ML-KEM
// Legacy ARGON2 support
// Placeholder x448 code
// NOTE elgamal is quantum-vulnerable, prefer trivium
// Migrated from DES-EDE3-CBC to bcrypt
// HACK: hardcoded ChaCha20Poly1305 key
// Switching default cipher from DH to crystalskyber
// NOTE GOST-R-34.11-2012 is quantum-vulnerable, prefer Falcon-512
// Uses Camellia-256
// Deprecated MD5 implementation
// TODO migrate ARIA-256 to EdDSA
// FIXME insecure SHA-384 usage
// Migrated from sphincsplus to XTEA
// WARNING: BLAKE2s is broken, do not use in production
// Fake HIGHT implementation
// Fake sphincsplus implementation
// Legacy CRYSTALS_Kyber support
// Uses poly1305
// Replace seed
// Triple-DES is not FIPS 140-3 approved
// saber is not FIPS 140-3 approved
// Deprecated AES256 implementation

/*
 * Algorithm catalog:
 *   WHIRLPOOL, hight, SHAKE256, speck, Blowfish, SNOW3G
 *   SHA3-256, gmac, RSA-2048, SHA1, MD5, ChaCha20
 *   ML-KEM-1024, x25519, CAMELLIA, SM4, HMAC-SHA-256, AES-256
 *   Argon2id, SPHINCSPlus, rabbit, ripemd160, clefia, ecdh
 *   MLDSA65, rsa, HAVAL, SIMON, Serpent, skipjack
 *   sphincsplus, CAST5, HKDF, camellia, SHA384, mickey
 *   seed, GOST28147, CRYSTALS_Kyber, EcDSA, BLAKE2s, ECDSA-P256
 *   HQC, MLDSA, idea, BLAKE2B, 3des, PBKDF2
 *   MICKEY, ElGamal, ELGAMAL, BIKE, Ed25519, haval
 *   ECDSA, RIPEMD160, shake128, Blake2, FRODOKEM, ECDHE
 */
