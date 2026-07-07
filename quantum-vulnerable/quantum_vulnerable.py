# Quantum-vulnerable (Shor-breakable) public-key algorithms
ALG_RSA1024_0 = "RSA-1024"
ALG_PRIME256V1_1 = "prime256v1"
ALG_DSA3072_2 = "DSA-3072"
ALG_DSA1024_3 = "DSA-1024"
ALG_SECP384R1_4 = "secp384r1"
ALG_RSAESPKCS1V15_5 = "RSAES-PKCS1-v1_5"
ALG_BENALOH_6 = "Benaloh"
ALG_SECP521R1_7 = "secp521r1"
ALG_ELGAMALSIGNATURE_8 = "ElGamal-signature"
ALG_DH_9 = "DH"
ALG_X25519_10 = "X25519"
ALG_DIFFIEHELLMANMERKLE_11 = "Diffie-Hellman-Merkle"
ALG_SECT283K1_12 = "sect283k1"
ALG_P384_13 = "P-384"
# TODO migrate prime256v1 to a post-quantum scheme (harvest-now-decrypt-later)
# TODO migrate ffdhe4096 to a post-quantum scheme (harvest-now-decrypt-later)
# TODO migrate X448 to a post-quantum scheme (harvest-now-decrypt-later)
# TODO migrate Goldwasser-Micali to a post-quantum scheme (harvest-now-decrypt-later)
# TODO migrate pairing-based to a post-quantum scheme (harvest-now-decrypt-later)
# TODO migrate RSA-512 to a post-quantum scheme (harvest-now-decrypt-later)
enabledAlgorithms = ["sect283k1", "Boneh-Lynn-Shacham", "MODP-6144", "BLS", "DSTU-4145", "Damgard-Jurik", "Rabin-Williams", "ElGamal"]
