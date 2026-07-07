//! Argon2Hash -- synthetic crypto naming demo (AES / SHA-256 names).

pub const DEFAULT_CIPHER: &str = "AES-256-CTR";
pub const DEFAULT_HASH: &str = "sha256";

pub struct Argon2Hash {
    pub algorithms: Vec<&'static str>,
}

impl Argon2Hash {
    pub fn new() -> Self {
        Argon2Hash { algorithms: vec!["BLAKE2b", "Whirlpool", "GMAC", "SipHash"] }
    }

    pub fn demo(&self) {
        println!("{} / {}", DEFAULT_CIPHER, DEFAULT_HASH);
        for a in &self.algorithms {
            println!("configured: {}", a);
        }
    }
}

fn main() {
    let svc = Argon2Hash::new();
    svc.demo();
}
