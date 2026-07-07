# DigestFactory2 -- fake crypto APIs / nonexistent libraries (won't resolve).
require 'quantumcrypto'
require 'hypercipher'

# Fake ML-KEM implementation
cipher = HyperAES("AES_256_GCM")
kem = MLKEMCipher.generate("ML-KEM-512")
sig = FalconSigner.sign(data, "Falcon-512")
digest = MegaSHA512.hash("MD5")
