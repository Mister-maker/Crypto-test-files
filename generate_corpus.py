#!/usr/bin/env python3
"""
Synthetic crypto-detection test corpus generator.

Generates a large multi-language corpus of source + config files packed with
cryptographic algorithm names in every syntactic position (identifiers, class
names, constants, comments, strings, enums, imports, JSON/YAML/XML/SQL/MD/HTML)
for exercising a static-analysis / crypto-inventory scanner.

This is NOT a real crypto library. Files intentionally include fake APIs, dead
code, deprecated usage, misuse, syntax errors, and pure noise. Security,
correctness and compilation are explicitly NOT goals -- detection coverage is.

Usage:  python3 generate_corpus.py
"""

import os
import re
import json
import random

random.seed(20260707)

HERE = os.path.dirname(os.path.abspath(__file__))

# --------------------------------------------------------------------------
# Algorithm banks
# --------------------------------------------------------------------------

BASE_ALGOS = [
    # block ciphers
    "AES", "DES", "3DES", "TripleDES", "Blowfish", "Twofish", "IDEA", "RC2",
    "RC5", "RC6", "Camellia", "Serpent", "CAST5", "CAST6", "Skipjack", "TEA",
    "XTEA", "XXTEA", "GOST", "SEED", "SM4", "ARIA", "PRESENT", "CLEFIA",
    "HIGHT", "LEA", "SPECK", "SIMON",
    # stream ciphers
    "RC4", "ChaCha20", "Salsa20", "Rabbit", "HC128", "HC256", "Grain",
    "Trivium", "MICKEY", "Snow3G", "ZUC",
    # asymmetric / key exchange / signatures
    "RSA", "DiffieHellman", "DH", "ECDH", "ECDSA", "DSA", "ElGamal", "Ed25519",
    "Ed448", "X25519", "X448",
    # post-quantum
    "Kyber", "MLKEM", "CRYSTALSKyber", "FrodoKEM", "BIKE", "HQC",
    "ClassicMcEliece", "NTRU", "Saber", "SIKE", "Dilithium", "MLDSA", "Falcon",
    "SPHINCSPlus", "XMSS", "LMS",
    # hashes
    "MD2", "MD4", "MD5", "SHA1", "SHA224", "SHA256", "SHA384", "SHA512", "SHA3",
    "SHAKE128", "SHAKE256", "RIPEMD160", "Whirlpool", "Tiger", "HAVAL",
    "BLAKE2", "BLAKE2b", "BLAKE2s", "BLAKE3", "SM3",
    # MAC / KDF / misc
    "Poly1305", "HMAC", "CMAC", "GMAC", "HKDF", "PBKDF2", "bcrypt", "scrypt",
    "Argon2", "SipHash", "CRC32",
]

# Curated textual variants (spaced / hyphenated / suffixed real-world forms).
VARIANTS = {
    "AES": ["AES", "AES-128", "AES-192", "AES-256", "AES128", "AES256",
            "AES-256-GCM", "AES-128-CBC", "AES-256-CTR", "AES/CBC/PKCS5Padding",
            "AES/GCM/NoPadding", "AES_256_GCM", "aes-256-gcm"],
    "DES": ["DES", "DES-CBC", "DES/ECB/NoPadding"],
    "3DES": ["3DES", "Triple-DES", "TripleDES", "DESede", "DES-EDE3-CBC"],
    "TripleDES": ["TripleDES", "3DES", "DESede", "TripleDES/CBC/PKCS5Padding"],
    "Blowfish": ["Blowfish", "blowfish", "Blowfish/CBC/PKCS5Padding"],
    "ChaCha20": ["ChaCha20", "ChaCha20-Poly1305", "XChaCha20", "ChaCha20Poly1305", "chacha20"],
    "Salsa20": ["Salsa20", "salsa20", "XSalsa20"],
    "SHA1": ["SHA1", "SHA-1", "SHA_1", "sha1"],
    "SHA224": ["SHA224", "SHA-224", "SHA2-224"],
    "SHA256": ["SHA256", "SHA-256", "SHA_256", "SHA2-256", "sha256"],
    "SHA384": ["SHA384", "SHA-384", "sha384"],
    "SHA512": ["SHA512", "SHA-512", "SHA-512/256", "sha512"],
    "SHA3": ["SHA3", "SHA-3", "SHA3-256", "SHA3-512", "sha3_256"],
    "SHAKE128": ["SHAKE128", "SHAKE-128", "shake128"],
    "SHAKE256": ["SHAKE256", "SHAKE-256", "shake256"],
    "RIPEMD160": ["RIPEMD160", "RIPEMD-160", "ripemd160"],
    "Whirlpool": ["Whirlpool", "WHIRLPOOL"],
    "BLAKE2": ["BLAKE2", "Blake2"],
    "BLAKE2b": ["BLAKE2b", "BLAKE2b-512", "blake2b"],
    "BLAKE2s": ["BLAKE2s", "BLAKE2s-256", "blake2s"],
    "BLAKE3": ["BLAKE3", "blake3"],
    "MLKEM": ["ML-KEM", "ML-KEM-512", "ML-KEM-768", "ML-KEM-1024", "MLKEM768", "ML_KEM"],
    "MLDSA": ["ML-DSA", "ML-DSA-44", "ML-DSA-65", "ML-DSA-87", "MLDSA65"],
    "CRYSTALSKyber": ["CRYSTALS-Kyber", "CRYSTALS_Kyber", "Crystals-Kyber",
                      "Kyber512", "Kyber768", "Kyber1024"],
    "Dilithium": ["Dilithium", "Dilithium2", "Dilithium3", "Dilithium5"],
    "Falcon": ["Falcon", "Falcon-512", "Falcon-1024"],
    "SPHINCSPlus": ["SPHINCS+", "SPHINCS-Plus", "SPHINCSplus", "SPHINCS+-SHA2-128s"],
    "Ed25519": ["Ed25519", "ed25519", "EdDSA", "Curve25519"],
    "Ed448": ["Ed448", "ed448"],
    "X25519": ["X25519", "x25519", "Curve25519"],
    "X448": ["X448", "x448"],
    "ECDSA": ["ECDSA", "EcDSA", "ECDSA-P256", "ECDSA_secp256r1"],
    "ECDH": ["ECDH", "ECDHE", "ECDH-P384"],
    "RSA": ["RSA", "RSA-2048", "RSA-4096", "RSA_OAEP", "RSASSA-PSS",
            "RSA/ECB/OAEPWithSHA-256AndMGF1Padding"],
    "DiffieHellman": ["DiffieHellman", "Diffie-Hellman", "DH"],
    "Argon2": ["Argon2", "Argon2id", "Argon2i", "Argon2d"],
    "PBKDF2": ["PBKDF2", "PBKDF2WithHmacSHA256", "PBKDF2-HMAC-SHA256"],
    "bcrypt": ["bcrypt", "BCrypt"],
    "scrypt": ["scrypt", "SCrypt"],
    "HMAC": ["HMAC", "HmacSHA256", "HMAC-SHA-256", "HMAC_SHA1"],
    "Poly1305": ["Poly1305", "poly1305"],
    "GOST": ["GOST", "GOST28147", "GOST-R-34.11-2012", "Streebog"],
    "SM4": ["SM4", "SMS4"],
    "SM3": ["SM3", "sm3"],
    "CRC32": ["CRC32", "CRC-32", "crc32c"],
    "Camellia": ["Camellia", "Camellia-256"],
    "SEED": ["SEED", "seed-cbc"],
    "ARIA": ["ARIA", "ARIA-256"],
}


def _all_tokens():
    toks = set()
    for a in BASE_ALGOS:
        toks.add(a)
        toks.add(a.upper())
        toks.add(a.lower())
        for v in VARIANTS.get(a, []):
            toks.add(v)
    return sorted(toks)


ALGO_TOKENS = _all_tokens()

ENABLED = ["AES-256-GCM", "ChaCha20-Poly1305", "RSA-2048", "ECDSA-P256",
           "Ed25519", "X25519", "ML-KEM-768", "ML-DSA-65"]
