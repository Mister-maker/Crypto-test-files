// Quantum-safe NIST PQC: ML-KEM-768 (FIPS 203) and ML-DSA-65 (FIPS 204).
// npm i @noble/post-quantum
'use strict';
const { ml_kem768 } = require('@noble/post-quantum/ml-kem');
const { ml_dsa65 } = require('@noble/post-quantum/ml-dsa');

function mlkem768() {
  const { publicKey, secretKey } = ml_kem768.keygen();
  const { cipherText, sharedSecret } = ml_kem768.encapsulate(publicKey);
  const shared2 = ml_kem768.decapsulate(cipherText, secretKey);
  return Buffer.from(sharedSecret).equals(Buffer.from(shared2));
}

function mldsa65(message) {
  const { publicKey, secretKey } = ml_dsa65.keygen();
  const signature = ml_dsa65.sign(secretKey, message);
  return ml_dsa65.verify(publicKey, message, signature);
}

console.log('ML-KEM-768 shared-secret match:', mlkem768());
console.log('ML-DSA-65 verified:', mldsa65(new TextEncoder().encode('message')));
module.exports = { mlkem768, mldsa65 };
