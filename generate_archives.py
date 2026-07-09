#!/usr/bin/env python3
"""
Generate archives/ : crypto assets packaged as .zip / .jar / .tar.gz / .tgz.

Exercises the scanner's ARCHIVE-UPLOAD path. Each archive bundles a mix of:
  - correct-crypto/     -> correctly-used real crypto  (detect as TRUE positives)
  - quantum-vulnerable/ + quantum-resistant/ -> real algorithms (detect)
  - false-positives/    -> lookalike decoys            (expect ZERO findings)

Contents are pulled from the folders that already exist in the corpus, so the
archived files match their unpacked counterparts. archives/README.md is the key.

Usage:  python3 generate_archives.py   (run after the other generators)
"""

import os
import io
import zipfile
import tarfile

HERE = os.path.dirname(os.path.abspath(__file__))
ARCH = os.path.join(HERE, "archives")
CODE = (".py", ".java", ".go", ".js", ".ts", ".c", ".cpp", ".cs", ".rs", ".rb")
ZDATE = (2026, 1, 1, 0, 0, 0)


def rel(p):
    return os.path.relpath(p, HERE).replace(os.sep, "/")


def read(p):
    with open(p, "rb") as f:
        return f.read()


def all_in(folder):
    base = os.path.join(HERE, folder)
    return [os.path.join(base, f) for f in sorted(os.listdir(base))
            if os.path.isfile(os.path.join(base, f)) and f.endswith(CODE)]


def one_per_subdir(folder):
    out = []
    base = os.path.join(HERE, folder)
    for sub in sorted(os.listdir(base)):
        d = os.path.join(base, sub)
        if os.path.isdir(d):
            for f in sorted(os.listdir(d)):
                if f.endswith(CODE):
                    out.append(os.path.join(d, f))
                    break
    return out


# --- selections -------------------------------------------------------------
TRUE_CORRECT = one_per_subdir("correct-crypto")          # ~1 per language
TRUE_QUANTUM = all_in("quantum-vulnerable")[:2] + all_in("quantum-resistant")[:2]
FALSE = all_in("false-positives")[:8]
JAVA_TP = all_in("correct-crypto/java")                  # real crypto Java
JAVA_FP = [p for p in all_in("false-positives") if p.endswith(".java")][:1]

ASSET_NOTE = (
    b"crypto-assets bundle (synthetic)\n"
    b"correct-crypto/       = correctly-used real crypto -> detect (true positives)\n"
    b"quantum-vulnerable/   = Shor-breakable real algorithms -> detect\n"
    b"quantum-resistant/    = post-quantum real algorithms -> detect\n"
    b"false-positives/      = lookalike decoys -> expect ZERO findings\n"
)

MANIFEST = (
    b"Manifest-Version: 1.0\r\n"
    b"Created-By: crypto-test-corpus\r\n"
    b"Implementation-Title: crypto-lib\r\n"
    b"Crypto-Algorithms: AES-256-GCM, PBKDF2, Ed25519, HMAC-SHA-256\r\n"
    b"Main-Class: com.example.crypto.AeadEncrypt\r\n"
    b"\r\n"
)


# --- writers ----------------------------------------------------------------
def write_zip(path, entries):
    with zipfile.ZipFile(path, "w", zipfile.ZIP_DEFLATED) as z:
        for arc, data in entries:
            zi = zipfile.ZipInfo(arc, date_time=ZDATE)
            zi.compress_type = zipfile.ZIP_DEFLATED
            z.writestr(zi, data)


def write_targz(path, entries):
    with tarfile.open(path, "w:gz") as t:
        for arc, data in entries:
            ti = tarfile.TarInfo(arc)
            ti.size = len(data)
            ti.mtime = 0
            t.addfile(ti, io.BytesIO(data))


def targz_bytes(entries):
    buf = io.BytesIO()
    with tarfile.open(fileobj=buf, mode="w:gz") as t:
        for arc, data in entries:
            ti = tarfile.TarInfo(arc)
            ti.size = len(data)
            ti.mtime = 0
            t.addfile(ti, io.BytesIO(data))
    return buf.getvalue()


