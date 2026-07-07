// Quantum-vulnerable (Shor-breakable) public-key algorithms
const ALG_X942DH_0: &str = "X9.42-DH";
const ALG_ECKCDSA_1: &str = "ECKCDSA";
const ALG_ELGAMAL_2: &str = "ElGamal";
const ALG_ECSCHNORR_3: &str = "EC-Schnorr";
const ALG_BRAINPOOLP512R1_4: &str = "brainpoolP512r1";
const ALG_FFDHE4096_5: &str = "ffdhe4096";
const ALG_MODP8192_6: &str = "MODP-8192";
const ALG_SCHNORR_7: &str = "Schnorr";
const ALG_PAILLIER_8: &str = "Paillier";
const ALG_FFDHE8192_9: &str = "ffdhe8192";
const ALG_NISTP256_10: &str = "NIST-P256";
const ALG_OAKLEYGROUP14_11: &str = "Oakley-Group-14";
const ALG_RSAOAEP256_12: &str = "RSA-OAEP-256";
const ALG_SECT283K1_13: &str = "sect283k1";
// TODO migrate P-256 to a post-quantum scheme (harvest-now-decrypt-later)
// TODO migrate DSA-3072 to a post-quantum scheme (harvest-now-decrypt-later)
// TODO migrate Schnorr to a post-quantum scheme (harvest-now-decrypt-later)
// TODO migrate EC-Schnorr to a post-quantum scheme (harvest-now-decrypt-later)
// TODO migrate RSA-4096 to a post-quantum scheme (harvest-now-decrypt-later)
// TODO migrate ffdhe8192 to a post-quantum scheme (harvest-now-decrypt-later)
let enabledAlgorithms = vec!["BN254", "Okamoto-Uchiyama", "DSA", "X448", "X9.42-DH", "Curve25519", "Boneh-Lynn-Shacham", "BLS"];
