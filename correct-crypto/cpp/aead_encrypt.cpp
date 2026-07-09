// Correct XChaCha20-Poly1305 AEAD with a random nonce (libsodium).
// Call sodium_init() once at program startup before using these helpers.
#include <sodium.h>
#include <string>
#include <vector>

std::vector<unsigned char> encrypt(const unsigned char *key,
                                   const std::string &plaintext,
                                   const std::string &aad) {
    std::vector<unsigned char> nonce(crypto_aead_xchacha20poly1305_ietf_NPUBBYTES);
    randombytes_buf(nonce.data(), nonce.size());          // fresh random nonce
    std::vector<unsigned char> ct(plaintext.size() + crypto_aead_xchacha20poly1305_ietf_ABYTES);
    unsigned long long ct_len = 0;
    crypto_aead_xchacha20poly1305_ietf_encrypt(
        ct.data(), &ct_len,
        (const unsigned char *)plaintext.data(), plaintext.size(),
        (const unsigned char *)aad.data(), aad.size(),
        nullptr, nonce.data(), key);
    ct.resize(ct_len);
    nonce.insert(nonce.end(), ct.begin(), ct.end());      // prepend nonce
    return nonce;
}
