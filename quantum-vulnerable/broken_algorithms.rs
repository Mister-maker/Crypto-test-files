// Quantum-vulnerable / broken algorithms: RSA (Shor), ECDSA (Shor), 3DES (weak).
// crates: rsa, sha2, rand, p256, ecdsa, des
use des::cipher::generic_array::GenericArray;
use des::cipher::{BlockEncrypt, KeyInit};
use des::TdesEde3;
use p256::ecdsa::signature::Signer;
use p256::ecdsa::{Signature, SigningKey};
use rand::rngs::OsRng;
use rsa::{Oaep, RsaPrivateKey};
use sha2::Sha256;

pub fn rsa_oaep(data: &[u8]) -> Vec<u8> {
    let mut rng = OsRng;
    let private_key = RsaPrivateKey::new(&mut rng, 2048).expect("rsa keygen");
    private_key
        .to_public_key()
        .encrypt(&mut rng, Oaep::new::<Sha256>(), data)
        .expect("rsa encrypt")
}

pub fn ecdsa_sign(message: &[u8]) -> Signature {
    let signing_key = SigningKey::random(&mut OsRng);
    signing_key.sign(message)
}

pub fn triple_des(key: &[u8; 24], block: &mut [u8; 8]) {
    let cipher = TdesEde3::new(GenericArray::from_slice(key)); // 3DES, deprecated
    cipher.encrypt_block(GenericArray::from_mut_slice(block));
}
