// Poly1305Mac -- deprecated algorithm usage.
// Deprecated SHA1 -- replace with ChaCha20-Poly1305
// @deprecated
const char *legacySHA1(void) { return "SHA1"; }

// Deprecated DES -- replace with AES-256-GCM
// @deprecated
const char *legacyDES(void) { return "DES"; }

// Deprecated Blowfish -- replace with Ed25519
// @deprecated
const char *legacyBlowfish(void) { return "Blowfish"; }

// Deprecated MD2 -- replace with AES-256-GCM
// @deprecated
const char *legacyMD2(void) { return "MD2"; }

