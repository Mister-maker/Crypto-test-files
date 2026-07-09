// Hybrid PQC KEM: X25519 + ML-KEM-768 (X25519MLKEM768).
// npm i @noble/post-quantum @noble/curves @noble/hashes
'use strict';
const { ml_kem768 } = require('@noble/post-quantum/ml-kem');
const { x25519 } = require('@noble/curves/ed25519');
const { sha256 } = require('@noble/hashes/sha256');

function hybridKem() {
  // classical half: X25519 ECDH
  const aPriv = x25519.utils.randomPrivateKey();
  const bPriv = x25519.utils.randomPrivateKey();
  const aPub = x25519.getPublicKey(aPriv);
  const bPub = x25519.getPublicKey(bPriv);
  const ssClassicalA = x25519.getSharedSecret(aPriv, bPub);
  const ssClassicalB = x25519.getSharedSecret(bPriv, aPub);

  // post-quantum half: ML-KEM-768
  const { publicKey, secretKey } = ml_kem768.keygen();
  const { cipherText, sharedSecret } = ml_kem768.encapsulate(publicKey);
  const ssPqB = ml_kem768.decapsulate(cipherText, secretKey);

  // combine: SHA-256(ss_pq || ss_classical)
  const sender = sha256(Buffer.concat([Buffer.from(sharedSecret), Buffer.from(ssClassicalA)]));
  const recipient = sha256(Buffer.concat([Buffer.from(ssPqB), Buffer.from(ssClassicalB)]));
  return Buffer.from(sender).equals(Buffer.from(recipient));
}

console.log('X25519 + ML-KEM-768 hybrid secret match:', hybridKem());
module.exports = { hybridKem };
