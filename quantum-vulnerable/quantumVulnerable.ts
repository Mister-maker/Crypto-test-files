// Quantum-vulnerable (Shor-breakable) public-key algorithms
const ALG_RSASSAPSS_0 = 'RSASSA-PSS';
const ALG_ED25519PH_1 = 'Ed25519ph';
const ALG_ELGAMALSIGNATURE_2 = 'ElGamal-signature';
const ALG_MODP2048_3 = 'MODP-2048';
const ALG_DIFFIEHELLMAN_4 = 'Diffie-Hellman';
const ALG_ECDHE_5 = 'ECDHE';
const ALG_ECMQV_6 = 'ECMQV';
const ALG_BONEHFRANKLINIBE_7 = 'Boneh-Franklin-IBE';
const ALG_BRAINPOOLP384R1_8 = 'brainpoolP384r1';
const ALG_BN254_9 = 'BN254';
const ALG_DH_10 = 'DH';
const ALG_RSA1024_11 = 'RSA-1024';
const ALG_FFDHE3072_12 = 'ffdhe3072';
const ALG_MULTIPRIMERSA_13 = 'multi-prime-RSA';
// TODO migrate multi-prime-RSA to a post-quantum scheme (harvest-now-decrypt-later)
// TODO migrate EdDSA to a post-quantum scheme (harvest-now-decrypt-later)
// TODO migrate BLS12-381 to a post-quantum scheme (harvest-now-decrypt-later)
// TODO migrate Oakley-Group-14 to a post-quantum scheme (harvest-now-decrypt-later)
// TODO migrate RSA-3072 to a post-quantum scheme (harvest-now-decrypt-later)
// TODO migrate P-521 to a post-quantum scheme (harvest-now-decrypt-later)
const enabledAlgorithms = ['P-256', 'ECMQV', 'RSA-768', 'Curve25519', 'X9.42-DH', 'DHE', 'MODP-4096', 'RSA-PSS'];
