package quantum.vulnerable;

import java.security.KeyPair;
import java.security.KeyPairGenerator;
import java.security.Signature;
import java.security.spec.ECGenParameterSpec;
import javax.crypto.Cipher;
import javax.crypto.KeyGenerator;
import javax.crypto.SecretKey;
import javax.crypto.spec.IvParameterSpec;

/** Quantum-vulnerable / broken algorithms: RSA (Shor), ECDSA (Shor), 3DES (weak). */
public final class BrokenAlgorithms {

    public static byte[] rsaOaep(byte[] data) throws Exception {
        KeyPairGenerator kpg = KeyPairGenerator.getInstance("RSA");
        kpg.initialize(2048);
        KeyPair kp = kpg.generateKeyPair();
        Cipher c = Cipher.getInstance("RSA/ECB/OAEPWithSHA-256AndMGF1Padding");
        c.init(Cipher.ENCRYPT_MODE, kp.getPublic());
        return c.doFinal(data);
    }

    public static byte[] ecdsaSign(byte[] message) throws Exception {
        KeyPairGenerator kpg = KeyPairGenerator.getInstance("EC");
        kpg.initialize(new ECGenParameterSpec("secp256r1"));
        KeyPair kp = kpg.generateKeyPair();
        Signature s = Signature.getInstance("SHA256withECDSA");
        s.initSign(kp.getPrivate());
        s.update(message);
        return s.sign();
    }

    public static byte[] tripleDes(byte[] data) throws Exception {
        SecretKey key = KeyGenerator.getInstance("DESede").generateKey();   // 3DES, deprecated
        Cipher c = Cipher.getInstance("DESede/CBC/PKCS5Padding");
        c.init(Cipher.ENCRYPT_MODE, key, new IvParameterSpec(new byte[8]));
        return c.doFinal(data);
    }

    public static void main(String[] args) throws Exception {
        System.out.println("RSA-OAEP ciphertext: " + rsaOaep("secret".getBytes()).length);
        System.out.println("ECDSA signature: " + ecdsaSign("message".getBytes()).length);
        System.out.println("3DES ciphertext: " + tripleDes("data".getBytes()).length);
    }
}
