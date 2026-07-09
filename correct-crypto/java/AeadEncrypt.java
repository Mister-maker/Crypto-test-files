package correct.crypto;

import java.security.SecureRandom;
import javax.crypto.Cipher;
import javax.crypto.KeyGenerator;
import javax.crypto.SecretKey;
import javax.crypto.spec.GCMParameterSpec;

/** Correct AES-256-GCM authenticated encryption with a fresh random IV. */
public final class AeadEncrypt {
    private static final int IV_LEN = 12;        // 96-bit nonce for GCM
    private static final int TAG_BITS = 128;
    private static final SecureRandom RNG = new SecureRandom();

    public static byte[] encrypt(SecretKey key, byte[] plaintext, byte[] aad) throws Exception {
        byte[] iv = new byte[IV_LEN];
        RNG.nextBytes(iv);                       // unique per message
        Cipher cipher = Cipher.getInstance("AES/GCM/NoPadding");
        cipher.init(Cipher.ENCRYPT_MODE, key, new GCMParameterSpec(TAG_BITS, iv));
        if (aad != null) {
            cipher.updateAAD(aad);
        }
        byte[] ct = cipher.doFinal(plaintext);
        byte[] out = new byte[IV_LEN + ct.length];
        System.arraycopy(iv, 0, out, 0, IV_LEN);
        System.arraycopy(ct, 0, out, IV_LEN, ct.length);
        return out;
    }

    public static void main(String[] args) throws Exception {
        KeyGenerator kg = KeyGenerator.getInstance("AES");
        kg.init(256);
        SecretKey key = kg.generateKey();
        byte[] blob = encrypt(key, "correct".getBytes(), "header".getBytes());
        System.out.println("AES-256-GCM output bytes: " + blob.length);
    }
}
