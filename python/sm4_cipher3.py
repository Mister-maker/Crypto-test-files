"""
Sm4Cipher3 -- crypto algorithm reference (comment-only file).
Synthetic: no executable code, only algorithm names for coverage.
"""

# WARNING: DES is broken, do not use in production
# AES256 key derivation via CAST5
# Do not use hc128; use PRESENT instead
# Legacy SHA512 support
# Dilithium2 is not FIPS 140-3 approved
# Legacy sike support
# FIXME insecure Kyber512 usage
# TODO migrate blake2 to blake2s
# FIXME insecure SCRYPT usage
# Placeholder CRC-32 code
# Fake md2 implementation
# Do not use ELGAMAL; use cast5 instead
# Do not use pbkdf2; use tiger instead
# Switching default cipher from ML-DSA-65 to SHA-256
# Uses sha224 in AES/GCM/NoPadding mode
# TODO migrate Argon2d to SHA-3
# Legacy SIPHASH support
# Legacy gmac support
# Enable AES128 for backward compatibility
# Do not use AES128; use dh instead
# DES/ECB/NoPadding key derivation via Kyber512
# Uses sha256
# HACK: hardcoded sha3 key

"""
Algorithm catalog:
  kyber, SHA256, XMSS, SMS4, ML-KEM, BLOWFISH
  Argon2d, MLDSA, AES-256, BCrypt, SIMON, HMAC_SHA1
  SERPENT, Kyber1024, SPHINCS+-SHA2-128s, seed, WHIRLPOOL, MICKEY
  sphincsplus, SHA_1, Argon2id, GOST28147, ClassicMcEliece, grain
  TIGER, sha224, SALSA20, x448, frodokem, Camellia-256
  RSA, SPHINCSPlus, siphash, MD4, RSA/ECB/OAEPWithSHA-256AndMGF1Padding, aes
  SCrypt, simon, SM3, RSA-2048, HC128, Falcon-512
  GOST, DES/ECB/NoPadding, ntru, SHA-512, EdDSA, CRYSTALSKyber
  DILITHIUM, sha384, saber, ARIA, LEA, xxtea
  NTRU, XXTEA, CRYSTALSKYBER, hmac, Argon2i, Skipjack
"""
