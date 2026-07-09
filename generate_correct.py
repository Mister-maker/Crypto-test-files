#!/usr/bin/env python3
"""
Generate correct-crypto/ : idiomatic, CORRECT use of strong cryptography.

One subfolder per language. Every file uses real, modern crypto the right way
(AEAD with fresh random nonces, memory-hard / high-iteration password KDFs,
Ed25519 / ECDSA signatures, HMAC with constant-time verification). There are:

  * no weak or deprecated algorithms (no MD5, SHA1, DES, RC4, ECB), and
  * no incidental lookalike tokens (nothing like Caesar / describe / cast),

so a precise scanner should flag every algorithm here as a TRUE positive and
report ZERO false positives. This is the "golden / true-negative-on-noise"
counterpart to false-positives/.

Usage:  python3 generate_correct.py
"""

import os

HERE = os.path.dirname(os.path.abspath(__file__))

FILES = {
    # ---------------------------------------------------------------- python
    "python": [
        ("aead_encrypt.py", r'''#!/usr/bin/env python3
"""Correct authenticated encryption with AES-256-GCM (AEAD).

A fresh random 96-bit nonce is generated per message and never reused; GCM
provides both confidentiality and integrity, and the associated data is
authenticated but not encrypted.
"""
import os
from cryptography.hazmat.primitives.ciphers.aead import AESGCM


def encrypt(key: bytes, plaintext: bytes, aad: bytes = b"") -> bytes:
    nonce = os.urandom(12)                       # unique per message
    ciphertext = AESGCM(key).encrypt(nonce, plaintext, aad)
    return nonce + ciphertext                    # prepend nonce for the receiver


def decrypt(key: bytes, blob: bytes, aad: bytes = b"") -> bytes:
    nonce, ciphertext = blob[:12], blob[12:]
    return AESGCM(key).decrypt(nonce, ciphertext, aad)


if __name__ == "__main__":
    key = AESGCM.generate_key(bit_length=256)
    blob = encrypt(key, b"correct and secure", b"header")
    assert decrypt(key, blob, b"header") == b"correct and secure"
    print("AES-256-GCM round-trip OK")
'''),
        ("password_hash.py", r'''#!/usr/bin/env python3
"""Correct password hashing with scrypt (a memory-hard KDF, stdlib only).

A random 16-byte salt is stored with the derived key, and verification is
constant-time. scrypt / Argon2id / PBKDF2 are the correct choices for
passwords -- never a bare fast hash.
"""
import hashlib
import hmac
import os


def hash_password(password: str) -> bytes:
    salt = os.urandom(16)
    dk = hashlib.scrypt(password.encode(), salt=salt, n=2 ** 14, r=8, p=1, dklen=32)
    return salt + dk


def verify_password(stored: bytes, password: str) -> bool:
    salt, expected = stored[:16], stored[16:]
    dk = hashlib.scrypt(password.encode(), salt=salt, n=2 ** 14, r=8, p=1, dklen=32)
    return hmac.compare_digest(dk, expected)     # constant-time


if __name__ == "__main__":
    record = hash_password("correct horse battery staple")
    assert verify_password(record, "correct horse battery staple")
    assert not verify_password(record, "wrong guess")
    print("scrypt password hash + verify OK")
'''),
        ("signature.py", r'''#!/usr/bin/env python3
"""Correct digital signatures with Ed25519."""
from cryptography.exceptions import InvalidSignature
from cryptography.hazmat.primitives.asymmetric.ed25519 import Ed25519PrivateKey


def demo() -> None:
    private_key = Ed25519PrivateKey.generate()
    public_key = private_key.public_key()
    message = b"sign me"
    signature = private_key.sign(message)
    try:
        public_key.verify(signature, message)    # raises if tampered
        print("Ed25519 signature verified")
    except InvalidSignature:
        print("Ed25519 verification failed")


if __name__ == "__main__":
    demo()
'''),
        ("hmac_hash.py", r'''#!/usr/bin/env python3
"""Correct hashing (SHA-256) and message authentication (HMAC-SHA-256, stdlib)."""
import hashlib
import hmac


def sha256_hex(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def hmac_sha256(key: bytes, data: bytes) -> bytes:
    return hmac.new(key, data, hashlib.sha256).digest()


def verify(key: bytes, data: bytes, tag: bytes) -> bool:
    return hmac.compare_digest(hmac_sha256(key, data), tag)   # constant-time


if __name__ == "__main__":
    key = b"secret-mac-key"
    tag = hmac_sha256(key, b"authenticate me")
    assert verify(key, b"authenticate me", tag)
    print("SHA-256:", sha256_hex(b"hello"))
    print("HMAC-SHA-256 verify OK")
'''),
    ],
    # ------------------------------------------------------------------ java
    "java": [
        ("AeadEncrypt.java", r'''package correct.crypto;

import java.security.SecureRandom;
import javax.crypto.Cipher;
import javax.crypto.KeyGenerator;
import javax.crypto.SecretKey;
import javax.crypto.spec.GCMParameterSpec;

/** Correct AES-256-GCM authenticated encryption with a fresh random IV. */
public final class AeadEncrypt {
    private static final int IV_LEN = 12;        // 96-bit nonce for GCM
    private static final int TAG_BITS = 128;
    private static final SecureRandom RNG = new SecureRandom();

    public static byte[] encrypt(SecretKey key, byte[] plaintext, byte[] aad) throws Exception {
        byte[] iv = new byte[IV_LEN];
        RNG.nextBytes(iv);                       // unique per message
        Cipher cipher = Cipher.getInstance("AES/GCM/NoPadding");
        cipher.init(Cipher.ENCRYPT_MODE, key, new GCMParameterSpec(TAG_BITS, iv));
        if (aad != null) {
            cipher.updateAAD(aad);
        }
        byte[] ct = cipher.doFinal(plaintext);
        byte[] out = new byte[IV_LEN + ct.length];
        System.arraycopy(iv, 0, out, 0, IV_LEN);
        System.arraycopy(ct, 0, out, IV_LEN, ct.length);
        return out;
    }

    public static void main(String[] args) throws Exception {
        KeyGenerator kg = KeyGenerator.getInstance("AES");
        kg.init(256);
        SecretKey key = kg.generateKey();
        byte[] blob = encrypt(key, "correct".getBytes(), "header".getBytes());
        System.out.println("AES-256-GCM output bytes: " + blob.length);
    }
}
'''),
        ("PasswordHash.java", r'''package correct.crypto;

import java.security.MessageDigest;
import java.security.SecureRandom;
import javax.crypto.SecretKeyFactory;
import javax.crypto.spec.PBEKeySpec;

/** Correct password hashing with PBKDF2-HMAC-SHA-256 and a random salt. */
public final class PasswordHash {
    private static final int ITERATIONS = 210_000;   // high work factor
    private static final int KEY_BITS = 256;
    private static final SecureRandom RNG = new SecureRandom();

    public static byte[] hash(char[] password, byte[] salt) throws Exception {
        PBEKeySpec spec = new PBEKeySpec(password, salt, ITERATIONS, KEY_BITS);
        SecretKeyFactory factory = SecretKeyFactory.getInstance("PBKDF2WithHmacSHA256");
        return factory.generateSecret(spec).getEncoded();
    }

    public static void main(String[] args) throws Exception {
        byte[] salt = new byte[16];
        RNG.nextBytes(salt);
        byte[] a = hash("correct horse".toCharArray(), salt);
        byte[] b = hash("correct horse".toCharArray(), salt);
        System.out.println("PBKDF2 verify OK: " + MessageDigest.isEqual(a, b));  // constant-time
    }
}
'''),
        ("SignatureEd25519.java", r'''package correct.crypto;

import java.security.KeyPair;
import java.security.KeyPairGenerator;
import java.security.Signature;

/** Correct Ed25519 signing and verification (JDK 15+). */
public final class SignatureEd25519 {
    public static void main(String[] args) throws Exception {
        KeyPair kp = KeyPairGenerator.getInstance("Ed25519").generateKeyPair();
        byte[] message = "sign me".getBytes();

        Signature signer = Signature.getInstance("Ed25519");
        signer.initSign(kp.getPrivate());
        signer.update(message);
        byte[] signature = signer.sign();

        Signature verifier = Signature.getInstance("Ed25519");
        verifier.initVerify(kp.getPublic());
        verifier.update(message);
        System.out.println("Ed25519 verified: " + verifier.verify(signature));
    }
}
'''),
        ("HmacHash.java", r'''package correct.crypto;

import java.security.MessageDigest;
import javax.crypto.Mac;
import javax.crypto.spec.SecretKeySpec;

/** Correct SHA-256 hashing and HMAC-SHA-256 with constant-time verification. */
public final class HmacHash {
    public static byte[] hmacSha256(byte[] key, byte[] data) throws Exception {
        Mac mac = Mac.getInstance("HmacSHA256");
        mac.init(new SecretKeySpec(key, "HmacSHA256"));
        return mac.doFinal(data);
    }

    public static void main(String[] args) throws Exception {
        byte[] digest = MessageDigest.getInstance("SHA-256").digest("hello".getBytes());
        byte[] key = "secret-mac-key".getBytes();
        byte[] a = hmacSha256(key, "authenticate me".getBytes());
        byte[] b = hmacSha256(key, "authenticate me".getBytes());
        System.out.println("SHA-256 length: " + digest.length);
        System.out.println("HMAC-SHA-256 verify OK: " + MessageDigest.isEqual(a, b));  // constant-time
    }
}
'''),
    ],
    # ------------------------------------------------------------ javascript
    "javascript": [
        ("aeadEncrypt.js", r'''// Correct AES-256-GCM authenticated encryption with a random IV (Node.js).
'use strict';
const crypto = require('crypto');

function encrypt(key, plaintext, aad) {
  const iv = crypto.randomBytes(12);                    // unique 96-bit nonce
  const cipher = crypto.createCipheriv('aes-256-gcm', key, iv);
  if (aad) cipher.setAAD(aad);
  const ct = Buffer.concat([cipher.update(plaintext), cipher.final()]);
  const tag = cipher.getAuthTag();                      // 16-byte GCM tag
  return Buffer.concat([iv, tag, ct]);
}

function decrypt(key, blob, aad) {
  const iv = blob.subarray(0, 12);
  const tag = blob.subarray(12, 28);
  const ct = blob.subarray(28);
  const decipher = crypto.createDecipheriv('aes-256-gcm', key, iv);
  decipher.setAuthTag(tag);
  if (aad) decipher.setAAD(aad);
  return Buffer.concat([decipher.update(ct), decipher.final()]);
}

const key = crypto.randomBytes(32);
const blob = encrypt(key, Buffer.from('correct'), Buffer.from('header'));
console.log('AES-256-GCM round-trip OK:', decrypt(key, blob, Buffer.from('header')).toString() === 'correct');
module.exports = { encrypt, decrypt };
'''),
        ("passwordHash.js", r'''// Correct password hashing with scrypt and a random salt (Node.js).
'use strict';
const crypto = require('crypto');

const PARAMS = { N: 2 ** 14, r: 8, p: 1 };

function hashPassword(password) {
  const salt = crypto.randomBytes(16);
  const dk = crypto.scryptSync(password, salt, 32, PARAMS);
  return Buffer.concat([salt, dk]);
}

function verifyPassword(stored, password) {
  const salt = stored.subarray(0, 16);
  const expected = stored.subarray(16);
  const dk = crypto.scryptSync(password, salt, 32, PARAMS);
  return crypto.timingSafeEqual(dk, expected);          // constant-time
}

const record = hashPassword('correct horse');
console.log('scrypt verify OK:', verifyPassword(record, 'correct horse'));
module.exports = { hashPassword, verifyPassword };
'''),
        ("signature.js", r'''// Correct Ed25519 signing and verification (Node.js).
'use strict';
const crypto = require('crypto');

const { publicKey, privateKey } = crypto.generateKeyPairSync('ed25519');
const message = Buffer.from('sign me');
const signature = crypto.sign(null, message, privateKey);   // null algorithm for Ed25519
const ok = crypto.verify(null, message, publicKey, signature);
console.log('Ed25519 verified:', ok);
module.exports = { publicKey, privateKey };
'''),
        ("hmacHash.js", r'''// Correct SHA-256 and HMAC-SHA-256 with constant-time verification (Node.js).
'use strict';
const crypto = require('crypto');

const sha256Hex = (data) => crypto.createHash('sha256').update(data).digest('hex');
const hmacSha256 = (key, data) => crypto.createHmac('sha256', key).update(data).digest();

function verify(key, data, tag) {
  const expected = hmacSha256(key, data);
  return expected.length === tag.length && crypto.timingSafeEqual(expected, tag);
}

const key = Buffer.from('secret-mac-key');
const tag = hmacSha256(key, Buffer.from('authenticate me'));
console.log('SHA-256:', sha256Hex('hello'));
console.log('HMAC-SHA-256 verify OK:', verify(key, Buffer.from('authenticate me'), tag));
module.exports = { sha256Hex, hmacSha256, verify };
'''),
    ],
    # ------------------------------------------------------------ typescript
    "typescript": [
        ("aeadEncrypt.ts", r'''// Correct AES-256-GCM authenticated encryption with WebCrypto (SubtleCrypto).
export async function generateKey(): Promise<CryptoKey> {
  return crypto.subtle.generateKey({ name: 'AES-GCM', length: 256 }, true, ['encrypt', 'decrypt']);
}

export async function encrypt(key: CryptoKey, plaintext: Uint8Array, aad: Uint8Array): Promise<Uint8Array> {
  const iv = crypto.getRandomValues(new Uint8Array(12));   // unique 96-bit nonce
  const ct = await crypto.subtle.encrypt(
    { name: 'AES-GCM', iv, additionalData: aad, tagLength: 128 },
    key,
    plaintext,
  );
  const out = new Uint8Array(iv.length + ct.byteLength);
  out.set(iv, 0);
  out.set(new Uint8Array(ct), iv.length);
  return out;
}
'''),
        ("passwordHash.ts", r'''// Correct password key derivation with PBKDF2-HMAC-SHA-256 (WebCrypto).
export function randomSalt(): Uint8Array {
  return crypto.getRandomValues(new Uint8Array(16));
}

export async function deriveKey(password: string, salt: Uint8Array): Promise<ArrayBuffer> {
  const material = await crypto.subtle.importKey(
    'raw', new TextEncoder().encode(password), 'PBKDF2', false, ['deriveBits'],
  );
  return crypto.subtle.deriveBits(
    { name: 'PBKDF2', salt, iterations: 210_000, hash: 'SHA-256' },
    material,
    256,
  );
}
'''),
        ("signature.ts", r'''// Correct ECDSA on NIST P-256 with SHA-256 (WebCrypto).
export async function signAndVerify(message: Uint8Array): Promise<boolean> {
  const { privateKey, publicKey } = await crypto.subtle.generateKey(
    { name: 'ECDSA', namedCurve: 'P-256' }, true, ['sign', 'verify'],
  );
  const signature = await crypto.subtle.sign({ name: 'ECDSA', hash: 'SHA-256' }, privateKey, message);
  return crypto.subtle.verify({ name: 'ECDSA', hash: 'SHA-256' }, publicKey, signature, message);
}
'''),
        ("hmacHash.ts", r'''// Correct SHA-256 digest and HMAC-SHA-256 (WebCrypto). WebCrypto verify is constant-time.
export async function sha256(data: Uint8Array): Promise<ArrayBuffer> {
  return crypto.subtle.digest('SHA-256', data);
}

async function importHmacKey(rawKey: Uint8Array): Promise<CryptoKey> {
  return crypto.subtle.importKey('raw', rawKey, { name: 'HMAC', hash: 'SHA-256' }, false, ['sign', 'verify']);
}

export async function tag(rawKey: Uint8Array, data: Uint8Array): Promise<ArrayBuffer> {
  return crypto.subtle.sign('HMAC', await importHmacKey(rawKey), data);
}

export async function verify(rawKey: Uint8Array, data: Uint8Array, mac: Uint8Array): Promise<boolean> {
  return crypto.subtle.verify('HMAC', await importHmacKey(rawKey), mac, data);
}
'''),
    ],
    # --------------------------------------------------------------------- c
    "c": [
        ("aead_encrypt.c", r'''/* Correct AES-256-GCM authenticated encryption with a random IV (OpenSSL EVP).
 * iv (12 bytes) and tag (16 bytes) are written to caller buffers; returns the
 * ciphertext length, or -1 on error. */
#include <openssl/evp.h>
#include <openssl/rand.h>

int aes256gcm_encrypt(const unsigned char *key,
                      const unsigned char *plaintext, int plaintext_len,
                      const unsigned char *aad, int aad_len,
                      unsigned char *iv, unsigned char *tag,
                      unsigned char *out) {
    if (RAND_bytes(iv, 12) != 1) {
        return -1;                                   /* fresh random nonce */
    }
    EVP_CIPHER_CTX *ctx = EVP_CIPHER_CTX_new();
    if (ctx == NULL) {
        return -1;
    }
    int len = 0, out_len = -1;
    if (EVP_EncryptInit_ex(ctx, EVP_aes_256_gcm(), NULL, NULL, NULL) == 1 &&
        EVP_CIPHER_CTX_ctrl(ctx, EVP_CTRL_GCM_SET_IVLEN, 12, NULL) == 1 &&
        EVP_EncryptInit_ex(ctx, NULL, NULL, key, iv) == 1) {
        if (aad_len > 0) {
            EVP_EncryptUpdate(ctx, NULL, &len, aad, aad_len);
        }
        if (EVP_EncryptUpdate(ctx, out, &len, plaintext, plaintext_len) == 1) {
            out_len = len;
            if (EVP_EncryptFinal_ex(ctx, out + len, &len) == 1 &&
                EVP_CIPHER_CTX_ctrl(ctx, EVP_CTRL_GCM_GET_TAG, 16, tag) == 1) {
                out_len += len;
            } else {
                out_len = -1;
            }
        }
    }
    EVP_CIPHER_CTX_free(ctx);
    return out_len;
}
'''),
        ("password_hash.c", r'''/* Correct password hashing with PBKDF2-HMAC-SHA-256 and a random salt (OpenSSL).
 * Fills salt (16 bytes) and derives a 32-byte key into out. Returns 1 on success. */
#include <openssl/evp.h>
#include <openssl/rand.h>

int pbkdf2_hash(const char *password, int password_len,
                unsigned char *salt, unsigned char *out) {
    if (RAND_bytes(salt, 16) != 1) {
        return 0;
    }
    return PKCS5_PBKDF2_HMAC(password, password_len,
                             salt, 16,
                             210000,                 /* iterations */
                             EVP_sha256(),
                             32, out);
}
'''),
        ("signature.c", r'''/* Correct Ed25519 signing and verification (OpenSSL EVP, 1.1.1+). */
#include <openssl/evp.h>

int ed25519_sign(EVP_PKEY *pkey, const unsigned char *msg, size_t msg_len,
                 unsigned char *sig, size_t *sig_len) {
    EVP_MD_CTX *ctx = EVP_MD_CTX_new();
    if (ctx == NULL) {
        return 0;
    }
    int ok = EVP_DigestSignInit(ctx, NULL, NULL, NULL, pkey) == 1 &&
             EVP_DigestSign(ctx, sig, sig_len, msg, msg_len) == 1;
    EVP_MD_CTX_free(ctx);
    return ok;
}

int ed25519_verify(EVP_PKEY *pkey, const unsigned char *msg, size_t msg_len,
                   const unsigned char *sig, size_t sig_len) {
    EVP_MD_CTX *ctx = EVP_MD_CTX_new();
    if (ctx == NULL) {
        return 0;
    }
    int ok = EVP_DigestVerifyInit(ctx, NULL, NULL, NULL, pkey) == 1 &&
             EVP_DigestVerify(ctx, sig, sig_len, msg, msg_len) == 1;
    EVP_MD_CTX_free(ctx);
    return ok;
}
'''),
        ("hmac_hash.c", r'''/* Correct SHA-256 digest and HMAC-SHA-256 with a constant-time compare (OpenSSL). */
#include <openssl/evp.h>
#include <openssl/hmac.h>
#include <openssl/crypto.h>

void sha256(const unsigned char *data, size_t len, unsigned char out[32]) {
    unsigned int n = 0;
    EVP_Digest(data, len, out, &n, EVP_sha256(), NULL);
}

int hmac_verify(const unsigned char *key, int key_len,
                const unsigned char *data, size_t data_len,
                const unsigned char *tag) {
    unsigned char mac[32];
    unsigned int mac_len = 0;
    HMAC(EVP_sha256(), key, key_len, data, data_len, mac, &mac_len);
    return CRYPTO_memcmp(mac, tag, 32) == 0;         /* constant-time */
}
'''),
    ],
    # ------------------------------------------------------------------- cpp
    "cpp": [
        ("aead_encrypt.cpp", r'''// Correct XChaCha20-Poly1305 AEAD with a random nonce (libsodium).
// Call sodium_init() once at program startup before using these helpers.
#include <sodium.h>
#include <string>
#include <vector>

std::vector<unsigned char> encrypt(const unsigned char *key,
                                   const std::string &plaintext,
                                   const std::string &aad) {
    std::vector<unsigned char> nonce(crypto_aead_xchacha20poly1305_ietf_NPUBBYTES);
    randombytes_buf(nonce.data(), nonce.size());          // fresh random nonce
    std::vector<unsigned char> ct(plaintext.size() + crypto_aead_xchacha20poly1305_ietf_ABYTES);
    unsigned long long ct_len = 0;
    crypto_aead_xchacha20poly1305_ietf_encrypt(
        ct.data(), &ct_len,
        (const unsigned char *)plaintext.data(), plaintext.size(),
        (const unsigned char *)aad.data(), aad.size(),
        nullptr, nonce.data(), key);
    ct.resize(ct_len);
    nonce.insert(nonce.end(), ct.begin(), ct.end());      // prepend nonce
    return nonce;
}
'''),
        ("password_hash.cpp", r'''// Correct password hashing with Argon2id (libsodium crypto_pwhash).
#include <sodium.h>
#include <string>

bool hash_password(const std::string &password, char out[crypto_pwhash_STRBYTES]) {
    return crypto_pwhash_str(
        out, password.c_str(), password.size(),
        crypto_pwhash_OPSLIMIT_MODERATE,
        crypto_pwhash_MEMLIMIT_MODERATE) == 0;
}

bool verify_password(const char *stored, const std::string &password) {
    return crypto_pwhash_str_verify(stored, password.c_str(), password.size()) == 0;
}
'''),
        ("signature.cpp", r'''// Correct Ed25519 signatures (libsodium crypto_sign).
#include <sodium.h>
#include <string>
#include <vector>

bool sign_and_verify(const std::string &message) {
    unsigned char pk[crypto_sign_PUBLICKEYBYTES];
    unsigned char sk[crypto_sign_SECRETKEYBYTES];
    crypto_sign_keypair(pk, sk);

    std::vector<unsigned char> signature(crypto_sign_BYTES);
    unsigned long long sig_len = 0;
    crypto_sign_detached(signature.data(), &sig_len,
                         (const unsigned char *)message.data(), message.size(), sk);
    return crypto_sign_verify_detached(signature.data(),
                                       (const unsigned char *)message.data(),
                                       message.size(), pk) == 0;
}
'''),
        ("hmac_hash.cpp", r'''// Correct hashing (BLAKE2b) and MAC (crypto_auth = HMAC-SHA-512-256) with libsodium.
#include <sodium.h>
#include <string>
#include <vector>

std::vector<unsigned char> hash(const std::string &data) {
    std::vector<unsigned char> out(crypto_generichash_BYTES);
    crypto_generichash(out.data(), out.size(),
                       (const unsigned char *)data.data(), data.size(),
                       nullptr, 0);
    return out;
}

bool authenticate_and_verify(const std::string &data,
                             const unsigned char *key) {
    unsigned char tag[crypto_auth_BYTES];
    crypto_auth(tag, (const unsigned char *)data.data(), data.size(), key);
    return crypto_auth_verify(tag, (const unsigned char *)data.data(),
                              data.size(), key) == 0;      // constant-time
}
'''),
    ],
    # ---------------------------------------------------------------- csharp
    "csharp": [
        ("AeadEncrypt.cs", r'''using System;
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
'''),
        ("PasswordHash.cs", r'''using System.Security.Cryptography;

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
'''),
        ("SignatureEcdsa.cs", r'''using System.Security.Cryptography;

namespace CorrectCrypto
{
    // Correct ECDSA on NIST P-256 with SHA-256.
    public static class SignatureEcdsa
    {
        public static bool SignAndVerify(byte[] message)
        {
            using var ecdsa = ECDsa.Create(ECCurve.NamedCurves.nistP256);
            byte[] signature = ecdsa.SignData(message, HashAlgorithmName.SHA256);
            return ecdsa.VerifyData(message, signature, HashAlgorithmName.SHA256);
        }
    }
}
'''),
        ("HmacHash.cs", r'''using System.Security.Cryptography;

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
'''),
    ],
    # -------------------------------------------------------------------- go
    "go": [
        ("aead_encrypt.go", r'''package correctcrypto

import (
	"crypto/aes"
	"crypto/cipher"
	"crypto/rand"
	"io"
)

// EncryptAESGCM performs AES-256-GCM AEAD with a fresh random nonce (32-byte key).
func EncryptAESGCM(key, plaintext, aad []byte) ([]byte, error) {
	block, err := aes.NewCipher(key)
	if err != nil {
		return nil, err
	}
	gcm, err := cipher.NewGCM(block)
	if err != nil {
		return nil, err
	}
	nonce := make([]byte, gcm.NonceSize())
	if _, err := io.ReadFull(rand.Reader, nonce); err != nil { // unique per message
		return nil, err
	}
	// Seal appends ciphertext+tag onto the nonce prefix.
	return gcm.Seal(nonce, nonce, plaintext, aad), nil
}
'''),
        ("password_hash.go", r'''package correctcrypto

import (
	"crypto/rand"
	"crypto/subtle"

	"golang.org/x/crypto/argon2"
)

// HashPassword derives an Argon2id hash with a fresh random salt.
func HashPassword(password []byte) ([]byte, error) {
	salt := make([]byte, 16)
	if _, err := rand.Read(salt); err != nil {
		return nil, err
	}
	key := argon2.IDKey(password, salt, 3, 64*1024, 4, 32) // time=3, mem=64MiB, threads=4
	return append(salt, key...), nil
}

// VerifyPassword recomputes the hash and compares it in constant time.
func VerifyPassword(stored, password []byte) bool {
	if len(stored) < 16 {
		return false
	}
	salt, expected := stored[:16], stored[16:]
	key := argon2.IDKey(password, salt, 3, 64*1024, 4, 32)
	return subtle.ConstantTimeCompare(key, expected) == 1
}
'''),
        ("signature.go", r'''package correctcrypto

import (
	"crypto/ed25519"
	"crypto/rand"
)

// SignAndVerify demonstrates correct Ed25519 signing and verification.
func SignAndVerify(message []byte) (bool, error) {
	public, private, err := ed25519.GenerateKey(rand.Reader)
	if err != nil {
		return false, err
	}
	signature := ed25519.Sign(private, message)
	return ed25519.Verify(public, message, signature), nil
}
'''),
        ("hmac_hash.go", r'''package correctcrypto

import (
	"crypto/hmac"
	"crypto/sha256"
)

// TagSHA256 computes an HMAC-SHA-256 tag over data.
func TagSHA256(key, data []byte) []byte {
	mac := hmac.New(sha256.New, key)
	mac.Write(data)
	return mac.Sum(nil)
}

// VerifyTag checks an HMAC-SHA-256 tag in constant time.
func VerifyTag(key, data, tag []byte) bool {
	return hmac.Equal(TagSHA256(key, data), tag) // constant-time
}

// Digest returns the SHA-256 hash of data.
func Digest(data []byte) [32]byte {
	return sha256.Sum256(data)
}
'''),
    ],
    # ------------------------------------------------------------------ rust
    "rust": [
        ("aead_encrypt.rs", r'''// Correct AES-256-GCM authenticated encryption with a random nonce (aes-gcm crate).
use aes_gcm::aead::{Aead, AeadCore, KeyInit, OsRng};
use aes_gcm::{Aes256Gcm, Nonce};

pub fn encrypt(key_bytes: &[u8; 32], plaintext: &[u8]) -> Vec<u8> {
    let cipher = Aes256Gcm::new(key_bytes.into());
    let nonce = Aes256Gcm::generate_nonce(&mut OsRng);  // fresh random 96-bit nonce
    let mut out = nonce.to_vec();
    let ciphertext = cipher.encrypt(&nonce, plaintext).expect("encryption failure");
    out.extend_from_slice(&ciphertext);
    out
}

pub fn decrypt(key_bytes: &[u8; 32], blob: &[u8]) -> Vec<u8> {
    let (nonce, ciphertext) = blob.split_at(12);
    let cipher = Aes256Gcm::new(key_bytes.into());
    cipher.decrypt(Nonce::from_slice(nonce), ciphertext).expect("decryption failure")
}
'''),
        ("password_hash.rs", r'''// Correct password hashing with Argon2id (argon2 crate).
use argon2::password_hash::rand_core::OsRng;
use argon2::password_hash::{PasswordHash, PasswordHasher, PasswordVerifier, SaltString};
use argon2::Argon2;

pub fn hash_password(password: &[u8]) -> String {
    let salt = SaltString::generate(&mut OsRng);        // random salt
    Argon2::default()
        .hash_password(password, &salt)
        .expect("hash failure")
        .to_string()
}

pub fn verify_password(encoded: &str, password: &[u8]) -> bool {
    match PasswordHash::new(encoded) {
        Ok(parsed) => Argon2::default().verify_password(password, &parsed).is_ok(),
        Err(_) => false,
    }
}
'''),
        ("signature.rs", r'''// Correct Ed25519 signatures (ed25519-dalek crate).
use ed25519_dalek::{Signature, Signer, SigningKey, Verifier};
use rand::rngs::OsRng;

pub fn sign_and_verify(message: &[u8]) -> bool {
    let mut csprng = OsRng;
    let signing_key = SigningKey::generate(&mut csprng);
    let signature: Signature = signing_key.sign(message);
    signing_key.verifying_key().verify(message, &signature).is_ok()
}
'''),
        ("hmac_hash.rs", r'''// Correct SHA-256 hashing and HMAC-SHA-256 with constant-time verification.
use hmac::{Hmac, Mac};
use sha2::{Digest, Sha256};

type HmacSha256 = Hmac<Sha256>;

pub fn digest(data: &[u8]) -> [u8; 32] {
    let mut hasher = Sha256::new();
    hasher.update(data);
    hasher.finalize().into()
}

pub fn verify(key: &[u8], data: &[u8], tag: &[u8]) -> bool {
    let mut mac = HmacSha256::new_from_slice(key).expect("HMAC accepts any key length");
    mac.update(data);
    mac.verify_slice(tag).is_ok() // constant-time
}
'''),
    ],
    # ------------------------------------------------------------------ ruby
    "ruby": [
        ("aead_encrypt.rb", r'''# frozen_string_literal: true
# Correct AES-256-GCM authenticated encryption with a random IV (OpenSSL).
require 'openssl'

def encrypt(key, plaintext, aad)
  cipher = OpenSSL::Cipher.new('aes-256-gcm')
  cipher.encrypt
  cipher.key = key
  iv = cipher.random_iv                 # fresh random 96-bit nonce
  cipher.auth_data = aad
  ciphertext = cipher.update(plaintext) + cipher.final
  iv + cipher.auth_tag + ciphertext     # 16-byte GCM tag
end

def decrypt(key, blob, aad)
  cipher = OpenSSL::Cipher.new('aes-256-gcm')
  cipher.decrypt
  cipher.key = key
  cipher.iv = blob[0, 12]
  cipher.auth_tag = blob[12, 16]
  cipher.auth_data = aad
  cipher.update(blob[28..]) + cipher.final
end
'''),
        ("password_hash.rb", r'''# frozen_string_literal: true
# Correct password hashing with scrypt and a random salt (OpenSSL::KDF).
require 'openssl'
require 'securerandom'

def hash_password(password)
  salt = SecureRandom.random_bytes(16)
  dk = OpenSSL::KDF.scrypt(password, salt: salt, N: 2**14, r: 8, p: 1, length: 32)
  salt + dk
end

def verify_password(stored, password)
  salt = stored[0, 16]
  expected = stored[16..]
  dk = OpenSSL::KDF.scrypt(password, salt: salt, N: 2**14, r: 8, p: 1, length: 32)
  OpenSSL.fixed_length_secure_compare(dk, expected) # constant-time
end
'''),
        ("signature.rb", r'''# frozen_string_literal: true
# Correct Ed25519 signing and verification (OpenSSL 3).
require 'openssl'

def sign_and_verify(message)
  key = OpenSSL::PKey.generate_key('ED25519')
  signature = key.sign(nil, message)    # Ed25519 uses no separate digest
  key.verify(nil, signature, message)
end
'''),
        ("hmac_hash.rb", r'''# frozen_string_literal: true
# Correct SHA-256 hashing and HMAC-SHA-256 with constant-time verification (OpenSSL).
require 'openssl'
require 'digest'

def sha256_hex(data)
  Digest::SHA256.hexdigest(data)
end

def hmac_sha256(key, data)
  OpenSSL::HMAC.digest('SHA256', key, data)
end

def verify(key, data, tag)
  OpenSSL.fixed_length_secure_compare(hmac_sha256(key, data), tag)
end
'''),
    ],
}

