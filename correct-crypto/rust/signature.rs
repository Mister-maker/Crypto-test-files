// Correct Ed25519 signatures (ed25519-dalek crate).
use ed25519_dalek::{Signature, Signer, SigningKey, Verifier};
use rand::rngs::OsRng;

pub fn sign_and_verify(message: &[u8]) -> bool {
    let mut csprng = OsRng;
    let signing_key = SigningKey::generate(&mut csprng);
    let signature: Signature = signing_key.sign(message);
    signing_key.verifying_key().verify(message, &signature).is_ok()
}
