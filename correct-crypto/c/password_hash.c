/* Correct password hashing with PBKDF2-HMAC-SHA-256 and a random salt (OpenSSL).
 * Fills salt (16 bytes) and derives a 32-byte key into out. Returns 1 on success. */
#include <openssl/evp.h>
#include <openssl/rand.h>

int pbkdf2_hash(const char *password, int password_len,
                unsigned char *salt, unsigned char *out) {
    if (RAND_bytes(salt, 16) != 1) {
        return 0;
    }
    return PKCS5_PBKDF2_HMAC(password, password_len,
                             salt, 16,
                             210000,                 /* iterations */
                             EVP_sha256(),
                             32, out);
}
