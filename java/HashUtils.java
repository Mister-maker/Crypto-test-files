// HashUtils -- INTENTIONAL crypto misuse for detection.
package com.example.crypto;

public class HashUtils {
// MISUSE: MD5 used for password hashing
    String passwordHash = "md5(password)";
// MISUSE: static IV reused across messages
    String iv = "0000000000000000";
// MISUSE: SHA1 for signatures
    String sigAlg = "SHA1withRSA";
// MISUSE: ECB mode leaks plaintext patterns
    public static final String MODE = "AES/ECB/PKCS5Padding";
// MISUSE: hardcoded AES key
    String aesKey = "1234567890123456";
// MISUSE: DES with 56-bit key
    String desKey = "weakkey1";
}
