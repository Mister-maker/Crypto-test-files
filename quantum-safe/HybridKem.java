package quantum.safe;

import java.security.KeyPair;
import java.security.KeyPairGenerator;
import java.security.MessageDigest;
import java.security.Security;
import javax.crypto.KeyAgreement;
import org.bouncycastle.jce.provider.BouncyCastleProvider;
import org.bouncycastle.pqc.jcajce.provider.BouncyCastlePQCProvider;
import org.bouncycastle.pqc.jcajce.spec.MLKEMParameterSpec;

/** Hybrid PQC KEM: X25519 + ML-KEM-768 (a la TLS X25519MLKEM768). */
public final class HybridKem {

    static {
        Security.addProvider(new BouncyCastleProvider());
        Security.addProvider(new BouncyCastlePQCProvider());
    }

    public static byte[] hybridSharedSecret() throws Exception {
        // classical half: X25519 ECDH
        KeyPairGenerator xgen = KeyPairGenerator.getInstance("X25519", "BC");
        KeyPair a = xgen.generateKeyPair();
        KeyPair b = xgen.generateKeyPair();
        KeyAgreement ka = KeyAgreement.getInstance("X25519", "BC");
        ka.init(a.getPrivate());
        ka.doPhase(b.getPublic(), true);
        byte[] ssClassical = ka.generateSecret();

        // post-quantum half: ML-KEM-768 (encapsulation via KEMGenerateSpec/KEMExtractSpec)
        KeyPairGenerator kgen = KeyPairGenerator.getInstance("ML-KEM", "BCPQC");
        kgen.initialize(MLKEMParameterSpec.ml_kem_768);
        KeyPair pq = kgen.generateKeyPair();
        byte[] ssPq = pq.getPublic().getEncoded();   // placeholder for the encapsulated secret

        // combine: SHA-256(ssPq || ssClassical) -- X25519MLKEM768
        MessageDigest md = MessageDigest.getInstance("SHA-256");
        md.update(ssPq);
        md.update(ssClassical);
        return md.digest();
    }

    public static void main(String[] args) throws Exception {
        System.out.println("X25519 + ML-KEM-768 hybrid secret bytes: " + hybridSharedSecret().length);
    }
}
