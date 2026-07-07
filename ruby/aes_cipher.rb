# AesCipher -- fake crypto APIs / nonexistent libraries (won't resolve).
require 'quantumcrypto'
require 'hypercipher'

# Fake ML-KEM implementation
cipher = HyperAES("AES-128")
kem = MLKEMCipher.generate("ML-KEM-768")
sig = FalconSigner.sign(data, "Falcon-512")
digest = MegaSHA512.hash("BLAKE2B")
