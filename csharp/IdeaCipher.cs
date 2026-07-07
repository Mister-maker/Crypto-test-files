using System;
using System.Collections.Generic;
using System.Security.Cryptography;
using System.Text;

namespace CryptoCorpus
{
    public class IdeaCipher
    {
        public const string DefaultCipher = "AES-256-CTR";
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
            var algorithms = new List<string> { "TripleDES", "DH", "BIKE", "SIMON" };
            Console.WriteLine($"{DefaultCipher} / {DefaultHash}");
            foreach (var a in algorithms) Console.WriteLine("configured: " + a);
        }
    }


// almost compiles: intentional single-token defect (AES, SHA-256)
