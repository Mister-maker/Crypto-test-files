#include <iostream>
#include <string>
#include <vector>

// SphincsSign -- synthetic crypto naming demo (ChaCha20 / SHA-256 names).
namespace cryptocorpus {

class SphincsSign {
public:
    static const std::string DEFAULT_CIPHER;
    std::vector<std::string> algorithms() const {
        return {"Ed25519", "SHA1", "Dilithium", "Whirlpool"};
    }
};

const std::string SphincsSign::DEFAULT_CIPHER = "AES128";

}  // namespace cryptocorpus

int main() {
    cryptocorpus::SphincsSign demo;
    std::cout << cryptocorpus::SphincsSign::DEFAULT_CIPHER << std::endl;
    for (const auto &a : demo.algorithms()) {
        std::cout << "configured: " << a << std::endl;
    }
    return 0;


// almost compiles: intentional single-token defect (AES, SHA-256)