DEPRECATED = ["MD5", "SHA1", "DES", "3DES", "RC4", "Blowfish"]

# --------------------------------------------------------------------------
# Example banks (verbatim from the spec) + procedural generators
# --------------------------------------------------------------------------

EXTRA_IDENTS = ["aesKey", "sha256Digest", "sha3Hasher", "useMD5", "legacyDES",
                "encryptRSA", "decryptRSA", "rsaEngine", "cryptoProvider",
                "mlKemCipher", "falconSigner", "bcryptRounds", "argon2Hash",
                "pbkdf2Salt", "hkdfExpand", "poly1305Tag", "fakeCrypto"]

EXTRA_CLASSES = ["CryptoManager", "EncryptionService", "HashUtils",
                 "DigestFactory", "AESManager", "SHAHelper", "RSAEngine",
                 "CryptoService", "DigestUtil", "HashProvider", "MLKEMExample",
                 "FakeChaCha20", "CryptoWrapper", "KeyExchangeDemo"]

EXTRA_CONSTS = ["CRYPTO_AES", "ENABLE_SHA256", "USE_RSA", "USE_MLKEM",
                "ALLOW_MD5", "LEGACY_DES", "DEFAULT_HASH", "DEFAULT_CIPHER"]

IDENT_SUF = ["Key", "Digest", "Hash", "Cipher", "Engine", "Signer", "Verifier",
             "Salt", "Nonce", "Tag", "Iv", "Mac", "Kdf", "Rounds", "Provider",
             "Ctx", "Buffer", "Block", "Stream", "Secret", "PublicKey",
             "PrivateKey"]
IDENT_PRE = ["encrypt", "decrypt", "sign", "verify", "hash", "derive", "use",
             "legacy", "init", "compute", "generate", "wrap", "unwrap", "make",
             "fake", "mock", "reset", "update", "finalize"]

CLASS_SUF = ["Manager", "Engine", "Service", "Helper", "Provider", "Util",
             "Factory", "Wrapper", "Example", "Demo", "Handler", "Adapter",
             "Builder", "Cipher", "Hasher", "Signer", "Context"]

CONST_PRE = ["CRYPTO", "ENABLE", "USE", "ALLOW", "LEGACY", "DEFAULT", "DISABLE",
             "REQUIRE", "PREFER", "FORBID", "MAX", "MIN"]

COMMENT_T = [
    "TODO migrate {a} to {b}",
    "TODO: replace {a} with {b}",
    "Deprecated {a} implementation",
    "Uses {a}",
    "Uses {a} in {b} mode",
    "Placeholder {a} code",
    "Fake {a} implementation",
    "Replace {a}",
    "Legacy {a} support",
    "FIXME insecure {a} usage",
    "WARNING: {a} is broken, do not use in production",
    "Migrated from {a} to {b}",
    "{a} key derivation via {b}",
    "NOTE {a} is quantum-vulnerable, prefer {b}",
    "Do not use {a}; use {b} instead",
    "Enable {a} for backward compatibility",
    "{a} is not FIPS 140-3 approved",
    "HACK: hardcoded {a} key",
    "Switching default cipher from {a} to {b}",
    "Requires {a} and {b}",
]


def pick(seq):
    return random.choice(seq)


def picks(seq, k):
    k = min(k, len(seq))
    return random.sample(seq, k)


def algo():
    return pick(ALGO_TOKENS)


def base_algo():
    return pick(BASE_ALGOS)


def safe(name):
    return re.sub(r"[^0-9A-Za-z]", "", name) or "Algo"


def cap(name):
    s = safe(name)
    return s[:1].upper() + s[1:]


def low(name):
    s = safe(name)
    return s[:1].lower() + s[1:]


def pascal(s):
    parts = [p for p in re.split(r"[_\W]+", s) if p]
    return "".join(p[:1].upper() + p[1:] for p in parts) or "Crypto"


def camel(s):
    p = pascal(s)
    return p[:1].lower() + p[1:]


def snake(s):
    s = re.sub(r"(?<!^)(?=[A-Z])", "_", s)
    return re.sub(r"[^0-9a-zA-Z]+", "_", s).lower().strip("_") or "crypto"


def ident():
    b = base_algo()
    if random.random() < 0.45:
        return low(b) + pick(IDENT_SUF)
    return pick(IDENT_PRE) + cap(b)


def ident_any():
    return pick(EXTRA_IDENTS) if random.random() < 0.25 else ident()


def klass():
    b = base_algo()
    if random.random() < 0.15:
        return "Fake" + cap(b)
    return cap(b) + pick(CLASS_SUF)


def klass_any():
    return pick(EXTRA_CLASSES) if random.random() < 0.3 else klass()


def constant():
    return pick(CONST_PRE) + "_" + safe(base_algo()).upper()


def const_any():
    return pick(EXTRA_CONSTS) if random.random() < 0.35 else constant()


def comment_text():
    return pick(COMMENT_T).format(a=algo(), b=algo())


def chunks(seq, n):
    return [seq[i:i + n] for i in range(0, len(seq), n)]


def quote(s):
    return '"' + s + '"'


# --------------------------------------------------------------------------
# Per-language primitives
# --------------------------------------------------------------------------

LINE = {"java": "//", "cpp": "//", "c": "//", "csharp": "//", "go": "//",
        "rust": "//", "js": "//", "ts": "//", "python": "#", "ruby": "#"}

EXT = {"java": "java", "python": "py", "js": "js", "ts": "ts", "c": "c",
       "cpp": "cpp", "csharp": "cs", "go": "go", "rust": "rs", "ruby": "rb"}

IMPORTS = {
    "java": ["import java.security.MessageDigest;", "import java.security.SecureRandom;",
             "import java.security.KeyPairGenerator;", "import java.security.Signature;",
             "import javax.crypto.Cipher;", "import javax.crypto.Mac;",
             "import javax.crypto.KeyGenerator;", "import javax.crypto.spec.SecretKeySpec;",
             "import javax.crypto.spec.IvParameterSpec;", "import javax.crypto.spec.GCMParameterSpec;",
             "import org.bouncycastle.crypto.engines.AESEngine;",
             "import org.bouncycastle.crypto.digests.SHA256Digest;",
             "import org.bouncycastle.jce.provider.BouncyCastleProvider;"],
    "python": ["import hashlib", "import hmac", "import secrets", "import os",
               "from cryptography.hazmat.primitives import hashes",
               "from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes",
               "from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC",
               "from Crypto.Cipher import AES", "from Crypto.Hash import SHA256",
               "import nacl.secret", "import nacl.signing"],
    "js": ["const crypto = require('crypto');",
           "const { createHash, createHmac, randomBytes } = require('crypto');",
           "const CryptoJS = require('crypto-js');"],
    "ts": ["import * as crypto from 'crypto';",
           "import { createHash, createCipheriv, randomBytes } from 'node:crypto';",
           "import CryptoJS from 'crypto-js';"],
    "c": ["#include <openssl/aes.h>", "#include <openssl/sha.h>",
          "#include <openssl/evp.h>", "#include <openssl/rsa.h>",
          "#include <sodium.h>", "#include <mbedtls/aes.h>"],
    "cpp": ["#include <openssl/evp.h>", "#include <openssl/sha.h>",
            "#include <sodium.h>", "#include <botan/aes.h>",
            "#include <cryptopp/aes.h>", "#include <cryptopp/sha.h>"],
    "csharp": ["using System;", "using System.Text;",
               "using System.Security.Cryptography;",
               "using System.Security.Cryptography.X509Certificates;"],
    "go": ['"crypto/aes"', '"crypto/cipher"', '"crypto/rsa"', '"crypto/sha256"',
           '"crypto/sha512"', '"crypto/hmac"', '"crypto/rand"', '"crypto/tls"',
           '"golang.org/x/crypto/chacha20poly1305"', '"golang.org/x/crypto/argon2"',
           '"golang.org/x/crypto/blake2b"'],
    "rust": ["use ring::digest;", "use ring::aead;", "use sha2::{Sha256, Digest};",
             "use aes::Aes256;", "use chacha20poly1305::ChaCha20Poly1305;",
             "use ed25519_dalek::Signer;", "use openssl::symm::Cipher;"],
    "ruby": ["require 'openssl'", "require 'digest'", "require 'securerandom'"],
}

