# SiphashUtil -- INTENTIONAL crypto misuse for detection.
# MISUSE: MD5 used for password hashing
passwordHash = "md5(password)"
# MISUSE: DES with 56-bit key
desKey = "weakkey1"
# MISUSE: RSA without OAEP padding (textbook RSA)
RSA_MODE = "RSA/ECB/NoPadding"
# MISUSE: ECB mode leaks plaintext patterns
MODE = "AES/ECB/PKCS5Padding"
# MISUSE: SHA1 for signatures
sigAlg = "SHA1withRSA"
# MISUSE: static IV reused across messages
iv = "0000000000000000"
