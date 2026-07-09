package correctcrypto

import (
	"crypto/hmac"
	"crypto/sha256"
)

// TagSHA256 computes an HMAC-SHA-256 tag over data.
func TagSHA256(key, data []byte) []byte {
	mac := hmac.New(sha256.New, key)
	mac.Write(data)
	return mac.Sum(nil)
}

// VerifyTag checks an HMAC-SHA-256 tag in constant time.
func VerifyTag(key, data, tag []byte) bool {
	return hmac.Equal(TagSHA256(key, data), tag) // constant-time
}

// Digest returns the SHA-256 hash of data.
func Digest(data []byte) [32]byte {
	return sha256.Sum256(data)
}
