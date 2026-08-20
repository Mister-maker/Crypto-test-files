// Command verify_artifacts is a CI/CD step that verifies release artifacts:
// it checks the Ed25519 signature over the SHA-256 checksum manifest before a
// deploy is allowed to proceed. Keys/secrets come from the CI environment.
package main

import (
	"crypto/ed25519"
	"crypto/sha256"
	"encoding/base64"
	"encoding/hex"
	"fmt"
	"os"
)

// verifyManifest checks the Ed25519 signature over the checksum manifest.
func verifyManifest(publicKey ed25519.PublicKey, manifest, signature []byte) bool {
	return ed25519.Verify(publicKey, manifest, signature)
}

// sha256Hex returns the SHA-256 hex digest of data.
func sha256Hex(data []byte) string {
	sum := sha256.Sum256(data)
	return hex.EncodeToString(sum[:])
}

func main() {
	pub, _ := base64.StdEncoding.DecodeString(os.Getenv("CI_RELEASE_PUBKEY")) // Ed25519 public key
	sig, _ := base64.StdEncoding.DecodeString(os.Getenv("CI_MANIFEST_SIG"))   // manifest signature

	manifest, err := os.ReadFile("SHA256SUMS")
	if err != nil {
		fmt.Fprintln(os.Stderr, "cannot read manifest:", err)
		os.Exit(1)
	}
	if !verifyManifest(ed25519.PublicKey(pub), manifest, sig) {
		fmt.Fprintln(os.Stderr, "Ed25519 manifest signature INVALID")
		os.Exit(1)
	}
	fmt.Println("manifest Ed25519 signature OK; SHA-256 checksums trusted")
	fmt.Println("manifest digest:", sha256Hex(manifest))
}
