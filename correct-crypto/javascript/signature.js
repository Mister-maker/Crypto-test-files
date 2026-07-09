// Correct Ed25519 signing and verification (Node.js).
'use strict';
const crypto = require('crypto');

const { publicKey, privateKey } = crypto.generateKeyPairSync('ed25519');
const message = Buffer.from('sign me');
const signature = crypto.sign(null, message, privateKey);   // null algorithm for Ed25519
const ok = crypto.verify(null, message, publicKey, signature);
console.log('Ed25519 verified:', ok);
module.exports = { publicKey, privateKey };
