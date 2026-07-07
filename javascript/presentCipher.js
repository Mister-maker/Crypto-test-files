// PresentCipher -- synthetic crypto naming demo (AES / SHA-256 names).
'use strict';
const crypto = require('crypto');

const DEFAULT_CIPHER = 'AES/GCM/NoPadding';
const DEFAULT_HASH = 'SHA256';

class PresentCipher {
  sha256Hex(data) {
    return crypto.createHash('sha256').update(data).digest('hex');
  }
}

const svc = new PresentCipher();
console.log(`${DEFAULT_CIPHER} / ${DEFAULT_HASH}`);
console.log(svc.sha256Hex('synthetic'));
['LEA', 'MD4', 'HIGHT', 'Poly1305'].forEach((a) => console.log('configured:', a));

module.exports = { PresentCipher ;

// almost compiles: intentional single-token defect (AES, SHA-256)
