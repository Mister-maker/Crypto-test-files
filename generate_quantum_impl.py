#!/usr/bin/env python3
"""
Generate real algorithm implementations for the three quantum folders, per the
user's taxonomy:

  quantum-vulnerable/  -> broken / weak algorithms: RSA, ECDSA, 3DES
  quantum-resistant/   -> symmetric primitives:      AES-256-GCM, SHA-512, HMAC
  quantum-safe/        -> NIST PQC:                   ML-KEM-768, ML-DSA-65

One file per language (Java, Rust, Go, Python, JavaScript) in each folder, using
each language's idiomatic library. Additive: it only writes these 15 files (and
creates quantum-safe/); existing catalog files are left untouched.

Usage:  python3 generate_quantum_impl.py
"""

import os

HERE = os.path.dirname(os.path.abspath(__file__))

FILES = {
    # ================================================================ VULNERABLE
    "quantum-vulnerable": [
        ("broken_algorithms.py", r'''#!/usr/bin/env python3
"""Quantum-vulnerable / broken algorithms: RSA, ECDSA, 3DES.

RSA and ECDSA are broken by Shor's algorithm on a large quantum computer; 3DES
(DESede) is a weak 64-bit-block legacy cipher. Kept for legacy/interop testing.
Requires: cryptography (pip install cryptography).
"""
import os
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import ec, padding, rsa
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes


def rsa_oaep(data: bytes) -> bytes:
    key = rsa.generate_private_key(public_exponent=65537, key_size=2048)
    pad = padding.OAEP(mgf=padding.MGF1(hashes.SHA256()), algorithm=hashes.SHA256(), label=None)
    return key.decrypt(key.public_key().encrypt(data, pad), pad)


def ecdsa_sign(message: bytes) -> bytes:
    key = ec.generate_private_key(ec.SECP256R1())
    signature = key.sign(message, ec.ECDSA(hashes.SHA256()))
    key.public_key().verify(signature, message, ec.ECDSA(hashes.SHA256()))
    return signature


def triple_des(block: bytes) -> bytes:
    key = os.urandom(24)                       # 3DES / DESede, 192-bit (deprecated)
    iv = os.urandom(8)
    encryptor = Cipher(algorithms.TripleDES(key), modes.CBC(iv)).encryptor()
    return encryptor.update(block) + encryptor.finalize()


if __name__ == "__main__":
    print("RSA-2048 OAEP round-trip:", rsa_oaep(b"secret"))
    print("ECDSA P-256 signature len:", len(ecdsa_sign(b"message")))
    print("3DES-CBC ciphertext len:", len(triple_des(b"8bytes!!")))
'''),
        ("BrokenAlgorithms.java", r'''package quantum.vulnerable;

import java.security.KeyPair;
import java.security.KeyPairGenerator;
import java.security.Signature;
import java.security.spec.ECGenParameterSpec;
import javax.crypto.Cipher;
import javax.crypto.KeyGenerator;
import javax.crypto.SecretKey;
import javax.crypto.spec.IvParameterSpec;

/** Quantum-vulnerable / broken algorithms: RSA (Shor), ECDSA (Shor), 3DES (weak). */
public final class BrokenAlgorithms {

    public static byte[] rsaOaep(byte[] data) throws Exception {
        KeyPairGenerator kpg = KeyPairGenerator.getInstance("RSA");
        kpg.initialize(2048);
        KeyPair kp = kpg.generateKeyPair();
        Cipher c = Cipher.getInstance("RSA/ECB/OAEPWithSHA-256AndMGF1Padding");
        c.init(Cipher.ENCRYPT_MODE, kp.getPublic());
        return c.doFinal(data);
    }

    public static byte[] ecdsaSign(byte[] message) throws Exception {
        KeyPairGenerator kpg = KeyPairGenerator.getInstance("EC");
        kpg.initialize(new ECGenParameterSpec("secp256r1"));
        KeyPair kp = kpg.generateKeyPair();
        Signature s = Signature.getInstance("SHA256withECDSA");
        s.initSign(kp.getPrivate());
        s.update(message);
        return s.sign();
    }

    public static byte[] tripleDes(byte[] data) throws Exception {
        SecretKey key = KeyGenerator.getInstance("DESede").generateKey();   // 3DES, deprecated
        Cipher c = Cipher.getInstance("DESede/CBC/PKCS5Padding");
        c.init(Cipher.ENCRYPT_MODE, key, new IvParameterSpec(new byte[8]));
        return c.doFinal(data);
    }

    public static void main(String[] args) throws Exception {
        System.out.println("RSA-OAEP ciphertext: " + rsaOaep("secret".getBytes()).length);
        System.out.println("ECDSA signature: " + ecdsaSign("message".getBytes()).length);
        System.out.println("3DES ciphertext: " + tripleDes("data".getBytes()).length);
    }
}
'''),
        ("broken_algorithms.go", r'''package quantumvulnerable

import (
	"crypto/des"
	"crypto/ecdsa"
	"crypto/elliptic"
	"crypto/rand"
	"crypto/rsa"
	"crypto/sha256"
)

// RSAEncryptOAEP uses RSA-2048 OAEP (broken by Shor's algorithm).
func RSAEncryptOAEP(data []byte) ([]byte, error) {
	key, err := rsa.GenerateKey(rand.Reader, 2048)
	if err != nil {
		return nil, err
	}
	return rsa.EncryptOAEP(sha256.New(), rand.Reader, &key.PublicKey, data, nil)
}

// ECDSASign signs with ECDSA on P-256 (broken by Shor's algorithm).
func ECDSASign(message []byte) ([]byte, error) {
	key, err := ecdsa.GenerateKey(elliptic.P256(), rand.Reader)
	if err != nil {
		return nil, err
	}
	digest := sha256.Sum256(message)
	return ecdsa.SignASN1(rand.Reader, key, digest[:])
}

// TripleDESEncrypt uses 3DES-ECB on one block (weak 64-bit legacy cipher).
func TripleDESEncrypt(key [24]byte, block [8]byte) ([]byte, error) {
	c, err := des.NewTripleDESCipher(key[:])
	if err != nil {
		return nil, err
	}
	out := make([]byte, des.BlockSize)
	c.Encrypt(out, block[:])
	return out, nil
}
'''),
        ("broken_algorithms.rs", r'''// Quantum-vulnerable / broken algorithms: RSA (Shor), ECDSA (Shor), 3DES (weak).
// crates: rsa, sha2, rand, p256, ecdsa, des
use des::cipher::generic_array::GenericArray;
use des::cipher::{BlockEncrypt, KeyInit};
use des::TdesEde3;
use p256::ecdsa::signature::Signer;
use p256::ecdsa::{Signature, SigningKey};
use rand::rngs::OsRng;
use rsa::{Oaep, RsaPrivateKey};
use sha2::Sha256;

pub fn rsa_oaep(data: &[u8]) -> Vec<u8> {
    let mut rng = OsRng;
    let private_key = RsaPrivateKey::new(&mut rng, 2048).expect("rsa keygen");
    private_key
        .to_public_key()
        .encrypt(&mut rng, Oaep::new::<Sha256>(), data)
        .expect("rsa encrypt")
}

pub fn ecdsa_sign(message: &[u8]) -> Signature {
    let signing_key = SigningKey::random(&mut OsRng);
    signing_key.sign(message)
}

pub fn triple_des(key: &[u8; 24], block: &mut [u8; 8]) {
    let cipher = TdesEde3::new(GenericArray::from_slice(key)); // 3DES, deprecated
    cipher.encrypt_block(GenericArray::from_mut_slice(block));
}
'''),
        ("brokenAlgorithms.js", r'''// Quantum-vulnerable / broken algorithms: RSA (Shor), ECDSA (Shor), 3DES (weak).
'use strict';
const crypto = require('crypto');

function rsaOaep(data) {
  const { publicKey } = crypto.generateKeyPairSync('rsa', { modulusLength: 2048 });
  return crypto.publicEncrypt(
    { key: publicKey, oaepHash: 'sha256', padding: crypto.constants.RSA_PKCS1_OAEP_PADDING },
    data,
  );
}

function ecdsaSign(message) {
  const { privateKey } = crypto.generateKeyPairSync('ec', { namedCurve: 'P-256' });
  return crypto.sign('sha256', message, privateKey);
}

function tripleDes(data) {
  const key = crypto.randomBytes(24);              // 3DES / des-ede3, deprecated
  const iv = crypto.randomBytes(8);
  const cipher = crypto.createCipheriv('des-ede3-cbc', key, iv);
  return Buffer.concat([cipher.update(data), cipher.final()]);
}

console.log('RSA-OAEP ciphertext:', rsaOaep(Buffer.from('secret')).length);
console.log('ECDSA signature:', ecdsaSign(Buffer.from('message')).length);
console.log('3DES ciphertext:', tripleDes(Buffer.from('12345678')).length);
module.exports = { rsaOaep, ecdsaSign, tripleDes };
'''),
    ],
    # ================================================================ RESISTANT
    "quantum-resistant": [
        ("symmetric_primitives.py", r'''#!/usr/bin/env python3
"""Quantum-resistant symmetric primitives: AES-256-GCM, SHA-512, HMAC-SHA-256.

Symmetric crypto is only weakened by Grover's algorithm (effective security
halved), so 256-bit keys and >=384-bit hashes stay quantum-resistant.
AES-256-GCM needs `cryptography`; SHA-512 and HMAC are standard library.
"""
import hashlib
import hmac
import os
from cryptography.hazmat.primitives.ciphers.aead import AESGCM


def aes256_gcm(plaintext: bytes) -> bytes:
    key = AESGCM.generate_key(bit_length=256)
    nonce = os.urandom(12)
    return nonce + AESGCM(key).encrypt(nonce, plaintext, None)


def sha512(data: bytes) -> str:
    return hashlib.sha512(data).hexdigest()


def hmac_sha256(key: bytes, data: bytes) -> str:
    return hmac.new(key, data, hashlib.sha256).hexdigest()


if __name__ == "__main__":
    print("AES-256-GCM output len:", len(aes256_gcm(b"quantum-resistant")))
    print("SHA-512:", sha512(b"data")[:32])
    print("HMAC-SHA-256:", hmac_sha256(b"key", b"data")[:32])
'''),
        ("SymmetricPrimitives.java", r'''package quantum.resistant;

import java.security.MessageDigest;
import java.security.SecureRandom;
import javax.crypto.Cipher;
import javax.crypto.KeyGenerator;
import javax.crypto.Mac;
import javax.crypto.spec.GCMParameterSpec;
import javax.crypto.spec.SecretKeySpec;

/** Quantum-resistant symmetric primitives: AES-256-GCM, SHA-512, HMAC-SHA-256. */
public final class SymmetricPrimitives {

    public static byte[] aes256Gcm(byte[] plaintext) throws Exception {
        KeyGenerator kg = KeyGenerator.getInstance("AES");
        kg.init(256);
        byte[] iv = new byte[12];
        new SecureRandom().nextBytes(iv);
        Cipher c = Cipher.getInstance("AES/GCM/NoPadding");
        c.init(Cipher.ENCRYPT_MODE, kg.generateKey(), new GCMParameterSpec(128, iv));
        return c.doFinal(plaintext);
    }

    public static byte[] sha512(byte[] data) throws Exception {
        return MessageDigest.getInstance("SHA-512").digest(data);
    }

    public static byte[] hmacSha256(byte[] key, byte[] data) throws Exception {
        Mac mac = Mac.getInstance("HmacSHA256");
        mac.init(new SecretKeySpec(key, "HmacSHA256"));
        return mac.doFinal(data);
    }

    public static void main(String[] args) throws Exception {
        System.out.println("AES-256-GCM: " + aes256Gcm("data".getBytes()).length);
        System.out.println("SHA-512: " + sha512("data".getBytes()).length);
        System.out.println("HMAC-SHA-256: " + hmacSha256("key".getBytes(), "data".getBytes()).length);
    }
}
'''),
        ("symmetric_primitives.go", r'''package quantumresistant

import (
	"crypto/aes"
	"crypto/cipher"
	"crypto/hmac"
	"crypto/rand"
	"crypto/sha256"
	"crypto/sha512"
	"io"
)

// AES256GCM encrypts with AES-256-GCM (32-byte key) and a random nonce.
func AES256GCM(key, plaintext []byte) ([]byte, error) {
	block, err := aes.NewCipher(key)
	if err != nil {
		return nil, err
	}
	gcm, err := cipher.NewGCM(block)
	if err != nil {
		return nil, err
	}
	nonce := make([]byte, gcm.NonceSize())
	if _, err := io.ReadFull(rand.Reader, nonce); err != nil {
		return nil, err
	}
	return gcm.Seal(nonce, nonce, plaintext, nil), nil
}

// SHA512 returns the SHA-512 digest of data.
func SHA512(data []byte) [64]byte { return sha512.Sum512(data) }

// HMACSHA256 returns an HMAC-SHA-256 tag over data.
func HMACSHA256(key, data []byte) []byte {
	mac := hmac.New(sha256.New, key)
	mac.Write(data)
	return mac.Sum(nil)
}
'''),
        ("symmetric_primitives.rs", r'''// Quantum-resistant symmetric primitives: AES-256-GCM, SHA-512, HMAC-SHA-256.
// crates: aes-gcm, sha2, hmac
use aes_gcm::aead::{Aead, AeadCore, KeyInit, OsRng};
use aes_gcm::Aes256Gcm;
use hmac::{Hmac, Mac};
use sha2::{Digest, Sha256, Sha512};

pub fn aes256_gcm(plaintext: &[u8]) -> Vec<u8> {
    let key = Aes256Gcm::generate_key(&mut OsRng);
    let cipher = Aes256Gcm::new(&key);
    let nonce = Aes256Gcm::generate_nonce(&mut OsRng);
    let mut out = nonce.to_vec();
    out.extend_from_slice(&cipher.encrypt(&nonce, plaintext).expect("encrypt"));
    out
}

pub fn sha512(data: &[u8]) -> [u8; 64] {
    let mut hasher = Sha512::new();
    hasher.update(data);
    hasher.finalize().into()
}

pub fn hmac_sha256(key: &[u8], data: &[u8]) -> Vec<u8> {
    let mut mac = <Hmac<Sha256>>::new_from_slice(key).expect("any key length");
    mac.update(data);
    mac.finalize().into_bytes().to_vec()
}
'''),
        ("symmetricPrimitives.js", r'''// Quantum-resistant symmetric primitives: AES-256-GCM, SHA-512, HMAC-SHA-256.
'use strict';
const crypto = require('crypto');

function aes256Gcm(plaintext) {
  const key = crypto.randomBytes(32);
  const iv = crypto.randomBytes(12);
  const cipher = crypto.createCipheriv('aes-256-gcm', key, iv);
  const ct = Buffer.concat([cipher.update(plaintext), cipher.final()]);
  return Buffer.concat([iv, cipher.getAuthTag(), ct]);
}

const sha512 = (data) => crypto.createHash('sha512').update(data).digest('hex');
const hmacSha256 = (key, data) => crypto.createHmac('sha256', key).update(data).digest('hex');

console.log('AES-256-GCM output len:', aes256Gcm(Buffer.from('data')).length);
console.log('SHA-512:', sha512('data').slice(0, 32));
console.log('HMAC-SHA-256:', hmacSha256('key', 'data').slice(0, 32));
module.exports = { aes256Gcm, sha512, hmacSha256 };
'''),
    ],
    # ===================================================================== SAFE
    "quantum-safe": [
        ("post_quantum.py", r'''#!/usr/bin/env python3
"""Quantum-safe NIST PQC: ML-KEM-768 (FIPS 203) and ML-DSA-65 (FIPS 204).

Uses liboqs via the `oqs` Python binding (pip install liboqs-python). ML-KEM
(formerly CRYSTALS-Kyber) is key encapsulation; ML-DSA (formerly CRYSTALS-
Dilithium) is digital signatures.
"""
import oqs


def mlkem768_kem() -> bool:
    with oqs.KeyEncapsulation("ML-KEM-768") as kem:
        public_key = kem.generate_keypair()
        ciphertext, shared_secret = kem.encap_secret(public_key)
        return kem.decap_secret(ciphertext) == shared_secret


def mldsa65_sign(message: bytes) -> bool:
    with oqs.Signature("ML-DSA-65") as signer:
        public_key = signer.generate_keypair()
        signature = signer.sign(message)
        return signer.verify(message, signature, public_key)


if __name__ == "__main__":
    print("ML-KEM-768 shared-secret match:", mlkem768_kem())
    print("ML-DSA-65 verified:", mldsa65_sign(b"message"))
'''),
        ("PostQuantum.java", r'''package quantum.safe;

import java.security.KeyPair;
import java.security.KeyPairGenerator;
import java.security.Security;
import java.security.Signature;
import org.bouncycastle.pqc.jcajce.provider.BouncyCastlePQCProvider;
import org.bouncycastle.pqc.jcajce.spec.MLDSAParameterSpec;
import org.bouncycastle.pqc.jcajce.spec.MLKEMParameterSpec;

/** Quantum-safe NIST PQC via BouncyCastle: ML-KEM-768 (FIPS 203), ML-DSA-65 (FIPS 204). */
public final class PostQuantum {

    static {
        Security.addProvider(new BouncyCastlePQCProvider());
    }

    /** Generates an ML-KEM-768 key pair (encapsulation uses KEMGenerateSpec/KEMExtractSpec). */
    public static KeyPair mlkem768KeyPair() throws Exception {
        KeyPairGenerator kpg = KeyPairGenerator.getInstance("ML-KEM", "BCPQC");
        kpg.initialize(MLKEMParameterSpec.ml_kem_768);
        return kpg.generateKeyPair();
    }

    public static byte[] mldsa65Sign(byte[] message) throws Exception {
        KeyPairGenerator kpg = KeyPairGenerator.getInstance("ML-DSA", "BCPQC");
        kpg.initialize(MLDSAParameterSpec.ml_dsa_65);
        KeyPair kp = kpg.generateKeyPair();
        Signature sig = Signature.getInstance("ML-DSA", "BCPQC");
        sig.initSign(kp.getPrivate());
        sig.update(message);
        return sig.sign();
    }

    public static void main(String[] args) throws Exception {
        System.out.println("ML-KEM-768 public key: " + mlkem768KeyPair().getPublic().getEncoded().length);
        System.out.println("ML-DSA-65 signature: " + mldsa65Sign("message".getBytes()).length);
    }
}
'''),
        ("post_quantum.go", r'''package quantumsafe

import (
	"github.com/cloudflare/circl/kem/mlkem/mlkem768"
	"github.com/cloudflare/circl/sign/mldsa/mldsa65"
)

// MLKEM768 runs ML-KEM-768 (FIPS 203) encapsulation + decapsulation.
func MLKEM768() (bool, error) {
	scheme := mlkem768.Scheme()
	pk, sk, err := scheme.GenerateKeyPair()
	if err != nil {
		return false, err
	}
	ct, ss1, err := scheme.Encapsulate(pk)
	if err != nil {
		return false, err
	}
	ss2, err := scheme.Decapsulate(sk, ct)
	if err != nil {
		return false, err
	}
	return string(ss1) == string(ss2), nil
}

// MLDSA65 signs and verifies with ML-DSA-65 (FIPS 204).
func MLDSA65(message []byte) bool {
	pk, sk, err := mldsa65.GenerateKey(nil)
	if err != nil {
		return false
	}
	sig := make([]byte, mldsa65.SignatureSize)
	mldsa65.SignTo(sk, message, nil, false, sig)
	return mldsa65.Verify(pk, message, nil, sig)
}
'''),
        ("post_quantum.rs", r'''// Quantum-safe NIST PQC: ML-KEM-768 (FIPS 203) and ML-DSA-65 (FIPS 204).
// crates: pqcrypto-mlkem, pqcrypto-mldsa, pqcrypto-traits
use pqcrypto_mldsa::mldsa65;
use pqcrypto_mlkem::mlkem768;
use pqcrypto_traits::kem::SharedSecret;

pub fn mlkem768_kem() -> bool {
    let (public_key, secret_key) = mlkem768::keypair();
    let (shared1, ciphertext) = mlkem768::encapsulate(&public_key);
    let shared2 = mlkem768::decapsulate(&ciphertext, &secret_key);
    shared1.as_bytes() == shared2.as_bytes()
}

pub fn mldsa65_sign(message: &[u8]) -> bool {
    let (public_key, secret_key) = mldsa65::keypair();
    let signed = mldsa65::sign(message, &secret_key);
    mldsa65::open(&signed, &public_key).is_ok()
}
'''),
        ("postQuantum.js", r'''// Quantum-safe NIST PQC: ML-KEM-768 (FIPS 203) and ML-DSA-65 (FIPS 204).
// npm i @noble/post-quantum
'use strict';
const { ml_kem768 } = require('@noble/post-quantum/ml-kem');
const { ml_dsa65 } = require('@noble/post-quantum/ml-dsa');

function mlkem768() {
  const { publicKey, secretKey } = ml_kem768.keygen();
  const { cipherText, sharedSecret } = ml_kem768.encapsulate(publicKey);
  const shared2 = ml_kem768.decapsulate(cipherText, secretKey);
  return Buffer.from(sharedSecret).equals(Buffer.from(shared2));
}

function mldsa65(message) {
  const { publicKey, secretKey } = ml_dsa65.keygen();
  const signature = ml_dsa65.sign(secretKey, message);
  return ml_dsa65.verify(publicKey, message, signature);
}

console.log('ML-KEM-768 shared-secret match:', mlkem768());
console.log('ML-DSA-65 verified:', mldsa65(new TextEncoder().encode('message')));
module.exports = { mlkem768, mldsa65 };
'''),
    ],
}

