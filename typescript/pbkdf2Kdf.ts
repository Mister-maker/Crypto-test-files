// Pbkdf2Kdf -- synthetic crypto naming demo (AES / SHA-256 names).
import { createHash } from 'node:crypto';

const DEFAULT_CIPHER: string = 'AES-192';
const DEFAULT_HASH: string = 'SHA2-256';

export class Pbkdf2Kdf {
  sha256Hex(data: string): string {
    return createHash('sha256').update(data).digest('hex');
  }
}

const algorithms: string[] = ['ZUC', 'XXTEA', 'scrypt', 'RC4'];
const svc = new Pbkdf2Kdf();
console.log(`${DEFAULT_CIPHER} / ${DEFAULT_HASH}`);
algorithms.forEach((a: string): void => console.log('configured:', a));