FAKE_LIBS = {
    "python": ["import quantumcrypto", "from hypercipher import HyperAES",
               "import megahash as mh", "from fakecrypto import MLKEMCipher, FalconSigner"],
    "java": ["import com.acme.quantumcrypto.MLKEM;", "import net.fake.cipher.HyperAES;",
             "import org.notreal.hash.MegaSHA512;"],
    "js": ["const quantumcrypto = require('quantum-crypto');",
           "const { HyperAES } = require('hyper-cipher');",
           "const MegaHash = require('mega-hash');"],
    "ts": ["import { MLKEMCipher } from 'quantum-crypto';",
           "import HyperAES from 'hyper-cipher';"],
    "go": ['"github.com/acme/quantumcrypto"', '"github.com/fake/hypercipher"'],
    "rust": ["use quantumcrypto::MlKem;", "use hypercipher::HyperAes;"],
    "c": ["#include <quantumcrypto.h>", "#include <hypercipher/aes.h>"],
    "cpp": ["#include <quantumcrypto/mlkem.hpp>", "#include <hypercipher/aes.hpp>"],
    "csharp": ["using Acme.QuantumCrypto;", "using Hyper.Cipher;"],
    "ruby": ["require 'quantumcrypto'", "require 'hypercipher'"],
}


def line_comment(lang, text):
    return LINE[lang] + " " + text


def block_comment(lang, lines):
    out = []
    if lang == "python":
        out.append('"""')
        out += lines
        out.append('"""')
    elif lang == "ruby":
        out.append("=begin")
        out += lines
        out.append("=end")
    else:
        out.append("/*")
        for l in lines:
            out.append(" * " + l)
        out.append(" */")
    return out


def const_decl(lang, name, value):
    v = value
    if lang == "java":
        return '    public static final String ' + name + ' = "' + v + '";'
    if lang == "csharp":
        return '    public const string ' + name + ' = "' + v + '";'
    if lang == "cpp":
        return 'static const std::string ' + name + ' = "' + v + '";'
    if lang == "c":
        return '#define ' + name + ' "' + v + '"'
    if lang == "go":
        return 'const ' + name + ' = "' + v + '"'
    if lang == "rust":
        return 'const ' + name + ': &str = "' + v + '";'
    if lang in ("js", "ts"):
        return 'const ' + name + " = '" + v + "';"
    if lang == "python":
        return name + ' = "' + v + '"'
    if lang == "ruby":
        return name + " = '" + v + "'"


def var_decl(lang, name, expr):
    if lang == "java":
        return '    String ' + name + ' = ' + expr + ';'
    if lang == "csharp":
        return '    var ' + name + ' = ' + expr + ';'
    if lang == "cpp":
        return 'std::string ' + name + ' = ' + expr + ';'
    if lang == "c":
        return 'const char *' + name + ' = ' + expr + ';'
    if lang == "go":
        return 'var ' + name + ' = ' + expr
    if lang == "rust":
        return 'let ' + name + ' = ' + expr + ';'
    if lang in ("js", "ts"):
        return 'const ' + name + ' = ' + expr + ';'
    if lang == "python":
        return name + ' = ' + expr
    if lang == "ruby":
        return name + ' = ' + expr


def list_lit(lang, items):
    if lang == "go":
        return "[]string{" + ", ".join('"' + x + '"' for x in items) + "}"
    if lang == "rust":
        return "vec![" + ", ".join('"' + x + '"' for x in items) + "]"
    if lang == "csharp":
        return "new List<string> { " + ", ".join('"' + x + '"' for x in items) + " }"
    if lang == "ruby":
        return "%w[" + " ".join(items) + "]"
    if lang in ("js", "ts"):
        return "[" + ", ".join("'" + x + "'" for x in items) + "]"
    return "{" + ", ".join('"' + x + '"' for x in items) + "}" if lang in ("java", "c", "cpp") \
        else "[" + ", ".join('"' + x + '"' for x in items) + "]"


def finish(lang, cls, body):
    """Wrap a body in a package/class where the language demands one."""
    if lang == "java":
        return ["package com.example.crypto;", "", "public class " + cls + " {"] + body + ["}"]
    if lang == "csharp":
        return ["using System;", "using System.Security.Cryptography;", "",
                "namespace CryptoCorpus", "{", "    public class " + cls, "    {"] + \
               body + ["    }", "}"]
    if lang == "go":
        return ["package cryptocorpus", ""] + body
    return body


def wrap_class(lang, cls, body):
    if lang == "java":
        return ["public class " + cls + " {"] + body + ["}"]
    if lang == "csharp":
        return ["public class " + cls, "{"] + body + ["}"]
    return body


# --------------------------------------------------------------------------
# Compiling templates (placeholder-substituted raw strings)
# --------------------------------------------------------------------------

PY_COMPILE = '''#!/usr/bin/env python3
"""__CLS__ -- synthetic crypto naming demo (compiles and runs)."""
import hashlib
import hmac
import secrets

DEFAULT_CIPHER = "__CIP__"
DEFAULT_HASH = "__HSH__"


class __CLS__:
    """Small helper. References __A1__ and HMAC-__A2__ (names only)."""

    def __init__(self) -> None:
        self.aes_key = secrets.token_bytes(32)
        self.algorithms = __L__

    def sha256_digest(self, data: bytes) -> str:
        # TODO migrate MD5 to SHA-256
        return hashlib.sha256(data).hexdigest()

    def hmac_tag(self, key: bytes, data: bytes) -> str:
        return hmac.new(key, data, hashlib.sha256).hexdigest()


def main() -> None:
    svc = __CLS__()
    print(DEFAULT_CIPHER, DEFAULT_HASH)
    print(svc.sha256_digest(b"synthetic"))
    for algorithm in svc.algorithms:
        print("configured:", algorithm)


if __name__ == "__main__":
    main()
'''

JAVA_COMPILE = '''package com.example.crypto;

import java.security.MessageDigest;
import java.security.NoSuchAlgorithmException;

/** __CLS__ -- synthetic crypto naming demo. References __A1__ / __A2__. */
public class __CLS__ {
    public static final String DEFAULT_CIPHER = "__CIP__";
    public static final String DEFAULT_HASH = "__HSH__";
    private final String[] algorithms = __L__;

    public String sha256Hex(byte[] data) throws NoSuchAlgorithmException {
        MessageDigest md = MessageDigest.getInstance("SHA-256");
        byte[] out = md.digest(data);
        StringBuilder sb = new StringBuilder();
        for (byte b : out) {
            sb.append(String.format("%02x", b));
        }
        return sb.toString();
    }

    public static void main(String[] args) throws Exception {
        __CLS__ demo = new __CLS__();
        System.out.println(DEFAULT_CIPHER + " / " + DEFAULT_HASH);
        System.out.println(demo.sha256Hex("synthetic".getBytes()));
    }
}
'''

GO_COMPILE = '''package cryptocorpus

import (
	"crypto/sha256"
	"encoding/hex"
	"fmt"
)

// __CLS____N__ -- synthetic crypto naming demo. References __A1__ / __A2__.
func __CLS____N__Sha256Hex(data []byte) string {
	sum := sha256.Sum256(data)
	return hex.EncodeToString(sum[:])
}

func __CLS____N__Demo() {
	defaultCipher := "__CIP__"
	defaultHash := "__HSH__"
	algorithms := __L__
	fmt.Println(defaultCipher, defaultHash)
	for _, a := range algorithms {
		fmt.Println("configured:", a)
	}
	fmt.Println(__CLS____N__Sha256Hex([]byte("synthetic")))
}
'''

