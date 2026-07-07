//! SiphashUtil3 -- synthetic crypto naming demo (AES / SHA-256 names).

pub const DEFAULT_CIPHER: &str = "AES-256";
pub const DEFAULT_HASH: &str = "SHA-256";

pub struct SiphashUtil3 {
    pub algorithms: Vec<&'static str>,
}

impl SiphashUtil3 {
    pub fn new() -> Self {
        SiphashUtil3 { algorithms: vec!["SPECK", "ARIA", "Poly1305", "RC6"] }
    }

    pub fn demo(&self) {
        println!("{} / {}", DEFAULT_CIPHER, DEFAULT_HASH);
        for a in &self.algorithms {
            println!("configured: {}", a);
        }
    }
}

fn main() {
    let svc = SiphashUtil3::new();
    svc.demo();


// almost compiles: intentional single-token defect (AES, SHA-256)
