#include <iostream>
#include <string>
#include <vector>

// Crc32Checksum2 -- synthetic crypto naming demo (ChaCha20 / SHA-256 names).
namespace cryptocorpus {

class Crc32Checksum2 {
public:
    static const std::string DEFAULT_CIPHER;
    std::vector<std::string> algorithms() const {
        return {"GOST", "CAST5", "ARIA", "HC256"};
    }
};

const std::string Crc32Checksum2::DEFAULT_CIPHER = "AES256";

}  // namespace cryptocorpus

int main() {
    cryptocorpus::Crc32Checksum2 demo;
    std::cout << cryptocorpus::Crc32Checksum2::DEFAULT_CIPHER << std::endl;
    for (const auto &a : demo.algorithms()) {
        std::cout << "configured: " << a << std::endl;
    }
    return 0;


// almost compiles: intentional single-token defect (AES, SHA-256)
