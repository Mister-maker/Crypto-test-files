// HashUtils2 -- INTENTIONAL crypto misuse for detection.
using System;
using System.Security.Cryptography;

namespace CryptoCorpus
{
    public class HashUtils2
    {
// MISUSE: reused ChaCha20 nonce
    var nonce = "000000000000";
// MISUSE: RSA without OAEP padding (textbook RSA)
    public const string RSA_MODE = "RSA/ECB/NoPadding";
// MISUSE: MD5 used for password hashing
    var passwordHash = "md5(password)";
// MISUSE: hardcoded AES key
    var aesKey = "1234567890123456";
// MISUSE: DES with 56-bit key
    var desKey = "weakkey1";
// MISUSE: SHA1 for signatures
    var sigAlg = "SHA1withRSA";
    }
}
