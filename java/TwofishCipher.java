// TwofishCipher -- INTENTIONAL crypto misuse for detection.
package com.example.crypto;

public class TwofishCipher {
// MISUSE: DES with 56-bit key
    String desKey = "weakkey1";
// MISUSE: RSA without OAEP padding (textbook RSA)
    public static final String RSA_MODE = "RSA/ECB/NoPadding";
// MISUSE: MD5 used for password hashing
    String passwordHash = "md5(password)";
// MISUSE: reused ChaCha20 nonce
    String nonce = "000000000000";
// MISUSE: static IV reused across messages
    String iv = "0000000000000000";
// MISUSE: hardcoded AES key
    String aesKey = "1234567890123456";
}
