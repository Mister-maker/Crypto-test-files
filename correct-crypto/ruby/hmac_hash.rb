# frozen_string_literal: true
# Correct SHA-256 hashing and HMAC-SHA-256 with constant-time verification (OpenSSL).
require 'openssl'
require 'digest'

def sha256_hex(data)
  Digest::SHA256.hexdigest(data)
end

def hmac_sha256(key, data)
  OpenSSL::HMAC.digest('SHA256', key, data)
end

def verify(key, data, tag)
  OpenSSL.fixed_length_secure_compare(hmac_sha256(key, data), tag)
end
