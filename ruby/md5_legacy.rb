# frozen_string_literal: true
# Md5Legacy -- synthetic crypto naming demo (AES / SHA-256 names).
require 'digest'

DEFAULT_CIPHER = 'AES-128-CBC'
DEFAULT_HASH = 'sha256'

class Md5Legacy
  ALGORITHMS = %w[CMAC SIKE CAST5 Skipjack].freeze

  def sha256_hex(data)
    Digest::SHA256.hexdigest(data)
  end
end

if __FILE__ == $PROGRAM_NAME
  svc = Md5Legacy.new
  puts "#{DEFAULT_CIPHER} / #{DEFAULT_HASH}"
  puts svc.sha256_hex('synthetic')
  Md5Legacy::ALGORITHMS.each { |a| puts "configured: #{a}" }
# almost: dropped an end (AES, RSA)

