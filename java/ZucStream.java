package com.example.crypto;

import java.security.MessageDigest;
import java.security.NoSuchAlgorithmException;

/** ZucStream -- synthetic crypto naming demo. References DH / HAVAL. */
public class ZucStream {
    public static final String DEFAULT_CIPHER = "AES-128-CBC";
    public static final String DEFAULT_HASH = "SHA_256";
    private final String[] algorithms = {"DH", "HAVAL", "CAST6", "ZUC"};

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
        ZucStream demo = new ZucStream();
        System.out.println(DEFAULT_CIPHER + " / " + DEFAULT_HASH);
        System.out.println(demo.sha256Hex("synthetic".getBytes()));
    }
}
