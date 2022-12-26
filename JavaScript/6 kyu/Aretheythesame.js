"use strict";

/* Given two arrays a and b write a function comp(a, b) (orcompSame(a, b)) that checks whether the two arrays have the "same" elements, with the same multiplicities (the multiplicity of a member is the number of times it appears). "Same" means, here, that the elements in b are the elements in a squared, regardless of the order. */

/* Remarks
a or b might be [] or {} (all languages except R, Shell).
a or b might be nil or null or None or nothing (except in C++, COBOL, Crystal, D, Dart, Elixir, Fortran, F#, Haskell, Nim, OCaml, Pascal, Perl, PowerShell, Prolog, PureScript, R, Racket, Rust, Shell, Swift).
If a or b are nil (or null or None, depending on the language), the problem doesn't make sense so return false.

Note for C
The two arrays have the same size (> 0) given as parameter in function comp. */

const comp = (array1, array2) => {
  if (array1 == null || array2 == null) return false;

  const arraySquare = array1.map((ele1) => ele1 ** 2).sort();

  return array2.sort().every((val, index) => val === arraySquare[index]);
};

//test data
const a = [121, 144, 19, 161, 19, 144, 19, 11];
const b = [121, 14641, 20736, 361, 25921, 361, 20736, 361];
console.log(comp(a, b));
/*comp(a, b) returns true because in b 121 is the square of 11, 14641 is the square of 121, 20736 the square of 144, 361 the square of 19, 25921 the square of 161, and so on. It gets obvious if we write b's elements in terms of squares: */

const c = [121, 144, 19, 161, 19, 144, 19, 11];
const d = [
  11 * 11,
  121 * 121,
  144 * 144,
  19 * 19,
  161 * 161,
  19 * 19,
  144 * 144,
  19 * 19,
];
console.log(comp(c, d));
/* Invalid arrays
If, for example, we change the first number to something else, comp is not returning true anymore:*/

const e = [121, 144, 19, 161, 19, 144, 19, 11];
const f = [132, 14641, 20736, 361, 25921, 361, 20736, 361];
console.log(comp(e, f));
// comp(a,b) returns false because in b 132 is not the square of any number of a.

const g = [121, 144, 19, 161, 19, 144, 19, 11];
const h = [121, 14641, 20736, 36100, 25921, 361, 20736, 361];
console.log(comp(g, h));
// comp(a,b) returns false because in b 36100 is not the square of any number of a.
