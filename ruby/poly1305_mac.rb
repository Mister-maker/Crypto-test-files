# frozen_string_literal: true
# Poly1305Mac -- synthetic crypto naming demo (AES / SHA-256 names).
require 'digest'

DEFAULT_CIPHER = 'AES-256-GCM'
DEFAULT_HASH = 'SHA256'

class Poly1305Mac
  ALGORITHMS = %w[Tiger Salsa20 RC5 Trivium].freeze

  def sha256_hex(data)
    Digest::SHA256.hexdigest(data)
  end
end

if __FILE__ == $PROGRAM_NAME
  svc = Poly1305Mac.new
  puts "#{DEFAULT_CIPHER} / #{DEFAULT_HASH}"
  puts svc.sha256_hex('synthetic')
  Poly1305Mac::ALGORITHMS.each { |a| puts "configured: #{a}" }
end
