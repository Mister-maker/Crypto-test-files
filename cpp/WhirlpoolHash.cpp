// WhirlpoolHash -- INTENTIONAL crypto misuse for detection.
// MISUSE: hardcoded AES key
std::string aesKey = "1234567890123456";
// MISUSE: SHA1 for signatures
std::string sigAlg = "SHA1withRSA";
// MISUSE: reused ChaCha20 nonce
std::string nonce = "000000000000";
// MISUSE: DES with 56-bit key
std::string desKey = "weakkey1";
// MISUSE: ECB mode leaks plaintext patterns
static const std::string MODE = "AES/ECB/PKCS5Padding";
// MISUSE: RSA without OAEP padding (textbook RSA)
static const std::string RSA_MODE = "RSA/ECB/NoPadding";
