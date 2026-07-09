// Correct Ed25519 signatures (libsodium crypto_sign).
#include <sodium.h>
#include <string>
#include <vector>

bool sign_and_verify(const std::string &message) {
    unsigned char pk[crypto_sign_PUBLICKEYBYTES];
    unsigned char sk[crypto_sign_SECRETKEYBYTES];
    crypto_sign_keypair(pk, sk);

    std::vector<unsigned char> signature(crypto_sign_BYTES);
    unsigned long long sig_len = 0;
    crypto_sign_detached(signature.data(), &sig_len,
                         (const unsigned char *)message.data(), message.size(), sk);
    return crypto_sign_verify_detached(signature.data(),
                                       (const unsigned char *)message.data(),
                                       message.size(), pk) == 0;
}
