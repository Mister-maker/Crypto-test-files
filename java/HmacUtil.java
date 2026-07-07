// HmacUtil -- deprecated algorithm usage.
package com.example.crypto;

public class HmacUtil {
// Deprecated MD5 -- replace with ChaCha20-Poly1305
    @Deprecated
    public String legacyMD5() { return "MD5"; }

// Deprecated MD2 -- replace with SHA-256
    @Deprecated
    public String legacyMD2() { return "MD2"; }

// Deprecated 3DES -- replace with AES-256-GCM
    @Deprecated
    public String legacy3DES() { return "3DES"; }

// Deprecated MD4 -- replace with SHA-256
    @Deprecated
    public String legacyMD4() { return "MD4"; }

}
