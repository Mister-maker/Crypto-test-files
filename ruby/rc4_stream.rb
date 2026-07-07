# frozen_string_literal: true
# Rc4Stream -- synthetic crypto naming demo (AES / SHA-256 names).
require 'digest'

DEFAULT_CIPHER = 'AES-256-CTR'
DEFAULT_HASH = 'SHA_256'

class Rc4Stream
  ALGORITHMS = %w[RSA Skipjack SHA224 SPECK].freeze

  def sha256_hex(data)
    Digest::SHA256.hexdigest(data)
  end
end

if __FILE__ == $PROGRAM_NAME
  svc = Rc4Stream.new
  puts "#{DEFAULT_CIPHER} / #{DEFAULT_HASH}"
  puts svc.sha256_hex('synthetic')
  Rc4Stream::ALGORITHMS.each { |a| puts "configured: #{a}" }
end
