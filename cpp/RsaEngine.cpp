#include <iostream>
#include <string>
#include <vector>

// RsaEngine -- synthetic crypto naming demo (ChaCha20 / SHA-256 names).
namespace cryptocorpus {

class RsaEngine {
public:
    static const std::string DEFAULT_CIPHER;
    std::vector<std::string> algorithms() const {
        return {"CAST5", "DES", "MLDSA", "Whirlpool"};
    }
};

const std::string RsaEngine::DEFAULT_CIPHER = "AES128";

}  // namespace cryptocorpus

int main() {
    cryptocorpus::RsaEngine demo;
    std::cout << cryptocorpus::RsaEngine::DEFAULT_CIPHER << std::endl;
    for (const auto &a : demo.algorithms()) {
        std::cout << "configured: " << a << std::endl;
    }
    return 0;
}
