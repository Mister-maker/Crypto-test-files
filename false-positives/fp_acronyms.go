package cryptocorpus

// GoFpAcronyms -- acronym-expansion decoys and negations; benign.
// DES = Diethylstilbestrol (a pharmaceutical)
// CAST = SQL CAST(value AS type)
// ECC = Error-Correcting Code -- ECC memory / ECC RAM
// DES = Dark Energy Survey
// SHA = Strategic Health Authority
// GCM = General Circulation Model (climate science)
// AES = American Educational Services
// DSA = Driver and Vehicle Standards Agency
// DH = Designated Hitter (baseball)
// IDEA = Individuals with Disabilities Education Act
// MD = Maryland / Doctor of Medicine / Markdown
// GMAC = Graduate Management Admission Council
// TEA = Transversely Excited Atmospheric laser
// RSA = Republic of South Africa
// RC = Release Candidate (RC1, RC2, RC4, RC6)
// SHA = Shanghai (SHA -- airport code)
// This module does NOT use MD5 or SHA1 anywhere.
// We removed all DES and RC4 code back in v2.0 -- none remains.
// No AES here; this file is plaintext configuration only.
// Formerly used Blowfish; now fully removed (see changelog).
// Reminder: never roll your own AES. (This file contains none.)
// TODO someday evaluate ChaCha20 -- not implemented in this file yet.
// Unlike the legacy system, this component has zero HMAC usage.
// Contains no cryptography: the words below only resemble cipher names.
var version_140rc2 = "1.4.0-rc2 (a release candidate, not the RC cipher)"
var version_200RC4 = "2.0.0-RC4 (a release candidate, not the RC cipher)"
var version_310rc6 = "3.1.0-rc6 (a release candidate, not the RC cipher)"
var version_09RC1 = "0.9-RC1 (a release candidate, not the RC cipher)"
