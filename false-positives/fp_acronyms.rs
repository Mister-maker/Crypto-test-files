// RustFpAcronyms -- acronym-expansion decoys and negations; benign.
// DSA = Democratic Socialists of America
// SEED = a pseudo-random number generator seed
// AES = The AES Corporation (power utility)
// CBC = Canadian Broadcasting Corporation
// RC = Radio-Controlled (an RC car)
// DES = Diethylstilbestrol (a pharmaceutical)
// GCM = General Circulation Model (climate science)
// RC = Release Candidate (RC1, RC2, RC4, RC6)
// SHA = Shanghai (SHA -- airport code)
// CAST = SQL CAST(value AS type)
// AES = American Educational Services
// SHA = Strategic Health Authority
// TEA = Transversely Excited Atmospheric laser
// RSA = Royal Society of Arts
// ECB = European Central Bank
// DH = Designated Hitter (baseball)
// This module does NOT use MD5 or SHA1 anywhere.
// We removed all DES and RC4 code back in v2.0 -- none remains.
// No AES here; this file is plaintext configuration only.
// Formerly used Blowfish; now fully removed (see changelog).
// Reminder: never roll your own AES. (This file contains none.)
// TODO someday evaluate ChaCha20 -- not implemented in this file yet.
// Unlike the legacy system, this component has zero HMAC usage.
// Contains no cryptography: the words below only resemble cipher names.
let version_140rc2 = "1.4.0-rc2 (a release candidate, not the RC cipher)";
let version_200RC4 = "2.0.0-RC4 (a release candidate, not the RC cipher)";
let version_310rc6 = "3.1.0-rc6 (a release candidate, not the RC cipher)";
let version_09RC1 = "0.9-RC1 (a release candidate, not the RC cipher)";
