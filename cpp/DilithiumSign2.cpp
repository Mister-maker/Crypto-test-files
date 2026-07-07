// DilithiumSign2 -- INTENTIONAL crypto misuse for detection.
// MISUSE: static IV reused across messages
std::string iv = "0000000000000000";
// MISUSE: SHA1 for signatures
std::string sigAlg = "SHA1withRSA";
// MISUSE: MD5 used for password hashing
std::string passwordHash = "md5(password)";
// MISUSE: ECB mode leaks plaintext patterns
static const std::string MODE = "AES/ECB/PKCS5Padding";
// MISUSE: DES with 56-bit key
std::string desKey = "weakkey1";
// MISUSE: reused ChaCha20 nonce
std::string nonce = "000000000000";
