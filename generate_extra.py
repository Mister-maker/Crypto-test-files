#!/usr/bin/env python3
"""
Additive corpus generator: three focused stress folders.

  quantum-vulnerable/  -- Shor-breakable classical public-key algorithms
  quantum-resistant/   -- post-quantum (PQC) algorithms
  false-positives/     -- lookalike / decoy content that a NAIVE keyword or
                          regex scanner will wrongly flag (precision benchmark)

Reuses the language primitives from generate_corpus.py. Purely additive: it
only creates the three new folders and never touches the existing corpus.

Usage:  python3 generate_extra.py
"""

import os
import sys
import json
import random

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import generate_corpus as g          # noqa: E402  (reuse primitives)

random.seed(424242)
HERE = os.path.dirname(os.path.abspath(__file__))
LANGS = g.LANG_DIR                    # dir -> internal lang key

# ==========================================================================
# Quantum-vulnerable (Shor-breakable) classical public-key algorithms
# ==========================================================================

QV = [
    "RSA", "RSA-512", "RSA-768", "RSA-1024", "RSA-2048", "RSA-3072", "RSA-4096",
    "RSA-8192", "RSA-PSS", "RSASSA-PSS", "RSASSA-PKCS1-v1_5", "RSAES-OAEP",
    "RSAES-PKCS1-v1_5", "RSA-OAEP-256", "textbook-RSA", "multi-prime-RSA",
    "Rabin", "Rabin-Williams",
    "DH", "DHE", "Diffie-Hellman", "Diffie-Hellman-Merkle", "MODP-1536",
    "MODP-2048", "MODP-3072", "MODP-4096", "MODP-6144", "MODP-8192", "ffdhe2048",
    "ffdhe3072", "ffdhe4096", "ffdhe6144", "ffdhe8192", "X9.42-DH", "static-DH",
    "ephemeral-DH", "Oakley-Group-14",
    "ECDH", "ECDHE", "ECDSA", "EdDSA", "Ed25519", "Ed25519ph", "Ed448", "ECIES",
    "ECMQV", "ECQV", "EC-Schnorr", "X25519", "X448",
    "secp192r1", "secp224r1", "secp256r1", "secp384r1", "secp521r1", "secp256k1",
    "prime256v1", "brainpoolP256r1", "brainpoolP384r1", "brainpoolP512r1",
    "Curve25519", "Curve448", "P-256", "P-384", "P-521", "NIST-P256",
    "sect283k1", "sect571r1",
    "DSA", "DSA-1024", "DSA-2048", "DSA-3072", "ElGamal", "ElGamal-signature",
    "Schnorr", "Schnorr-signature", "GOST-R-34.10-2012", "ECGDSA", "ECKCDSA",
    "KCDSA", "DSTU-4145", "EC-GOST",
    "Paillier", "Cramer-Shoup", "Goldwasser-Micali", "Benaloh", "Naccache-Stern",
    "Damgard-Jurik", "Okamoto-Uchiyama", "BLS", "BLS12-381", "BN254",
    "pairing-based", "Boneh-Franklin-IBE", "Boneh-Lynn-Shacham",
]

# ==========================================================================
# Quantum-resistant / post-quantum (PQC)
# ==========================================================================

