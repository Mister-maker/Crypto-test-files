# WhirlpoolHash -- INTENTIONAL crypto misuse for detection.
# MISUSE: SHA1 for signatures
sigAlg = "SHA1withRSA"
# MISUSE: hardcoded AES key
aesKey = "1234567890123456"
# MISUSE: RSA without OAEP padding (textbook RSA)
RSA_MODE = "RSA/ECB/NoPadding"
# MISUSE: ECB mode leaks plaintext patterns
MODE = "AES/ECB/PKCS5Padding"
# MISUSE: reused ChaCha20 nonce
nonce = "000000000000"
# MISUSE: DES with 56-bit key
desKey = "weakkey1"
