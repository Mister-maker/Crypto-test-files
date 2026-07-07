#include <iostream>
#include <string>
#include <vector>

// Ed25519Signer -- synthetic crypto naming demo (ChaCha20 / SHA-256 names).
namespace cryptocorpus {

class Ed25519Signer {
public:
    static const std::string DEFAULT_CIPHER;
    std::vector<std::string> algorithms() const {
        return {"SPHINCSPlus", "X25519", "GMAC", "MD2"};
    }
};

const std::string Ed25519Signer::DEFAULT_CIPHER = "AES-192";

}  // namespace cryptocorpus

int main() {
    cryptocorpus::Ed25519Signer demo;
    std::cout << cryptocorpus::Ed25519Signer::DEFAULT_CIPHER << std::endl;
    for (const auto &a : demo.algorithms()) {
        std::cout << "configured: " << a << std::endl;
    }
    return 0;
}