QR = [
    "ML-KEM", "ML-KEM-512", "ML-KEM-768", "ML-KEM-1024", "FIPS-203", "Kyber",
    "Kyber512", "Kyber768", "Kyber1024", "CRYSTALS-Kyber",
    "ML-DSA", "ML-DSA-44", "ML-DSA-65", "ML-DSA-87", "FIPS-204", "Dilithium",
    "Dilithium2", "Dilithium3", "Dilithium5", "CRYSTALS-Dilithium",
    "Falcon", "Falcon-512", "Falcon-1024", "FN-DSA", "FIPS-206",
    "SLH-DSA", "FIPS-205", "SPHINCS+", "SPHINCS+-SHA2-128s", "SPHINCS+-SHA2-128f",
    "SPHINCS+-SHA2-192s", "SPHINCS+-SHA2-256s", "SPHINCS+-SHAKE-128s",
    "SPHINCS+-SHAKE-256f", "SPHINCS-plus", "Gravity-SPHINCS",
    "XMSS", "XMSS-MT", "XMSSMT", "LMS", "HSS", "LM-OTS", "WOTS", "WOTS+",
    "Merkle-signature",
    "Classic-McEliece", "mceliece348864", "mceliece348864f", "mceliece460896",
    "mceliece6688128", "mceliece6960119", "mceliece8192128", "BIKE", "BIKE-L1",
    "BIKE-L3", "BIKE-L5", "HQC", "HQC-128", "HQC-192", "HQC-256", "LEDAcrypt",
    "ROLLO", "RQC",
    "NTRU", "NTRU-HPS", "NTRU-HRSS", "NTRU-HPS-2048-509", "NTRU-HPS-2048-677",
    "NTRU-HPS-4096-821", "NTRU-HRSS-701", "NTRU-Prime", "Streamlined-NTRU-Prime",
    "sntrup761", "sntrup857", "ntrulpr761", "NTRU-LPRime",
    "Saber", "LightSaber", "FireSaber", "FrodoKEM", "FrodoKEM-640-AES",
    "FrodoKEM-976-SHAKE", "FrodoKEM-1344-AES", "NewHope", "NewHope-512",
    "NewHope-1024", "ThreeBears", "BabyBear", "MamaBear", "PapaBear", "Round5",
    "LAC", "Titanium",
    "Rainbow", "GeMSS", "LUOV", "MQDSS", "UOV", "HFE", "Oil-and-Vinegar",
    "Picnic", "Picnic3", "qTESLA", "BLISS", "GLP",
    "SIKE", "SIDH", "SIKEp434", "SIKEp503", "SIKEp751", "CSIDH", "B-SIDH",
    "X25519MLKEM768", "X25519Kyber768", "SecP256r1MLKEM768", "P256-Kyber512",
    "hybrid-KEM", "post-quantum", "quantum-safe", "quantum-resistant", "PQC",
    "NIST-PQC", "Shor-resistant", "Grover-resistant",
]

# ==========================================================================
# False-positive banks
# ==========================================================================

# English words / names that merely CONTAIN an algorithm name as a substring.
SUBSTRING_TRAPS = {
    "AES": ["Caesar", "aesthetic", "aesthetics", "aesthete", "anaesthesia", "maestro", "paesano"],
    "DES": ["describe", "design", "designer", "destiny", "destination", "desktop",
            "dessert", "desert", "despite", "nodes", "modes", "codes", "besides", "Andes", "Mercedes"],
    "SHA": ["share", "shared", "shall", "shallow", "shard", "sharp", "shark",
            "marshal", "marshalling", "marshmallow", "Sasha", "Shanghai", "Ashanti"],
    "RSA": ["versatile", "adversarial", "universal", "conversation", "rehearsal",
            "reversal", "traversal", "dorsal", "hearsay", "Marsala"],
    "DH": ["childhood", "Gandhi", "Buddha", "handheld", "roadhouse", "bloodhound", "headhunter"],
    "TEA": ["team", "teach", "teacher", "teapot", "steam", "steady", "instead", "plateau", "teaspoon"],
    "IDEA": ["idea", "ideal", "ideas", "ideate", "idealism", "ideally"],
    "SEED": ["seed", "seeds", "seedling", "aniseed", "linseed", "reseed", "seedy"],
    "GOST": ["ghost", "ghosts", "ghostly", "ghosting", "ghostwriter"],
    "SIMON": ["Simon", "Simone", "Simon-says", "Simonson"],
    "SPECK": ["speck", "speckle", "speckled", "specks", "bespeckled"],
    "Grain": ["grain", "grains", "migraine", "ingrained", "grainy", "wholegrain"],
    "Rabbit": ["rabbit", "rabbits", "jackrabbit", "rabbit-hole"],
    "Serpent": ["serpent", "serpents", "serpentine"],
    "Camellia": ["camellia", "camellias"],
    "Falcon": ["falcon", "falcons", "falconry", "falconer", "gyrfalcon"],
    "Tiger": ["tiger", "tigers", "Tigris", "tiger-lily"],
    "Whirlpool": ["whirlpool", "whirlpools"],
    "Saber": ["saber", "sabers", "saber-tooth", "lightsaber", "sabermetrics"],
    "Salsa": ["salsa", "salsa-verde"],
    "MARS": ["Mars", "Marshall", "marsh", "marshy", "marsupial", "Marseille"],
    "LEA": ["please", "release", "pleasure", "clean", "gleam", "nuclear", "leather", "leader", "leaf"],
    "ARIA": ["aria", "Maria", "malaria", "Bavaria", "Ariana"],
    "LMS": ["films", "elms", "realms", "helms", "psalms", "qualms", "alms", "overwhelms"],
    "BIKE": ["bike", "bikes", "biker", "motorbike", "bike-shed"],
}

