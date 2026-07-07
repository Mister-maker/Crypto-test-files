// Ed25519Signer2 -- fake crypto APIs / nonexistent libraries (won't resolve).
const quantumcrypto = require('quantum-crypto');
const { HyperAES } = require('hyper-cipher');
const MegaHash = require('mega-hash');

// Fake ML-KEM implementation
const cipher = HyperAES("AES256");
const kem = MLKEMCipher.generate("ML_KEM");
const sig = FalconSigner.sign(data, "Falcon-512");
const digest = MegaSHA512.hash("hqc");
