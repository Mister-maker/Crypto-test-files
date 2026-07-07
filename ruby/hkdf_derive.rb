=begin
HkdfDerive -- INTENTIONAL SYNTAX ERRORS (scanner robustness).
Mentions AES, RSA, SHA-256, ChaCha20, MD5, ML-KEM, Ed25519.
=end

def broken
  x = "ChaCha20  # unterminated
  cipher = AES::::new(
  end end end
