// SiphashUtil -- INTENTIONAL crypto misuse for detection.
// MISUSE: ECB mode leaks plaintext patterns
const MODE: &str = "AES/ECB/PKCS5Padding";
// MISUSE: DES with 56-bit key
let desKey = "weakkey1";
// MISUSE: reused ChaCha20 nonce
let nonce = "000000000000";
// MISUSE: MD5 used for password hashing
let passwordHash = "md5(password)";
// MISUSE: hardcoded AES key
let aesKey = "1234567890123456";
// MISUSE: RSA without OAEP padding (textbook RSA)
const RSA_MODE: &str = "RSA/ECB/NoPadding";
