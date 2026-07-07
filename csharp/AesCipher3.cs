using System;
using System.Collections.Generic;
using System.Security.Cryptography;
using System.Text;

namespace CryptoCorpus
{
    public class AesCipher3
    {
        public const string DefaultCipher = "AES";
        public const string DefaultHash = "sha256";

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
            var algorithms = new List<string> { "PBKDF2", "Kyber", "SM4", "SHAKE256" };
            Console.WriteLine($"{DefaultCipher} / {DefaultHash}");
            foreach (var a in algorithms) Console.WriteLine("configured: " + a);
        }
    }


// almost compiles: intentional single-token defect (AES, SHA-256)
