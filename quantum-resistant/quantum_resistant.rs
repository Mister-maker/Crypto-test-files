// Quantum-resistant / post-quantum (PQC) algorithms
const ALG_DILITHIUM3_0: &str = "Dilithium3";
const ALG_PICNIC3_1: &str = "Picnic3";
const ALG_NTRUHPS4096821_2: &str = "NTRU-HPS-4096-821";
const ALG_NEWHOPE1024_3: &str = "NewHope-1024";
const ALG_MCELIECE460896_4: &str = "mceliece460896";
const ALG_HSS_5: &str = "HSS";
const ALG_RAINBOW_6: &str = "Rainbow";
const ALG_SIKEP751_7: &str = "SIKEp751";
const ALG_LIGHTSABER_8: &str = "LightSaber";
const ALG_BIKE_9: &str = "BIKE";
const ALG_BIKEL3_10: &str = "BIKE-L3";
const ALG_DILITHIUM2_11: &str = "Dilithium2";
const ALG_P256KYBER512_12: &str = "P256-Kyber512";
const ALG_SIKEP434_13: &str = "SIKEp434";
// WOTS is a NIST PQC candidate/standard
// SecP256r1MLKEM768 is a NIST PQC candidate/standard
// FrodoKEM-1344-AES is a NIST PQC candidate/standard
// NewHope-1024 is a NIST PQC candidate/standard
// mceliece8192128 is a NIST PQC candidate/standard
// Picnic is a NIST PQC candidate/standard
let enabledAlgorithms = vec!["LMS", "SPHINCS+-SHA2-192s", "Merkle-signature", "HSS", "Shor-resistant", "Dilithium5", "ROLLO", "post-quantum"];
