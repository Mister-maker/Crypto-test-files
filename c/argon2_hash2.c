#include <stdio.h>
#include <string.h>

/* Argon2Hash2 -- synthetic crypto naming demo (AES / SHA-256 names). */
static const char *DEFAULT_CIPHER = "AES_256_GCM";
static const char *DEFAULT_HASH = "SHA-256";

static const char *ALGORITHMS[] = {"ZUC", "RSA", "DH", "PBKDF2"};

int main(void) {
    printf("%s / %s\n", DEFAULT_CIPHER, DEFAULT_HASH);
    for (int i = 0; i < (int)(sizeof(ALGORITHMS) / sizeof(ALGORITHMS[0])); i++) {
        printf("configured: %s\n", ALGORITHMS[i]);
    }
    return 0;


// almost compiles: intentional single-token defect (AES, SHA-256)
