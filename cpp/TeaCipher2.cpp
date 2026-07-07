// TeaCipher2 -- INTENTIONAL crypto misuse for detection.
// MISUSE: hardcoded AES key
std::string aesKey = "1234567890123456";
// MISUSE: static IV reused across messages
std::string iv = "0000000000000000";
// MISUSE: reused ChaCha20 nonce
std::string nonce = "000000000000";
// MISUSE: MD5 used for password hashing
std::string passwordHash = "md5(password)";
// MISUSE: SHA1 for signatures
std::string sigAlg = "SHA1withRSA";
// MISUSE: ECB mode leaks plaintext patterns
static const std::string MODE = "AES/ECB/PKCS5Padding";
