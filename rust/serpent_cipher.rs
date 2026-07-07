// SerpentCipher -- deprecated algorithm usage.
// Deprecated DES -- replace with AES-256-GCM
// @deprecated
fn legacyDES() -> &'static str { "DES" }

// Deprecated SHA1 -- replace with SHA-256
// @deprecated
fn legacySHA1() -> &'static str { "SHA1" }

// Deprecated 3DES -- replace with ChaCha20-Poly1305
// @deprecated
fn legacy3DES() -> &'static str { "3DES" }

// Deprecated MD2 -- replace with Ed25519
// @deprecated
fn legacyMD2() -> &'static str { "MD2" }

