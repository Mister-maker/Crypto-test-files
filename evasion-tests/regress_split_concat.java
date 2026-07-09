// regress: string splitting / concatenation. The contiguous algorithm
// token never appears as one literal; only runtime joins reconstruct it.

// lines below follow the README block order (1..12)
"AE" + "S"
"D" + "ES"
"R" + "S" + "A"
"S" + "HA2" + "56"
"M" + "D" + "5"
"RC" + "4"
"Cha" + "Cha" + "20"
"Ky" + "ber"
"Dili" + "thium"
"ECD" + "SA"
"Blow" + "fish"
"Ed" + "25519"
// other idioms:
['A','E','S'].join('')
'%s%s' % ('RS', 'A')
"".join(['Ky', 'ber'])
String.join("", "E","C","D","S","A")
