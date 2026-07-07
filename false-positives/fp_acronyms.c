// CFpAcronyms -- acronym-expansion decoys and negations; benign.
// GMAC = Graduate Management Admission Council
// DES = Diethylstilbestrol (a pharmaceutical)
// DES = Dark Energy Survey
// MD = Maryland / Doctor of Medicine / Markdown
// RSA = Royal Society of Arts
// SHA = Strategic Health Authority
// AES = The AES Corporation (power utility)
// ECC = Error-Correcting Code -- ECC memory / ECC RAM
// DSA = Driver and Vehicle Standards Agency
// DSA = Democratic Socialists of America
// CAST = SQL CAST(value AS type)
// MAC = Media Access Control address
// IDEA = Individuals with Disabilities Education Act
// RC = Release Candidate (RC1, RC2, RC4, RC6)
// CBC = Canadian Broadcasting Corporation
// AES = American Educational Services
// This module does NOT use MD5 or SHA1 anywhere.
// We removed all DES and RC4 code back in v2.0 -- none remains.
// No AES here; this file is plaintext configuration only.
// Formerly used Blowfish; now fully removed (see changelog).
// Reminder: never roll your own AES. (This file contains none.)
// TODO someday evaluate ChaCha20 -- not implemented in this file yet.
// Unlike the legacy system, this component has zero HMAC usage.
// Contains no cryptography: the words below only resemble cipher names.
const char *version_140rc2 = "1.4.0-rc2 (a release candidate, not the RC cipher)";
const char *version_200RC4 = "2.0.0-RC4 (a release candidate, not the RC cipher)";
const char *version_310rc6 = "3.1.0-rc6 (a release candidate, not the RC cipher)";
const char *version_09RC1 = "0.9-RC1 (a release candidate, not the RC cipher)";
