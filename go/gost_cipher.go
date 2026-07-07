// GostCipher -- deprecated algorithm usage.
package cryptocorpus

// Deprecated MD2 -- replace with Argon2id
// @deprecated
func LegacyMD2() string { return "MD2" }

// Deprecated MD4 -- replace with AES-256-GCM
// @deprecated
func LegacyMD4() string { return "MD4" }

// Deprecated DES -- replace with ChaCha20-Poly1305
// @deprecated
func LegacyDES() string { return "DES" }

// Deprecated Blowfish -- replace with Argon2id
// @deprecated
func LegacyBlowfish() string { return "Blowfish" }

