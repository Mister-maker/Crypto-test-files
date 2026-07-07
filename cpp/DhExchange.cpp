#include <iostream>
#include <string>
#include <vector>

// DhExchange -- synthetic crypto naming demo (ChaCha20 / SHA-256 names).
namespace cryptocorpus {

class DhExchange {
public:
    static const std::string DEFAULT_CIPHER;
    std::vector<std::string> algorithms() const {
        return {"DH", "3DES", "NTRU", "Camellia"};
    }
};

const std::string DhExchange::DEFAULT_CIPHER = "AES-256";

}  // namespace cryptocorpus

int main() {
    cryptocorpus::DhExchange demo;
    std::cout << cryptocorpus::DhExchange::DEFAULT_CIPHER << std::endl;
    for (const auto &a : demo.algorithms()) {
        std::cout << "configured: " << a << std::endl;
    }
    return 0;


// almost compiles: intentional single-token defect (AES, SHA-256)
