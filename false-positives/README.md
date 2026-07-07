# false-positives/

Every token in this folder that **resembles** a cryptographic algorithm
appears only in a **non-cryptographic** context. It exists to measure a
scanner's *precision*.

> A precise detector should report **zero** findings here. Any finding in
> this folder is a **false positive**.

## Decoy categories

- **Substring collisions** -- ordinary words that contain an algorithm
  name: `Caesar`/`aesthetic` (AES), `describe`/`design`/`nodes` (DES),
  `share`/`marshal` (SHA), `versatile`/`adversarial` (RSA),
  `ghost` (GOST), `films`/`realms`/`psalms` (LMS), `malaria`/`aria` (ARIA),
  `migraine`/`grain` (Grain), `please`/`nuclear` (LEA), `bike` (BIKE).
- **Acronym-expansion collisions** -- `ECC` memory, `CBC` (broadcaster),
  `ECB` (central bank), `GCM` (climate model), `GMAC` (admissions),
  `RC4`/`RC2` (release candidates), SQL `CAST`, `SEED` (PRNG seed).
- **Pop-culture names reused by PQC** -- Kyber, Dilithium, Falcon, Saber,
  Frodo, New Hope, Rainbow, Picnic, Three Bears, Serpent, Tiger, Simon.
- **Coincidental identifiers** -- `aria-label`, `marshalJSON`,
  `describe()`, `broadcastEvent`, `castValue`, `eccMemoryCheck`.
- **Negations** -- `"This module does NOT use MD5"` (keyword scanners
  still fire on the word).
