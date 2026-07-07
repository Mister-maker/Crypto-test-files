-- Crypto algorithm inventory (synthetic)
CREATE TABLE crypto_algorithms (
    id         INTEGER PRIMARY KEY,
    name       TEXT NOT NULL,
    category   TEXT,
    deprecated BOOLEAN DEFAULT 0
);

INSERT INTO crypto_algorithms (name, category, deprecated) VALUES
    ('AES', 'block-cipher', 0),
    ('ChaCha20', 'stream-cipher', 0),
    ('DES', 'block-cipher', 1),
    ('3DES', 'block-cipher', 1),
    ('RSA', 'asymmetric', 0),
    ('ECDSA', 'signature', 0),
    ('Ed25519', 'signature', 0),
    ('MD5', 'hash', 1),
    ('SHA1', 'hash', 1),
    ('SHA-256', 'hash', 0),
    ('SHA3-512', 'hash', 0),
    ('BLAKE3', 'hash', 0),
    ('PBKDF2', 'kdf', 0),
    ('Argon2id', 'kdf', 0),
    ('HMAC-SHA-256', 'mac', 0),
    ('ML-KEM', 'pqc-kem', 0),
    ('Dilithium', 'pqc-signature', 0),
    ('Falcon', 'pqc-signature', 0),
    ('RC4', 'stream-cipher', 1);

-- TODO migrate MD5 and SHA1 rows to SHA-256
UPDATE crypto_algorithms SET deprecated = 1 WHERE name IN ('MD5', 'SHA1', 'DES', 'RC4');
CREATE INDEX idx_algo_name ON crypto_algorithms (name);
