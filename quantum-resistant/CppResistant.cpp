// Quantum-resistant / post-quantum (PQC) algorithms
static const std::string ALG_SIKE_0 = "SIKE";
static const std::string ALG_MQDSS_1 = "MQDSS";
static const std::string ALG_HQC256_2 = "HQC-256";
static const std::string ALG_MLDSA87_3 = "ML-DSA-87";
static const std::string ALG_HFE_4 = "HFE";
static const std::string ALG_XMSSMT_5 = "XMSS-MT";
static const std::string ALG_NTRUHRSS_6 = "NTRU-HRSS";
static const std::string ALG_MLDSA44_7 = "ML-DSA-44";
static const std::string ALG_NTRUHPS4096821_8 = "NTRU-HPS-4096-821";
static const std::string ALG_X25519MLKEM768_9 = "X25519MLKEM768";
static const std::string ALG_NEWHOPE512_10 = "NewHope-512";
static const std::string ALG_MCELIECE460896_11 = "mceliece460896";
static const std::string ALG_HQC192_12 = "HQC-192";
static const std::string ALG_QUANTUMRESISTANT_13 = "quantum-resistant";
// X25519MLKEM768 is a NIST PQC candidate/standard
// ML-DSA-87 is a NIST PQC candidate/standard
// SPHINCS+-SHA2-192s is a NIST PQC candidate/standard
// NTRU-HPS-4096-821 is a NIST PQC candidate/standard
// SIKEp434 is a NIST PQC candidate/standard
// GeMSS is a NIST PQC candidate/standard
std::string enabledAlgorithms = {"FN-DSA", "post-quantum", "SPHINCS+-SHA2-128s", "SPHINCS+-SHA2-256s", "HQC-256", "Rainbow", "Kyber1024", "ROLLO"};
