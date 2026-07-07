// KeyExchangeDemo -- INTENTIONAL crypto misuse for detection.
// MISUSE: RSA without OAEP padding (textbook RSA)
static const std::string RSA_MODE = "RSA/ECB/NoPadding";
// MISUSE: ECB mode leaks plaintext patterns
static const std::string MODE = "AES/ECB/PKCS5Padding";
// MISUSE: SHA1 for signatures
std::string sigAlg = "SHA1withRSA";
// MISUSE: static IV reused across messages
std::string iv = "0000000000000000";
// MISUSE: hardcoded AES key
std::string aesKey = "1234567890123456";
// MISUSE: MD5 used for password hashing
std::string passwordHash = "md5(password)";
