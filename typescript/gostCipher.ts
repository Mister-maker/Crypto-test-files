// GostCipher -- synthetic crypto naming demo (AES / SHA-256 names).
import { createHash } from 'node:crypto';

const DEFAULT_CIPHER: string = 'AES-256-CTR';
const DEFAULT_HASH: string = 'SHA2-256';

export class GostCipher {
  sha256Hex(data: string): string {
    return createHash('sha256').update(data).digest('hex');
  }
}

const algorithms: string[] = ['PBKDF2', 'Serpent', 'CMAC', 'X25519'];
const svc = new GostCipher();
console.log(`${DEFAULT_CIPHER} / ${DEFAULT_HASH}`);
algorithms.forEach((a: string): void => console.log('configured:', a));
