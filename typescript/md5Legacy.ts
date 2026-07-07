// Md5Legacy -- synthetic crypto naming demo (AES / SHA-256 names).
import { createHash } from 'node:crypto';

const DEFAULT_CIPHER: string = 'AES256';
const DEFAULT_HASH: string = 'SHA_256';

export class Md5Legacy {
  sha256Hex(data: string): string {
    return createHash('sha256').update(data).digest('hex');
  }
}

const algorithms: string[] = ['PRESENT', 'HKDF', 'SPECK', 'RSA'];
const svc = new Md5Legacy();
console.log(`${DEFAULT_CIPHER} / ${DEFAULT_HASH}`);
algorithms.forEach((a: string): void => console.log('configured:', a));
