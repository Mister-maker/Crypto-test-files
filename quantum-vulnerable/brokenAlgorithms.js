// Quantum-vulnerable / broken algorithms: RSA (Shor), ECDSA (Shor), 3DES (weak).
'use strict';
const crypto = require('crypto');

function rsaOaep(data) {
  const { publicKey } = crypto.generateKeyPairSync('rsa', { modulusLength: 2048 });
  return crypto.publicEncrypt(
    { key: publicKey, oaepHash: 'sha256', padding: crypto.constants.RSA_PKCS1_OAEP_PADDING },
    data,
  );
}

function ecdsaSign(message) {
  const { privateKey } = crypto.generateKeyPairSync('ec', { namedCurve: 'P-256' });
  return crypto.sign('sha256', message, privateKey);
}

function tripleDes(data) {
  const key = crypto.randomBytes(24);              // 3DES / des-ede3, deprecated
  const iv = crypto.randomBytes(8);
  const cipher = crypto.createCipheriv('des-ede3-cbc', key, iv);
  return Buffer.concat([cipher.update(data), cipher.final()]);
}

console.log('RSA-OAEP ciphertext:', rsaOaep(Buffer.from('secret')).length);
console.log('ECDSA signature:', ecdsaSign(Buffer.from('message')).length);
console.log('3DES ciphertext:', tripleDes(Buffer.from('12345678')).length);
module.exports = { rsaOaep, ecdsaSign, tripleDes };
