// Correct AES-256-GCM authenticated encryption with a random IV (Node.js).
'use strict';
const crypto = require('crypto');

function encrypt(key, plaintext, aad) {
  const iv = crypto.randomBytes(12);                    // unique 96-bit nonce
  const cipher = crypto.createCipheriv('aes-256-gcm', key, iv);
  if (aad) cipher.setAAD(aad);
  const ct = Buffer.concat([cipher.update(plaintext), cipher.final()]);
  const tag = cipher.getAuthTag();                      // 16-byte GCM tag
  return Buffer.concat([iv, tag, ct]);
}

function decrypt(key, blob, aad) {
  const iv = blob.subarray(0, 12);
  const tag = blob.subarray(12, 28);
  const ct = blob.subarray(28);
  const decipher = crypto.createDecipheriv('aes-256-gcm', key, iv);
  decipher.setAuthTag(tag);
  if (aad) decipher.setAAD(aad);
  return Buffer.concat([decipher.update(ct), decipher.final()]);
}

const key = crypto.randomBytes(32);
const blob = encrypt(key, Buffer.from('correct'), Buffer.from('header'));
console.log('AES-256-GCM round-trip OK:', decrypt(key, blob, Buffer.from('header')).toString() === 'correct');
module.exports = { encrypt, decrypt };
