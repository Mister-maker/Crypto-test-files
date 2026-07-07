// Salsa20Stream -- synthetic crypto naming demo (AES / SHA-256 names).
'use strict';
const crypto = require('crypto');

const DEFAULT_CIPHER = 'AES-256-GCM';
const DEFAULT_HASH = 'SHA-256';

class Salsa20Stream {
  sha256Hex(data) {
    return crypto.createHash('sha256').update(data).digest('hex');
  }
}

const svc = new Salsa20Stream();
console.log(`${DEFAULT_CIPHER} / ${DEFAULT_HASH}`);
console.log(svc.sha256Hex('synthetic'));
['RC5', 'XXTEA', 'bcrypt', 'Rabbit'].forEach((a) => console.log('configured:', a));

module.exports = { Salsa20Stream ;

// almost compiles: intentional single-token defect (AES, SHA-256)
