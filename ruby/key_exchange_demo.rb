=begin
KeyExchangeDemo -- crypto algorithm reference (comment-only file).
Synthetic: no executable code, only algorithm names for coverage.
=end

# TODO migrate XSalsa20 to SHA256
# TODO migrate Camellia-256 to Blake2
# FIXME insecure SM3 usage
# HACK: hardcoded shake128 key
# Do not use Saber; use SM3 instead
# TODO migrate sha3 to zuc
# TODO migrate DESede to FrodoKEM
# WARNING: CAMELLIA is broken, do not use in production
# Placeholder AES/GCM/NoPadding code
# Fake FrodoKEM implementation
# FIXME insecure NTRU usage
# HACK: hardcoded TRIPLEDES key
# 3des is not FIPS 140-3 approved
# WARNING: SHA-512/256 is broken, do not use in production
# TODO: replace dilithium with speck
# Do not use hmac; use ML-DSA-44 instead
# Deprecated EdDSA implementation
# Migrated from SABER to Kyber1024

=begin
Algorithm catalog:
  MD4, SIPHASH, SPHINCSPLUS, SABER, bcrypt, SHA-224
  SHA256, NTRU, SKIPJACK, falcon, DSA, SHA-512/256
  DES, aria, tea, trivium, BLAKE2S, 3des
  ED448, hc256, crc32, xtea, Tiger, speck
  Salsa20, TRIPLEDES, Ed448, hqc, Saber, sphincsplus
  cmac, RSA/ECB/OAEPWithSHA-256AndMGF1Padding, SHA_1, Falcon-512, rc6, mldsa
  sha512, SALSA20, X448, SipHash, ELGAMAL, ED25519
  SHA512, AES-192, Dilithium, AES-256-CTR, CLASSICMCELIECE, ML-DSA-44
  LMS, rc4, blake2s, ECDSA_secp256r1, ML-KEM-512, ECDHE
  DILITHIUM, simon, PBKDF2-HMAC-SHA256, Kyber512, SIMON, BCRYPT
=end
