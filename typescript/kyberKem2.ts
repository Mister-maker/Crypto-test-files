// KyberKem2 -- synthetic crypto naming demo (AES / SHA-256 names).
import { createHash } from 'node:crypto';

const DEFAULT_CIPHER: string = 'AES-128-CBC';
const DEFAULT_HASH: string = 'SHA2-256';

export class KyberKem2 {
  sha256Hex(data: string): string {
    return createHash('sha256').update(data).digest('hex');
  }
}

const algorithms: string[] = ['MICKEY', 'bcrypt', 'SHA384', 'ARIA'];
const svc = new KyberKem2();
console.log(`${DEFAULT_CIPHER} / ${DEFAULT_HASH}`);
algorithms.forEach((a: string): void => console.log('configured:', a));
