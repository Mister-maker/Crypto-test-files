# archives/ -- crypto assets packaged as archives

Exercises the scanner's **archive-upload** path (`.zip` / `.jar` / `.tar.gz`
/ `.tgz`). Each archive bundles a mix of real crypto (true positives) and
lookalike decoys (false positives), taken from the corpus folders:

- `correct-crypto/` -> correctly-used real crypto -> **detect**
- `quantum-vulnerable/` + `quantum-resistant/` -> real algorithms -> **detect**
- `false-positives/` -> lookalike decoys -> **expect zero findings**

| Archive | Format | Contents | Tests |
|---|---|---|---|
| `crypto_assets.zip` | zip | mixed tree (TP + FP) | zip extraction |
| `crypto_assets.tar.gz` | tar + gzip | mixed tree | tar.gz extraction |
| `crypto_assets.tgz` | tar + gzip | mixed tree | `.tgz` alias |
| `crypto_lib.jar` | jar (zip) | `META-INF/MANIFEST.MF` (`Crypto-Algorithms` header) + Java TP + one Java FP | jar + manifest scanning |
| `nested_crypto.zip` | zip -> tar.gz | `inner_crypto.tar.gz` inside | **recursive** extraction |

## Expected

The scanner should unpack each archive and report the real algorithms from the
`correct-crypto` / `quantum-*` entries, and nothing from the `false-positives`
entries. If it cannot recurse into `nested_crypto.zip`'s inner tarball, the
crypto inside is a false negative.

Rebuild: `python3 generate_archives.py` (run after the other generators).
