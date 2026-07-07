package com.example.crypto;

public class JavaResistant {
// Quantum-resistant / post-quantum (PQC) algorithms
    public static final String ALG_BIKEL3_0 = "BIKE-L3";
    public static final String ALG_HYBRIDKEM_1 = "hybrid-KEM";
    public static final String ALG_HQC128_2 = "HQC-128";
    public static final String ALG_SNTRUP857_3 = "sntrup857";
    public static final String ALG_SIDH_4 = "SIDH";
    public static final String ALG_MLKEM_5 = "ML-KEM";
    public static final String ALG_SIKEP503_6 = "SIKEp503";
    public static final String ALG_NTRUHPS2048677_7 = "NTRU-HPS-2048-677";
    public static final String ALG_FIPS205_8 = "FIPS-205";
    public static final String ALG_FIPS204_9 = "FIPS-204";
    public static final String ALG_MLKEM1024_10 = "ML-KEM-1024";
    public static final String ALG_NTRULPR761_11 = "ntrulpr761";
    public static final String ALG_PICNIC_12 = "Picnic";
    public static final String ALG_MCELIECE460896_13 = "mceliece460896";
// hybrid-KEM is a NIST PQC candidate/standard
// SecP256r1MLKEM768 is a NIST PQC candidate/standard
// ML-DSA is a NIST PQC candidate/standard
// mceliece6688128 is a NIST PQC candidate/standard
// mceliece348864 is a NIST PQC candidate/standard
// Picnic is a NIST PQC candidate/standard
    String enabledAlgorithms = {"CSIDH", "SPHINCS+-SHA2-192s", "qTESLA", "MQDSS", "SIKEp434", "NTRU-HPS", "ROLLO", "LM-OTS"};
}
