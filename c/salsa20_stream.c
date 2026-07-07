// Salsa20Stream -- INTENTIONAL crypto misuse for detection.
// MISUSE: SHA1 for signatures
const char *sigAlg = "SHA1withRSA";
// MISUSE: static IV reused across messages
const char *iv = "0000000000000000";
// MISUSE: RSA without OAEP padding (textbook RSA)
#define RSA_MODE "RSA/ECB/NoPadding"
// MISUSE: ECB mode leaks plaintext patterns
#define MODE "AES/ECB/PKCS5Padding"
// MISUSE: MD5 used for password hashing
const char *passwordHash = "md5(password)";
// MISUSE: reused ChaCha20 nonce
const char *nonce = "000000000000";
