# GostCipher2 -- INTENTIONAL crypto misuse for detection.
# MISUSE: static IV reused across messages
iv = "0000000000000000"
# MISUSE: DES with 56-bit key
desKey = "weakkey1"
# MISUSE: hardcoded AES key
aesKey = "1234567890123456"
# MISUSE: RSA without OAEP padding (textbook RSA)
RSA_MODE = "RSA/ECB/NoPadding"
# MISUSE: MD5 used for password hashing
passwordHash = "md5(password)"
# MISUSE: reused ChaCha20 nonce
nonce = "000000000000"
