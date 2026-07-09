/* Correct SHA-256 digest and HMAC-SHA-256 with a constant-time compare (OpenSSL). */
#include <openssl/evp.h>
#include <openssl/hmac.h>
#include <openssl/crypto.h>

void sha256(const unsigned char *data, size_t len, unsigned char out[32]) {
    unsigned int n = 0;
    EVP_Digest(data, len, out, &n, EVP_sha256(), NULL);
}

int hmac_verify(const unsigned char *key, int key_len,
                const unsigned char *data, size_t data_len,
                const unsigned char *tag) {
    unsigned char mac[32];
    unsigned int mac_len = 0;
    HMAC(EVP_sha256(), key, key_len, data, data_len, mac, &mac_len);
    return CRYPTO_memcmp(mac, tag, 32) == 0;         /* constant-time */
}
