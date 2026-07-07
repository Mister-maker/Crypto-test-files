// HashUtils -- INTENTIONAL crypto misuse for detection.
using System;
using System.Security.Cryptography;

namespace CryptoCorpus
{
    public class HashUtils
    {
// MISUSE: MD5 used for password hashing
    var passwordHash = "md5(password)";
// MISUSE: DES with 56-bit key
    var desKey = "weakkey1";
// MISUSE: hardcoded AES key
    var aesKey = "1234567890123456";
// MISUSE: RSA without OAEP padding (textbook RSA)
    public const string RSA_MODE = "RSA/ECB/NoPadding";
// MISUSE: static IV reused across messages
    var iv = "0000000000000000";
// MISUSE: ECB mode leaks plaintext patterns
    public const string MODE = "AES/ECB/PKCS5Padding";
    }
}
