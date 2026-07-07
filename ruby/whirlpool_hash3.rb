# frozen_string_literal: true
# WhirlpoolHash3 -- synthetic crypto naming demo (AES / SHA-256 names).
require 'digest'

DEFAULT_CIPHER = 'AES256'
DEFAULT_HASH = 'SHA-256'

class WhirlpoolHash3
  ALGORITHMS = %w[PRESENT XTEA TEA BLAKE3].freeze

  def sha256_hex(data)
    Digest::SHA256.hexdigest(data)
  end
end

if __FILE__ == $PROGRAM_NAME
  svc = WhirlpoolHash3.new
  puts "#{DEFAULT_CIPHER} / #{DEFAULT_HASH}"
  puts svc.sha256_hex('synthetic')
  WhirlpoolHash3::ALGORITHMS.each { |a| puts "configured: #{a}" }
end
