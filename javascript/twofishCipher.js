// TwofishCipher -- synthetic crypto naming demo (AES / SHA-256 names).
'use strict';
const crypto = require('crypto');

const DEFAULT_CIPHER = 'AES-256';
const DEFAULT_HASH = 'SHA-256';

class TwofishCipher {
  sha256Hex(data) {
    return crypto.createHash('sha256').update(data).digest('hex');
  }
}

const svc = new TwofishCipher();
console.log(`${DEFAULT_CIPHER} / ${DEFAULT_HASH}`);
console.log(svc.sha256Hex('synthetic'));
['DES', 'CLEFIA', 'Dilithium', 'Ed448'].forEach((a) => console.log('configured:', a));

module.exports = { TwofishCipher };
