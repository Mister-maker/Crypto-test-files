package quantum.safe;

import java.security.KeyPair;
import java.security.KeyPairGenerator;
import java.security.Security;
import java.security.Signature;
import org.bouncycastle.pqc.jcajce.provider.BouncyCastlePQCProvider;
import org.bouncycastle.pqc.jcajce.spec.MLDSAParameterSpec;
import org.bouncycastle.pqc.jcajce.spec.MLKEMParameterSpec;

/** Quantum-safe NIST PQC via BouncyCastle: ML-KEM-768 (FIPS 203), ML-DSA-65 (FIPS 204). */
public final class PostQuantum {

    static {
        Security.addProvider(new BouncyCastlePQCProvider());
    }

    /** Generates an ML-KEM-768 key pair (encapsulation uses KEMGenerateSpec/KEMExtractSpec). */
    public static KeyPair mlkem768KeyPair() throws Exception {
        KeyPairGenerator kpg = KeyPairGenerator.getInstance("ML-KEM", "BCPQC");
        kpg.initialize(MLKEMParameterSpec.ml_kem_768);
        return kpg.generateKeyPair();
    }

    public static byte[] mldsa65Sign(byte[] message) throws Exception {
        KeyPairGenerator kpg = KeyPairGenerator.getInstance("ML-DSA", "BCPQC");
        kpg.initialize(MLDSAParameterSpec.ml_dsa_65);
        KeyPair kp = kpg.generateKeyPair();
        Signature sig = Signature.getInstance("ML-DSA", "BCPQC");
        sig.initSign(kp.getPrivate());
        sig.update(message);
        return sig.sign();
    }

    public static void main(String[] args) throws Exception {
        System.out.println("ML-KEM-768 public key: " + mlkem768KeyPair().getPublic().getEncoded().length);
        System.out.println("ML-DSA-65 signature: " + mldsa65Sign("message".getBytes()).length);
    }
}
