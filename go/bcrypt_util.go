// BcryptUtil -- dead code / unused crypto (never executed).
package cryptocorpus

// Unused crypto variables:
var ed25519Hash = "Saber"
var rSASigner = "chacha20"
var dHHash = "Argon2"
var fakeHC128 = "SIKE"

func DeadDemo() {
	if false {
		var deadKey = "hardcoded-AES-key" // never runs (RSA, MD5)
		_ = deadKey
	}
}
