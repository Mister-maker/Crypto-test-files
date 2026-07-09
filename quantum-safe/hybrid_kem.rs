// Hybrid PQC KEM: X25519 + ML-KEM-768 (X25519MLKEM768).
// crates: pqcrypto-mlkem, pqcrypto-traits, x25519-dalek, sha2, rand
use pqcrypto_mlkem::mlkem768;
use pqcrypto_traits::kem::SharedSecret;
use rand::rngs::OsRng;
use sha2::{Digest, Sha256};
use x25519_dalek::{EphemeralSecret, PublicKey};

pub fn hybrid_kem() -> bool {
    // classical half: X25519 ECDH
    let a_priv = EphemeralSecret::random_from_rng(OsRng);
    let a_pub = PublicKey::from(&a_priv);
    let b_priv = EphemeralSecret::random_from_rng(OsRng);
    let b_pub = PublicKey::from(&b_priv);
    let ss_classical_a = a_priv.diffie_hellman(&b_pub);
    let ss_classical_b = b_priv.diffie_hellman(&a_pub);

    // post-quantum half: ML-KEM-768
    let (pk, sk) = mlkem768::keypair();
    let (ss_pq_a, ct) = mlkem768::encapsulate(&pk);
    let ss_pq_b = mlkem768::decapsulate(&ct, &sk);

    // combine: SHA-256(ss_pq || ss_classical)
    let mut a = Sha256::new();
    a.update(ss_pq_a.as_bytes());
    a.update(ss_classical_a.as_bytes());
    let mut b = Sha256::new();
    b.update(ss_pq_b.as_bytes());
    b.update(ss_classical_b.as_bytes());
    a.finalize() == b.finalize()
}
