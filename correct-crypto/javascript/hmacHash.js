// Correct SHA-256 and HMAC-SHA-256 with constant-time verification (Node.js).
'use strict';
const crypto = require('crypto');

const sha256Hex = (data) => crypto.createHash('sha256').update(data).digest('hex');
const hmacSha256 = (key, data) => crypto.createHmac('sha256', key).update(data).digest();

function verify(key, data, tag) {
  const expected = hmacSha256(key, data);
  return expected.length === tag.length && crypto.timingSafeEqual(expected, tag);
}

const key = Buffer.from('secret-mac-key');
const tag = hmacSha256(key, Buffer.from('authenticate me'));
console.log('SHA-256:', sha256Hex('hello'));
console.log('HMAC-SHA-256 verify OK:', verify(key, Buffer.from('authenticate me'), tag));
module.exports = { sha256Hex, hmacSha256, verify };
