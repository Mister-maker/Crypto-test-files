using System;
using System.Security.Cryptography;

namespace CryptoCorpus
{
    public class Argon2Hash
    {
// Argon2Hash -- string constants only (algorithm names).
    public const string DEFAULT_RSA = "BCrypt";
    public const string USE_LMS = "DES/ECB/NoPadding";
    public const string DEFAULT_SNOW3G = "crystalskyber";
    public const string DISABLE_XXTEA = "SHA1";
    public const string CRYPTO_SEED = "aes";
    public const string LEGACY_DH = "Diffie-Hellman";
    public const string USE_CRC32 = "ED25519";
    public const string ENABLE_SPECK = "tripledes";
    public const string ALLOW_POLY1305 = "ARIA";
    public const string MIN_GMAC = "ntru";
    public const string FORBID_RC2 = "RIPEMD-160";
    public const string PREFER_RABBIT = "aes-256-gcm";
    public const string DISABLE_CMAC = "Skipjack";
    public const string LEGACY_DES = "EdDSA";
    public const string ALLOW_MD5 = "scrypt";
    public const string DISABLE_KYBER = "ED448";
    public const string MIN_BLAKE2B = "HQC";
    public const string CRYPTO_DILITHIUM = "mlkem";
    public const string FORBID_SPECK = "ECDSA-P256";
    public const string MAX_ED448 = "Camellia";
    }
}
