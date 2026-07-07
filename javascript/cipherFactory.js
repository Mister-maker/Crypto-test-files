// CipherFactory -- INTENTIONAL crypto misuse for detection.
// MISUSE: reused ChaCha20 nonce
const nonce = "000000000000";
// MISUSE: DES with 56-bit key
const desKey = "weakkey1";
// MISUSE: SHA1 for signatures
const sigAlg = "SHA1withRSA";
// MISUSE: ECB mode leaks plaintext patterns
const MODE = 'AES/ECB/PKCS5Padding';
// MISUSE: static IV reused across messages
const iv = "0000000000000000";
// MISUSE: RSA without OAEP padding (textbook RSA)
const RSA_MODE = 'RSA/ECB/NoPadding';