# Acronyms that expand to something entirely non-cryptographic.
ACRONYMS = [
    ("ECC", "Error-Correcting Code -- ECC memory / ECC RAM"),
    ("CBC", "Canadian Broadcasting Corporation"),
    ("ECB", "European Central Bank"),
    ("GCM", "General Circulation Model (climate science)"),
    ("GMAC", "Graduate Management Admission Council"),
    ("RSA", "Republic of South Africa"),
    ("RSA", "Royal Society of Arts"),
    ("DSA", "Democratic Socialists of America"),
    ("DSA", "Driver and Vehicle Standards Agency"),
    ("DH", "Designated Hitter (baseball)"),
    ("AES", "The AES Corporation (power utility)"),
    ("AES", "American Educational Services"),
    ("DES", "Diethylstilbestrol (a pharmaceutical)"),
    ("DES", "Dark Energy Survey"),
    ("SHA", "Strategic Health Authority"),
    ("SHA", "Shanghai (SHA -- airport code)"),
    ("MD", "Maryland / Doctor of Medicine / Markdown"),
    ("IDEA", "Individuals with Disabilities Education Act"),
    ("MAC", "Media Access Control address"),
    ("RC", "Release Candidate (RC1, RC2, RC4, RC6)"),
    ("RC", "Radio-Controlled (an RC car)"),
    ("CAST", "SQL CAST(value AS type)"),
    ("SEED", "a pseudo-random number generator seed"),
    ("TEA", "Transversely Excited Atmospheric laser"),
]

# PQC / cipher names that are borrowed from pop culture and common words.
POP = [
    ("Kyber", "Star Wars -- kyber crystals power lightsabers"),
    ("Dilithium", "Star Trek -- dilithium crystals regulate the warp core"),
    ("Falcon", "the Millennium Falcon / a peregrine falcon / Atlanta Falcons"),
    ("Saber", "a lightsaber, a cavalry saber, or Saber from Fate/stay night"),
    ("Frodo", "Frodo Baggins carries the Ring to Mordor"),
    ("NewHope", "Star Wars Episode IV: A New Hope"),
    ("Rainbow", "Reading Rainbow / Rainbow Dash / a double rainbow"),
    ("Picnic", "a teddy bears' picnic in the park"),
    ("ThreeBears", "Goldilocks and the Three Bears -- Baby, Mama, Papa Bear"),
    ("Serpent", "the serpent in the garden / Serpentor from G.I. Joe"),
    ("Tiger", "Tony the Tiger / Tiger Woods / Year of the Tiger"),
    ("Simon", "Simon says / Simon & Garfunkel / Simon Cowell"),
    ("Trivium", "the metal band Trivium / trivia night"),
    ("Grain", "a grain of rice / going against the grain"),
    ("Rabbit", "the White Rabbit / Roger Rabbit / a rabbit's foot"),
    ("Salsa", "salsa dancing / a jar of tomato salsa"),
    ("ChaCha", "the cha-cha-cha ballroom dance"),
    ("Camellia", "a blooming camellia flower"),
    ("Whirlpool", "a Whirlpool washing machine / a whirlpool in the sea"),
    ("Mars", "the planet Mars / a Mars bar / Bruno Mars"),
    ("Blowfish", "Hootie & the Blowfish / a spiky pufferfish"),
]

# Ordinary code identifiers that happen to contain an algorithm substring.
COINCIDENTAL = [
    "describeBlock", "describeTest", "nodesById", "modeSelector", "besideText",
    "marshalJSON", "unmarshalPayload", "marshallingQueue", "sharedState",
    "sharePrice", "shallowCopy", "shardIndex", "versatileParser",
    "adversarialSample", "universalLink", "conversationThread", "traversalOrder",
    "dorsalFin", "childhoodMemory", "handheldDevice", "teamRoster", "steamPipe",
    "steadyState", "insteadOf", "plateauDetector", "ideaBoard", "idealValue",
    "seedDatabase", "seedlingTray", "reseedCache", "ghostElement",
    "speckleNoise", "migraineTracker", "grainSize", "rabbitHole",
    "serpentinePath", "falconLauncher", "tigerStripes", "whirlpoolMixer",
    "saberMetricsReport", "lightsaberDuel", "salsaRecipe", "marshLand",
    "marsRover", "pleaseWait", "releaseCandidate", "cleanBuffer", "leaderElection",
    "ariaLabel", "ariaDescribedBy", "malariaMap", "filmsList", "realmsRegistry",
    "psalmsChapter", "bikeShedColor", "picnicBasket", "trivialCase",
    "castValue", "broadcastEvent", "forecastModel", "typecastHelper",
    "podcastFeed", "eccMemoryCheck", "ecbInterestRate", "gcmClimateGrid",
    "designSystem", "destinyPath", "desktopIcon", "dessertMenu",
]

