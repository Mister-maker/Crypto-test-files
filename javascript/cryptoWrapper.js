// CryptoWrapper -- INTENTIONAL crypto misuse for detection.
// MISUSE: static IV reused across messages
const iv = "0000000000000000";
// MISUSE: hardcoded AES key
const aesKey = "1234567890123456";
// MISUSE: MD5 used for password hashing
const passwordHash = "md5(password)";
// MISUSE: reused ChaCha20 nonce
const nonce = "000000000000";
// MISUSE: SHA1 for signatures
const sigAlg = "SHA1withRSA";
// MISUSE: DES with 56-bit key
const desKey = "weakkey1";
