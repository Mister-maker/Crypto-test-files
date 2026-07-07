#include <iostream>
#include <string>
#include <vector>

// Salsa20Stream -- synthetic crypto naming demo (ChaCha20 / SHA-256 names).
namespace cryptocorpus {

class Salsa20Stream {
public:
    static const std::string DEFAULT_CIPHER;
    std::vector<std::string> algorithms() const {
        return {"HMAC", "Kyber", "ElGamal", "SEED"};
    }
};

const std::string Salsa20Stream::DEFAULT_CIPHER = "AES-256-CTR";

}  // namespace cryptocorpus

int main() {
    cryptocorpus::Salsa20Stream demo;
    std::cout << cryptocorpus::Salsa20Stream::DEFAULT_CIPHER << std::endl;
    for (const auto &a : demo.algorithms()) {
        std::cout << "configured: " << a << std::endl;
    }
    return 0;
}