NEGATIONS = [
    "This module does NOT use MD5 or SHA1 anywhere.",
    "We removed all DES and RC4 code back in v2.0 -- none remains.",
    "No AES here; this file is plaintext configuration only.",
    "Formerly used Blowfish; now fully removed (see changelog).",
    "Reminder: never roll your own AES. (This file contains none.)",
    "TODO someday evaluate ChaCha20 -- not implemented in this file yet.",
    "Unlike the legacy system, this component has zero HMAC usage.",
    "Contains no cryptography: the words below only resemble cipher names.",
]

INNOCENT_VALUES = [
    "salad topping", "memory module", "TV schedule", "garden plant", "dance move",
    "movie night", "sports roster", "release build", "climate grid",
    "admission score", "flower bed", "river bank", "washing machine",
    "teddy bears picnic", "trivia night", "coffee break", "walking trail",
]


# ==========================================================================
# Emitters
# ==========================================================================

def clean(s):
    return s.replace('"', "").replace("'", "")


def q(s):
    return '"' + clean(s) + '"'


def write(path, content):
    with open(path, "w", encoding="utf-8") as f:
        f.write(content)


def fname(lang, stem, cls):
    ext = g.EXT[lang]
    if lang in ("java", "csharp", "cpp"):
        return cls + "." + ext
    if lang in ("js", "ts"):
        return g.camel(stem) + "." + ext
    return g.snake(stem) + "." + ext


def algo_source(lang, cls, algos, banner, tag):
    body = [g.line_comment(lang, banner)]
    for i, a in enumerate(random.sample(algos, min(14, len(algos)))):
        body.append(g.const_decl(lang, "ALG_" + g.safe(a).upper()[:26] + "_" + str(i), a))
    for a in random.sample(algos, min(6, len(algos))):
        body.append(g.line_comment(lang, tag.format(a=a)))
    body.append(g.var_decl(lang, "enabledAlgorithms",
                           g.list_lit(lang, random.sample(algos, min(8, len(algos))))))
    return "\n".join(g.finish(lang, cls, body)) + "\n"


def fp_substrings(lang, cls):
    body = [g.line_comment(lang, cls + " -- substring/lookalike decoys; NO cryptography here.")]
    words = [w for lst in SUBSTRING_TRAPS.values() for w in lst]
    for _ in range(random.randint(14, 20)):
        w = random.sample(words, 4)
        body.append(g.line_comment(lang, "The {} vendor praised the {}, the {} and the {}.".format(*w)))
    for name, ctx in random.sample(POP, min(10, len(POP))):
        body.append(g.line_comment(lang, name + ": " + ctx))
    body.append(g.var_decl(lang, "menuItems",
                           g.list_lit(lang, [clean(w) for w in random.sample(words, 8)])))
    return "\n".join(g.finish(lang, cls, body)) + "\n"


def fp_identifiers(lang, cls):
    body = [g.line_comment(lang, cls + " -- coincidental identifiers that resemble crypto; all benign.")]
    for name in random.sample(COINCIDENTAL, min(18, len(COINCIDENTAL))):
        body.append(g.var_decl(lang, name, q(random.choice(INNOCENT_VALUES))))
    body.append(g.line_comment(lang, "aria-label, marshalJSON, describe(), broadcast(), CAST(): none are crypto."))
    return "\n".join(g.finish(lang, cls, body)) + "\n"


def fp_acronyms(lang, cls):
    body = [g.line_comment(lang, cls + " -- acronym-expansion decoys and negations; benign.")]
    for ac, exp in random.sample(ACRONYMS, min(16, len(ACRONYMS))):
        body.append(g.line_comment(lang, ac + " = " + exp))
    for n in NEGATIONS:
        body.append(g.line_comment(lang, n))
    for v in ["1.4.0-rc2", "2.0.0-RC4", "3.1.0-rc6", "0.9-RC1"]:
        body.append(g.var_decl(lang, "version_" + g.safe(v), q(v + " (a release candidate, not the RC cipher)")))
    return "\n".join(g.finish(lang, cls, body)) + "\n"


# ==========================================================================
# Data / prose files
# ==========================================================================

