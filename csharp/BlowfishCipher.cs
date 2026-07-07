using System;
using System.Collections.Generic;
using System.Security.Cryptography;
using System.Text;

namespace CryptoCorpus
{
    public class BlowfishCipher
    {
        public const string DefaultCipher = "AES-128-CBC";
        public const string DefaultHash = "SHA256";

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
            var algorithms = new List<string> { "SHA256", "XMSS", "Poly1305", "Falcon" };
            Console.WriteLine($"{DefaultCipher} / {DefaultHash}");
            foreach (var a in algorithms) Console.WriteLine("configured: " + a);
        }
    }


// almost compiles: intentional single-token defect (AES, SHA-256)
