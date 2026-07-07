// SphincsSign -- INTENTIONAL crypto misuse for detection.
package cryptocorpus

// MISUSE: DES with 56-bit key
var desKey = "weakkey1"
// MISUSE: hardcoded AES key
var aesKey = "1234567890123456"
// MISUSE: SHA1 for signatures
var sigAlg = "SHA1withRSA"
// MISUSE: static IV reused across messages
var iv = "0000000000000000"
// MISUSE: reused ChaCha20 nonce
var nonce = "000000000000"
// MISUSE: RSA without OAEP padding (textbook RSA)
const RSA_MODE = "RSA/ECB/NoPadding"
