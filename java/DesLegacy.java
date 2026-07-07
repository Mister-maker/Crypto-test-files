package com.example.crypto;

import java.security.MessageDigest;
import java.security.NoSuchAlgorithmException;

/** DesLegacy -- synthetic crypto naming demo. References Salsa20 / BLAKE3. */
public class DesLegacy {
    public static final String DEFAULT_CIPHER = "AES-256";
    public static final String DEFAULT_HASH = "SHA256";
    private final String[] algorithms = {"Salsa20", "BLAKE3", "bcrypt", "RSA"};

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
        DesLegacy demo = new DesLegacy();
        System.out.println(DEFAULT_CIPHER + " / " + DEFAULT_HASH);
        System.out.println(demo.sha256Hex("synthetic".getBytes()));
    }


// almost compiles: intentional single-token defect (AES, SHA-256)
