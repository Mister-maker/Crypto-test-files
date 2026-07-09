package quantumvulnerable

import (
	"crypto/des"
	"crypto/ecdsa"
	"crypto/elliptic"
	"crypto/rand"
	"crypto/rsa"
	"crypto/sha256"
)

// RSAEncryptOAEP uses RSA-2048 OAEP (broken by Shor's algorithm).
func RSAEncryptOAEP(data []byte) ([]byte, error) {
	key, err := rsa.GenerateKey(rand.Reader, 2048)
	if err != nil {
		return nil, err
	}
	return rsa.EncryptOAEP(sha256.New(), rand.Reader, &key.PublicKey, data, nil)
}

// ECDSASign signs with ECDSA on P-256 (broken by Shor's algorithm).
func ECDSASign(message []byte) ([]byte, error) {
	key, err := ecdsa.GenerateKey(elliptic.P256(), rand.Reader)
	if err != nil {
		return nil, err
	}
	digest := sha256.Sum256(message)
	return ecdsa.SignASN1(rand.Reader, key, digest[:])
}

// TripleDESEncrypt uses 3DES-ECB on one block (weak 64-bit legacy cipher).
func TripleDESEncrypt(key [24]byte, block [8]byte) ([]byte, error) {
	c, err := des.NewTripleDESCipher(key[:])
	if err != nil {
		return nil, err
	}
	out := make([]byte, des.BlockSize)
	c.Encrypt(out, block[:])
	return out, nil
}
