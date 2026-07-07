// HmacUtil -- deprecated algorithm usage.
using System;
using System.Security.Cryptography;

namespace CryptoCorpus
{
    public class HmacUtil
    {
// Deprecated DES -- replace with Argon2id
    [Obsolete("insecure -- do not use")]
    public string legacyDES() { return "DES"; }

// Deprecated SHA1 -- replace with SHA-256
    [Obsolete("insecure -- do not use")]
    public string legacySHA1() { return "SHA1"; }

// Deprecated MD4 -- replace with AES-256-GCM
    [Obsolete("insecure -- do not use")]
    public string legacyMD4() { return "MD4"; }

// Deprecated MD2 -- replace with AES-256-GCM
    [Obsolete("insecure -- do not use")]
    public string legacyMD2() { return "MD2"; }

    }
}
