/* Correct AES-256-GCM authenticated encryption with a random IV (OpenSSL EVP).
 * iv (12 bytes) and tag (16 bytes) are written to caller buffers; returns the
 * ciphertext length, or -1 on error. */
#include <openssl/evp.h>
#include <openssl/rand.h>

int aes256gcm_encrypt(const unsigned char *key,
                      const unsigned char *plaintext, int plaintext_len,
                      const unsigned char *aad, int aad_len,
                      unsigned char *iv, unsigned char *tag,
                      unsigned char *out) {
    if (RAND_bytes(iv, 12) != 1) {
        return -1;                                   /* fresh random nonce */
    }
    EVP_CIPHER_CTX *ctx = EVP_CIPHER_CTX_new();
    if (ctx == NULL) {
        return -1;
    }
    int len = 0, out_len = -1;
    if (EVP_EncryptInit_ex(ctx, EVP_aes_256_gcm(), NULL, NULL, NULL) == 1 &&
        EVP_CIPHER_CTX_ctrl(ctx, EVP_CTRL_GCM_SET_IVLEN, 12, NULL) == 1 &&
        EVP_EncryptInit_ex(ctx, NULL, NULL, key, iv) == 1) {
        if (aad_len > 0) {
            EVP_EncryptUpdate(ctx, NULL, &len, aad, aad_len);
        }
        if (EVP_EncryptUpdate(ctx, out, &len, plaintext, plaintext_len) == 1) {
            out_len = len;
            if (EVP_EncryptFinal_ex(ctx, out + len, &len) == 1 &&
                EVP_CIPHER_CTX_ctrl(ctx, EVP_CTRL_GCM_GET_TAG, 16, tag) == 1) {
                out_len += len;
            } else {
                out_len = -1;
            }
        }
    }
    EVP_CIPHER_CTX_free(ctx);
    return out_len;
}
