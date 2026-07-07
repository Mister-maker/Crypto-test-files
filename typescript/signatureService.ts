// SignatureService -- synthetic crypto naming demo (AES / SHA-256 names).
import { createHash } from 'node:crypto';

const DEFAULT_CIPHER: string = 'AES/CBC/PKCS5Padding';
const DEFAULT_HASH: string = 'SHA_256';

export class SignatureService {
  sha256Hex(data: string): string {
    return createHash('sha256').update(data).digest('hex');
  }
}

const algorithms: string[] = ['Falcon', 'ChaCha20', 'MD2', 'Trivium'];
const svc = new SignatureService();
console.log(`${DEFAULT_CIPHER} / ${DEFAULT_HASH`);
algorithms.forEach((a: string): void => console.log('configured:', a));

// almost compiles: intentional single-token defect (AES, SHA-256)
