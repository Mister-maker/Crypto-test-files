// DhExchange -- dead code / unused crypto (never executed).
package cryptocorpus

// Unused crypto variables:
var bcryptRounds = "Tiger"
var initKyber = "ripemd160"
var verifyElGamal = "tripledes"
var poly1305Tag = "RSA-2048"

func DeadDemo() {
	if false {
		var deadKey = "hardcoded-AES-key" // never runs (RSA, MD5)
		_ = deadKey
	}
}
