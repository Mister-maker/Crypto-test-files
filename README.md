# crypto-test-corpus

A **synthetic** multi-language test corpus for exercising a static-analysis /
crypto-inventory scanner. Every file is generated to be packed with
cryptographic algorithm names in as many syntactic positions as possible:
identifiers, class names, constants, enums, comments, string literals,
imports, and embedded JSON / YAML / XML / SQL / Markdown / HTML.

> This is NOT a real cryptography library. Security, correctness and
> compilation are explicitly not goals -- detection **coverage** is.

## Languages

`java/ python/ javascript/ typescript/ c/ cpp/ csharp/ go/ rust/ ruby/`

## Stress folders

Additional top-level folders target detection quality specifically.

The three `quantum-*` folders hold **real implementations** (one file per language:
Java, Rust, Go, Python, JavaScript) grouped by quantum-security class:

| Folder | Implements | Expected scanner result |
|---|---|---|
| `quantum-vulnerable/` | broken / weak: RSA-OAEP, ECDSA-P256, 3DES | true positives; flag as vulnerable/deprecated |
| `quantum-resistant/` | symmetric (safe at 256-bit): AES-256-GCM, SHA-512, HMAC-SHA-256 | true positives |
| `quantum-safe/` | NIST PQC: ML-KEM-768 (FIPS 203), ML-DSA-65 (FIPS 204) | true positives; flag as post-quantum |

The remaining folders target precision:

| Folder | Purpose | Expected scanner result |
|---|---|---|
| `false-positives/` | Lookalike/decoy content in **non-crypto** context: substring collisions (`Caesar`, `ghost`, `films`, `malaria`, `marshalJSON`), acronym clashes (`ECC` memory, `CBC`/`ECB`, `RC4` release-candidate, SQL `CAST`), pop-culture PQC names (Kyber, Dilithium, Falcon, Saber, Frodo, New Hope, Rainbow, Picnic), coincidental identifiers (`aria-label`, `describe()`, `broadcast()`) | **zero** findings — any hit is a false positive |
| `correct-crypto/` | Idiomatic, **correct** use of strong modern crypto per language: AEAD (AES-256-GCM / XChaCha20-Poly1305, random nonces), password KDFs (Argon2id / scrypt / PBKDF2), signatures (Ed25519 / ECDSA-P256), HMAC with constant-time verify. No weak algos, no lookalike tokens. | flag every algorithm as a **true positive**; zero false positives |

The `false-positives/` folder is a **precision benchmark**: a naive substring scanner
finds ~1,700 "matches" there, all wrong. The `correct-crypto/` folder is the clean
true-positive counterpart — every hit is real, correctly-used crypto, and nothing there
should ever trigger a false positive. Together they measure precision from both sides.

Regenerate with:

```
python3 generate_quantum_impl.py   # quantum-vulnerable/, quantum-resistant/, quantum-safe/
python3 generate_extra.py          # false-positives/
python3 generate_correct.py        # correct-crypto/
```

## File flavors (per language)

| Flavor | Description |
|---|---|
| compiling | Valid, runnable code using real crypto-ish APIs |
| almost | Valid code with a single intentional defect |
| syntax_error | Deliberately broken syntax |
| comment_only | Only comments, full of algorithm names |
| string_only | Only string constants |
| fake_api | Calls into nonexistent crypto libraries |
| dead_code | Unused variables and unreachable branches |
| deprecated | MD5/SHA1/DES/RC4 with deprecation markers |
| misuse | Hardcoded keys, ECB mode, reused nonces, etc. |
| random_words | Random crypto tokens with no functionality |
| docs_only | Pure documentation |

Plus per-language config/data files: `crypto_config.json`, `algorithms.yaml`,
`crypto_policy.xml`, `crypto_inventory.sql`, `ALGORITHMS.md`,
`crypto_dashboard.html`, and build manifests (`package.json`, `Cargo.toml`,
`go.mod`, `pom`-style `application.properties`, `Gemfile`, `CMakeLists.txt`, ...).

## Regenerate

```
python3 generate_corpus.py
```

Deterministic (fixed seed) -- re-running reproduces the same corpus.

## Algorithm families covered

Block/stream ciphers (AES, DES, 3DES, Blowfish, Twofish, IDEA, RC2/4/5/6,
Camellia, Serpent, CAST5/6, Skipjack, TEA/XTEA/XXTEA, GOST, SEED, SM4, ARIA,
PRESENT, CLEFIA, HIGHT, LEA, SPECK, SIMON, ChaCha20, Salsa20, Rabbit, HC128/256,
Grain, Trivium, MICKEY, Snow3G, ZUC); asymmetric (RSA, DH, ECDH, ECDSA, DSA,
ElGamal, Ed25519/448, X25519/448); PQC (Kyber/ML-KEM, CRYSTALS-Kyber, FrodoKEM,
BIKE, HQC, Classic McEliece, NTRU, Saber, SIKE, Dilithium/ML-DSA, Falcon,
SPHINCS+, XMSS, LMS); hashes (MD2/4/5, SHA1/2/3, SHAKE, RIPEMD-160, Whirlpool,
Tiger, HAVAL, BLAKE2/3, SM3); MAC/KDF (Poly1305, HMAC, CMAC, GMAC, HKDF, PBKDF2,
bcrypt, scrypt, Argon2, SipHash, CRC32).
