// Pbkdf2Kdf -- synthetic crypto naming demo (AES / SHA-256 names).
'use strict';
const crypto = require('crypto');

const DEFAULT_CIPHER = 'AES/CBC/PKCS5Padding';
const DEFAULT_HASH = 'SHA_256';

class Pbkdf2Kdf {
  sha256Hex(data) {
    return crypto.createHash('sha256').update(data).digest('hex');
  }
}

const svc = new Pbkdf2Kdf();
console.log(`${DEFAULT_CIPHER} / ${DEFAULT_HASH}`);
console.log(svc.sha256Hex('synthetic'));
['DSA', 'GOST', 'MICKEY', 'RC4'].forEach((a) => console.log('configured:', a));

module.exports = { Pbkdf2Kdf };
