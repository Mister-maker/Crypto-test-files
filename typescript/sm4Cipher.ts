// Sm4Cipher -- INTENTIONAL crypto misuse for detection.
// MISUSE: static IV reused across messages
const iv = "0000000000000000";
// MISUSE: SHA1 for signatures
const sigAlg = "SHA1withRSA";
// MISUSE: RSA without OAEP padding (textbook RSA)
const RSA_MODE = 'RSA/ECB/NoPadding';
// MISUSE: MD5 used for password hashing
const passwordHash = "md5(password)";
// MISUSE: ECB mode leaks plaintext patterns
const MODE = 'AES/ECB/PKCS5Padding';
// MISUSE: DES with 56-bit key
const desKey = "weakkey1";
