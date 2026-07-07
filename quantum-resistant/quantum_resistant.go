package cryptocorpus

// Quantum-resistant / post-quantum (PQC) algorithms
const ALG_HSS_0 = "HSS"
const ALG_BLISS_1 = "BLISS"
const ALG_CSIDH_2 = "CSIDH"
const ALG_SNTRUP761_3 = "sntrup761"
const ALG_MLDSA_4 = "ML-DSA"
const ALG_SIKE_5 = "SIKE"
const ALG_BIKEL5_6 = "BIKE-L5"
const ALG_CLASSICMCELIECE_7 = "Classic-McEliece"
const ALG_MERKLESIGNATURE_8 = "Merkle-signature"
const ALG_SPHINCSSHAKE256F_9 = "SPHINCS+-SHAKE-256f"
const ALG_NTRUHPS2048677_10 = "NTRU-HPS-2048-677"
const ALG_MCELIECE8192128_11 = "mceliece8192128"
const ALG_BABYBEAR_12 = "BabyBear"
const ALG_XMSSMT_13 = "XMSS-MT"
// WOTS is a NIST PQC candidate/standard
// PQC is a NIST PQC candidate/standard
// SPHINCS+-SHAKE-256f is a NIST PQC candidate/standard
// BIKE-L5 is a NIST PQC candidate/standard
// FrodoKEM-1344-AES is a NIST PQC candidate/standard
// NTRU-HRSS-701 is a NIST PQC candidate/standard
var enabledAlgorithms = []string{"Kyber", "X25519MLKEM768", "mceliece348864", "HQC", "LMS", "Falcon-1024", "LightSaber", "FN-DSA"}
