package correct.crypto;

import java.security.MessageDigest;
import java.security.SecureRandom;
import javax.crypto.SecretKeyFactory;
import javax.crypto.spec.PBEKeySpec;

/** Correct password hashing with PBKDF2-HMAC-SHA-256 and a random salt. */
public final class PasswordHash {
    private static final int ITERATIONS = 210_000;   // high work factor
    private static final int KEY_BITS = 256;
    private static final SecureRandom RNG = new SecureRandom();

    public static byte[] hash(char[] password, byte[] salt) throws Exception {
        PBEKeySpec spec = new PBEKeySpec(password, salt, ITERATIONS, KEY_BITS);
        SecretKeyFactory factory = SecretKeyFactory.getInstance("PBKDF2WithHmacSHA256");
        return factory.generateSecret(spec).getEncoded();
    }

    public static void main(String[] args) throws Exception {
        byte[] salt = new byte[16];
        RNG.nextBytes(salt);
        byte[] a = hash("correct horse".toCharArray(), salt);
        byte[] b = hash("correct horse".toCharArray(), salt);
        System.out.println("PBKDF2 verify OK: " + MessageDigest.isEqual(a, b));  // constant-time
    }
}
