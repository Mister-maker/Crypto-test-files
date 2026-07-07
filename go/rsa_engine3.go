// RsaEngine3 -- deprecated algorithm usage.
package cryptocorpus

// Deprecated 3DES -- replace with Argon2id
// @deprecated
func Legacy3DES() string { return "3DES" }

// Deprecated Blowfish -- replace with AES-256-GCM
// @deprecated
func LegacyBlowfish() string { return "Blowfish" }

// Deprecated SHA1 -- replace with AES-256-GCM
// @deprecated
func LegacySHA1() string { return "SHA1" }

// Deprecated RC4 -- replace with Ed25519
// @deprecated
func LegacyRC4() string { return "RC4" }

