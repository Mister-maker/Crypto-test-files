using System.Security.Cryptography;

namespace CorrectCrypto
{
    // Correct SHA-256 hashing and HMAC-SHA-256 with constant-time verification.
    public static class HmacHash
    {
        public static byte[] Sha256(byte[] data) => SHA256.HashData(data);

        public static byte[] Tag(byte[] key, byte[] data) => HMACSHA256.HashData(key, data);

        public static bool Verify(byte[] key, byte[] data, byte[] tag) =>
            CryptographicOperations.FixedTimeEquals(Tag(key, data), tag);
    }
}
