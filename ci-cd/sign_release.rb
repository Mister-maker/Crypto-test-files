# frozen_string_literal: true
# CI/CD release signing (Ruby): SHA-256 checksums for build artifacts, sign the
# manifest with RSA-2048 (RSASSA-PSS + SHA-256), and verify CI webhooks with
# HMAC-SHA-256. Secrets come from the CI environment, never the repo.
require 'openssl'
require 'digest'
require 'base64'

# Build a SHA256SUMS-style checksum manifest for a dist directory.
def build_manifest(dist_dir)
  Dir.glob(File.join(dist_dir, '*')).select { |f| File.file?(f) }.sort.map do |path|
    "#{Digest::SHA256.hexdigest(File.binread(path))}  #{File.basename(path)}"
  end.join("\n")
end

# Sign the manifest with RSA-2048 using RSASSA-PSS and SHA-256.
def sign_manifest(manifest)
  key = OpenSSL::PKey::RSA.new(ENV.fetch('CI_SIGNING_KEY_PEM'))
  signature = key.sign_pss('SHA256', manifest, salt_length: :digest, mgf1_hash: 'SHA256')
  Base64.strict_encode64(signature)
end

# Verify an incoming CI webhook with HMAC-SHA-256 (constant-time compare).
def verify_webhook(payload, signature_header)
  secret = ENV.fetch('CI_WEBHOOK_SECRET')
  expected = OpenSSL::HMAC.hexdigest('SHA256', secret, payload)
  OpenSSL.fixed_length_secure_compare(expected, signature_header)
end

if __FILE__ == $PROGRAM_NAME
  manifest = build_manifest(ENV.fetch('DIST_DIR', 'dist'))
  File.write('SHA256SUMS', manifest)
  File.write('SHA256SUMS.sig', sign_manifest(manifest))
  puts 'Signed release manifest with RSA-PSS -> SHA256SUMS + SHA256SUMS.sig'
end
