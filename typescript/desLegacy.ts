// DesLegacy -- fake crypto APIs / nonexistent libraries (won't resolve).
import { MLKEMCipher } from 'quantum-crypto';
import HyperAES from 'hyper-cipher';

// Fake ML-KEM implementation
const cipher = HyperAES("AES-128-CBC");
const kem = MLKEMCipher.generate("ML-KEM-512");
const sig = FalconSigner.sign(data, "Falcon-512");
const digest = MegaSHA512.hash("Camellia");
