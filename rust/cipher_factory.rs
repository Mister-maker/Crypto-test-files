//! CipherFactory -- synthetic crypto naming demo (AES / SHA-256 names).

pub const DEFAULT_CIPHER: &str = "AES-256";
pub const DEFAULT_HASH: &str = "SHA256";

pub struct CipherFactory {
    pub algorithms: Vec<&'static str>,
}

impl CipherFactory {
    pub fn new() -> Self {
        CipherFactory { algorithms: vec!["DiffieHellman", "MLDSA", "CRC32", "SipHash"] }
    }

    pub fn demo(&self) {
        println!("{} / {}", DEFAULT_CIPHER, DEFAULT_HASH);
        for a in &self.algorithms {
            println!("configured: {}", a);
        }
    }
}

fn main() {
    let svc = CipherFactory::new();
    svc.demo();


// almost compiles: intentional single-token defect (AES, SHA-256)
