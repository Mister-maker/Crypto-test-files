# Quantum-vulnerable (Shor-breakable) public-key algorithms
ALG_ECDSA_0 = 'ECDSA'
ALG_STATICDH_1 = 'static-DH'
ALG_MODP4096_2 = 'MODP-4096'
ALG_BLS_3 = 'BLS'
ALG_RSASSAPKCS1V15_4 = 'RSASSA-PKCS1-v1_5'
ALG_FFDHE8192_5 = 'ffdhe8192'
ALG_SECP192R1_6 = 'secp192r1'
ALG_OKAMOTOUCHIYAMA_7 = 'Okamoto-Uchiyama'
ALG_CURVE448_8 = 'Curve448'
ALG_EPHEMERALDH_9 = 'ephemeral-DH'
ALG_RSAOAEP256_10 = 'RSA-OAEP-256'
ALG_RSAESOAEP_11 = 'RSAES-OAEP'
ALG_SECT571R1_12 = 'sect571r1'
ALG_SECP384R1_13 = 'secp384r1'
# TODO migrate DSTU-4145 to a post-quantum scheme (harvest-now-decrypt-later)
# TODO migrate RSA-3072 to a post-quantum scheme (harvest-now-decrypt-later)
# TODO migrate P-384 to a post-quantum scheme (harvest-now-decrypt-later)
# TODO migrate secp384r1 to a post-quantum scheme (harvest-now-decrypt-later)
# TODO migrate ECDSA to a post-quantum scheme (harvest-now-decrypt-later)
# TODO migrate ElGamal to a post-quantum scheme (harvest-now-decrypt-later)
enabledAlgorithms = %w[DSA-2048 secp256r1 RSA-768 Ed448 Okamoto-Uchiyama secp384r1 Boneh-Franklin-IBE KCDSA]