def mixed_entries():
    e = []
    for p in TRUE_CORRECT + TRUE_QUANTUM + FALSE:
        e.append(("crypto-assets/" + rel(p), read(p)))
    e.append(("crypto-assets/README.txt", ASSET_NOTE))
    return e


README = (
    "# archives/ -- crypto assets packaged as archives\n\n"
    "Exercises the scanner's **archive-upload** path (`.zip` / `.jar` / `.tar.gz`\n"
    "/ `.tgz`). Each archive bundles a mix of real crypto (true positives) and\n"
    "lookalike decoys (false positives), taken from the corpus folders:\n\n"
    "- `correct-crypto/` -> correctly-used real crypto -> **detect**\n"
    "- `quantum-vulnerable/` + `quantum-resistant/` -> real algorithms -> **detect**\n"
    "- `false-positives/` -> lookalike decoys -> **expect zero findings**\n\n"
    "| Archive | Format | Contents | Tests |\n"
    "|---|---|---|---|\n"
    "| `crypto_assets.zip` | zip | mixed tree (TP + FP) | zip extraction |\n"
    "| `crypto_assets.tar.gz` | tar + gzip | mixed tree | tar.gz extraction |\n"
    "| `crypto_assets.tgz` | tar + gzip | mixed tree | `.tgz` alias |\n"
    "| `crypto_lib.jar` | jar (zip) | `META-INF/MANIFEST.MF` (`Crypto-Algorithms` header) + Java TP + one Java FP | jar + manifest scanning |\n"
    "| `nested_crypto.zip` | zip -> tar.gz | `inner_crypto.tar.gz` inside | **recursive** extraction |\n\n"
    "## Expected\n\n"
    "The scanner should unpack each archive and report the real algorithms from the\n"
    "`correct-crypto` / `quantum-*` entries, and nothing from the `false-positives`\n"
    "entries. If it cannot recurse into `nested_crypto.zip`'s inner tarball, the\n"
    "crypto inside is a false negative.\n\n"
    "Rebuild: `python3 generate_archives.py` (run after the other generators).\n"
)


def main():
    os.makedirs(ARCH, exist_ok=True)
    mixed = mixed_entries()

    write_zip(os.path.join(ARCH, "crypto_assets.zip"), mixed)
    write_targz(os.path.join(ARCH, "crypto_assets.tar.gz"), mixed)
    write_targz(os.path.join(ARCH, "crypto_assets.tgz"), mixed)

    jar = [("META-INF/MANIFEST.MF", MANIFEST)]
    for p in JAVA_TP:
        jar.append(("com/example/crypto/" + os.path.basename(p), read(p)))
    for p in JAVA_FP:
        jar.append(("com/example/util/" + os.path.basename(p), read(p)))
    write_zip(os.path.join(ARCH, "crypto_lib.jar"), jar)

    # nested: an inner tar.gz (real + decoy) placed inside an outer zip
    inner = targz_bytes([("inner/" + rel(p), read(p)) for p in (TRUE_CORRECT[:2] + FALSE[:2])])
    write_zip(os.path.join(ARCH, "nested_crypto.zip"), [
        ("bundle/inner_crypto.tar.gz", inner),
        ("bundle/note.txt",
         b"Recursion test: the scanner must also extract inner_crypto.tar.gz,\n"
         b"which contains real crypto (AES-256-GCM, Ed25519) and decoys.\n"),
    ])

    with open(os.path.join(ARCH, "README.md"), "w", encoding="utf-8") as f:
        f.write(README)

    print("archives/ written:")
    for fn in sorted(os.listdir(ARCH)):
        size = os.path.getsize(os.path.join(ARCH, fn))
        print("  %-24s %6d bytes" % (fn, size))
    print("bundled: %d true-positive + %d quantum + %d false-positive source files"
          % (len(TRUE_CORRECT), len(TRUE_QUANTUM), len(FALSE)))


if __name__ == "__main__":
    main()
