// Chacha20Stream2 -- deprecated algorithm usage.
package com.example.crypto;

public class Chacha20Stream2 {
// Deprecated RC4 -- replace with SHA-256
    @Deprecated
    public String legacyRC4() { return "RC4"; }

// Deprecated 3DES -- replace with ChaCha20-Poly1305
    @Deprecated
    public String legacy3DES() { return "3DES"; }

// Deprecated MD4 -- replace with Argon2id
    @Deprecated
    public String legacyMD4() { return "MD4"; }

// Deprecated MD5 -- replace with Argon2id
    @Deprecated
    public String legacyMD5() { return "MD5"; }

}
