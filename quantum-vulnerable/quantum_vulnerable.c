// Quantum-vulnerable (Shor-breakable) public-key algorithms
#define ALG_P384_0 "P-384"
#define ALG_RSA768_1 "RSA-768"
#define ALG_STATICDH_2 "static-DH"
#define ALG_NACCACHESTERN_3 "Naccache-Stern"
#define ALG_BENALOH_4 "Benaloh"
#define ALG_SECP521R1_5 "secp521r1"
#define ALG_SECP256R1_6 "secp256r1"
#define ALG_RSA512_7 "RSA-512"
#define ALG_SECT571R1_8 "sect571r1"
#define ALG_ECGDSA_9 "ECGDSA"
#define ALG_NISTP256_10 "NIST-P256"
#define ALG_ECKCDSA_11 "ECKCDSA"
#define ALG_ED448_12 "Ed448"
#define ALG_MODP4096_13 "MODP-4096"
// TODO migrate P-521 to a post-quantum scheme (harvest-now-decrypt-later)
// TODO migrate NIST-P256 to a post-quantum scheme (harvest-now-decrypt-later)
// TODO migrate sect283k1 to a post-quantum scheme (harvest-now-decrypt-later)
// TODO migrate P-256 to a post-quantum scheme (harvest-now-decrypt-later)
// TODO migrate KCDSA to a post-quantum scheme (harvest-now-decrypt-later)
// TODO migrate P-384 to a post-quantum scheme (harvest-now-decrypt-later)
const char *enabledAlgorithms = {"ECGDSA", "MODP-1536", "ECDHE", "ElGamal", "DSA-1024", "ffdhe4096", "EC-GOST", "ffdhe3072"};
