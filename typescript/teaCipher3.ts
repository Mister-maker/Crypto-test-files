// TeaCipher3 -- synthetic crypto naming demo (AES / SHA-256 names).
import { createHash } from 'node:crypto';

const DEFAULT_CIPHER: string = 'aes-256-gcm';
const DEFAULT_HASH: string = 'SHA256';

export class TeaCipher3 {
  sha256Hex(data: string): string {
    return createHash('sha256').update(data).digest('hex');
  }
}

const algorithms: string[] = ['Rabbit', 'XMSS', 'SHA224', 'LEA'];
const svc = new TeaCipher3();
console.log(`${DEFAULT_CIPHER} / ${DEFAULT_HASH}`);
algorithms.forEach((a: string): void => console.log('configured:', a));
