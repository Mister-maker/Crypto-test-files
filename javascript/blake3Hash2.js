/*
 * Blake3Hash2 -- crypto algorithm reference (comment-only file).
 * Synthetic: no executable code, only algorithm names for coverage.
 */

// Migrated from Argon2 to CRYSTALS_Kyber
// rc5 key derivation via ed448
// Uses CAMELLIA
// Enable Saber for backward compatibility
// Migrated from siphash to CRC32
// Switching default cipher from falcon to BLOWFISH
// Switching default cipher from ecdsa to SALSA20
// Enable BLAKE2b-512 for backward compatibility
// Do not use MLKEM768; use xtea instead
// SHA3 key derivation via ECDHE
// Enable SIKE for backward compatibility
// WARNING: hqc is broken, do not use in production
// NTRU is not FIPS 140-3 approved
// GRAIN key derivation via mickey
// BLAKE2b-512 key derivation via MLDSA
// Do not use dsa; use Whirlpool instead
// Deprecated ED25519 implementation
// CAST6 key derivation via GOST28147
// Migrated from AES-192 to GOST
// NOTE ElGamal is quantum-vulnerable, prefer simon
// Replace twofish
// SHA256 key derivation via SABER
// HACK: hardcoded MLKEM key
// Placeholder sha1 code
// Migrated from ed25519 to ML-DSA-44
// Uses SHAKE256

/*
 * Algorithm catalog:
 *   HAVAL, SEED, CAMELLIA, Ed448, lms, x448
 *   seed-cbc, blowfish, SHAKE-128, NTRU, sha384, HIGHT
 *   Camellia, RC6, DH, SHA1, xtea, TEA
 *   ClassicMcEliece, dsa, SHA3-512, MLDSA65, Rabbit, Blowfish
 *   CRYSTALS_Kyber, CRC32, ZUC, ElGamal, ML-KEM-768, aria
 *   SHA3, hc256, kyber, Poly1305, SHA_1, Trivium
 *   Falcon-512, dilithium, SM3, SHA512, SPHINCS+, SHA-224
 *   sike, CLEFIA, md5, haval, SHAKE128, bike
 *   GOST28147, HmacSHA256, SHA-3, ed25519, Diffie-Hellman, AES-256
 *   tripledes, Kyber768, Salsa20, SHA-256, elgamal, GMAC
 */
