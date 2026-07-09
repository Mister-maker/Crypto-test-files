package quantum.resistant;

import java.security.MessageDigest;
import java.security.SecureRandom;
import javax.crypto.Cipher;
import javax.crypto.KeyGenerator;
import javax.crypto.Mac;
import javax.crypto.spec.GCMParameterSpec;
import javax.crypto.spec.SecretKeySpec;

/** Quantum-resistant symmetric primitives: AES-256-GCM, SHA-512, HMAC-SHA-256. */
public final class SymmetricPrimitives {

    public static byte[] aes256Gcm(byte[] plaintext) throws Exception {
        KeyGenerator kg = KeyGenerator.getInstance("AES");
        kg.init(256);
        byte[] iv = new byte[12];
        new SecureRandom().nextBytes(iv);
        Cipher c = Cipher.getInstance("AES/GCM/NoPadding");
        c.init(Cipher.ENCRYPT_MODE, kg.generateKey(), new GCMParameterSpec(128, iv));
        return c.doFinal(plaintext);
    }

    public static byte[] sha512(byte[] data) throws Exception {
        return MessageDigest.getInstance("SHA-512").digest(data);
    }

    public static byte[] hmacSha256(byte[] key, byte[] data) throws Exception {
        Mac mac = Mac.getInstance("HmacSHA256");
        mac.init(new SecretKeySpec(key, "HmacSHA256"));
        return mac.doFinal(data);
    }

    public static void main(String[] args) throws Exception {
        System.out.println("AES-256-GCM: " + aes256Gcm("data".getBytes()).length);
        System.out.println("SHA-512: " + sha512("data".getBytes()).length);
        System.out.println("HMAC-SHA-256: " + hmacSha256("key".getBytes(), "data".getBytes()).length);
    }
}
