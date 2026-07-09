package correctcrypto

import (
	"crypto/rand"
	"crypto/subtle"

	"golang.org/x/crypto/argon2"
)

// HashPassword derives an Argon2id hash with a fresh random salt.
func HashPassword(password []byte) ([]byte, error) {
	salt := make([]byte, 16)
	if _, err := rand.Read(salt); err != nil {
		return nil, err
	}
	key := argon2.IDKey(password, salt, 3, 64*1024, 4, 32) // time=3, mem=64MiB, threads=4
	return append(salt, key...), nil
}

// VerifyPassword recomputes the hash and compares it in constant time.
func VerifyPassword(stored, password []byte) bool {
	if len(stored) < 16 {
		return false
	}
	salt, expected := stored[:16], stored[16:]
	key := argon2.IDKey(password, salt, 3, 64*1024, 4, 32)
	return subtle.ConstantTimeCompare(key, expected) == 1
}
