// Correct password hashing with scrypt and a random salt (Node.js).
'use strict';
const crypto = require('crypto');

const PARAMS = { N: 2 ** 14, r: 8, p: 1 };

function hashPassword(password) {
  const salt = crypto.randomBytes(16);
  const dk = crypto.scryptSync(password, salt, 32, PARAMS);
  return Buffer.concat([salt, dk]);
}

function verifyPassword(stored, password) {
  const salt = stored.subarray(0, 16);
  const expected = stored.subarray(16);
  const dk = crypto.scryptSync(password, salt, 32, PARAMS);
  return crypto.timingSafeEqual(dk, expected);          // constant-time
}

const record = hashPassword('correct horse');
console.log('scrypt verify OK:', verifyPassword(record, 'correct horse'));
module.exports = { hashPassword, verifyPassword };
