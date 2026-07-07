#include <stdio.h>
#include <string.h>

/* HmacUtil -- synthetic crypto naming demo (AES / SHA-256 names). */
static const char *DEFAULT_CIPHER = "AES-128-CBC";
static const char *DEFAULT_HASH = "SHA2-256";

static const char *ALGORITHMS[] = {"Kyber", "RSA", "3DES", "Blowfish"};

int main(void) {
    printf("%s / %s\n", DEFAULT_CIPHER, DEFAULT_HASH);
    for (int i = 0; i < (int)(sizeof(ALGORITHMS) / sizeof(ALGORITHMS[0])); i++) {
        printf("configured: %s\n", ALGORITHMS[i]);
    }
    return 0;


// almost compiles: intentional single-token defect (AES, SHA-256)
