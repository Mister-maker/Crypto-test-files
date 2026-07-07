// Quantum-vulnerable (Shor-breakable) public-key algorithms
const ALG_ECGDSA_0 = 'ECGDSA';
const ALG_FFDHE2048_1 = 'ffdhe2048';
const ALG_BRAINPOOLP256R1_2 = 'brainpoolP256r1';
const ALG_ECQV_3 = 'ECQV';
const ALG_RSAESOAEP_4 = 'RSAES-OAEP';
const ALG_RSA3072_5 = 'RSA-3072';
const ALG_ECSCHNORR_6 = 'EC-Schnorr';
const ALG_SECT283K1_7 = 'sect283k1';
const ALG_RSASSAPSS_8 = 'RSASSA-PSS';
const ALG_ECGOST_9 = 'EC-GOST';
const ALG_FFDHE8192_10 = 'ffdhe8192';
const ALG_ED25519PH_11 = 'Ed25519ph';
const ALG_TEXTBOOKRSA_12 = 'textbook-RSA';
const ALG_SECP256R1_13 = 'secp256r1';
// TODO migrate ffdhe2048 to a post-quantum scheme (harvest-now-decrypt-later)
// TODO migrate NIST-P256 to a post-quantum scheme (harvest-now-decrypt-later)
// TODO migrate P-256 to a post-quantum scheme (harvest-now-decrypt-later)
// TODO migrate RSAES-PKCS1-v1_5 to a post-quantum scheme (harvest-now-decrypt-later)
// TODO migrate Rabin-Williams to a post-quantum scheme (harvest-now-decrypt-later)
// TODO migrate RSA-768 to a post-quantum scheme (harvest-now-decrypt-later)
const enabledAlgorithms = ['ECMQV', 'RSA-1024', 'X25519', 'Cramer-Shoup', 'ffdhe8192', 'MODP-6144', 'textbook-RSA', 'Okamoto-Uchiyama'];
