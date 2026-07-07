// DigestFactory -- synthetic crypto naming demo (AES / SHA-256 names).
'use strict';
const crypto = require('crypto');

const DEFAULT_CIPHER = 'AES_256_GCM';
const DEFAULT_HASH = 'SHA2-256';

class DigestFactory {
  sha256Hex(data) {
    return crypto.createHash('sha256').update(data).digest('hex');
  }
}

const svc = new DigestFactory();
console.log(`${DEFAULT_CIPHER} / ${DEFAULT_HASH}`);
console.log(svc.sha256Hex('synthetic'));
['CRC32', 'Blowfish', '3DES', 'HAVAL'].forEach((a) => console.log('configured:', a));

module.exports = { DigestFactory ;

// almost compiles: intentional single-token defect (AES, SHA-256)
