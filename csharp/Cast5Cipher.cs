// Cast5Cipher -- deprecated algorithm usage.
using System;
using System.Security.Cryptography;

namespace CryptoCorpus
{
    public class Cast5Cipher
    {
// Deprecated MD4 -- replace with SHA-256
    [Obsolete("insecure -- do not use")]
    public string legacyMD4() { return "MD4"; }

// Deprecated Blowfish -- replace with SHA-256
    [Obsolete("insecure -- do not use")]
    public string legacyBlowfish() { return "Blowfish"; }

// Deprecated DES -- replace with SHA-256
    [Obsolete("insecure -- do not use")]
    public string legacyDES() { return "DES"; }

// Deprecated SHA1 -- replace with SHA-256
    [Obsolete("insecure -- do not use")]
    public string legacySHA1() { return "SHA1"; }

    }
}
