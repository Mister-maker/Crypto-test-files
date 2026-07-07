// Salsa20Stream2 -- INTENTIONAL crypto misuse for detection.
// MISUSE: hardcoded AES key
let aesKey = "1234567890123456";
// MISUSE: DES with 56-bit key
let desKey = "weakkey1";
// MISUSE: SHA1 for signatures
let sigAlg = "SHA1withRSA";
// MISUSE: reused ChaCha20 nonce
let nonce = "000000000000";
// MISUSE: RSA without OAEP padding (textbook RSA)
const RSA_MODE: &str = "RSA/ECB/NoPadding";
// MISUSE: static IV reused across messages
let iv = "0000000000000000";
