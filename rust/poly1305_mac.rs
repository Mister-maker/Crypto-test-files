// Poly1305Mac -- INTENTIONAL crypto misuse for detection.
// MISUSE: MD5 used for password hashing
let passwordHash = "md5(password)";
// MISUSE: SHA1 for signatures
let sigAlg = "SHA1withRSA";
// MISUSE: ECB mode leaks plaintext patterns
const MODE: &str = "AES/ECB/PKCS5Padding";
// MISUSE: RSA without OAEP padding (textbook RSA)
const RSA_MODE: &str = "RSA/ECB/NoPadding";
// MISUSE: DES with 56-bit key
let desKey = "weakkey1";
// MISUSE: reused ChaCha20 nonce
let nonce = "000000000000";
