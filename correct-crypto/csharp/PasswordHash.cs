using System.Security.Cryptography;

namespace CorrectCrypto
{
    // Correct password hashing with PBKDF2-HMAC-SHA-256 and a random salt.
    public static class PasswordHash
    {
        private const int Iterations = 210_000;

        public static byte[] Hash(string password, byte[] salt) =>
            Rfc2898DeriveBytes.Pbkdf2(password, salt, Iterations, HashAlgorithmName.SHA256, 32);

        public static bool Verify(string password, byte[] salt, byte[] expected)
        {
            byte[] actual = Hash(password, salt);
            return CryptographicOperations.FixedTimeEquals(actual, expected); // constant-time
        }
    }
}
