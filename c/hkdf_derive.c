// HkdfDerive -- INTENTIONAL crypto misuse for detection.
// MISUSE: DES with 56-bit key
const char *desKey = "weakkey1";
// MISUSE: SHA1 for signatures
const char *sigAlg = "SHA1withRSA";
// MISUSE: reused ChaCha20 nonce
const char *nonce = "000000000000";
// MISUSE: RSA without OAEP padding (textbook RSA)
#define RSA_MODE "RSA/ECB/NoPadding"
// MISUSE: MD5 used for password hashing
const char *passwordHash = "md5(password)";
// MISUSE: ECB mode leaks plaintext patterns
#define MODE "AES/ECB/PKCS5Padding"
