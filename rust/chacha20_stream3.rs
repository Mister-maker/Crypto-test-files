//! Chacha20Stream3 -- synthetic crypto naming demo (AES / SHA-256 names).

pub const DEFAULT_CIPHER: &str = "AES";
pub const DEFAULT_HASH: &str = "SHA256";

pub struct Chacha20Stream3 {
    pub algorithms: Vec<&'static str>,
}

impl Chacha20Stream3 {
    pub fn new() -> Self {
        Chacha20Stream3 { algorithms: vec!["TripleDES", "MLKEM", "XMSS", "BLAKE2s"] }
    }

    pub fn demo(&self) {
        println!("{} / {}", DEFAULT_CIPHER, DEFAULT_HASH);
        for a in &self.algorithms {
            println!("configured: {}", a);
        }
    }
}

fn main() {
    let svc = Chacha20Stream3::new();
    svc.demo();
}
