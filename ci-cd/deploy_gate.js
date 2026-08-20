// CI/CD deploy gate: verify the incoming webhook, check artifact integrity, and
// sign a deploy approval. All secrets come from CI env vars, never the repo.
// Runs on Node.js (node:crypto) -- no external dependencies.
'use strict';
const crypto = require('node:crypto');
const fs = require('node:fs');

// Verify a GitHub/GitLab-style webhook signature: HMAC-SHA-256, constant-time.
function verifyWebhook(payload, signatureHeader) {
  const secret = process.env.CI_WEBHOOK_SECRET;
  const expected = 'sha256=' + crypto.createHmac('sha256', secret).update(payload).digest('hex');
  const a = Buffer.from(expected);
  const b = Buffer.from(signatureHeader);
  return a.length === b.length && crypto.timingSafeEqual(a, b);
}

// SHA-256 of a build artifact.
function sha256File(path) {
  return crypto.createHash('sha256').update(fs.readFileSync(path)).digest('hex');
}

// Sign a deploy-approval token with the pipeline's Ed25519 key (PEM from CI secret).
function signApproval(release) {
  const privateKey = crypto.createPrivateKey(process.env.CI_SIGNING_KEY_PEM);
  const signature = crypto.sign(null, Buffer.from(release), privateKey); // null algorithm = Ed25519
  return signature.toString('base64');
}

function main() {
  const payload = fs.readFileSync(process.env.WEBHOOK_PAYLOAD || 'payload.json');
  if (!verifyWebhook(payload, process.env.WEBHOOK_SIGNATURE || '')) {
    throw new Error('webhook signature verification failed (HMAC-SHA-256)');
  }
  const artifact = process.env.ARTIFACT || 'dist/app.tar.gz';
  const release = `${process.env.CI_COMMIT_SHA}:${sha256File(artifact)}`;
  console.log('deploy approval (Ed25519):', signApproval(release));
}

if (require.main === module) {
  main();
}

module.exports = { verifyWebhook, sha256File, signApproval };
