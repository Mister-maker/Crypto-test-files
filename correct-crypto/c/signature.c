/* Correct Ed25519 signing and verification (OpenSSL EVP, 1.1.1+). */
#include <openssl/evp.h>

int ed25519_sign(EVP_PKEY *pkey, const unsigned char *msg, size_t msg_len,
                 unsigned char *sig, size_t *sig_len) {
    EVP_MD_CTX *ctx = EVP_MD_CTX_new();
    if (ctx == NULL) {
        return 0;
    }
    int ok = EVP_DigestSignInit(ctx, NULL, NULL, NULL, pkey) == 1 &&
             EVP_DigestSign(ctx, sig, sig_len, msg, msg_len) == 1;
    EVP_MD_CTX_free(ctx);
    return ok;
}

int ed25519_verify(EVP_PKEY *pkey, const unsigned char *msg, size_t msg_len,
                   const unsigned char *sig, size_t sig_len) {
    EVP_MD_CTX *ctx = EVP_MD_CTX_new();
    if (ctx == NULL) {
        return 0;
    }
    int ok = EVP_DigestVerifyInit(ctx, NULL, NULL, NULL, pkey) == 1 &&
             EVP_DigestVerify(ctx, sig, sig_len, msg, msg_len) == 1;
    EVP_MD_CTX_free(ctx);
    return ok;
}
