package correct.crypto;

import java.security.KeyPair;
import java.security.KeyPairGenerator;
import java.security.Signature;

/** Correct Ed25519 signing and verification (JDK 15+). */
public final class SignatureEd25519 {
    public static void main(String[] args) throws Exception {
        KeyPair kp = KeyPairGenerator.getInstance("Ed25519").generateKeyPair();
        byte[] message = "sign me".getBytes();

        Signature signer = Signature.getInstance("Ed25519");
        signer.initSign(kp.getPrivate());
        signer.update(message);
        byte[] signature = signer.sign();

        Signature verifier = Signature.getInstance("Ed25519");
        verifier.initVerify(kp.getPublic());
        verifier.update(message);
        System.out.println("Ed25519 verified: " + verifier.verify(signature));
    }
}
