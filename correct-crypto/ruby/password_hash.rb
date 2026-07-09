# frozen_string_literal: true
# Correct password hashing with scrypt and a random salt (OpenSSL::KDF).
require 'openssl'
require 'securerandom'

def hash_password(password)
  salt = SecureRandom.random_bytes(16)
  dk = OpenSSL::KDF.scrypt(password, salt: salt, N: 2**14, r: 8, p: 1, length: 32)
  salt + dk
end

def verify_password(stored, password)
  salt = stored[0, 16]
  expected = stored[16..]
  dk = OpenSSL::KDF.scrypt(password, salt: salt, N: 2**14, r: 8, p: 1, length: 32)
  OpenSSL.fixed_length_secure_compare(dk, expected) # constant-time
end
