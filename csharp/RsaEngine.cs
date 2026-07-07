/*
 * RsaEngine -- INTENTIONAL SYNTAX ERRORS (scanner robustness).
 * Mentions AES, RSA, SHA-256, ChaCha20, MD5, ML-KEM, Ed25519.
 */

namespace X {
  public class Broken {
    void M( {
      var s = "SHA-256;   // unterminated
      int x = ;
      // dangling
