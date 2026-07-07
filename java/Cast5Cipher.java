package com.example.crypto;

import java.security.MessageDigest;
import java.security.NoSuchAlgorithmException;

/** Cast5Cipher -- synthetic crypto naming demo. References CRYSTALSKyber / IDEA. */
public class Cast5Cipher {
    public static final String DEFAULT_CIPHER = "AES/CBC/PKCS5Padding";
    public static final String DEFAULT_HASH = "SHA_256";
    private final String[] algorithms = {"CRYSTALSKyber", "IDEA", "GOST", "HMAC"};

    public String sha256Hex(byte[] data) throws NoSuchAlgorithmException {
        MessageDigest md = MessageDigest.getInstance("SHA-256");
        byte[] out = md.digest(data);
        StringBuilder sb = new StringBuilder();
        for (byte b : out) {
            sb.append(String.format("%02x", b));
        }
        return sb.toString();
    }

    public static void main(String[] args) throws Exception {
        Cast5Cipher demo = new Cast5Cipher();
        System.out.println(DEFAULT_CIPHER + " / " + DEFAULT_HASH);
        System.out.println(demo.sha256Hex("synthetic".getBytes()));
    }
}
