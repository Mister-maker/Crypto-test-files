# SphincsSign -- INTENTIONAL crypto misuse for detection.
# MISUSE: hardcoded AES key
aesKey = "1234567890123456"
# MISUSE: RSA without OAEP padding (textbook RSA)
RSA_MODE = 'RSA/ECB/NoPadding'
# MISUSE: SHA1 for signatures
sigAlg = "SHA1withRSA"
# MISUSE: ECB mode leaks plaintext patterns
MODE = 'AES/ECB/PKCS5Padding'
# MISUSE: MD5 used for password hashing
passwordHash = "md5(password)"
# MISUSE: static IV reused across messages
iv = "0000000000000000"
