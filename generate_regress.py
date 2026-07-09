#!/usr/bin/env python3
"""
Generate evasion-tests/regress_* : an adversarial detection-ROBUSTNESS regression
suite for the crypto-inventory scanner.

Each regress_* file hides the SAME 12 algorithms with a different evasion
technique (string splitting, encodings, Unicode look-alikes, zero-width
injection, separators, comment/token-paste splicing, pathological input).

Files carry real language extensions (.java, .js, .py, .ts, .cs, .c, .go) so a
source scanner picks them up; the comment style of each file matches its
extension. The obfuscation payloads themselves are language-agnostic.

A naive literal / regex / keyword scanner finds few or none of them -> false
negatives to fix. A robust scanner that normalizes encodings, Unicode and
token boundaries should still recover all 12. evasion-tests/README.md is the key.

Usage:  python3 generate_regress.py
"""

import os
import base64
import codecs

HERE = os.path.dirname(os.path.abspath(__file__))
TEXT = os.path.join(HERE, "evasion-tests")

# The 12 algorithms hidden (in this fixed "block" order) in every file.
TARGETS = ["AES", "DES", "RSA", "SHA256", "MD5", "RC4",
           "ChaCha20", "Kyber", "Dilithium", "ECDSA", "Blowfish", "Ed25519"]

# -- encoders (return ENCODED text only; the name is never left in clear) -----

def hex_esc(s):
    return "".join("\\x%02x" % b for b in s.encode())

def oct_esc(s):
    return "".join("\\%03o" % b for b in s.encode())

def uni_esc(s):
    return "".join("\\u%04x" % ord(c) for c in s)

def html_dec(s):
    return "".join("&#%d;" % ord(c) for c in s)

def html_hex(s):
    return "".join("&#x%x;" % ord(c) for c in s)

def url_enc(s):
    return "".join("%%%02X" % b for b in s.encode())

def b64(s):
    return base64.b64encode(s.encode()).decode()

def rot13(s):
    return codecs.encode(s, "rot_13")

# -- Unicode transforms (built from code points; no exotic glyphs in source) --

CYR = {"A": 0x0410, "B": 0x0412, "C": 0x0421, "E": 0x0415, "H": 0x041D,
       "K": 0x041A, "M": 0x041C, "O": 0x041E, "P": 0x0420, "S": 0x0405,
       "T": 0x0422, "X": 0x0425, "a": 0x0430, "c": 0x0441, "e": 0x0435,
       "o": 0x043E, "p": 0x0440, "x": 0x0445, "y": 0x0443}

def cyrillic(name):
    out = []
    for ch in name:
        if ch not in CYR:
            return None
        out.append(chr(CYR[ch]))
    return "".join(out)

def fullwidth(s):
    return "".join(chr(ord(c) + 0xFEE0) if 0x21 <= ord(c) <= 0x7E else c for c in s)

def math_bold(s):
    out = []
    for c in s:
        if "A" <= c <= "Z":
            out.append(chr(0x1D5D4 + ord(c) - ord("A")))
        elif "a" <= c <= "z":
            out.append(chr(0x1D5EE + ord(c) - ord("a")))
        elif "0" <= c <= "9":
            out.append(chr(0x1D7EC + ord(c) - ord("0")))
        else:
            out.append(c)
    return "".join(out)

def circled(s):
    out = []
    for c in s:
        if "A" <= c <= "Z":
            out.append(chr(0x24B6 + ord(c) - ord("A")))
        elif "a" <= c <= "z":
            out.append(chr(0x24D0 + ord(c) - ord("a")))
        elif "1" <= c <= "9":
            out.append(chr(0x2460 + ord(c) - ord("1")))
        elif c == "0":
            out.append("⓪")
        else:
            out.append(c)
    return "".join(out)

def zwidth(s, sep):
    return sep.join(list(s))

# -- file builders (cc = this file's line-comment prefix) ---------------------