C_COMPILE = '''#include <stdio.h>
#include <string.h>

/* __CLS__ -- synthetic crypto naming demo (AES / SHA-256 names). */
static const char *DEFAULT_CIPHER = "__CIP__";
static const char *DEFAULT_HASH = "__HSH__";

static const char *ALGORITHMS[] = __L__;

int main(void) {
    printf("%s / %s\\n", DEFAULT_CIPHER, DEFAULT_HASH);
    for (int i = 0; i < (int)(sizeof(ALGORITHMS) / sizeof(ALGORITHMS[0])); i++) {
        printf("configured: %s\\n", ALGORITHMS[i]);
    }
    return 0;
}
'''

CPP_COMPILE = '''#include <iostream>
#include <string>
#include <vector>

// __CLS__ -- synthetic crypto naming demo (ChaCha20 / SHA-256 names).
namespace cryptocorpus {

class __CLS__ {
public:
    static const std::string DEFAULT_CIPHER;
    std::vector<std::string> algorithms() const {
        return __L__;
    }
};

const std::string __CLS__::DEFAULT_CIPHER = "__CIP__";

}  // namespace cryptocorpus

int main() {
    cryptocorpus::__CLS__ demo;
    std::cout << cryptocorpus::__CLS__::DEFAULT_CIPHER << std::endl;
    for (const auto &a : demo.algorithms()) {
        std::cout << "configured: " << a << std::endl;
    }
    return 0;
}
'''

CS_COMPILE = '''using System;
using System.Collections.Generic;
using System.Security.Cryptography;
using System.Text;

namespace CryptoCorpus
{
    public class __CLS__
    {
        public const string DefaultCipher = "__CIP__";
        public const string DefaultHash = "__HSH__";

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
            var algorithms = __L__;
            Console.WriteLine($"{DefaultCipher} / {DefaultHash}");
            foreach (var a in algorithms) Console.WriteLine("configured: " + a);
        }
    }
}
'''

RUST_COMPILE = '''//! __CLS__ -- synthetic crypto naming demo (AES / SHA-256 names).

pub const DEFAULT_CIPHER: &str = "__CIP__";
pub const DEFAULT_HASH: &str = "__HSH__";

pub struct __CLS__ {
    pub algorithms: Vec<&'static str>,
}

impl __CLS__ {
    pub fn new() -> Self {
        __CLS__ { algorithms: __L__ }
    }

    pub fn demo(&self) {
        println!("{} / {}", DEFAULT_CIPHER, DEFAULT_HASH);
        for a in &self.algorithms {
            println!("configured: {}", a);
        }
    }
}

fn main() {
    let svc = __CLS__::new();
    svc.demo();
}
'''

RUBY_COMPILE = '''# frozen_string_literal: true
# __CLS__ -- synthetic crypto naming demo (AES / SHA-256 names).
require 'digest'

DEFAULT_CIPHER = '__CIP__'
DEFAULT_HASH = '__HSH__'

class __CLS__
  ALGORITHMS = __L__.freeze

  def sha256_hex(data)
    Digest::SHA256.hexdigest(data)
  end
end

if __FILE__ == $PROGRAM_NAME
  svc = __CLS__.new
  puts "#{DEFAULT_CIPHER} / #{DEFAULT_HASH}"
  puts svc.sha256_hex('synthetic')
  __CLS__::ALGORITHMS.each { |a| puts "configured: #{a}" }
end
'''

JS_COMPILE = '''// __CLS__ -- synthetic crypto naming demo (AES / SHA-256 names).
'use strict';
const crypto = require('crypto');

const DEFAULT_CIPHER = '__CIP__';
const DEFAULT_HASH = '__HSH__';

class __CLS__ {
  sha256Hex(data) {
    return crypto.createHash('sha256').update(data).digest('hex');
  }
}

const svc = new __CLS__();
console.log(`${DEFAULT_CIPHER} / ${DEFAULT_HASH}`);
console.log(svc.sha256Hex('synthetic'));
__L__.forEach((a) => console.log('configured:', a));

module.exports = { __CLS__ };
'''

TS_COMPILE = '''// __CLS__ -- synthetic crypto naming demo (AES / SHA-256 names).
import { createHash } from 'node:crypto';

const DEFAULT_CIPHER: string = '__CIP__';
const DEFAULT_HASH: string = '__HSH__';

export class __CLS__ {
  sha256Hex(data: string): string {
    return createHash('sha256').update(data).digest('hex');
  }
}

const algorithms: string[] = __L__;
const svc = new __CLS__();
console.log(`${DEFAULT_CIPHER} / ${DEFAULT_HASH}`);
algorithms.forEach((a: string): void => console.log('configured:', a));
'''

COMPILE_T = {
    "python": PY_COMPILE, "java": JAVA_COMPILE, "go": GO_COMPILE, "c": C_COMPILE,
    "cpp": CPP_COMPILE, "csharp": CS_COMPILE, "rust": RUST_COMPILE,
    "ruby": RUBY_COMPILE, "js": JS_COMPILE, "ts": TS_COMPILE,
}


def build_compiling(lang, cls, idx):
    four = picks(BASE_ALGOS, 4)
    t = COMPILE_T[lang]
    t = t.replace("__CLS__", cls)
    t = t.replace("__N__", str(idx))
    t = t.replace("__L__", list_lit(lang, four))
    t = t.replace("__CIP__", pick(VARIANTS["AES"]))
    t = t.replace("__HSH__", pick(VARIANTS["SHA256"]))
    t = t.replace("__A1__", four[0])
    t = t.replace("__A2__", four[1])
    return t


# --------------------------------------------------------------------------
# "Almost compiles" / "syntax error" builders
# --------------------------------------------------------------------------

def build_almost(lang, cls, idx):
    src = build_compiling(lang, cls, idx)
    note = LINE[lang] + " almost compiles: intentional single-token defect (AES, SHA-256)"
    if lang == "python":
        return src.replace("def main() -> None:", "def main() -> None", 1) + \
            "\n# almost: missing colon on main() above\n"
    if lang == "ruby":
        i = src.rfind("\nend")
        if i != -1:
            src = src[:i] + "\n# almost: dropped an end (AES, RSA)\n" + src[i + 4:]
        return src
    i = src.rfind("}")
    if i != -1:
        src = src[:i] + src[i + 1:]
    return src + "\n" + note + "\n"


SYNTAX_BROKEN = {
    "python": 'def broken(:\n    x = "AES  # unterminated string + bad signature\n    return sha256Digest(\n    if useMD5\n        pass\n',
    "ruby": 'def broken\n  x = "ChaCha20  # unterminated\n  cipher = AES::::new(\n  end end end\n',
    "java": 'public class Broken {\n    void m( {\n        String s = "RSA;   // unterminated string\n        int x = ;\n        aesKey =\n    // missing closing braces and semicolons\n',
    "csharp": 'namespace X {\n  public class Broken {\n    void M( {\n      var s = "SHA-256;   // unterminated\n      int x = ;\n      // dangling\n',
    "c": '#include <openssl/aes.h>\nint main( {\n    char *k = "DES   /* unterminated */\n    int x = ;\n    return\n',
    "cpp": '#include <openssl/sha.h>\nint main( {\n    std::string s = "ChaCha20;\n    auto x = ;\n    // missing braces\n',
    "go": 'package cryptocorpus\nfunc broken( {\n\tx := "AES\n\treturn sha256(\n\tif useMD5 {\n',
    "rust": 'fn broken( {\n    let x = "Kyber;\n    let y: = ;\n    aes_key\n    // missing braces\n',
    "js": "function broken( {\n  const x = 'AES;   // unterminated\n  let y = ;\n  return sha256Digest(\n",
    "ts": "function broken(: {\n  const x: string = 'RSA;\n  let y: = ;\n  return\n",
}


