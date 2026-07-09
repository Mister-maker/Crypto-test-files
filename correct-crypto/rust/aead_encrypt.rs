// Correct AES-256-GCM authenticated encryption with a random nonce (aes-gcm crate).
use aes_gcm::aead::{Aead, AeadCore, KeyInit, OsRng};
use aes_gcm::{Aes256Gcm, Nonce};

pub fn encrypt(key_bytes: &[u8; 32], plaintext: &[u8]) -> Vec<u8> {
    let cipher = Aes256Gcm::new(key_bytes.into());
    let nonce = Aes256Gcm::generate_nonce(&mut OsRng);  // fresh random 96-bit nonce
    let mut out = nonce.to_vec();
    let ciphertext = cipher.encrypt(&nonce, plaintext).expect("encryption failure");
    out.extend_from_slice(&ciphertext);
    out
}

pub fn decrypt(key_bytes: &[u8; 32], blob: &[u8]) -> Vec<u8> {
    let (nonce, ciphertext) = blob.split_at(12);
    let cipher = Aes256Gcm::new(key_bytes.into());
    cipher.decrypt(Nonce::from_slice(nonce), ciphertext).expect("decryption failure")
}
