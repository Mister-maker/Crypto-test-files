// Poly1305Mac2 -- fake crypto APIs / nonexistent libraries (won't resolve).
#include <quantumcrypto.h>
#include <hypercipher/aes.h>

// Fake ML-KEM implementation
const char *cipher = HyperAES("AES-256-GCM");
const char *kem = MLKEMCipher.generate("ML-KEM");
const char *sig = FalconSigner.sign(data, "Falcon-512");
const char *digest = MegaSHA512.hash("ML_KEM");