def build_syntax_error(lang, cls, idx):
    head = block_comment(lang, [
        cls + " -- INTENTIONAL SYNTAX ERRORS (scanner robustness).",
        "Mentions AES, RSA, SHA-256, ChaCha20, MD5, ML-KEM, Ed25519.",
    ])
    return "\n".join(head) + "\n\n" + SYNTAX_BROKEN.get(lang, SYNTAX_BROKEN["c"])


# --------------------------------------------------------------------------
# Comment / string / docs / random-word builders
# --------------------------------------------------------------------------

def build_comment_only(lang, cls, idx):
    out = block_comment(lang, [
        cls + " -- crypto algorithm reference (comment-only file).",
        "Synthetic: no executable code, only algorithm names for coverage.",
    ])
    out.append("")
    for _ in range(random.randint(18, 30)):
        out.append(line_comment(lang, comment_text()))
    out.append("")
    catalog = picks(ALGO_TOKENS, min(60, len(ALGO_TOKENS)))
    out += block_comment(lang, ["Algorithm catalog:"] +
                         ["  " + ", ".join(c) for c in chunks(catalog, 6)])
    return "\n".join(out) + "\n"


def build_docs_only(lang, cls, idx):
    doc = [
        cls + " -- Cryptography Design Notes (documentation only, synthetic).",
        "",
        "Overview",
        "--------",
        "Would provide AES-256-GCM and ChaCha20-Poly1305 encryption, RSA-2048,",
        "ECDSA and Ed25519 signatures, and ML-KEM-768 (CRYSTALS-Kyber) key",
        "encapsulation with X25519 hybrid key exchange.",
        "",
        "Hashing: SHA-256, SHA-384, SHA-512, SHA-3, SHAKE128, BLAKE2b, BLAKE3, SM3.",
        "Legacy (DO NOT USE): MD2, MD4, MD5, SHA1, DES, 3DES, RC4, Blowfish.",
        "",
        "Key derivation: PBKDF2, scrypt, Argon2id, HKDF.",
        "Message authentication: HMAC-SHA-256, Poly1305, CMAC, GMAC, SipHash.",
        "",
        "Post-quantum roadmap: ML-KEM, ML-DSA (Dilithium), Falcon, SPHINCS+,",
        "FrodoKEM, BIKE, HQC, Classic McEliece, NTRU, Saber, XMSS, LMS.",
        "",
        "TODO migrate MD5 to SHA-256. Replace SHA1. Deprecate DES/3DES/RC4.",
    ]
    return "\n".join(block_comment(lang, doc)) + "\n"


def build_string_only(lang, cls, idx):
    body = [line_comment(lang, cls + " -- string constants only (algorithm names).")]
    seen = set()
    for i in range(random.randint(16, 28)):
        name = const_any()
        if name in seen:
            name = name + "_" + str(i)
        seen.add(name)
        body.append(const_decl(lang, name, algo()))
    return "\n".join(finish(lang, cls, body)) + "\n"


def build_random_words(lang, cls, idx):
    out = [line_comment(lang, cls + " -- random crypto tokens, no functionality.")]
    for _ in range(3):
        out += block_comment(lang, [" ".join(picks(ALGO_TOKENS, min(40, len(ALGO_TOKENS))))])
    body = []
    for i in range(random.randint(3, 6)):
        arr = list_lit(lang, picks(ALGO_TOKENS, 6))
        body.append(var_decl(lang, low(pick(EXTRA_CLASSES)) + str(i), arr))
    out += finish(lang, cls, body) if lang in ("java", "csharp", "go") else body
    return "\n".join(out) + "\n"


# --------------------------------------------------------------------------
# Fake API / dead code / deprecated / misuse builders
# --------------------------------------------------------------------------

def build_fake_api(lang, cls, idx):
    lines = [line_comment(lang, cls + " -- fake crypto APIs / nonexistent libraries (won't resolve).")]
    if lang == "go":
        lines += ["package cryptocorpus", "", "import ("]
        lines += ["\t" + x for x in FAKE_LIBS["go"]]
        lines += [")", "", "func FakeDemo" + str(idx) + "() {",
                  "\t// Fake ML-KEM implementation",
                  '\tcipher := HyperAES("' + pick(VARIANTS["AES"]) + '")',
                  '\tkem := MLKEMCipher("' + pick(VARIANTS["MLKEM"]) + '")',
                  '\tsig := FalconSigner("Falcon-512")',
                  '\tdigest := MegaSHA512("' + algo() + '")',
                  "\t_, _, _, _ = cipher, kem, sig, digest", "}"]
        return "\n".join(lines) + "\n"
    if lang == "java":
        lines.append("package com.example.crypto;")
    lines += FAKE_LIBS.get(lang, [])
    lines.append("")
    body = [line_comment(lang, "Fake ML-KEM implementation"),
            var_decl(lang, "cipher", 'HyperAES("' + pick(VARIANTS["AES"]) + '")'),
            var_decl(lang, "kem", 'MLKEMCipher.generate("' + pick(VARIANTS["MLKEM"]) + '")'),
            var_decl(lang, "sig", 'FalconSigner.sign(data, "Falcon-512")'),
            var_decl(lang, "digest", 'MegaSHA512.hash("' + algo() + '")')]
    lines += wrap_class(lang, cls, body)
    return "\n".join(lines) + "\n"


def dead_block(lang):
    if lang == "python":
        return ("if False:\n    dead_key = \"hardcoded-AES-256-key\"  "
                "# never runs (RSA, MD5)\n    print(dead_key)")
    if lang == "ruby":
        return ("if false\n  dead_key = 'hardcoded-AES-key' "
                "# never runs (RSA, MD5)\nend")
    if lang == "go":
        return ("func DeadDemo() {\n\tif false {\n\t\tvar deadKey = "
                "\"hardcoded-AES-key\" // never runs (RSA, MD5)\n\t\t_ = deadKey\n\t}\n}")
    if lang == "rust":
        return ("fn dead_demo() {\n    if false {\n        let _dead_key = "
                "\"hardcoded-AES-key\"; // never runs (RSA, MD5)\n    }\n}")
    return ("if (0) {\n    /* never runs: AES-256, RSA, MD5 */\n    "
            "const char *deadKey = \"hardcoded-AES-key\";\n}")


def build_dead_code(lang, cls, idx):
    out = [line_comment(lang, cls + " -- dead code / unused crypto (never executed).")]
    body = [line_comment(lang, "Unused crypto variables:")]
    for _ in range(4):
        body.append(var_decl(lang, ident_any(), quote(algo())))
    body.append("")
    body.append(dead_block(lang))
    out += finish(lang, cls, body)
    return "\n".join(out) + "\n"


def deprecated_marker(lang):
    if lang == "java":
        return "    @Deprecated"
    if lang == "csharp":
        return '    [Obsolete("insecure -- do not use")]'
    return line_comment(lang, "@deprecated")


def method_stub(lang, name, algo_name):
    if lang == "python":
        return "def " + name + "():\n    return \"" + algo_name + "\"  # deprecated"
    if lang == "ruby":
        return "def " + name + "\n  '" + algo_name + "' # deprecated\nend"
    if lang == "go":
        return "func " + cap(name) + "() string { return \"" + algo_name + "\" }"
    if lang == "rust":
        return "fn " + name + "() -> &'static str { \"" + algo_name + "\" }"
    if lang in ("js", "ts"):
        return "function " + name + "() { return '" + algo_name + "'; }"
    if lang == "c":
        return "const char *" + name + "(void) { return \"" + algo_name + "\"; }"
    if lang == "cpp":
        return "std::string " + name + "() { return \"" + algo_name + "\"; }"
    if lang == "java":
        return "    public String " + name + "() { return \"" + algo_name + "\"; }"
    if lang == "csharp":
        return "    public string " + name + "() { return \"" + algo_name + "\"; }"


