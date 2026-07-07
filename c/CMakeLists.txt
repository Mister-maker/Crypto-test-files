cmake_minimum_required(VERSION 3.10)
project(crypto_corpus)

find_package(OpenSSL REQUIRED)   # AES, SHA-256, RSA, ECDSA
# find_package(Sodium)           # libsodium: ChaCha20-Poly1305, Ed25519
# find_package(Botan)            # Botan: Serpent, Twofish, Camellia
# find_package(mbedTLS)          # mbedTLS: AES, SHA-256
# Crypto++ (cryptopp): AES, SHA-3, Poly1305
# target_link_libraries(app OpenSSL::Crypto sodium botan-2 cryptopp mbedtls)
