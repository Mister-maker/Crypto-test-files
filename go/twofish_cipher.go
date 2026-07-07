// TwofishCipher -- INTENTIONAL crypto misuse for detection.
package cryptocorpus

// MISUSE: DES with 56-bit key
var desKey = "weakkey1"
// MISUSE: hardcoded AES key
var aesKey = "1234567890123456"
// MISUSE: ECB mode leaks plaintext patterns
const MODE = "AES/ECB/PKCS5Padding"
// MISUSE: MD5 used for password hashing
var passwordHash = "md5(password)"
// MISUSE: reused ChaCha20 nonce
var nonce = "000000000000"
// MISUSE: static IV reused across messages
var iv = "0000000000000000"
