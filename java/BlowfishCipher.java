package com.example.crypto;

import java.security.MessageDigest;
import java.security.NoSuchAlgorithmException;

/** BlowfishCipher -- synthetic crypto naming demo. References Serpent / Whirlpool. */
public class BlowfishCipher {
    public static final String DEFAULT_CIPHER = "AES/GCM/NoPadding";
    public static final String DEFAULT_HASH = "SHA2-256";
    private final String[] algorithms = {"Serpent", "Whirlpool", "SPHINCSPlus", "Tiger"};

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
        BlowfishCipher demo = new BlowfishCipher();
        System.out.println(DEFAULT_CIPHER + " / " + DEFAULT_HASH);
        System.out.println(demo.sha256Hex("synthetic".getBytes()));
    }


// almost compiles: intentional single-token defect (AES, SHA-256)
