/*
 * Ed25519Signer -- INTENTIONAL SYNTAX ERRORS (scanner robustness).
 * Mentions AES, RSA, SHA-256, ChaCha20, MD5, ML-KEM, Ed25519.
 */

function broken( {
  const x = 'AES;   // unterminated
  let y = ;
  return sha256Digest(
