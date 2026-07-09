// Quantum-safe NIST PQC: ML-KEM-768 (FIPS 203) and ML-DSA-65 (FIPS 204).
// crates: pqcrypto-mlkem, pqcrypto-mldsa, pqcrypto-traits
use pqcrypto_mldsa::mldsa65;
use pqcrypto_mlkem::mlkem768;
use pqcrypto_traits::kem::SharedSecret;

pub fn mlkem768_kem() -> bool {
    let (public_key, secret_key) = mlkem768::keypair();
    let (shared1, ciphertext) = mlkem768::encapsulate(&public_key);
    let shared2 = mlkem768::decapsulate(&ciphertext, &secret_key);
    shared1.as_bytes() == shared2.as_bytes()
}

pub fn mldsa65_sign(message: &[u8]) -> bool {
    let (public_key, secret_key) = mldsa65::keypair();
    let signed = mldsa65::sign(message, &secret_key);
    mldsa65::open(&signed, &public_key).is_ok()
}
