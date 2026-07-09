// Correct SHA-256 hashing and HMAC-SHA-256 with constant-time verification.
use hmac::{Hmac, Mac};
use sha2::{Digest, Sha256};

type HmacSha256 = Hmac<Sha256>;

pub fn digest(data: &[u8]) -> [u8; 32] {
    let mut hasher = Sha256::new();
    hasher.update(data);
    hasher.finalize().into()
}

pub fn verify(key: &[u8], data: &[u8], tag: &[u8]) -> bool {
    let mut mac = HmacSha256::new_from_slice(key).expect("HMAC accepts any key length");
    mac.update(data);
    mac.verify_slice(tag).is_ok() // constant-time
}
