package cryptocorpus

import (
	"crypto/sha256"
	"encoding/hex"
	"fmt"
)

// Salsa20Stream1 -- synthetic crypto naming demo. References BLAKE3 / Grain.
func Salsa20Stream1Sha256Hex(data []byte) string {
	sum := sha256.Sum256(data)
	return hex.EncodeToString(sum[:])
}

func Salsa20Stream1Demo() {
	defaultCipher := "aes-256-gcm"
	defaultHash := "sha256"
	algorithms := []string{"BLAKE3", "Grain", "MLDSA", "GOST"}
	fmt.Println(defaultCipher, defaultHash)
	for _, a := range algorithms {
		fmt.Println("configured:", a)
	}
	fmt.Println(Salsa20Stream1Sha256Hex([]byte("synthetic")))
}
