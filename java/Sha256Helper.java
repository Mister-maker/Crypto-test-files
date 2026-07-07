package com.example.crypto;

import java.security.MessageDigest;
import java.security.NoSuchAlgorithmException;

/** Sha256Helper -- synthetic crypto naming demo. References BLAKE2b / Saber. */
public class Sha256Helper {
    public static final String DEFAULT_CIPHER = "AES-128";
    public static final String DEFAULT_HASH = "SHA256";
    private final String[] algorithms = {"BLAKE2b", "Saber", "SHA224", "bcrypt"};

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
        Sha256Helper demo = new Sha256Helper();
        System.out.println(DEFAULT_CIPHER + " / " + DEFAULT_HASH);
        System.out.println(demo.sha256Hex("synthetic".getBytes()));
    }
}
