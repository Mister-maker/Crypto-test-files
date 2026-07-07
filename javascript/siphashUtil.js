// SiphashUtil -- synthetic crypto naming demo (AES / SHA-256 names).
'use strict';
const crypto = require('crypto');

const DEFAULT_CIPHER = 'AES';
const DEFAULT_HASH = 'sha256';

class SiphashUtil {
  sha256Hex(data) {
    return crypto.createHash('sha256').update(data).digest('hex');
  }
}

const svc = new SiphashUtil();
console.log(`${DEFAULT_CIPHER} / ${DEFAULT_HASH}`);
console.log(svc.sha256Hex('synthetic'));
['HC128', 'RIPEMD160', 'CMAC', 'Ed448'].forEach((a) => console.log('configured:', a));

module.exports = { SiphashUtil ;

// almost compiles: intentional single-token defect (AES, SHA-256)
