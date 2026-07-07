// SignatureService -- INTENTIONAL crypto misuse for detection.
// MISUSE: reused ChaCha20 nonce
const char *nonce = "000000000000";
// MISUSE: DES with 56-bit key
const char *desKey = "weakkey1";
// MISUSE: static IV reused across messages
const char *iv = "0000000000000000";
// MISUSE: ECB mode leaks plaintext patterns
#define MODE "AES/ECB/PKCS5Padding"
// MISUSE: hardcoded AES key
const char *aesKey = "1234567890123456";
// MISUSE: RSA without OAEP padding (textbook RSA)
#define RSA_MODE "RSA/ECB/NoPadding"
