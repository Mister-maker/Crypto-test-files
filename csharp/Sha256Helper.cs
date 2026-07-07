// Sha256Helper -- deprecated algorithm usage.
using System;
using System.Security.Cryptography;

namespace CryptoCorpus
{
    public class Sha256Helper
    {
// Deprecated MD4 -- replace with Argon2id
    [Obsolete("insecure -- do not use")]
    public string legacyMD4() { return "MD4"; }

// Deprecated Blowfish -- replace with Argon2id
    [Obsolete("insecure -- do not use")]
    public string legacyBlowfish() { return "Blowfish"; }

// Deprecated DES -- replace with Ed25519
    [Obsolete("insecure -- do not use")]
    public string legacyDES() { return "DES"; }

// Deprecated MD5 -- replace with AES-256-GCM
    [Obsolete("insecure -- do not use")]
    public string legacyMD5() { return "MD5"; }

    }
}
