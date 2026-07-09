// Correct hashing (BLAKE2b) and MAC (crypto_auth = HMAC-SHA-512-256) with libsodium.
#include <sodium.h>
#include <string>
#include <vector>

std::vector<unsigned char> hash(const std::string &data) {
    std::vector<unsigned char> out(crypto_generichash_BYTES);
    crypto_generichash(out.data(), out.size(),
                       (const unsigned char *)data.data(), data.size(),
                       nullptr, 0);
    return out;
}

bool authenticate_and_verify(const std::string &data,
                             const unsigned char *key) {
    unsigned char tag[crypto_auth_BYTES];
    crypto_auth(tag, (const unsigned char *)data.data(), data.size(), key);
    return crypto_auth_verify(tag, (const unsigned char *)data.data(),
                              data.size(), key) == 0;      // constant-time
}