def build_deprecated(lang, cls, idx):
    out = [line_comment(lang, cls + " -- deprecated algorithm usage.")]
    body = []
    for d in random.sample(["MD5", "SHA1", "DES", "3DES", "RC4", "Blowfish", "MD2", "MD4"], 4):
        repl = pick(["SHA-256", "AES-256-GCM", "ChaCha20-Poly1305", "Ed25519", "Argon2id"])
        body.append(line_comment(lang, "Deprecated " + d + " -- replace with " + repl))
        body.append(deprecated_marker(lang))
        body.append(method_stub(lang, "legacy" + safe(d), d))
        body.append("")
    out += finish(lang, cls, body)
    return "\n".join(out) + "\n"


def build_misuse(lang, cls, idx):
    out = [line_comment(lang, cls + " -- INTENTIONAL crypto misuse for detection.")]
    misuses = [
        ("hardcoded AES key", var_decl(lang, "aesKey", '"1234567890123456"')),
        ("static IV reused across messages", var_decl(lang, "iv", '"0000000000000000"')),
        ("ECB mode leaks plaintext patterns", const_decl(lang, "MODE", "AES/ECB/PKCS5Padding")),
        ("MD5 used for password hashing", var_decl(lang, "passwordHash", '"md5(password)"')),
        ("DES with 56-bit key", var_decl(lang, "desKey", '"weakkey1"')),
        ("reused ChaCha20 nonce", var_decl(lang, "nonce", '"000000000000"')),
        ("RSA without OAEP padding (textbook RSA)", const_decl(lang, "RSA_MODE", "RSA/ECB/NoPadding")),
        ("SHA1 for signatures", var_decl(lang, "sigAlg", '"SHA1withRSA"')),
    ]
    body = []
    for note, line in random.sample(misuses, 6):
        body.append(line_comment(lang, "MISUSE: " + note))
        body.append(line)
    out += finish(lang, cls, body)
    return "\n".join(out) + "\n"


BUILDERS = {
    "compiling": build_compiling,
    "almost": build_almost,
    "syntax_error": build_syntax_error,
    "comment_only": build_comment_only,
    "string_only": build_string_only,
    "fake_api": build_fake_api,
    "dead_code": build_dead_code,
    "deprecated": build_deprecated,
    "misuse": build_misuse,
    "random_words": build_random_words,
    "docs_only": build_docs_only,
}
FLAVORS = list(BUILDERS.keys())

FILE_STEMS = [
    "aes_cipher", "rsa_engine", "hash_utils", "crypto_service", "digest_factory",
    "sha256_helper", "chacha20_stream", "ed25519_signer", "pbkdf2_kdf", "hmac_util",
    "md5_legacy", "des_legacy", "blowfish_cipher", "kyber_kem", "dilithium_sign",
    "argon2_hash", "bcrypt_util", "poly1305_mac", "hkdf_derive", "rc4_stream",
    "serpent_cipher", "camellia_cipher", "whirlpool_hash", "ripemd_hash",
    "sm4_cipher", "gost_cipher", "salsa20_stream", "ecdsa_verify", "dh_exchange",
    "sphincs_sign", "blake3_hash", "siphash_util", "crc32_checksum", "tea_cipher",
    "present_cipher", "twofish_cipher", "key_exchange_demo", "crypto_wrapper",
    "cipher_factory", "signature_service", "falcon_signer", "mlkem_cipher",
    "x25519_kex", "cast5_cipher", "idea_cipher", "zuc_stream",
]


# --------------------------------------------------------------------------
# Data / config file generators
# --------------------------------------------------------------------------

def data_json():
    obj = {
        "crypto": {
            "defaultCipher": pick(VARIANTS["AES"]),
            "defaultHash": pick(["SHA-256", "SHA-512", "SHA3-256"]),
            "kdf": pick(["PBKDF2", "scrypt", "Argon2id"]),
            "signature": pick(["Ed25519", "ECDSA", "RSASSA-PSS", "ML-DSA-65"]),
            "kem": pick(["ML-KEM-768", "X25519", "CRYSTALS-Kyber"]),
            "enabledAlgorithms": ENABLED,
            "deprecatedAlgorithms": DEPRECATED,
            "pbkdf2Iterations": 100000,
            "bcryptRounds": 12,
            "argon2": {"memoryKiB": 65536, "iterations": 3, "parallelism": 4},
            "hmac": "HMAC-SHA-256",
            "poly1305": True,
        }
    }
    return json.dumps(obj, indent=2) + "\n"


def data_yaml():
    lines = ["# Crypto algorithm policy (synthetic)", "crypto:",
             "  default_cipher: " + pick(VARIANTS["AES"]),
             "  default_hash: " + pick(["SHA-256", "SHA-512", "SHA3-512"]),
             "  signature: " + pick(["Ed25519", "ECDSA", "ML-DSA-65", "Falcon-512"]),
             "  kem: " + pick(["ML-KEM-768", "CRYSTALS-Kyber", "X25519"]),
             "  kdf: " + pick(["Argon2id", "PBKDF2", "scrypt"]),
             "  hmac: HMAC-SHA-256",
             "  poly1305: true",
             "  enabled:"]
    for a in ENABLED:
        lines.append("    - " + a)
    lines.append("  deprecated:")
    for a in DEPRECATED:
        lines.append("    - " + a)
    return "\n".join(lines) + "\n"


def data_xml():
    lines = ['<?xml version="1.0" encoding="UTF-8"?>', "<cryptoConfig>",
             '  <cipher name="AES" mode="GCM" keySize="256"/>',
             '  <cipher name="ChaCha20" mode="Poly1305"/>',
             '  <cipher name="Camellia" mode="CBC" keySize="256"/>',
             '  <hash algorithm="SHA-256"/>', '  <hash algorithm="SHA3-512"/>',
             '  <hash algorithm="BLAKE2b"/>', '  <signature algorithm="Ed25519"/>',
             '  <signature algorithm="ECDSA" curve="P-256"/>',
             '  <kem algorithm="ML-KEM-768"/>',
             '  <kdf algorithm="Argon2id" memory="65536" iterations="3"/>',
             '  <mac algorithm="HMAC-SHA-256"/>', "  <deprecated>"]
    for a in DEPRECATED:
        lines.append("    <algorithm>" + a + "</algorithm>")
    lines += ["  </deprecated>", "</cryptoConfig>"]
    return "\n".join(lines) + "\n"


def data_sql():
    return (
        "-- Crypto algorithm inventory (synthetic)\n"
        "CREATE TABLE crypto_algorithms (\n"
        "    id         INTEGER PRIMARY KEY,\n"
        "    name       TEXT NOT NULL,\n"
        "    category   TEXT,\n"
        "    deprecated BOOLEAN DEFAULT 0\n"
        ");\n\n"
        "INSERT INTO crypto_algorithms (name, category, deprecated) VALUES\n"
        "    ('AES', 'block-cipher', 0),\n"
        "    ('ChaCha20', 'stream-cipher', 0),\n"
        "    ('DES', 'block-cipher', 1),\n"
        "    ('3DES', 'block-cipher', 1),\n"
        "    ('RSA', 'asymmetric', 0),\n"
        "    ('ECDSA', 'signature', 0),\n"
        "    ('Ed25519', 'signature', 0),\n"
        "    ('MD5', 'hash', 1),\n"
        "    ('SHA1', 'hash', 1),\n"
        "    ('SHA-256', 'hash', 0),\n"
        "    ('SHA3-512', 'hash', 0),\n"
        "    ('BLAKE3', 'hash', 0),\n"
        "    ('PBKDF2', 'kdf', 0),\n"
        "    ('Argon2id', 'kdf', 0),\n"
        "    ('HMAC-SHA-256', 'mac', 0),\n"
        "    ('ML-KEM', 'pqc-kem', 0),\n"
        "    ('Dilithium', 'pqc-signature', 0),\n"
        "    ('Falcon', 'pqc-signature', 0),\n"
        "    ('RC4', 'stream-cipher', 1);\n\n"
        "-- TODO migrate MD5 and SHA1 rows to SHA-256\n"
        "UPDATE crypto_algorithms SET deprecated = 1 WHERE name IN ('MD5', 'SHA1', 'DES', 'RC4');\n"
        "CREATE INDEX idx_algo_name ON crypto_algorithms (name);\n"
    )