def qv_json():
    return json.dumps({"quantumVulnerable": {
        "note": "Shor-breakable public-key primitives; migrate to PQC.",
        "keyExchange": ["DH", "ECDH", "ECDHE", "X25519", "X448", "ffdhe3072"],
        "signatures": ["RSA", "RSA-PSS", "DSA", "ECDSA", "EdDSA", "Ed25519",
                       "Ed448", "ElGamal", "Schnorr", "GOST-R-34.10-2012", "BLS12-381"],
        "encryption": ["RSA-OAEP", "RSAES-PKCS1-v1_5", "ElGamal", "Paillier", "ECIES"],
        "curves": ["P-256", "P-384", "P-521", "secp256k1", "brainpoolP256r1",
                   "Curve25519", "Curve448"],
        "rsaKeySizes": [512, 1024, 2048, 3072, 4096, 8192],
    }}, indent=2) + "\n"


def qr_json():
    return json.dumps({"quantumResistant": {
        "note": "Post-quantum (PQC) primitives.",
        "kem": ["ML-KEM-512", "ML-KEM-768", "ML-KEM-1024", "Kyber768",
                "FrodoKEM-976-SHAKE", "Classic-McEliece", "BIKE-L3", "HQC-192",
                "NTRU-HRSS-701", "sntrup761"],
        "signatures": ["ML-DSA-44", "ML-DSA-65", "ML-DSA-87", "Dilithium3",
                       "Falcon-512", "Falcon-1024", "SLH-DSA", "SPHINCS+-SHA2-128s",
                       "XMSS", "LMS", "Rainbow", "Picnic"],
        "hybrid": ["X25519MLKEM768", "X25519Kyber768", "SecP256r1MLKEM768"],
        "standards": ["FIPS-203", "FIPS-204", "FIPS-205", "FIPS-206"],
    }}, indent=2) + "\n"


def qv_yaml():
    return ("# Quantum-vulnerable (Shor-breakable) inventory\n"
            "quantum_vulnerable:\n"
            "  key_exchange: [DH, ECDH, ECDHE, X25519, X448]\n"
            "  signatures: [RSA, RSA-PSS, DSA, ECDSA, Ed25519, Ed448, ElGamal, Schnorr]\n"
            "  encryption: [RSA-OAEP, ElGamal, Paillier, ECIES]\n"
            "  curves: [P-256, P-384, P-521, secp256k1, brainpoolP256r1, Curve25519]\n"
            "  rsa_key_sizes: [1024, 2048, 3072, 4096, 8192]\n"
            "  migrate_to: [ML-KEM-768, ML-DSA-65, SLH-DSA]\n")


def qr_yaml():
    return ("# Quantum-resistant (PQC) inventory\n"
            "quantum_resistant:\n"
            "  kem: [ML-KEM-512, ML-KEM-768, ML-KEM-1024, Kyber768, FrodoKEM, BIKE, HQC, NTRU, Saber]\n"
            "  signatures: [ML-DSA-65, Dilithium3, Falcon-512, SLH-DSA, SPHINCS+, XMSS, LMS, Rainbow, Picnic]\n"
            "  code_based: [Classic-McEliece, mceliece6688128, BIKE-L3, HQC-192]\n"
            "  hybrid: [X25519MLKEM768, X25519Kyber768]\n"
            "  standards: [FIPS-203, FIPS-204, FIPS-205]\n")


def qv_readme():
    return ("# quantum-vulnerable/\n\n"
            "Classical public-key algorithms broken by a large-scale quantum computer\n"
            "via **Shor's algorithm**: RSA (all key sizes and paddings), finite-field\n"
            "Diffie-Hellman (DH/DHE/MODP/ffdhe), elliptic-curve schemes (ECDH, ECDSA,\n"
            "EdDSA/Ed25519/Ed448, ECIES, X25519/X448 and named curves), DSA, ElGamal,\n"
            "Schnorr, GOST signatures, and pairing/factoring schemes (BLS, Paillier,\n"
            "Rabin, Cramer-Shoup).\n\n"
            "These should all be flagged as **quantum-vulnerable / harvest-now-decrypt-later**.\n")


def qr_readme():
    return ("# quantum-resistant/\n\n"
            "Post-quantum (PQC) algorithms. Lattice KEMs (ML-KEM/Kyber, FrodoKEM,\n"
            "NTRU, Saber), lattice signatures (ML-DSA/Dilithium, Falcon), hash-based\n"
            "signatures (SLH-DSA/SPHINCS+, XMSS, LMS), code-based (Classic McEliece,\n"
            "BIKE, HQC), multivariate (Rainbow, GeMSS, UOV), isogeny (SIKE/SIDH/CSIDH),\n"
            "and hybrid suites (X25519MLKEM768). Includes NIST FIPS 203/204/205 names.\n")


