using System;
using System.Security.Cryptography;

namespace CorrectCrypto
{
    // Correct AES-256-GCM authenticated encryption with a random nonce.
    public static class AeadEncrypt
    {
        public static byte[] Encrypt(byte[] key, byte[] plaintext, byte[] aad)
        {
            byte[] nonce = RandomNumberGenerator.GetBytes(AesGcm.NonceByteSizes.MaxSize); // 12 bytes
            byte[] tag = new byte[AesGcm.TagByteSizes.MaxSize];                            // 16 bytes
            byte[] ciphertext = new byte[plaintext.Length];

            using var aes = new AesGcm(key, tag.Length);
            aes.Encrypt(nonce, plaintext, ciphertext, tag, aad);

            byte[] output = new byte[nonce.Length + tag.Length + ciphertext.Length];
            Buffer.BlockCopy(nonce, 0, output, 0, nonce.Length);
            Buffer.BlockCopy(tag, 0, output, nonce.Length, tag.Length);
            Buffer.BlockCopy(ciphertext, 0, output, nonce.Length + tag.Length, ciphertext.Length);
            return output;
        }
    }
}
