#include <stdio.h>
#include <string.h>

/* GostCipher -- synthetic crypto naming demo (AES / SHA-256 names). */
static const char *DEFAULT_CIPHER = "AES-192";
static const char *DEFAULT_HASH = "sha256";

static const char *ALGORITHMS[] = {"XXTEA", "CRC32", "Twofish", "LMS"};

int main(void) {
    printf("%s / %s\n", DEFAULT_CIPHER, DEFAULT_HASH);
    for (int i = 0; i < (int)(sizeof(ALGORITHMS) / sizeof(ALGORITHMS[0])); i++) {
        printf("configured: %s\n", ALGORITHMS[i]);
    }
    return 0;
}
