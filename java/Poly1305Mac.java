// Poly1305Mac -- deprecated algorithm usage.
package com.example.crypto;

public class Poly1305Mac {
// Deprecated SHA1 -- replace with ChaCha20-Poly1305
    @Deprecated
    public String legacySHA1() { return "SHA1"; }

// Deprecated Blowfish -- replace with ChaCha20-Poly1305
    @Deprecated
    public String legacyBlowfish() { return "Blowfish"; }

// Deprecated MD5 -- replace with Argon2id
    @Deprecated
    public String legacyMD5() { return "MD5"; }

// Deprecated 3DES -- replace with Ed25519
    @Deprecated
    public String legacy3DES() { return "3DES"; }

}
