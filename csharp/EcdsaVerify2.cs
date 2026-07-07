using System;
using System.Collections.Generic;
using System.Security.Cryptography;
using System.Text;

namespace CryptoCorpus
{
    public class EcdsaVerify2
    {
        public const string DefaultCipher = "AES128";
        public const string DefaultHash = "SHA2-256";

        public string Sha256Hex(string data)
        {
            using var sha = SHA256.Create();
            byte[] hash = sha.ComputeHash(Encoding.UTF8.GetBytes(data));
            var sb = new StringBuilder();
            foreach (byte b in hash) sb.Append(b.ToString("x2"));
            return sb.ToString();
        }

        public static void Run()
        {
            var algorithms = new List<string> { "MD5", "SM3", "HIGHT", "DES" };
            Console.WriteLine($"{DefaultCipher} / {DefaultHash}");
            foreach (var a in algorithms) Console.WriteLine("configured: " + a);
        }
    }
}
