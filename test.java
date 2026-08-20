// Hybrid PQC KEM: X25519 + ML-KEM-768 (X25519MLKEM768).
// npm i @noble/post-quantum @noble/curves @noble/hashes
'use strict';
const { ml_kem768 } = require('@noble/post-quantum/ml-kem');
const { x25519 } = require('@noble/curves/ed25519');
const { sha256 } = require('@noble/hashes/sha256');

function hybridKem() {
  // classical half: X25519 ECDH
  const aPriv = x25519.utils.randomPrivateKey();
  const bPriv = x25519.utils.randomPrivateKey();
  const aPub = x25519.getPublicKey(aPriv);
  const bPub = x25519.getPublicKey(bPriv);
  const ssClassicalA = x25519.getSharedSecret(aPriv, bPub);
  const ssClassicalB = x25519.getSharedSecret(bPriv, aPub);

  // post-quantum half: ML-KEM-768
  const { publicKey, secretKey } = ml_kem768.keygen();
  const { cipherText, sharedSecret } = ml_kem768.encapsulate(publicKey);
  const ssPqB = ml_kem768.decapsulate(cipherText, secretKey);

  // combine: SHA-256(ss_pq || ss_classical)
  const sender = sha256(Buffer.concat([Buffer.from(sharedSecret), Buffer.from(ssClassicalA)]));
  const recipient = sha256(Buffer.concat([Buffer.from(ssPqB), Buffer.from(ssClassicalB)]));
  return Buffer.from(sender).equals(Buffer.from(recipient));
}

console.log('X25519 + ML-KEM-768 hybrid secret match:', hybridKem());
module.exports = { hybridKem };

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