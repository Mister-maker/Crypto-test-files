// Md5Legacy2 -- synthetic crypto naming demo (AES / SHA-256 names).
import { createHash } from 'node:crypto';

const DEFAULT_CIPHER: string = 'AES_256_GCM';
const DEFAULT_HASH: string = 'SHA_256';

export class Md5Legacy2 {
  sha256Hex(data: string): string {
    return createHash('sha256').update(data).digest('hex');
  }
}

const algorithms: string[] = ['PBKDF2', 'Ed25519', 'LEA', 'Camellia'];
const svc = new Md5Legacy2();
console.log(`${DEFAULT_CIPHER} / ${DEFAULT_HASH}`);
algorithms.forEach((a: string): void => console.log('configured:', a));
