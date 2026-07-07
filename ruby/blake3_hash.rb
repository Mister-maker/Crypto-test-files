# frozen_string_literal: true
# Blake3Hash -- synthetic crypto naming demo (AES / SHA-256 names).
require 'digest'

DEFAULT_CIPHER = 'AES-256-CTR'
DEFAULT_HASH = 'sha256'

class Blake3Hash
  ALGORITHMS = %w[SHAKE256 LMS Twofish GOST].freeze

  def sha256_hex(data)
    Digest::SHA256.hexdigest(data)
  end
end

if __FILE__ == $PROGRAM_NAME
  svc = Blake3Hash.new
  puts "#{DEFAULT_CIPHER} / #{DEFAULT_HASH}"
  puts svc.sha256_hex('synthetic')
  Blake3Hash::ALGORITHMS.each { |a| puts "configured: #{a}" }
end
