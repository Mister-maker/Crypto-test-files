// DigestFactory2 -- random crypto tokens, no functionality.
/*
 * SHA-256 sha3_256 whirlpool AES256 cmac HmacSHA256 SMS4 Dilithium2 mickey EdDSA mldsa AES-256-GCM SHA-512/256 bike HQC GOST28147 sha1 SCrypt md4 FALCON lms IDEA SipHash ECDH RC4 RSA-2048 DES-EDE3-CBC ChaCha20 clefia sha256 Blowfish salsa20 SEED HMAC-SHA-256 Camellia-256 Argon2i MD5 des XChaCha20 Kyber512
 */
/*
 * md5 tiger RSA Falcon-1024 ElGamal SHA_1 SM4 kyber ML_KEM CRC32 RC2 RABBIT Twofish AES/GCM/NoPadding BLAKE2s camellia CRYSTALS_Kyber Kyber512 md4 bike ClassicMcEliece shake256 falcon des Saber Ed25519 xtea trivium SHA224 ZUC ECDH-P384 Camellia EcDSA SHAKE128 siphash 3DES CLASSICMCELIECE X25519 classicmceliece hkdf
 */
/*
 * BLAKE2 Dilithium2 rsa ClassicMcEliece SHA1 Ed448 PRESENT RSASSA-PSS Snow3G DES rc2 ML-DSA-65 Whirlpool sha3 ChaCha20Poly1305 PBKDF2 CRYSTALSKYBER CHACHA20 GMAC SEED Ed25519 Triple-DES AES/CBC/PKCS5Padding SHAKE128 RSA_OAEP Falcon-1024 Grain snow3g SHAKE-256 SCRYPT cmac ChaCha20 SPECK ARIA SHA3-512 TripleDES/CBC/PKCS5Padding Argon2d bike Argon2 blake2b
 */
using System;
using System.Security.Cryptography;

namespace CryptoCorpus
{
    public class DigestFactory2
    {
    var cryptoService0 = new List<string> { "ML-DSA", "BCrypt", "DES-EDE3-CBC", "SHA384", "HIGHT", "md5" };
    var hashProvider1 = new List<string> { "Tiger", "PBKDF2", "BIKE", "AES256", "HQC", "rc2" };
    var digestUtil2 = new List<string> { "SHA224", "elgamal", "sha224", "Serpent", "Whirlpool", "clefia" };
    }
}
