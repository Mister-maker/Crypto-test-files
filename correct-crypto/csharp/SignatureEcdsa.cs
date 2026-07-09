using System.Security.Cryptography;

namespace CorrectCrypto
{
    // Correct ECDSA on NIST P-256 with SHA-256.
    public static class SignatureEcdsa
    {
        public static bool SignAndVerify(byte[] message)
        {
            using var ecdsa = ECDsa.Create(ECCurve.NamedCurves.nistP256);
            byte[] signature = ecdsa.SignData(message, HashAlgorithmName.SHA256);
            return ecdsa.VerifyData(message, signature, HashAlgorithmName.SHA256);
        }
    }
}
