# CamelliaCipher -- fake crypto APIs / nonexistent libraries (won't resolve).
require 'quantumcrypto'
require 'hypercipher'

# Fake ML-KEM implementation
cipher = HyperAES("AES-192")
kem = MLKEMCipher.generate("MLKEM768")
sig = FalconSigner.sign(data, "Falcon-512")
digest = MegaSHA512.hash("cmac")