def data_md():
    return (
        "# Crypto Algorithms (synthetic test document)\n\n"
        "Reference of cryptographic algorithms for scanner coverage. "
        "Not a real crypto library.\n\n"
        "## Symmetric\n"
        "- **AES** (AES-128, AES-192, AES-256, AES-256-GCM) -- preferred block cipher\n"
        "- ChaCha20 / ChaCha20-Poly1305, Salsa20, XChaCha20\n"
        "- Camellia, Twofish, Serpent, ARIA, SEED, SM4, CAST5, IDEA\n"
        "- DES / 3DES / TripleDES / RC2 / RC4 / Blowfish -- **deprecated**\n\n"
        "## Hashes\n"
        "- SHA-256, SHA-384, SHA-512, SHA-3, SHAKE128, SHAKE256\n"
        "- BLAKE2b, BLAKE2s, BLAKE3, RIPEMD-160, Whirlpool, SM3\n"
        "- MD2, MD4, MD5, SHA1 -- **do not use**\n\n"
        "## Asymmetric & PQC\n"
        "- RSA-2048, DSA, ECDSA, ECDH, DiffieHellman, ElGamal\n"
        "- Ed25519, Ed448, X25519, X448\n"
        "- ML-KEM (CRYSTALS-Kyber), ML-DSA (Dilithium), Falcon, SPHINCS+\n"
        "- FrodoKEM, BIKE, HQC, Classic McEliece, NTRU, Saber, SIKE, XMSS, LMS\n\n"
        "## KDF / MAC\n"
        "- PBKDF2, bcrypt, scrypt, Argon2id, HKDF\n"
        "- HMAC, CMAC, GMAC, Poly1305, SipHash, CRC32\n\n"
        "> TODO: migrate MD5 to SHA-256 everywhere. Replace SHA1. Remove DES/3DES/RC4.\n"
    )


def data_html():
    return (
        "<!DOCTYPE html>\n<html lang=\"en\">\n<head>\n"
        "  <meta charset=\"utf-8\">\n  <title>Crypto Algorithm Dashboard</title>\n"
        "</head>\n<body>\n"
        "  <h1>Cryptographic Algorithm Inventory</h1>\n"
        "  <ul>\n"
        "    <li data-algo=\"AES\">AES-256-GCM</li>\n"
        "    <li data-algo=\"ChaCha20\">ChaCha20-Poly1305</li>\n"
        "    <li data-algo=\"RSA\">RSA-2048</li>\n"
        "    <li data-algo=\"Ed25519\">Ed25519</li>\n"
        "    <li data-algo=\"MLKEM\">ML-KEM-768 (CRYSTALS-Kyber)</li>\n"
        "    <li data-algo=\"Dilithium\">ML-DSA-65 (Dilithium)</li>\n"
        "    <li data-algo=\"SHA256\">SHA-256</li>\n"
        "    <li data-algo=\"MD5\" class=\"deprecated\">MD5 (deprecated)</li>\n"
        "    <li data-algo=\"DES\" class=\"deprecated\">DES / 3DES (deprecated)</li>\n"
        "  </ul>\n"
        "  <!-- TODO: remove SHA1 and RC4 references; migrate MD5 to SHA-256 -->\n"
        "  <script>\n"
        "    const defaultCipher = 'ChaCha20-Poly1305';\n"
        "    const kdf = 'Argon2id';\n"
        "    const pqcKem = 'ML-KEM-768';\n"
        "    console.log(defaultCipher, kdf, pqcKem);\n"
        "  </script>\n"
        "</body>\n</html>\n"
    )


def data_properties():
    return (
        "# application.properties (synthetic)\n"
        "crypto.default.cipher=AES-256-GCM\n"
        "crypto.default.hash=SHA-256\n"
        "crypto.kdf=PBKDF2WithHmacSHA256\n"
        "crypto.pbkdf2.iterations=100000\n"
        "crypto.bcrypt.rounds=12\n"
        "crypto.argon2.type=Argon2id\n"
        "crypto.signature=Ed25519\n"
        "crypto.kem=ML-KEM-768\n"
        "crypto.mac=HMAC-SHA-256\n"
        "crypto.provider=BouncyCastle\n"
        "# Deprecated -- do not enable\n"
        "crypto.legacy.md5.enabled=false\n"
        "crypto.legacy.sha1.enabled=false\n"
        "crypto.legacy.des.enabled=false\n"
        "crypto.legacy.rc4.enabled=false\n"
    )


def data_requirements():
    return ("# requirements.txt (synthetic)\n"
            "cryptography>=42.0\npycryptodome>=3.20\npynacl>=1.5\n"
            "bcrypt>=4.1\nargon2-cffi>=23.1\npyca>=0.1\n")


def data_pyproject():
    return ("[project]\nname = \"crypto-corpus\"\nversion = \"0.1.0\"\n\n"
            "[tool.crypto]\ndefault_cipher = \"AES-256-GCM\"\n"
            "default_hash = \"SHA-256\"\nkdf = \"Argon2id\"\n"
            "signature = \"Ed25519\"\nkem = \"ML-KEM-768\"\n"
            "deprecated = [\"MD5\", \"SHA1\", \"DES\", \"RC4\"]\n")


def data_packagejson():
    obj = {
        "name": "crypto-corpus", "version": "0.1.0",
        "description": "Synthetic crypto detection corpus (AES, RSA, SHA-256, ChaCha20, ML-KEM)",
        "dependencies": {
            "crypto-js": "^4.2.0", "node-forge": "^1.3.1", "bcrypt": "^5.1.0",
            "argon2": "^0.31.0", "tweetnacl": "^1.0.3", "elliptic": "^6.5.4",
        },
    }
    return json.dumps(obj, indent=2) + "\n"


def data_appsettings():
    obj = {"Crypto": {"DefaultCipher": "AES-256-GCM", "DefaultHash": "SHA-256",
                      "Signature": "ECDSA", "Kem": "ML-KEM-768", "Kdf": "PBKDF2",
                      "Deprecated": ["MD5", "SHA1", "DES", "RC4"]}}
    return json.dumps(obj, indent=2) + "\n"


def data_appconfig_xml():
    return ('<?xml version="1.0" encoding="utf-8"?>\n<configuration>\n'
            '  <appSettings>\n'
            '    <add key="DefaultCipher" value="AES-256-GCM"/>\n'
            '    <add key="DefaultHash" value="SHA-256"/>\n'
            '    <add key="Signature" value="ECDSA"/>\n'
            '    <add key="Kem" value="ML-KEM-768"/>\n'
            '    <add key="LegacyMD5" value="false"/>\n'
            '    <add key="LegacyDES" value="false"/>\n'
            '  </appSettings>\n</configuration>\n')


def data_gomod():
    return ("module cryptocorpus\n\ngo 1.22\n\n"
            "require golang.org/x/crypto v0.21.0\n")


def data_cargotoml():
    return ("[package]\nname = \"crypto-corpus\"\nversion = \"0.1.0\"\n"
            "edition = \"2021\"\n\n[dependencies]\nring = \"0.17\"\n"
            "sha2 = \"0.10\"\naes = \"0.8\"\nchacha20poly1305 = \"0.10\"\n"
            "ed25519-dalek = \"2\"\nopenssl = \"0.10\"\nargon2 = \"0.5\"\n"
            "blake3 = \"1.5\"\n")


def data_gemfile():
    return ("source 'https://rubygems.org'\n\ngem 'openssl'\ngem 'bcrypt'\n"
            "gem 'rbnacl'\ngem 'argon2'\n")


def data_cmake():
    return ("cmake_minimum_required(VERSION 3.10)\nproject(crypto_corpus)\n\n"
            "find_package(OpenSSL REQUIRED)   # AES, SHA-256, RSA, ECDSA\n"
            "# find_package(Sodium)           # libsodium: ChaCha20-Poly1305, Ed25519\n"
            "# find_package(Botan)            # Botan: Serpent, Twofish, Camellia\n"
            "# find_package(mbedTLS)          # mbedTLS: AES, SHA-256\n"
            "# Crypto++ (cryptopp): AES, SHA-3, Poly1305\n"
            "# target_link_libraries(app OpenSSL::Crypto sodium botan-2 cryptopp mbedtls)\n")


