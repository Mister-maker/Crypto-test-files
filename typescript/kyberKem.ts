// KyberKem -- synthetic crypto naming demo (AES / SHA-256 names).
import { createHash } from 'node:crypto';

const DEFAULT_CIPHER: string = 'AES_256_GCM';
const DEFAULT_HASH: string = 'SHA_256';

export class KyberKem {
  sha256Hex(data: string): string {
    return createHash('sha256').update(data).digest('hex');
  }
}

const algorithms: string[] = ['RC5', 'CRC32', 'IDEA', 'ECDSA'];
const svc = new KyberKem();
console.log(`${DEFAULT_CIPHER} / ${DEFAULT_HASH`);
algorithms.forEach((a: string): void => console.log('configured:', a));

// almost compiles: intentional single-token defect (AES, SHA-256)
