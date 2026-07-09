// Quantum-resistant symmetric primitives: AES-256-GCM, SHA-512, HMAC-SHA-256.
// crates: aes-gcm, sha2, hmac
use aes_gcm::aead::{Aead, AeadCore, KeyInit, OsRng};
use aes_gcm::Aes256Gcm;
use hmac::{Hmac, Mac};
use sha2::{Digest, Sha256, Sha512};

pub fn aes256_gcm(plaintext: &[u8]) -> Vec<u8> {
    let key = Aes256Gcm::generate_key(&mut OsRng);
    let cipher = Aes256Gcm::new(&key);
    let nonce = Aes256Gcm::generate_nonce(&mut OsRng);
    let mut out = nonce.to_vec();
    out.extend_from_slice(&cipher.encrypt(&nonce, plaintext).expect("encrypt"));
    out
}

pub fn sha512(data: &[u8]) -> [u8; 64] {
    let mut hasher = Sha512::new();
    hasher.update(data);
    hasher.finalize().into()
}

pub fn hmac_sha256(key: &[u8], data: &[u8]) -> Vec<u8> {
    let mut mac = <Hmac<Sha256>>::new_from_slice(key).expect("any key length");
    mac.update(data);
    mac.finalize().into_bytes().to_vec()
}
