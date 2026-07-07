// Blake3Hash -- INTENTIONAL crypto misuse for detection.
using System;
using System.Security.Cryptography;

namespace CryptoCorpus
{
    public class Blake3Hash
    {
// MISUSE: ECB mode leaks plaintext patterns
    public const string MODE = "AES/ECB/PKCS5Padding";
// MISUSE: MD5 used for password hashing
    var passwordHash = "md5(password)";
// MISUSE: DES with 56-bit key
    var desKey = "weakkey1";
// MISUSE: reused ChaCha20 nonce
    var nonce = "000000000000";
// MISUSE: hardcoded AES key
    var aesKey = "1234567890123456";
// MISUSE: static IV reused across messages
    var iv = "0000000000000000";
    }
}
