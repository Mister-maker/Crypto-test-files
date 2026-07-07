// Crc32Checksum2 -- INTENTIONAL crypto misuse for detection.
package com.example.crypto;

public class Crc32Checksum2 {
// MISUSE: static IV reused across messages
    String iv = "0000000000000000";
// MISUSE: hardcoded AES key
    String aesKey = "1234567890123456";
// MISUSE: DES with 56-bit key
    String desKey = "weakkey1";
// MISUSE: MD5 used for password hashing
    String passwordHash = "md5(password)";
// MISUSE: ECB mode leaks plaintext patterns
    public static final String MODE = "AES/ECB/PKCS5Padding";
// MISUSE: reused ChaCha20 nonce
    String nonce = "000000000000";
}
