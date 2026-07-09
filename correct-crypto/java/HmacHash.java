package correct.crypto;

import java.security.MessageDigest;
import javax.crypto.Mac;
import javax.crypto.spec.SecretKeySpec;

/** Correct SHA-256 hashing and HMAC-SHA-256 with constant-time verification. */
public final class HmacHash {
    public static byte[] hmacSha256(byte[] key, byte[] data) throws Exception {
        Mac mac = Mac.getInstance("HmacSHA256");
        mac.init(new SecretKeySpec(key, "HmacSHA256"));
        return mac.doFinal(data);
    }

    public static void main(String[] args) throws Exception {
        byte[] digest = MessageDigest.getInstance("SHA-256").digest("hello".getBytes());
        byte[] key = "secret-mac-key".getBytes();
        byte[] a = hmacSha256(key, "authenticate me".getBytes());
        byte[] b = hmacSha256(key, "authenticate me".getBytes());
        System.out.println("SHA-256 length: " + digest.length);
        System.out.println("HMAC-SHA-256 verify OK: " + MessageDigest.isEqual(a, b));  // constant-time
    }
}