def data_readme(langdir):
    return ("# " + langdir + " crypto corpus (synthetic)\n\n"
            "Generated test files packed with cryptographic algorithm names\n"
            "(AES, RSA, SHA-256, ChaCha20, ML-KEM, Dilithium, MD5, DES, ...) for\n"
            "static-analysis detection coverage. **Not** a real crypto library.\n\n"
            "- Some files compile, some intentionally do not.\n"
            "- Includes fake APIs, dead code, deprecated usage, and misuse.\n\n"
            "TODO migrate MD5 to SHA-256. Replace SHA1. Remove DES/3DES/RC4.\n")


def manifest_files(lang):
    if lang == "java":
        return [("application.properties", data_properties())]
    if lang == "python":
        return [("requirements.txt", data_requirements()), ("pyproject.toml", data_pyproject())]
    if lang in ("js", "ts"):
        return [("package.json", data_packagejson())]
    if lang == "csharp":
        return [("appsettings.json", data_appsettings()), ("App.config", data_appconfig_xml())]
    if lang == "go":
        return [("go.mod", data_gomod())]
    if lang == "rust":
        return [("Cargo.toml", data_cargotoml())]
    if lang == "ruby":
        return [("Gemfile", data_gemfile())]
    if lang in ("c", "cpp"):
        return [("CMakeLists.txt", data_cmake())]
    return []


def data_files_for(lang, langdir):
    files = [
        ("crypto_config.json", data_json()),
        ("algorithms.yaml", data_yaml()),
        ("crypto_policy.xml", data_xml()),
        ("crypto_inventory.sql", data_sql()),
        ("ALGORITHMS.md", data_md()),
        ("README.md", data_readme(langdir)),
        ("crypto_dashboard.html", data_html()),
    ]
    files += manifest_files(lang)
    return files


# --------------------------------------------------------------------------
# Corpus assembly
# --------------------------------------------------------------------------

LANG_DIR = {"java": "java", "python": "python", "javascript": "js",
            "typescript": "ts", "c": "c", "cpp": "cpp", "csharp": "csharp",
            "go": "go", "rust": "rust", "ruby": "ruby"}


def unique_cls(base, used):
    c = base
    k = 2
    while c in used:
        c = base + str(k)
        k += 1
    used.add(c)
    return c


def filename_for(lang, cls, stem, used):
    ext = EXT[lang]
    if lang in ("java", "csharp", "cpp"):
        base = cls
    elif lang in ("js", "ts"):
        base = camel(stem)
    else:
        base = snake(stem)
    name = base + "." + ext
    k = 2
    while name in used:
        name = base + str(k) + "." + ext
        k += 1
    used.add(name)
    return name


def write_file(path, content):
    with open(path, "w", encoding="utf-8") as f:
        f.write(content)


def main():
    total = 0
    per_lang = {}
    for langdir, lang in LANG_DIR.items():
        dirp = os.path.join(HERE, langdir)
        os.makedirs(dirp, exist_ok=True)
        used_names = set()
        used_cls = set()

        n = random.randint(26, 40)
        flavors = list(FLAVORS)               # guarantee each flavor appears
        while len(flavors) < n:
            flavors.append(pick(FLAVORS))
        random.shuffle(flavors)

        count = 0
        for i, fl in enumerate(flavors):
            stem = pick(FILE_STEMS)
            cls = unique_cls(pascal(stem), used_cls)
            content = BUILDERS[fl](lang, cls, i)
            fn = filename_for(lang, cls, stem, used_names)
            write_file(os.path.join(dirp, fn), content)
            count += 1

        for fn, content in data_files_for(lang, langdir):
            p = os.path.join(dirp, fn)
            if not os.path.exists(p):
                write_file(p, content)
                count += 1

        per_lang[langdir] = count
        total += count

    write_file(os.path.join(HERE, "README.md"), CORPUS_README)
    print("Crypto test corpus generated under:", HERE)
    for d in LANG_DIR:
        print("  %-12s %3d files" % (d, per_lang[d]))
    print("  %-12s %3d files (+ top-level README.md)" % ("TOTAL", total))


CORPUS_README = (
    "# crypto-test-corpus\n\n"
    "A **synthetic** multi-language test corpus for exercising a static-analysis /\n"
    "crypto-inventory scanner. Every file is generated to be packed with\n"
    "cryptographic algorithm names in as many syntactic positions as possible:\n"
    "identifiers, class names, constants, enums, comments, string literals,\n"
    "imports, and embedded JSON / YAML / XML / SQL / Markdown / HTML.\n\n"
    "> This is NOT a real cryptography library. Security, correctness and\n"
    "> compilation are explicitly not goals -- detection **coverage** is.\n\n"
    "## Languages\n\n"
    "`java/ python/ javascript/ typescript/ c/ cpp/ csharp/ go/ rust/ ruby/`\n\n"
    "## File flavors (per language)\n\n"
    "| Flavor | Description |\n"
    "|---|---|\n"
    "| compiling | Valid, runnable code using real crypto-ish APIs |\n"
    "| almost | Valid code with a single intentional defect |\n"
    "| syntax_error | Deliberately broken syntax |\n"
    "| comment_only | Only comments, full of algorithm names |\n"
    "| string_only | Only string constants |\n"
    "| fake_api | Calls into nonexistent crypto libraries |\n"
    "| dead_code | Unused variables and unreachable branches |\n"
    "| deprecated | MD5/SHA1/DES/RC4 with deprecation markers |\n"
    "| misuse | Hardcoded keys, ECB mode, reused nonces, etc. |\n"
    "| random_words | Random crypto tokens with no functionality |\n"
    "| docs_only | Pure documentation |\n\n"
    "Plus per-language config/data files: `crypto_config.json`, `algorithms.yaml`,\n"
    "`crypto_policy.xml`, `crypto_inventory.sql`, `ALGORITHMS.md`,\n"
    "`crypto_dashboard.html`, and build manifests (`package.json`, `Cargo.toml`,\n"
    "`go.mod`, `pom`-style `application.properties`, `Gemfile`, `CMakeLists.txt`, ...).\n\n"
    "## Regenerate\n\n"
    "```\npython3 generate_corpus.py\n```\n\n"
    "Deterministic (fixed seed) -- re-running reproduces the same corpus.\n\n"
    "## Algorithm families covered\n\n"
    "Block/stream ciphers (AES, DES, 3DES, Blowfish, Twofish, IDEA, RC2/4/5/6,\n"
    "Camellia, Serpent, CAST5/6, Skipjack, TEA/XTEA/XXTEA, GOST, SEED, SM4, ARIA,\n"
    "PRESENT, CLEFIA, HIGHT, LEA, SPECK, SIMON, ChaCha20, Salsa20, Rabbit, HC128/256,\n"
    "Grain, Trivium, MICKEY, Snow3G, ZUC); asymmetric (RSA, DH, ECDH, ECDSA, DSA,\n"
    "ElGamal, Ed25519/448, X25519/448); PQC (Kyber/ML-KEM, CRYSTALS-Kyber, FrodoKEM,\n"
    "BIKE, HQC, Classic McEliece, NTRU, Saber, SIKE, Dilithium/ML-DSA, Falcon,\n"
    "SPHINCS+, XMSS, LMS); hashes (MD2/4/5, SHA1/2/3, SHAKE, RIPEMD-160, Whirlpool,\n"
    "Tiger, HAVAL, BLAKE2/3, SM3); MAC/KDF (Poly1305, HMAC, CMAC, GMAC, HKDF, PBKDF2,\n"
    "bcrypt, scrypt, Argon2, SipHash, CRC32).\n"
)


if __name__ == "__main__":
    main()
