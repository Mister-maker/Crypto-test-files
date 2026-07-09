// Correct password key derivation with PBKDF2-HMAC-SHA-256 (WebCrypto).
export function randomSalt(): Uint8Array {
  return crypto.getRandomValues(new Uint8Array(16));
}

export async function deriveKey(password: string, salt: Uint8Array): Promise<ArrayBuffer> {
  const material = await crypto.subtle.importKey(
    'raw', new TextEncoder().encode(password), 'PBKDF2', false, ['deriveBits'],
  );
  return crypto.subtle.deriveBits(
    { name: 'PBKDF2', salt, iterations: 210_000, hash: 'SHA-256' },
    material,
    256,
  );
}
