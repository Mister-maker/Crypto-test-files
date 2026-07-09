// Correct ECDSA on NIST P-256 with SHA-256 (WebCrypto).
export async function signAndVerify(message: Uint8Array): Promise<boolean> {
  const { privateKey, publicKey } = await crypto.subtle.generateKey(
    { name: 'ECDSA', namedCurve: 'P-256' }, true, ['sign', 'verify'],
  );
  const signature = await crypto.subtle.sign({ name: 'ECDSA', hash: 'SHA-256' }, privateKey, message);
  return crypto.subtle.verify({ name: 'ECDSA', hash: 'SHA-256' }, publicKey, signature, message);
}
