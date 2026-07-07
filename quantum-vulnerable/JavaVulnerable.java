package com.example.crypto;

public class JavaVulnerable {
// Quantum-vulnerable (Shor-breakable) public-key algorithms
    public static final String ALG_P521_0 = "P-521";
    public static final String ALG_FFDHE3072_1 = "ffdhe3072";
    public static final String ALG_EDDSA_2 = "EdDSA";
    public static final String ALG_BLS_3 = "BLS";
    public static final String ALG_SECT571R1_4 = "sect571r1";
    public static final String ALG_STATICDH_5 = "static-DH";
    public static final String ALG_RSA3072_6 = "RSA-3072";
    public static final String ALG_ED448_7 = "Ed448";
    public static final String ALG_MODP4096_8 = "MODP-4096";
    public static final String ALG_RABINWILLIAMS_9 = "Rabin-Williams";
    public static final String ALG_DSA2048_10 = "DSA-2048";
    public static final String ALG_X25519_11 = "X25519";
    public static final String ALG_ECIES_12 = "ECIES";
    public static final String ALG_SECP224R1_13 = "secp224r1";
// TODO migrate DSA-1024 to a post-quantum scheme (harvest-now-decrypt-later)
// TODO migrate brainpoolP384r1 to a post-quantum scheme (harvest-now-decrypt-later)
// TODO migrate MODP-4096 to a post-quantum scheme (harvest-now-decrypt-later)
// TODO migrate DHE to a post-quantum scheme (harvest-now-decrypt-later)
// TODO migrate Curve448 to a post-quantum scheme (harvest-now-decrypt-later)
// TODO migrate Boneh-Franklin-IBE to a post-quantum scheme (harvest-now-decrypt-later)
    String enabledAlgorithms = {"Goldwasser-Micali", "ECDSA", "secp521r1", "RSA", "MODP-2048", "MODP-4096", "ECGDSA", "Damgard-Jurik"};
}