def qr_migration_md():
    return ("# PQC Migration Notes (synthetic)\n\n"
            "**Harvest now, decrypt later**: adversaries can record RSA/ECDH-protected\n"
            "traffic today and decrypt it once a cryptographically-relevant quantum\n"
            "computer exists.\n\n"
            "| Legacy (quantum-vulnerable) | Replace with (PQC) |\n"
            "|---|---|\n"
            "| RSA-2048 / RSA-4096 key transport | ML-KEM-768 (Kyber) |\n"
            "| ECDH / X25519 key agreement | X25519MLKEM768 hybrid |\n"
            "| RSA-PSS / ECDSA / Ed25519 signatures | ML-DSA-65 or SLH-DSA |\n"
            "| Long-lived firmware signing | LMS / XMSS (stateful hash-based) |\n\n"
            "TODO: inventory all RSA, DH, ECDH, ECDSA, EdDSA usage and stage the\n"
            "migration to ML-KEM, ML-DSA, Falcon and SLH-DSA (FIPS 203/204/205).\n")


def fp_readme():
    return ("# false-positives/\n\n"
            "Every token in this folder that **resembles** a cryptographic algorithm\n"
            "appears only in a **non-cryptographic** context. It exists to measure a\n"
            "scanner's *precision*.\n\n"
            "> A precise detector should report **zero** findings here. Any finding in\n"
            "> this folder is a **false positive**.\n\n"
            "## Decoy categories\n\n"
            "- **Substring collisions** -- ordinary words that contain an algorithm\n"
            "  name: `Caesar`/`aesthetic` (AES), `describe`/`design`/`nodes` (DES),\n"
            "  `share`/`marshal` (SHA), `versatile`/`adversarial` (RSA),\n"
            "  `ghost` (GOST), `films`/`realms`/`psalms` (LMS), `malaria`/`aria` (ARIA),\n"
            "  `migraine`/`grain` (Grain), `please`/`nuclear` (LEA), `bike` (BIKE).\n"
            "- **Acronym-expansion collisions** -- `ECC` memory, `CBC` (broadcaster),\n"
            "  `ECB` (central bank), `GCM` (climate model), `GMAC` (admissions),\n"
            "  `RC4`/`RC2` (release candidates), SQL `CAST`, `SEED` (PRNG seed).\n"
            "- **Pop-culture names reused by PQC** -- Kyber, Dilithium, Falcon, Saber,\n"
            "  Frodo, New Hope, Rainbow, Picnic, Three Bears, Serpent, Tiger, Simon.\n"
            "- **Coincidental identifiers** -- `aria-label`, `marshalJSON`,\n"
            "  `describe()`, `broadcastEvent`, `castValue`, `eccMemoryCheck`.\n"
            "- **Negations** -- `\"This module does NOT use MD5\"` (keyword scanners\n"
            "  still fire on the word).\n")


def fp_prose_md():
    return ("# A Perfectly Ordinary Afternoon (contains no cryptography)\n\n"
            "In a quiet garden of camellia blooms and serpentine hedges, Simon brewed a\n"
            "pot of tea and had a brilliant idea. A falcon circled overhead while a\n"
            "rabbit nibbled a grain of wheat beside the whirlpool fountain. He admired\n"
            "the aesthetic of a Caesar salad, hummed a salsa tune, and watched a ghost\n"
            "of mist rise over the Andes.\n\n"
            "His designated hitter days behind him, Simon now studies malaria maps in\n"
            "Bavaria, files old films of psalms under \"realms\", and rides his bike past\n"
            "the marsh to a teddy bears' picnic. Frodo the beagle chased a rainbow while\n"
            "the local ECB (the European Central Bank) aired a forecast on CBC.\n\n"
            "None of this is cryptography. Every capitalized word that resembles a\n"
            "cipher -- Simon, Falcon, Serpent, Tiger, Rainbow, Picnic, Saber, Kyber,\n"
            "Dilithium -- is just a name, a plant, a pet, or a movie reference.\n")


def fp_story_txt():
    return ("RELEASE PARTY, TAKE FOUR\n\n"
            "We shipped 2.0.0-rc4 on Friday. (Yes, RC4 -- release candidate four, not\n"
            "the cipher.) The ECC memory in the build server finally passed its test,\n"
            "the CAST(price AS money) report ran clean, and marketing broadcast the\n"
            "news on three podcasts.\n\n"
            "Maria brought salsa. Simon brought trivia. Someone queued a New Hope\n"
            "marathon and argued about whether a lightsaber saber counts as a real\n"
            "saber. Frodo (the office cat) knocked a camellia off the shelf. The DH --\n"
            "our softball team's designated hitter -- ate all the dessert.\n\n"
            "Nothing here is encrypted. It only reads like a keyword scanner's worst day.\n")


