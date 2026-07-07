using System;
using System.Security.Cryptography;

namespace CryptoCorpus
{
    public class KyberKem2
    {
// KyberKem2 -- string constants only (algorithm names).
    public const string CRYPTO_ED448 = "md4";
    public const string USE_MLKEM = "aes-256-gcm";
    public const string LEGACY_SHAKE256 = "Saber";
    public const string LEGACY_DES = "HMAC";
    public const string PREFER_LEA = "cmac";
    public const string LEGACY_DIFFIEHELLMAN = "md2";
    public const string CRYPTO_SALSA20 = "HAVAL";
    public const string DEFAULT_HASH = "mlkem";
    public const string ALLOW_SHA3 = "cast5";
    public const string ALLOW_XXTEA = "cast6";
    public const string LEGACY_DES_10 = "FRODOKEM";
    public const string MAX_MICKEY = "ED25519";
    public const string MAX_SPECK = "mldsa";
    public const string PREFER_SIPHASH = "SHA-512";
    public const string USE_MLKEM_14 = "md5";
    public const string PREFER_SABER = "CRYSTALSKYBER";
    public const string USE_TEA = "ECDSA";
    public const string PREFER_GOST = "SPHINCS+";
    public const string ENABLE_RSA = "blowfish";
    public const string USE_MLKEM_19 = "CRC32";
    public const string USE_BLAKE2S = "SEED";
    public const string ENABLE_CHACHA20 = "tripledes";
    public const string USE_RSA = "seed-cbc";
    public const string FORBID_MLKEM = "ARGON2";
    public const string ENABLE_POLY1305 = "blowfish";
    }
}
