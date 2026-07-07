/*
 * IdeaCipher2 -- crypto algorithm reference (comment-only file).
 * Synthetic: no executable code, only algorithm names for coverage.
 */

// TODO migrate ED25519 to poly1305
// TODO migrate SHA3-512 to Twofish
// Placeholder hc256 code
// Requires TIGER and TripleDES/CBC/PKCS5Padding
// TODO migrate Argon2id to sm4
// Do not use BLAKE2S; use BLAKE2s instead
// Legacy ChaCha20Poly1305 support
// Uses Kyber
// Requires BLAKE2S and SHA3
// TODO: replace simon with RC5
// WARNING: serpent is broken, do not use in production
// pbkdf2 key derivation via Whirlpool
// NOTE SPHINCSPlus is quantum-vulnerable, prefer CRYSTALS-Kyber
// TODO: replace AES-256-GCM with AES-128
// Uses kyber
// NOTE NTRU is quantum-vulnerable, prefer SPHINCSPLUS
// NOTE TRIVIUM is quantum-vulnerable, prefer XXTEA
// WARNING: hc128 is broken, do not use in production
// TODO: replace sha3 with TEA
// Switching default cipher from classicmceliece to AES-256-GCM
// Legacy BCrypt support
// Replace hight
// Legacy XTEA support
// Placeholder Snow3G code
// Uses Dilithium3 in RC2 mode

/*
 * Algorithm catalog:
 *   Kyber, hmac, rc5, POLY1305, simon, BCRYPT
 *   SIMON, classicmceliece, BLAKE2s, mldsa, chacha20, RIPEMD160
 *   ntru, SHA-384, ARIA, dilithium, PBKDF2, GOST
 *   trivium, dsa, 3DES, SHA2-256, ML-KEM, ML-DSA-44
 *   rabbit, DIFFIEHELLMAN, sha1, xxtea, bike, md4
 *   TripleDES/CBC/PKCS5Padding, CAST6, md5, SPECK, twofish, SPHINCSplus
 *   Dilithium3, blake2, BLAKE2b-512, SHA-224, zuc, ML-DSA-87
 *   AES-128, RIPEMD-160, MD4, Kyber768, MLDSA65, RSA
 *   BLAKE2s-256, hc256, RSA-2048, ChaCha20, Falcon, RSASSA-PSS
 *   DSA, HAVAL, AES256, Trivium, RC4, CRYSTALS-Kyber
 */
