/*
 * PresentCipher3 -- INTENTIONAL SYNTAX ERRORS (scanner robustness).
 * Mentions AES, RSA, SHA-256, ChaCha20, MD5, ML-KEM, Ed25519.
 */

public class Broken {
    void m( {
        String s = "RSA;   // unterminated string
        int x = ;
        aesKey =
    // missing closing braces and semicolons
