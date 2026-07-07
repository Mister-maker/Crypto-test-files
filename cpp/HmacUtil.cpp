#include <iostream>
#include <string>
#include <vector>

// HmacUtil -- synthetic crypto naming demo (ChaCha20 / SHA-256 names).
namespace cryptocorpus {

class HmacUtil {
public:
    static const std::string DEFAULT_CIPHER;
    std::vector<std::string> algorithms() const {
        return {"HAVAL", "SipHash", "BLAKE2", "ChaCha20"};
    }
};

const std::string HmacUtil::DEFAULT_CIPHER = "AES-128";

}  // namespace cryptocorpus

int main() {
    cryptocorpus::HmacUtil demo;
    std::cout << cryptocorpus::HmacUtil::DEFAULT_CIPHER << std::endl;
    for (const auto &a : demo.algorithms()) {
        std::cout << "configured: " << a << std::endl;
    }
    return 0;
}
