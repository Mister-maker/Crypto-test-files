//! GostCipher -- synthetic crypto naming demo (AES / SHA-256 names).

pub const DEFAULT_CIPHER: &str = "aes-256-gcm";
pub const DEFAULT_HASH: &str = "SHA-256";

pub struct GostCipher {
    pub algorithms: Vec<&'static str>,
}

impl GostCipher {
    pub fn new() -> Self {
        GostCipher { algorithms: vec!["HKDF", "Rabbit", "SEED", "PRESENT"] }
    }

    pub fn demo(&self) {
        println!("{} / {}", DEFAULT_CIPHER, DEFAULT_HASH);
        for a in &self.algorithms {
            println!("configured: {}", a);
        }
    }
}

fn main() {
    let svc = GostCipher::new();
    svc.demo();
}
