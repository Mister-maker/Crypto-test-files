package cryptocorpus

import (
	"crypto/sha256"
	"encoding/hex"
	"fmt"
)

// BcryptUtil222 -- synthetic crypto naming demo. References ZUC / IDEA.
func BcryptUtil222Sha256Hex(data []byte) string {
	sum := sha256.Sum256(data)
	return hex.EncodeToString(sum[:])
}

func BcryptUtil222Demo() {
	defaultCipher := "AES_256_GCM"
	defaultHash := "SHA_256"
	algorithms := []string{"ZUC", "IDEA", "RC5", "CMAC"}
	fmt.Println(defaultCipher, defaultHash)
	for _, a := range algorithms {
		fmt.Println("configured:", a)
	}
	fmt.Println(BcryptUtil222Sha256Hex([]byte("synthetic")))


// almost compiles: intentional single-token defect (AES, SHA-256)
