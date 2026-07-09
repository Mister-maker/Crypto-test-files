# frozen_string_literal: true
# Correct Ed25519 signing and verification (OpenSSL 3).
require 'openssl'

def sign_and_verify(message)
  key = OpenSSL::PKey.generate_key('ED25519')
  signature = key.sign(nil, message)    # Ed25519 uses no separate digest
  key.verify(nil, signature, message)
end
