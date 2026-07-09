package correctcrypto

import (
	"crypto/ed25519"
	"crypto/rand"
)

// SignAndVerify demonstrates correct Ed25519 signing and verification.
func SignAndVerify(message []byte) (bool, error) {
	public, private, err := ed25519.GenerateKey(rand.Reader)
	if err != nil {
		return false, err
	}
	signature := ed25519.Sign(private, message)
	return ed25519.Verify(public, message, signature), nil
}
