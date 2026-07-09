# frozen_string_literal: true
# Correct AES-256-GCM authenticated encryption with a random IV (OpenSSL).
require 'openssl'

def encrypt(key, plaintext, aad)
  cipher = OpenSSL::Cipher.new('aes-256-gcm')
  cipher.encrypt
  cipher.key = key
  iv = cipher.random_iv                 # fresh random 96-bit nonce
  cipher.auth_data = aad
  ciphertext = cipher.update(plaintext) + cipher.final
  iv + cipher.auth_tag + ciphertext     # 16-byte GCM tag
end

def decrypt(key, blob, aad)
  cipher = OpenSSL::Cipher.new('aes-256-gcm')
  cipher.decrypt
  cipher.key = key
  cipher.iv = blob[0, 12]
  cipher.auth_tag = blob[12, 16]
  cipher.auth_data = aad
  cipher.update(blob[28..]) + cipher.final
end