def build_encodings(cc):
    lines = [cc + " regress: value-encoding evasion. Each block encodes ONE algorithm",
             cc + " 7 ways; the plaintext name never appears. Block order: see README.", ""]
    for i, t in enumerate(TARGETS, 1):
        lines += [
            cc + " block %d" % i,
            "hex:     " + hex_esc(t),
            "octal:   " + oct_esc(t),
            "unicode: " + uni_esc(t),
            "htmldec: " + html_dec(t),
            "htmlhex: " + html_hex(t),
            "url:     " + url_enc(t),
            "base64:  " + b64(t),
            "rot13:   " + rot13(t),
            "",
        ]
    return "\n".join(lines) + "\n"

def build_homoglyphs(cc):
    lines = [cc + " regress: Unicode confusable / look-alike evasion. Bytes differ from",
             cc + " ASCII, so byte-literal matching misses them. Block order: see README.", ""]
    for i, t in enumerate(TARGETS, 1):
        cy = cyrillic(t) or "(no full cyrillic confusable)"
        lines += [
            cc + " block %d" % i,
            "cyrillic:  " + cy,
            "fullwidth: " + fullwidth(t),
            "mathbold:  " + math_bold(t),
            "circled:   " + circled(t),
            "",
        ]
    return "\n".join(lines) + "\n"

def build_zerowidth(cc):
    lines = [cc + " regress: zero-width / invisible-character injection between letters.",
             cc + " Characters really present (U+200B/200C/200D/FEFF). Order: README.", ""]
    for i, t in enumerate(TARGETS, 1):
        lines += [
            cc + " block %d" % i,
            "zwsp: " + zwidth(t, "​"),
            "zwnj: " + zwidth(t, "‌"),
            "zwj:  " + zwidth(t, "‍"),
            "bom:  " + "﻿" + zwidth(t, "​"),
            "",
        ]
    return "\n".join(lines) + "\n"

def build_split_concat(cc):
    lines = [
        cc + " regress: string splitting / concatenation. The contiguous algorithm",
        cc + " token never appears as one literal; only runtime joins reconstruct it.",
        "",
        cc + " lines below follow the README block order (1..12)",
        '"AE" + "S"',
        '"D" + "ES"',
        '"R" + "S" + "A"',
        '"S" + "HA2" + "56"',
        '"M" + "D" + "5"',
        '"RC" + "4"',
        '"Cha" + "Cha" + "20"',
        '"Ky" + "ber"',
        '"Dili" + "thium"',
        '"ECD" + "SA"',
        '"Blow" + "fish"',
        '"Ed" + "25519"',
        cc + " other idioms:",
        "['A','E','S'].join('')",
        "'%s%s' % ('RS', 'A')",
        "\"\".join(['Ky', 'ber'])",
        "String.join(\"\", \"E\",\"C\",\"D\",\"S\",\"A\")",
    ]
    return "\n".join(lines) + "\n"

def build_separators(cc):
    lines = [
        cc + " regress: separator / case / reversal evasion (block order per README).",
        "",
        "A.E.S",
        "D-E-S",
        "R_S_A",
        "S H A 2 5 6",
        "m d 5",
        "R/C/4",
        "C-h-a-C-h-a-2-0",
        "K.y.b.e.r",
        "D i l i t h i u m",
        "E|C|D|S|A",
        "B.l.o.w.f.i.s.h",
        "E d 2 5 5 1 9",
        "reversed:  SEA  ASR  AHS  5DM   " + cc + " forward names hidden by reversal",
    ]
    return "\n".join(lines) + "\n"

def build_comment_injection(cc):
    lines = [
        cc + " regress: comment / line-continuation / token-paste splicing (C/cpp).",
        "",
        '"AE" "S"            /* adjacent C string literals concatenate at compile time */',
        '"RS" "A"',
        '"Blow" "fish"',
        '"Cha" "Cha" "20"',
        '"SHA2" "56"',
        "AE\\",             # backslash-newline line continuation splices the next line
        "S256",
        "#define PASTE(a,b) a##b",
        "PASTE(Ed, 25519)   /* preprocessor token paste */",
        "PASTE(ECD, SA)     /* preprocessor token paste */",
        "K/**/y/**/b/**/e/**/r   " + cc + " comments between letters",
    ]
    return "\n".join(lines) + "\n"

