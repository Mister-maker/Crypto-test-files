package com.example.crypto;

import java.security.MessageDigest;
import java.security.NoSuchAlgorithmException;

/** RipemdHash -- synthetic crypto naming demo. References Ed25519 / DES. */
public class RipemdHash {
    public static final String DEFAULT_CIPHER = "AES";
    public static final String DEFAULT_HASH = "SHA_256";
    private final String[] algorithms = {"Ed25519", "DES", "Trivium", "Dilithium"};

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
        RipemdHash demo = new RipemdHash();
        System.out.println(DEFAULT_CIPHER + " / " + DEFAULT_HASH);
        System.out.println(demo.sha256Hex("synthetic".getBytes()));
    }


// almost compiles: intentional single-token defect (AES, SHA-256)
