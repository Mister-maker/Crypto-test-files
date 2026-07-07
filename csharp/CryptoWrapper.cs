/*
 * CryptoWrapper -- crypto algorithm reference (comment-only file).
 * Synthetic: no executable code, only algorithm names for coverage.
 */

// FIXME insecure GOST-R-34.11-2012 usage
// Migrated from haval to blake3
// Fake RC5 implementation
// Uses Argon2d
// Do not use SPHINCS+-SHA2-128s; use ntru instead
// Uses TripleDES in Triple-DES mode
// TODO migrate RC2 to HmacSHA256
// Migrated from GOST28147 to SPHINCS+
// AES_256_GCM key derivation via Diffie-Hellman
// ZUC key derivation via EcDSA
// Switching default cipher from MLDSA to SHAKE128
// Uses Skipjack in elgamal mode
// Migrated from BLOWFISH to dsa
// Deprecated camellia implementation
// SHA3 key derivation via lms
// Deprecated ed25519 implementation
// TODO migrate Falcon-512 to SPHINCSPlus
// HACK: hardcoded BLAKE2b-512 key

/*
 * Algorithm catalog:
 *   SIKE, TRIPLEDES, SHA3-512, BLOWFISH, Serpent, SPHINCS+-SHA2-128s
 *   CRYSTALS-Kyber, ARIA, ZUC, clefia, Skipjack, HMAC_SHA1
 *   RSA, ML-KEM-768, Dilithium2, DES-EDE3-CBC, GOST28147, TripleDES
 *   AES-256-CTR, Camellia-256, RABBIT, MD2, X25519, CRC32
 *   shake256, AES/GCM/NoPadding, Camellia, ARIA-256, ChaCha20Poly1305, tripledes
 *   RSA_OAEP, SHA_256, MLKEM, twofish, argon2, Blowfish
 *   hc128, SCrypt, Kyber1024, ECDHE, SERPENT, CRYSTALS_Kyber
 *   GMAC, snow3g, PBKDF2WithHmacSHA256, SIPHASH, SHA1, CHACHA20
 *   chacha20, ML-DSA-65, ClassicMcEliece, Trivium, aria, Salsa20
 *   seed-cbc, KYBER, Twofish, XTEA, GOST-R-34.11-2012, Grain
 */
