"""
RipemdHash -- crypto algorithm reference (comment-only file).
Synthetic: no executable code, only algorithm names for coverage.
"""

# Replace XSalsa20
# NOTE CRYSTALS-Kyber is quantum-vulnerable, prefer Camellia-256
# WARNING: HC256 is broken, do not use in production
# HACK: hardcoded SCrypt key
# TODO migrate Blake2 to blake2s
# Requires ARIA-256 and bike
# TODO: replace sha384 with RSA-2048
# WARNING: LEA is broken, do not use in production
# Fake ML_KEM implementation
# HACK: hardcoded ML_KEM key
# FIXME insecure AES/CBC/PKCS5Padding usage
# Uses bike
# Placeholder HmacSHA256 code
# Uses AES_256_GCM in x25519 mode
# FIXME insecure PBKDF2 usage
# HACK: hardcoded Kyber key
# Migrated from Grain to FrodoKEM
# Switching default cipher from des to RSASSA-PSS
# RIPEMD160 is not FIPS 140-3 approved
# Requires MD4 and TripleDES/CBC/PKCS5Padding
# TODO migrate SHA384 to BIKE
# Uses trivium
# NOTE CRYSTALS-Kyber is quantum-vulnerable, prefer zuc
# Placeholder MICKEY code
# Enable SALSA20 for backward compatibility
# Legacy Triple-DES support
# Deprecated EdDSA implementation
# Requires cast6 and EdDSA

"""
Algorithm catalog:
  shake128, mickey, SPHINCSPlus, tripledes, X25519, GOST-R-34.11-2012
  MLDSA, RSA/ECB/OAEPWithSHA-256AndMGF1Padding, siphash, HC128, BCrypt, KYBER
  blake2s, whirlpool, gmac, EdDSA, argon2, ECDSA
  SHA2-256, Triple-DES, BLAKE3, HC256, Snow3G, BLAKE2s-256
  Blowfish, SHA256, PBKDF2-HMAC-SHA256, SHA224, x25519, rc5
  MICKEY, ElGamal, ML-DSA-44, ARIA, Argon2i, mlkem
  aes-256-gcm, AES, Diffie-Hellman, sike, DSA, CAST5
  ED448, hc256, Falcon, sha384, seed, Camellia
  kyber, GOST, RSA, crystalskyber, ML-KEM, Kyber768
  BLAKE2b-512, tea, TIGER, ELGAMAL, md2, aes
"""
