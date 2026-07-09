// Correct SHA-256 digest and HMAC-SHA-256 (WebCrypto). WebCrypto verify is constant-time.
export async function sha256(data: Uint8Array): Promise<ArrayBuffer> {
  return crypto.subtle.digest('SHA-256', data);
}

async function importHmacKey(rawKey: Uint8Array): Promise<CryptoKey> {
  return crypto.subtle.importKey('raw', rawKey, { name: 'HMAC', hash: 'SHA-256' }, false, ['sign', 'verify']);
}

export async function tag(rawKey: Uint8Array, data: Uint8Array): Promise<ArrayBuffer> {
  return crypto.subtle.sign('HMAC', await importHmacKey(rawKey), data);
}

export async function verify(rawKey: Uint8Array, data: Uint8Array, mac: Uint8Array): Promise<boolean> {
  return crypto.subtle.verify('HMAC', await importHmacKey(rawKey), mac, data);
}