def fp_release_notes_md():
    return ("# Release Notes\n\n"
            "## v3.1.0-RC6\n"
            "- Fixed an **ECC memory** parity error on the build host.\n"
            "- `CAST(...)` in the analytics query now targets DECIMAL.\n"
            "- Added `aria-label` / `aria-describedby` to all dialogs.\n"
            "- Renamed `marshalJSON` -> `unmarshalPayload` in the codec.\n\n"
            "## v2.0.0-RC4\n"
            "- Broadcast (CBC) integration for the newsroom widget.\n"
            "- `describe()` test coverage raised to 92%.\n"
            "- Note: this project ships **no cryptography**; the tokens above are benign.\n")


def fp_decoys_json():
    return json.dumps({
        "ariaLabel": "Close dialog",
        "cssClasses": ["tiger", "falcon", "serpent", "salsa", "camellia"],
        "release": {"channel": "rc4", "version": "3.1.0-RC6", "note": "release candidate"},
        "hardware": {"memory": "ECC", "note": "error-correcting-code RAM"},
        "broadcast": {"network": "CBC", "bank": "ECB", "model": "GCM"},
        "pets": ["Simon", "Frodo", "Kyber", "Dilithium", "Rainbow", "Picnic", "Saber"],
        "note": "All values are benign lookalikes; zero cryptography.",
    }, indent=2) + "\n"


def fp_decoys_yaml():
    return ("# Benign app config -- lookalike tokens only, no crypto.\n"
            "ui:\n"
            "  ariaLabel: \"Share menu\"      # aria-* attributes contain 'ARIA'\n"
            "  theme: camellia\n"
            "  cssClasses: [tiger, serpent, salsa, falcon]\n"
            "release:\n"
            "  channel: rc4                 # release candidate 4, NOT the RC4 cipher\n"
            "  version: 2.0.0-RC2\n"
            "hardware:\n"
            "  memory: ECC                  # error-correcting-code RAM\n"
            "media:\n"
            "  network: CBC                 # Canadian Broadcasting Corporation\n"
            "pets: [Simon, Frodo, Kyber, Rainbow, Picnic, Saber]\n")


def fp_decoys_xml():
    return ('<?xml version="1.0" encoding="UTF-8"?>\n'
            '<ui>\n'
            '  <button aria-label="Share" class="falcon" data-mode="broadcast"/>\n'
            '  <panel class="camellia serpent" aria-describedby="tea-tooltip"/>\n'
            '  <release channel="rc4" version="2.0.0-RC6"/>\n'
            '  <hardware memory="ECC"/>\n'
            '  <list>\n'
            '    <item>Simon</item><item>Rainbow</item><item>Picnic</item><item>Saber</item>\n'
            '  </list>\n'
            '  <!-- ECB = European Central Bank; CBC = Canadian Broadcasting Corporation -->\n'
            '</ui>\n')


def fp_data_csv():
    return ("name,category,notes\n"
            "Simon,pet,a tabby cat named after Simon says\n"
            "Falcon,bird,a peregrine falcon at the sanctuary\n"
            "Tiger,pet,orange tabby; Year of the Tiger\n"
            "Rainbow,color,double rainbow after the storm\n"
            "Picnic,event,teddy bears picnic in the park\n"
            "Saber,toy,plastic lightsaber from the fair\n"
            "Frodo,dog,a hobbit-footed beagle\n"
            "Kyber,mineral,glowing crystal prop from the convention\n"
            "Salsa,food,jar of medium tomato salsa\n"
            "Serpent,ride,the Serpent roller coaster\n"
            "Camellia,plant,a potted camellia in the lobby\n")


def fp_queries_sql():
    return ("-- Benign analytics; CAST/BROADCAST are SQL, not the CAST5/CAST6 ciphers.\n"
            "SELECT CAST(price AS DECIMAL(10,2)) AS amount FROM orders;      -- type conversion\n"
            "SELECT /*+ BROADCAST(t) */ * FROM sales s JOIN teams t ON s.tid = t.id;\n"
            "CREATE TABLE seeds (id INT, grain TEXT, rabbit_count INT);      -- garden inventory\n"
            "INSERT INTO seeds VALUES (1, 'wheat grain', 4), (2, 'aniseed', 2);\n"
            "SELECT name FROM pets WHERE name IN ('Simon','Falcon','Tiger','Frodo','Kyber');\n"
            "-- The ECB aired the forecast; the ECC memory module passed its test.\n")


