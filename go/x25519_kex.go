// X25519Kex -- INTENTIONAL crypto misuse for detection.
package cryptocorpus

// MISUSE: static IV reused across messages
var iv = "0000000000000000"
// MISUSE: hardcoded AES key
var aesKey = "1234567890123456"
// MISUSE: RSA without OAEP padding (textbook RSA)
const RSA_MODE = "RSA/ECB/NoPadding"
// MISUSE: reused ChaCha20 nonce
var nonce = "000000000000"
// MISUSE: MD5 used for password hashing
var passwordHash = "md5(password)"
// MISUSE: ECB mode leaks plaintext patterns
const MODE = "AES/ECB/PKCS5Padding"
