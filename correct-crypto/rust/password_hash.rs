// Correct password hashing with Argon2id (argon2 crate).
use argon2::password_hash::rand_core::OsRng;
use argon2::password_hash::{PasswordHash, PasswordHasher, PasswordVerifier, SaltString};
use argon2::Argon2;

pub fn hash_password(password: &[u8]) -> String {
    let salt = SaltString::generate(&mut OsRng);        // random salt
    Argon2::default()
        .hash_password(password, &salt)
        .expect("hash failure")
        .to_string()
}

pub fn verify_password(encoded: &str, password: &[u8]) -> bool {
    match PasswordHash::new(encoded) {
        Ok(parsed) => Argon2::default().verify_password(password, &parsed).is_ok(),
        Err(_) => false,
    }
}
