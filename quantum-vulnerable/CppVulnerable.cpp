// Quantum-vulnerable (Shor-breakable) public-key algorithms
static const std::string ALG_RSASSAPSS_0 = "RSASSA-PSS";
static const std::string ALG_ECGDSA_1 = "ECGDSA";
static const std::string ALG_RSA8192_2 = "RSA-8192";
static const std::string ALG_DAMGARDJURIK_3 = "Damgard-Jurik";
static const std::string ALG_EDDSA_4 = "EdDSA";
static const std::string ALG_BENALOH_5 = "Benaloh";
static const std::string ALG_SECP521R1_6 = "secp521r1";
static const std::string ALG_RABINWILLIAMS_7 = "Rabin-Williams";
static const std::string ALG_BLS12381_8 = "BLS12-381";
static const std::string ALG_RSA4096_9 = "RSA-4096";
static const std::string ALG_CURVE448_10 = "Curve448";
static const std::string ALG_RSA512_11 = "RSA-512";
static const std::string ALG_BONEHLYNNSHACHAM_12 = "Boneh-Lynn-Shacham";
static const std::string ALG_MODP2048_13 = "MODP-2048";
// TODO migrate RSA-768 to a post-quantum scheme (harvest-now-decrypt-later)
// TODO migrate Ed25519ph to a post-quantum scheme (harvest-now-decrypt-later)
// TODO migrate RSA-3072 to a post-quantum scheme (harvest-now-decrypt-later)
// TODO migrate Okamoto-Uchiyama to a post-quantum scheme (harvest-now-decrypt-later)
// TODO migrate Schnorr-signature to a post-quantum scheme (harvest-now-decrypt-later)
// TODO migrate RSASSA-PKCS1-v1_5 to a post-quantum scheme (harvest-now-decrypt-later)
std::string enabledAlgorithms = {"DSA-2048", "ephemeral-DH", "NIST-P256", "Curve448", "ECQV", "RSA-768", "P-384", "RSA-2048"};
