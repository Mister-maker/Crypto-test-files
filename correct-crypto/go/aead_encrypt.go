package correctcrypto

import (
	"crypto/aes"
	"crypto/cipher"
	"crypto/rand"
	"io"
)

// EncryptAESGCM performs AES-256-GCM AEAD with a fresh random nonce (32-byte key).
func EncryptAESGCM(key, plaintext, aad []byte) ([]byte, error) {
	block, err := aes.NewCipher(key)
	if err != nil {
		return nil, err
	}
	gcm, err := cipher.NewGCM(block)
	if err != nil {
		return nil, err
	}
	nonce := make([]byte, gcm.NonceSize())
	if _, err := io.ReadFull(rand.Reader, nonce); err != nil { // unique per message
		return nil, err
	}
	// Seal appends ciphertext+tag onto the nonce prefix.
	return gcm.Seal(nonce, nonce, plaintext, aad), nil
}
