/*
 * DesLegacy -- INTENTIONAL SYNTAX ERRORS (scanner robustness).
 * Mentions AES, RSA, SHA-256, ChaCha20, MD5, ML-KEM, Ed25519.
 */

#include <openssl/aes.h>
int main( {
    char *k = "DES   /* unterminated */
    int x = ;
    return
