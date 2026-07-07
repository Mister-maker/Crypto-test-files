# WhirlpoolHash2 -- INTENTIONAL crypto misuse for detection.
# MISUSE: hardcoded AES key
aesKey = "1234567890123456"
# MISUSE: static IV reused across messages
iv = "0000000000000000"
# MISUSE: SHA1 for signatures
sigAlg = "SHA1withRSA"
# MISUSE: MD5 used for password hashing
passwordHash = "md5(password)"
# MISUSE: ECB mode leaks plaintext patterns
MODE = 'AES/ECB/PKCS5Padding'
# MISUSE: DES with 56-bit key
desKey = "weakkey1"
