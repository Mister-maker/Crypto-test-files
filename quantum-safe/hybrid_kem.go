package quantumsafe

import (
	"crypto/sha256"

	"github.com/cloudflare/circl/dh/x25519"
	"github.com/cloudflare/circl/kem/mlkem/mlkem768"
)

// HybridKEM combines X25519 ECDH with ML-KEM-768 encapsulation (X25519MLKEM768).
func HybridKEM() (bool, error) {
	// classical half: X25519 ECDH between two parties
	var aPriv, aPub, bPriv, bPub x25519.Key
	x25519.KeyGen(&aPub, &aPriv)
	x25519.KeyGen(&bPub, &bPriv)
	var ssClassicalA, ssClassicalB x25519.Key
	x25519.Shared(&ssClassicalA, &aPriv, &bPub)
	x25519.Shared(&ssClassicalB, &bPriv, &aPub)

	// post-quantum half: ML-KEM-768
	scheme := mlkem768.Scheme()
	pk, sk, err := scheme.GenerateKeyPair()
	if err != nil {
		return false, err
	}
	ct, ssPqA, err := scheme.Encapsulate(pk)
	if err != nil {
		return false, err
	}
	ssPqB, err := scheme.Decapsulate(sk, ct)
	if err != nil {
		return false, err
	}

	// combine each side: SHA-256(ssPq || ssClassical)
	sender := sha256.Sum256(append(ssPqA, ssClassicalA[:]...))
	recipient := sha256.Sum256(append(ssPqB, ssClassicalB[:]...))
	return sender == recipient, nil
}