def build_pathological(cc):
    header = (cc + " regress: pathological input (parser stress). A real token sits at the\n"
              + cc + " far end of each huge line -- scanners with line-length limits, regex\n"
              + cc + " catastrophic backtracking, or recursion limits will miss it or hang.\n\n")
    long_line = "a" * 50000 + "AES256"
    redos = "a" * 20000 + "!"
    nested = "(" * 2000 + "RSA" + ")" * 2000
    csv_bomb = ",".join(["col"] * 8000) + ",Ed25519"
    return header + "\n".join([long_line, redos, nested, csv_bomb, ""]) + "\n"

# (basename, extension, line-comment prefix, builder)
SPEC = [
    ("regress_split_concat", "java", "//", build_split_concat),
    ("regress_encoding_escapes", "js", "//", build_encodings),
    ("regress_unicode_homoglyph", "py", "#", build_homoglyphs),
    ("regress_zero_width", "ts", "//", build_zerowidth),
    ("regress_separators_case", "cs", "//", build_separators),
    ("regress_comment_injection", "c", "//", build_comment_injection),
    ("regress_pathological", "go", "//", build_pathological),
]

README = (
    "# evasion-tests/ -- detection-robustness regression suite\n\n"
    "Adversarial fixtures for the crypto-inventory scanner. Each `regress_*` file\n"
    "hides the **same 12 algorithms** with a different evasion technique. Files use\n"
    "real language extensions so a source scanner will process them; the obfuscation\n"
    "payloads are language-agnostic. A naive literal / regex / keyword scanner finds\n"
    "few or none of them -- each miss is a **false negative** to fix. A robust scanner\n"
    "that normalizes encodings, Unicode and token boundaries should recover all 12.\n\n"
    "## Ground truth (hidden in every regress_* file, in this block order)\n\n"
    "1 AES  2 DES  3 RSA  4 SHA256  5 MD5  6 RC4  7 ChaCha20  8 Kyber  9 Dilithium\n"
    "10 ECDSA  11 Blowfish  12 Ed25519\n\n"
    "## Files\n\n"
    "| File | Technique | What it breaks |\n"
    "|---|---|---|\n"
    "| `regress_split_concat.java` | string splitting / concatenation | contiguous token never appears |\n"
    "| `regress_encoding_escapes.js` | hex / octal / `\\u` / HTML-entity / URL / base64 / ROT13 | name only present once decoded |\n"
    "| `regress_unicode_homoglyph.py` | Cyrillic / fullwidth / math-bold / circled look-alikes | bytes differ from ASCII |\n"
    "| `regress_zero_width.ts` | zero-width space/joiner between letters | token split by invisible chars |\n"
    "| `regress_separators_case.cs` | separators, case, reversal | token shape altered |\n"
    "| `regress_comment_injection.c` | comment / line-continuation / token-paste splicing | name forms only after preprocessing |\n"
    "| `regress_pathological.go` | huge lines, ReDoS bait, deep nesting | line-length limit / regex hang / recursion |\n\n"
    "## How to use\n\n"
    "Upload each file to the scanner and compare against the ground truth above.\n"
    "Any algorithm it fails to surface is a regression (false negative) to fix.\n"
    "The extensions are only routing hints -- the payloads are the same across all\n"
    "files. `aes.java` is the plain comma-separated algorithm-name list.\n"
)


def main():
    os.makedirs(TEXT, exist_ok=True)
    # remove stale regress_* files (any extension) so renames don't leave orphans
    for f in os.listdir(TEXT):
        if f.startswith("regress_"):
            os.remove(os.path.join(TEXT, f))

    written = []
    for base, ext, cc, builder in SPEC:
        fn = base + "." + ext
        with open(os.path.join(TEXT, fn), "w", encoding="utf-8") as f:
            f.write(builder(cc))
        written.append(fn)
    with open(os.path.join(TEXT, "README.md"), "w", encoding="utf-8") as f:
        f.write(README)
    written.append("README.md")

    print("evasion-tests/ regression suite written:", len(written), "files")
    for fn in written:
        print("  ", fn)


if __name__ == "__main__":
    main()
