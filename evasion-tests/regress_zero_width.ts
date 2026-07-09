// regress: zero-width / invisible-character injection between letters.
// Characters really present (U+200B/200C/200D/FEFF). Order: README.

// block 1
zwsp: A​E​S
zwnj: A‌E‌S
zwj:  A‍E‍S
bom:  ﻿A​E​S

// block 2
zwsp: D​E​S
zwnj: D‌E‌S
zwj:  D‍E‍S
bom:  ﻿D​E​S

// block 3
zwsp: R​S​A
zwnj: R‌S‌A
zwj:  R‍S‍A
bom:  ﻿R​S​A

// block 4
zwsp: S​H​A​2​5​6
zwnj: S‌H‌A‌2‌5‌6
zwj:  S‍H‍A‍2‍5‍6
bom:  ﻿S​H​A​2​5​6

// block 5
zwsp: M​D​5
zwnj: M‌D‌5
zwj:  M‍D‍5
bom:  ﻿M​D​5

// block 6
zwsp: R​C​4
zwnj: R‌C‌4
zwj:  R‍C‍4
bom:  ﻿R​C​4

// block 7
zwsp: C​h​a​C​h​a​2​0
zwnj: C‌h‌a‌C‌h‌a‌2‌0
zwj:  C‍h‍a‍C‍h‍a‍2‍0
bom:  ﻿C​h​a​C​h​a​2​0

// block 8
zwsp: K​y​b​e​r
zwnj: K‌y‌b‌e‌r
zwj:  K‍y‍b‍e‍r
bom:  ﻿K​y​b​e​r

// block 9
zwsp: D​i​l​i​t​h​i​u​m
zwnj: D‌i‌l‌i‌t‌h‌i‌u‌m
zwj:  D‍i‍l‍i‍t‍h‍i‍u‍m
bom:  ﻿D​i​l​i​t​h​i​u​m

// block 10
zwsp: E​C​D​S​A
zwnj: E‌C‌D‌S‌A
zwj:  E‍C‍D‍S‍A
bom:  ﻿E​C​D​S​A

// block 11
zwsp: B​l​o​w​f​i​s​h
zwnj: B‌l‌o‌w‌f‌i‌s‌h
zwj:  B‍l‍o‍w‍f‍i‍s‍h
bom:  ﻿B​l​o​w​f​i​s​h

// block 12
zwsp: E​d​2​5​5​1​9
zwnj: E‌d‌2‌5‌5‌1‌9
zwj:  E‍d‍2‍5‍5‍1‍9
bom:  ﻿E​d​2​5​5​1​9

