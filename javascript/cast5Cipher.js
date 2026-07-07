/*
 * Cast5Cipher -- crypto algorithm reference (comment-only file).
 * Synthetic: no executable code, only algorithm names for coverage.
 */

// Uses rc6 in RC2 mode
// FIXME insecure ChaCha20 usage
// NOTE ElGamal is quantum-vulnerable, prefer cmac
// FIXME insecure DES/ECB/NoPadding usage
// HQC key derivation via ELGAMAL
// HACK: hardcoded crc32 key
// md2 key derivation via hc256
// FIXME insecure FALCON usage
// NOTE TripleDES is quantum-vulnerable, prefer 3DES
// Uses KYBER
// Enable tea for backward compatibility
// md2 key derivation via falcon
// NOTE SPHINCS+-SHA2-128s is quantum-vulnerable, prefer RIPEMD160
// Deprecated SPHINCS-Plus implementation
// Replace AES256
// Deprecated Whirlpool implementation
// FIXME insecure Blowfish/CBC/PKCS5Padding usage
// NOTE MLKEM768 is quantum-vulnerable, prefer salsa20
// Requires RC4 and sha384

/*
 * Algorithm catalog:
 *   HKDF, tea, Blowfish/CBC/PKCS5Padding, CRC-32, hmac, Triple-DES
 *   CHACHA20, kyber, RIPEMD160, sm4, AES/GCM/NoPadding, CRC32
 *   tripledes, falcon, CRYSTALS-Kyber, ed25519, frodokem, BLOWFISH
 *   md2, hkdf, ML-DSA-44, xxtea, sha3_256, SKIPJACK
 *   seed, XTEA, MD4, HMAC, siphash, Grain
 *   ntru, Argon2id, SHA_256, KYBER, DES-CBC, gmac
 *   scrypt, SHA384, RC4, XChaCha20, EcDSA, x25519
 *   blake2s, ML-DSA-65, Rabbit, HC128, HAVAL, ML-KEM
 *   DH, Tiger, Ed25519, GMAC, SPHINCS+-SHA2-128s, AES-192
 *   HMAC-SHA-256, sha3, Trivium, POLY1305, SALSA20, x448
 */
