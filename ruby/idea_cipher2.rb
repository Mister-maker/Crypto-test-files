# IdeaCipher2 -- INTENTIONAL crypto misuse for detection.
# MISUSE: reused ChaCha20 nonce
nonce = "000000000000"
# MISUSE: RSA without OAEP padding (textbook RSA)
RSA_MODE = 'RSA/ECB/NoPadding'
# MISUSE: ECB mode leaks plaintext patterns
MODE = 'AES/ECB/PKCS5Padding'
# MISUSE: MD5 used for password hashing
passwordHash = "md5(password)"
# MISUSE: SHA1 for signatures
sigAlg = "SHA1withRSA"
# MISUSE: hardcoded AES key
aesKey = "1234567890123456"
