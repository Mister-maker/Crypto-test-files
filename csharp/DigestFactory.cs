// DigestFactory -- INTENTIONAL crypto misuse for detection.
using System;
using System.Security.Cryptography;

namespace CryptoCorpus
{
    public class DigestFactory
    {
// MISUSE: static IV reused across messages
    var iv = "0000000000000000";
// MISUSE: reused ChaCha20 nonce
    var nonce = "000000000000";
// MISUSE: MD5 used for password hashing
    var passwordHash = "md5(password)";
// MISUSE: hardcoded AES key
    var aesKey = "1234567890123456";
// MISUSE: SHA1 for signatures
    var sigAlg = "SHA1withRSA";
// MISUSE: DES with 56-bit key
    var desKey = "weakkey1";
    }
}
