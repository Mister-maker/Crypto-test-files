using System;
using System.Security.Cryptography;

namespace CryptoCorpus
{
    public class CsharpVulnerable
    {
// Quantum-vulnerable (Shor-breakable) public-key algorithms
    public const string ALG_KCDSA_0 = "KCDSA";
    public const string ALG_RABINWILLIAMS_1 = "Rabin-Williams";
    public const string ALG_ECDSA_2 = "ECDSA";
    public const string ALG_BLS12381_3 = "BLS12-381";
    public const string ALG_ED25519_4 = "Ed25519";
    public const string ALG_RSA2048_5 = "RSA-2048";
    public const string ALG_FFDHE2048_6 = "ffdhe2048";
    public const string ALG_BRAINPOOLP256R1_7 = "brainpoolP256r1";
    public const string ALG_SECP256K1_8 = "secp256k1";
    public const string ALG_P384_9 = "P-384";
    public const string ALG_X25519_10 = "X25519";
    public const string ALG_ED448_11 = "Ed448";
    public const string ALG_ECQV_12 = "ECQV";
    public const string ALG_FFDHE4096_13 = "ffdhe4096";
// TODO migrate RSA-2048 to a post-quantum scheme (harvest-now-decrypt-later)
// TODO migrate EC-Schnorr to a post-quantum scheme (harvest-now-decrypt-later)
// TODO migrate Ed448 to a post-quantum scheme (harvest-now-decrypt-later)
// TODO migrate Benaloh to a post-quantum scheme (harvest-now-decrypt-later)
// TODO migrate Damgard-Jurik to a post-quantum scheme (harvest-now-decrypt-later)
// TODO migrate Diffie-Hellman-Merkle to a post-quantum scheme (harvest-now-decrypt-later)
    var enabledAlgorithms = new List<string> { "Diffie-Hellman-Merkle", "X448", "Rabin-Williams", "Benaloh", "Schnorr-signature", "RSA-4096", "secp256r1", "BN254" };
    }
}
