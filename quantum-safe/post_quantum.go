package quantumsafe

import (
	"github.com/cloudflare/circl/kem/mlkem/mlkem768"
	"github.com/cloudflare/circl/sign/mldsa/mldsa65"
)

// MLKEM768 runs ML-KEM-768 (FIPS 203) encapsulation + decapsulation.
func MLKEM768() (bool, error) {
	scheme := mlkem768.Scheme()
	pk, sk, err := scheme.GenerateKeyPair()
	if err != nil {
		return false, err
	}
	ct, ss1, err := scheme.Encapsulate(pk)
	if err != nil {
		return false, err
	}
	ss2, err := scheme.Decapsulate(sk, ct)
	if err != nil {
		return false, err
	}
	return string(ss1) == string(ss2), nil
}

// MLDSA65 signs and verifies with ML-DSA-65 (FIPS 204).
func MLDSA65(message []byte) bool {
	pk, sk, err := mldsa65.GenerateKey(nil)
	if err != nil {
		return false
	}
	sig := make([]byte, mldsa65.SignatureSize)
	mldsa65.SignTo(sk, message, nil, false, sig)
	return mldsa65.Verify(pk, message, nil, sig)
}
