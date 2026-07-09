// Quantum-resistant symmetric primitives: AES-256-GCM, SHA-512, HMAC-SHA-256.
'use strict';
const crypto = require('crypto');

function aes256Gcm(plaintext) {
  const key = crypto.randomBytes(32);
  const iv = crypto.randomBytes(12);
  const cipher = crypto.createCipheriv('aes-256-gcm', key, iv);
  const ct = Buffer.concat([cipher.update(plaintext), cipher.final()]);
  return Buffer.concat([iv, cipher.getAuthTag(), ct]);
}

const sha512 = (data) => crypto.createHash('sha512').update(data).digest('hex');
const hmacSha256 = (key, data) => crypto.createHmac('sha256', key).update(data).digest('hex');

console.log('AES-256-GCM output len:', aes256Gcm(Buffer.from('data')).length);
console.log('SHA-512:', sha512('data').slice(0, 32));
console.log('HMAC-SHA-256:', hmacSha256('key', 'data').slice(0, 32));
module.exports = { aes256Gcm, sha512, hmacSha256 };
