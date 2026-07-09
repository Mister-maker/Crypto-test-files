# evasion-tests/ -- detection-robustness regression suite

Adversarial fixtures for the crypto-inventory scanner. Each `regress_*` file
hides the **same 12 algorithms** with a different evasion technique. Files use
real language extensions so a source scanner will process them; the obfuscation
payloads are language-agnostic. A naive literal / regex / keyword scanner finds
few or none of them -- each miss is a **false negative** to fix. A robust scanner
that normalizes encodings, Unicode and token boundaries should recover all 12.

## Ground truth (hidden in every regress_* file, in this block order)

1 AES  2 DES  3 RSA  4 SHA256  5 MD5  6 RC4  7 ChaCha20  8 Kyber  9 Dilithium
10 ECDSA  11 Blowfish  12 Ed25519

## Files

| File | Technique | What it breaks |
|---|---|---|
| `regress_split_concat.java` | string splitting / concatenation | contiguous token never appears |
| `regress_encoding_escapes.js` | hex / octal / `\u` / HTML-entity / URL / base64 / ROT13 | name only present once decoded |
| `regress_unicode_homoglyph.py` | Cyrillic / fullwidth / math-bold / circled look-alikes | bytes differ from ASCII |
| `regress_zero_width.ts` | zero-width space/joiner between letters | token split by invisible chars |
| `regress_separators_case.cs` | separators, case, reversal | token shape altered |
| `regress_comment_injection.c` | comment / line-continuation / token-paste splicing | name forms only after preprocessing |
| `regress_pathological.go` | huge lines, ReDoS bait, deep nesting | line-length limit / regex hang / recursion |

## How to use

Upload each file to the scanner and compare against the ground truth above.
Any algorithm it fails to surface is a regression (false negative) to fix.
The extensions are only routing hints -- the payloads are the same across all
files. `aes.java` is the plain comma-separated algorithm-name list.
