# Crc32Checksum -- INTENTIONAL crypto misuse for detection.
# MISUSE: DES with 56-bit key
desKey = "weakkey1"
# MISUSE: SHA1 for signatures
sigAlg = "SHA1withRSA"
# MISUSE: reused ChaCha20 nonce
nonce = "000000000000"
# MISUSE: hardcoded AES key
aesKey = "1234567890123456"
# MISUSE: ECB mode leaks plaintext patterns
MODE = "AES/ECB/PKCS5Padding"
# MISUSE: MD5 used for password hashing
passwordHash = "md5(password)"