def fp_aria_html():
    return ('<!DOCTYPE html>\n<html lang="en">\n<head>\n'
            '  <meta charset="utf-8">\n  <title>Accessible Widget (no crypto)</title>\n'
            '  <style>.falcon{}.serpent{}.camellia{}.salsa{}.tiger{}</style>\n'
            '</head>\n<body>\n'
            '  <nav aria-label="Primary">\n'
            '    <button aria-label="Share" class="falcon">Share</button>\n'
            '    <button aria-label="Broadcast" class="serpent">Broadcast</button>\n'
            '  </nav>\n'
            '  <section aria-describedby="tea" class="camellia">\n'
            '    <!-- aria-* attributes literally contain "ARIA"; rc4 below = release candidate -->\n'
            '    <p>Version 2.0.0-rc4 -- Simon, Frodo and Rainbow tested it over tea.</p>\n'
            '  </section>\n'
            '</body>\n</html>\n')


# ==========================================================================
# Main
# ==========================================================================

def main():
    total = 0

    # --- quantum-vulnerable ---
    qv_dir = os.path.join(HERE, "quantum-vulnerable")
    os.makedirs(qv_dir, exist_ok=True)
    for d, lang in LANGS.items():
        cls = g.pascal(d) + "Vulnerable"
        write(os.path.join(qv_dir, fname(lang, "quantum_vulnerable", cls)),
              algo_source(lang, cls, QV,
                          "Quantum-vulnerable (Shor-breakable) public-key algorithms",
                          "TODO migrate {a} to a post-quantum scheme (harvest-now-decrypt-later)"))
        total += 1
    for fn, ct in [("quantum_vulnerable_inventory.json", qv_json()),
                   ("quantum_vulnerable.yaml", qv_yaml()),
                   ("README.md", qv_readme())]:
        write(os.path.join(qv_dir, fn), ct)
        total += 1

    # --- quantum-resistant ---
    qr_dir = os.path.join(HERE, "quantum-resistant")
    os.makedirs(qr_dir, exist_ok=True)
    for d, lang in LANGS.items():
        cls = g.pascal(d) + "Resistant"
        write(os.path.join(qr_dir, fname(lang, "quantum_resistant", cls)),
              algo_source(lang, cls, QR,
                          "Quantum-resistant / post-quantum (PQC) algorithms",
                          "{a} is a NIST PQC candidate/standard"))
        total += 1
    for fn, ct in [("quantum_resistant_inventory.json", qr_json()),
                   ("quantum_resistant.yaml", qr_yaml()),
                   ("MIGRATION.md", qr_migration_md()),
                   ("README.md", qr_readme())]:
        write(os.path.join(qr_dir, fn), ct)
        total += 1

    # --- false-positives ---
    fp_dir = os.path.join(HERE, "false-positives")
    os.makedirs(fp_dir, exist_ok=True)
    themes = [("fp_substrings", fp_substrings), ("fp_identifiers", fp_identifiers),
              ("fp_acronyms", fp_acronyms)]
    for d, lang in LANGS.items():
        for stem, fn_builder in themes:
            cls = g.pascal(d) + g.pascal(stem)
            write(os.path.join(fp_dir, fname(lang, stem, cls)), fn_builder(lang, cls))
            total += 1
    for fn, ct in [("README.md", fp_readme()),
                   ("ordinary_afternoon.md", fp_prose_md()),
                   ("release_party.txt", fp_story_txt()),
                   ("RELEASE_NOTES.md", fp_release_notes_md()),
                   ("app_config.json", fp_decoys_json()),
                   ("app_config.yaml", fp_decoys_yaml()),
                   ("ui_layout.xml", fp_decoys_xml()),
                   ("pets.csv", fp_data_csv()),
                   ("analytics_queries.sql", fp_queries_sql()),
                   ("accessible_widget.html", fp_aria_html())]:
        write(os.path.join(fp_dir, fn), ct)
        total += 1

    print("Extra stress folders generated under:", HERE)
    for name in ("quantum-vulnerable", "quantum-resistant", "false-positives"):
        n = len(os.listdir(os.path.join(HERE, name)))
        print("  %-20s %3d files" % (name + "/", n))
    print("  %-20s %3d files added" % ("TOTAL", total))


if __name__ == "__main__":
    main()
