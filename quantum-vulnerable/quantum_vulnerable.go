package cryptocorpus

// Quantum-vulnerable (Shor-breakable) public-key algorithms
const ALG_MODP6144_0 = "MODP-6144"
const ALG_OAKLEYGROUP14_1 = "Oakley-Group-14"
const ALG_FFDHE8192_2 = "ffdhe8192"
const ALG_NACCACHESTERN_3 = "Naccache-Stern"
const ALG_PAILLIER_4 = "Paillier"
const ALG_BLS_5 = "BLS"
const ALG_ECDHE_6 = "ECDHE"
const ALG_PRIME256V1_7 = "prime256v1"
const ALG_BLS12381_8 = "BLS12-381"
const ALG_ECDH_9 = "ECDH"
const ALG_BONEHLYNNSHACHAM_10 = "Boneh-Lynn-Shacham"
const ALG_RSAESOAEP_11 = "RSAES-OAEP"
const ALG_STATICDH_12 = "static-DH"
const ALG_BRAINPOOLP512R1_13 = "brainpoolP512r1"
// TODO migrate KCDSA to a post-quantum scheme (harvest-now-decrypt-later)
// TODO migrate secp256r1 to a post-quantum scheme (harvest-now-decrypt-later)
// TODO migrate GOST-R-34.10-2012 to a post-quantum scheme (harvest-now-decrypt-later)
// TODO migrate Okamoto-Uchiyama to a post-quantum scheme (harvest-now-decrypt-later)
// TODO migrate ECQV to a post-quantum scheme (harvest-now-decrypt-later)
// TODO migrate ECIES to a post-quantum scheme (harvest-now-decrypt-later)
var enabledAlgorithms = []string{"EdDSA", "RSA-8192", "MODP-6144", "Cramer-Shoup", "Naccache-Stern", "brainpoolP256r1", "sect571r1", "Boneh-Franklin-IBE"}
