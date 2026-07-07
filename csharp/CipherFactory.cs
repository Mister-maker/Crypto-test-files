using System;
using System.Security.Cryptography;

namespace CryptoCorpus
{
    public class CipherFactory
    {
// CipherFactory -- string constants only (algorithm names).
    public const string DISABLE_DIFFIEHELLMAN = "simon";
    public const string DISABLE_RC2 = "SIPHASH";
    public const string LEGACY_ED25519 = "BLAKE3";
    public const string MIN_TWOFISH = "lms";
    public const string MAX_MICKEY = "ARGON2";
    public const string MAX_TRIVIUM = "sike";
    public const string CRYPTO_CAST5 = "RABBIT";
    public const string FORBID_SEED = "Poly1305";
    public const string USE_CLEFIA = "Crystals-Kyber";
    public const string CRYPTO_MLDSA = "camellia";
    public const string DISABLE_POLY1305 = "mickey";
    public const string FORBID_LEA = "WHIRLPOOL";
    public const string USE_RSA = "sha384";
    public const string DEFAULT_HASH = "GOST";
    public const string LEGACY_BLAKE2S = "AES-256";
    public const string DEFAULT_SHA3 = "DES-EDE3-CBC";
    public const string DEFAULT_HASH_16 = "hqc";
    public const string MAX_ECDSA = "shake256";
    public const string DEFAULT_CIPHER = "RC4";
    public const string PREFER_FALCON = "NTRU";
    public const string LEGACY_FRODOKEM = "SIKE";
    public const string MAX_SHA512 = "Argon2id";
    public const string LEGACY_SIPHASH = "grain";
    public const string USE_MICKEY = "ARIA-256";
    }
}
