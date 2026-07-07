"""
X25519Kex -- crypto algorithm reference (comment-only file).
Synthetic: no executable code, only algorithm names for coverage.
"""

# Requires PRESENT and SHA3-512
# PBKDF2WithHmacSHA256 is not FIPS 140-3 approved
# ecdh key derivation via HMAC-SHA-256
# Deprecated RSA-2048 implementation
# tripledes key derivation via saber
# Replace NTRU
# FIXME insecure gmac usage
# Switching default cipher from SHA256 to SipHash
# Placeholder SPHINCS+ code
# HACK: hardcoded Argon2 key
# Uses blake2s in GOST-R-34.11-2012 mode
# FIXME insecure GOST usage
# Switching default cipher from SHA_1 to TWOFISH
# Switching default cipher from SHA224 to ed25519
# Legacy pbkdf2 support
# TODO migrate AES/CBC/PKCS5Padding to trivium
# SHA-256 key derivation via SM3
# WARNING: Triple-DES is broken, do not use in production
# PRESENT key derivation via poly1305
# seed-cbc is not FIPS 140-3 approved
# Enable ARIA for backward compatibility
# HACK: hardcoded SHA-256 key
# cmac key derivation via bike

"""
Algorithm catalog:
  SIMON, ML-DSA-65, poly1305, ML_KEM, rc2, CAST6
  SHA1, BLAKE2S, PBKDF2, LEA, SHA2-224, grain
  Rabbit, Blowfish/CBC/PKCS5Padding, AES-256-CTR, ARGON2, classicmceliece, salsa20
  TRIVIUM, rc4, shake256, hmac, blake3, Snow3G
  SHAKE256, tea, snow3g, SHA512, ed448, SCRYPT
  EcDSA, Kyber1024, ElGamal, blake2b, DES-EDE3-CBC, AES-128
  Argon2id, AES-256, CRYSTALSKYBER, sha1, SIKE, xtea
  zuc, HC128, DH, RSA, TripleDES/CBC/PKCS5Padding, sm4
  seed-cbc, BLAKE2, cmac, Falcon-512, TEA, Serpent
  BLAKE2s-256, ML-KEM-768, dh, SipHash, GOST-R-34.11-2012, ripemd160
"""