SAFE_README = (
    "# quantum-safe/ -- NIST post-quantum implementations\n\n"
    "Real implementations of the top NIST-standardized PQC algorithms:\n\n"
    "- **ML-KEM-768** (FIPS 203, formerly CRYSTALS-Kyber) -- key encapsulation\n"
    "- **ML-DSA-65** (FIPS 204, formerly CRYSTALS-Dilithium) -- digital signatures\n\n"
    "One file per language (Java, Rust, Go, Python, JavaScript), each using that\n"
    "language's idiomatic PQC library: BouncyCastle (Java), pqcrypto (Rust),\n"
    "Cloudflare CIRCL (Go), liboqs/oqs (Python), @noble/post-quantum (JavaScript).\n\n"
    "These are TRUE positives -- real post-quantum crypto. Libraries are third-party;\n"
    "see each file's header for the dependency.\n"
)


def main():
    total = 0
    for folder, files in FILES.items():
        d = os.path.join(HERE, folder)
        os.makedirs(d, exist_ok=True)
        for fn, content in files:
            with open(os.path.join(d, fn), "w", encoding="utf-8") as f:
                f.write(content)
            total += 1
    with open(os.path.join(HERE, "quantum-safe", "README.md"), "w", encoding="utf-8") as f:
        f.write(SAFE_README)
    total += 1

    print("quantum implementation files written:", total)
    for folder, files in FILES.items():
        print("  %-20s %d files" % (folder + "/", len(files)))


if __name__ == "__main__":
    main()