MANIFESTS = {
    "python": [("requirements.txt",
                "# correct-crypto Python demos\n"
                "cryptography>=42.0   # AESGCM, Ed25519 (aead_encrypt.py, signature.py)\n"
                "# password_hash.py and hmac_hash.py use only the standard library\n")],
    "go": [("go.mod",
            "module correctcrypto\n\ngo 1.22\n\nrequire golang.org/x/crypto v0.21.0\n")],
    "rust": [("Cargo.toml",
              "[package]\nname = \"correct-crypto\"\nversion = \"0.1.0\"\nedition = \"2021\"\n\n"
              "[dependencies]\naes-gcm = \"0.10\"\nargon2 = \"0.5\"\ned25519-dalek = \"2\"\n"
              "sha2 = \"0.10\"\nhmac = \"0.12\"\nrand = \"0.8\"\n")],
}

README = (
    "# correct-crypto/\n\n"
    "Idiomatic, **correct** use of strong modern cryptography via real libraries,\n"
    "one subfolder per language. Unlike the intentionally-broken files elsewhere\n"
    "in this corpus (the `misuse` flavor and `false-positives/`), every file here\n"
    "uses crypto the right way:\n\n"
    "- **AEAD**: AES-256-GCM / XChaCha20-Poly1305 with a fresh random nonce per message.\n"
    "- **Password hashing**: Argon2id / scrypt / PBKDF2-HMAC-SHA-256 with a random\n"
    "  salt and a high work factor.\n"
    "- **Signatures**: Ed25519 / ECDSA-P256 with SHA-256.\n"
    "- **Hash + MAC**: SHA-256 / BLAKE2b and HMAC-SHA-256 with constant-time verification.\n\n"
    "Every algorithm reference here is a genuine primitive in real use, so a scanner\n"
    "should report all of them as **true positives**. This folder deliberately contains:\n\n"
    "- no weak or deprecated algorithms (no legacy hashes or ciphers), and\n"
    "- no decoy or lookalike tokens: no ordinary words that merely resemble cipher names,\n\n"
    "so a precise scanner should also produce **zero false positives** here. It is the\n"
    "correct counterpart to `false-positives/`.\n\n"
    "## Files (per language)\n\n"
    "| File | Primitive |\n"
    "|---|---|\n"
    "| `aead_encrypt` | authenticated symmetric encryption |\n"
    "| `password_hash` | password key-derivation |\n"
    "| `signature` | digital signature |\n"
    "| `hmac_hash` | hash + MAC with constant-time verify |\n\n"
    "The Python `password_hash.py` / `hmac_hash.py` and the Node.js files run on the\n"
    "standard library alone; the rest need the libraries in each language's manifest\n"
    "(`requirements.txt`, `go.mod`, `Cargo.toml`).\n"
)


def main():
    root = os.path.join(HERE, "correct-crypto")
    total = 0
    per = {}
    for langdir, files in FILES.items():
        d = os.path.join(root, langdir)
        os.makedirs(d, exist_ok=True)
        entries = files + MANIFESTS.get(langdir, [])
        for fn, content in entries:
            with open(os.path.join(d, fn), "w", encoding="utf-8") as f:
                f.write(content)
        per[langdir] = len(entries)
        total += len(entries)
    with open(os.path.join(root, "README.md"), "w", encoding="utf-8") as f:
        f.write(README)
    total += 1

    print("correct-crypto/ generated under:", root)
    for langdir in FILES:
        print("  %-12s %d files" % (langdir, per[langdir]))
    print("  %-12s %d files (+ README.md)" % ("TOTAL", total))


if __name__ == "__main__":
    main()
