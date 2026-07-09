// Correct password hashing with Argon2id (libsodium crypto_pwhash).
#include <sodium.h>
#include <string>

bool hash_password(const std::string &password, char out[crypto_pwhash_STRBYTES]) {
    return crypto_pwhash_str(
        out, password.c_str(), password.size(),
        crypto_pwhash_OPSLIMIT_MODERATE,
        crypto_pwhash_MEMLIMIT_MODERATE) == 0;
}

bool verify_password(const char *stored, const std::string &password) {
    return crypto_pwhash_str_verify(stored, password.c_str(), password.size()) == 0;
}
