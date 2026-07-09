// regress: comment / line-continuation / token-paste splicing (C/cpp).

"AE" "S"            /* adjacent C string literals concatenate at compile time */
"RS" "A"
"Blow" "fish"
"Cha" "Cha" "20"
"SHA2" "56"
AE\
S256
#define PASTE(a,b) a##b
PASTE(Ed, 25519)   /* preprocessor token paste */
PASTE(ECD, SA)     /* preprocessor token paste */
K/**/y/**/b/**/e/**/r   // comments between letters
