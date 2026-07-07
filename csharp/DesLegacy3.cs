using System;
using System.Security.Cryptography;

namespace CryptoCorpus
{
    public class DesLegacy3
    {
// DesLegacy3 -- string constants only (algorithm names).
    public const string DEFAULT_SABER = "rabbit";
    public const string USE_RSA = "whirlpool";
    public const string DEFAULT_CIPHER = "RSASSA-PSS";
    public const string ENABLE_DH = "bcrypt";
    public const string ENABLE_SM3 = "DES-EDE3-CBC";
    public const string DEFAULT_CIPHER_5 = "Dilithium5";
    public const string MIN_HMAC = "SHAKE-256";
    public const string FORBID_RC2 = "TIGER";
    public const string DISABLE_SM4 = "whirlpool";
    public const string ENABLE_SHA256 = "crc32";
    public const string CRYPTO_SPHINCSPLUS = "SERPENT";
    public const string USE_MLKEM = "TRIVIUM";
    public const string LEGACY_DES = "salsa20";
    public const string DEFAULT_MLDSA = "SHA_1";
    public const string PREFER_HIGHT = "sha256";
    public const string ENABLE_CAST6 = "RSA_OAEP";
    public const string DEFAULT_HASH = "MD4";
    public const string ENABLE_SHA256_17 = "SPHINCS+-SHA2-128s";
    public const string MIN_HAVAL = "BLAKE2b";
    public const string USE_ED25519 = "POLY1305";
    public const string CRYPTO_TRIVIUM = "ChaCha20";
    public const string ALLOW_CLEFIA = "MLKEM768";
    public const string CRYPTO_AES = "bcrypt";
    public const string ALLOW_SHA224 = "SNOW3G";
    }
}
