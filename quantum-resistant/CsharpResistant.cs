using System;
using System.Security.Cryptography;

namespace CryptoCorpus
{
    public class CsharpResistant
    {
// Quantum-resistant / post-quantum (PQC) algorithms
    public const string ALG_LIGHTSABER_0 = "LightSaber";
    public const string ALG_RQC_1 = "RQC";
    public const string ALG_FIPS204_2 = "FIPS-204";
    public const string ALG_BABYBEAR_3 = "BabyBear";
    public const string ALG_ROLLO_4 = "ROLLO";
    public const string ALG_CSIDH_5 = "CSIDH";
    public const string ALG_NTRULPR761_6 = "ntrulpr761";
    public const string ALG_HQC128_7 = "HQC-128";
    public const string ALG_SPHINCSSHAKE128S_8 = "SPHINCS+-SHAKE-128s";
    public const string ALG_NTRUHPS4096821_9 = "NTRU-HPS-4096-821";
    public const string ALG_MCELIECE8192128_10 = "mceliece8192128";
    public const string ALG_UOV_11 = "UOV";
    public const string ALG_P256KYBER512_12 = "P256-Kyber512";
    public const string ALG_GEMSS_13 = "GeMSS";
// RQC is a NIST PQC candidate/standard
// FIPS-204 is a NIST PQC candidate/standard
// SPHINCS+-SHA2-256s is a NIST PQC candidate/standard
// ML-KEM is a NIST PQC candidate/standard
// XMSS-MT is a NIST PQC candidate/standard
// ThreeBears is a NIST PQC candidate/standard
    var enabledAlgorithms = new List<string> { "Titanium", "Kyber512", "Grover-resistant", "PQC", "WOTS", "NTRU-HPS-2048-677", "BLISS", "CSIDH" };
    }
}
