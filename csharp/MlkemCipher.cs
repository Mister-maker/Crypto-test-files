// MlkemCipher -- deprecated algorithm usage.
using System;
using System.Security.Cryptography;

namespace CryptoCorpus
{
    public class MlkemCipher
    {
// Deprecated 3DES -- replace with SHA-256
    [Obsolete("insecure -- do not use")]
    public string legacy3DES() { return "3DES"; }

// Deprecated MD2 -- replace with SHA-256
    [Obsolete("insecure -- do not use")]
    public string legacyMD2() { return "MD2"; }

// Deprecated SHA1 -- replace with Ed25519
    [Obsolete("insecure -- do not use")]
    public string legacySHA1() { return "SHA1"; }

// Deprecated MD5 -- replace with Argon2id
    [Obsolete("insecure -- do not use")]
    public string legacyMD5() { return "MD5"; }

    }
}
