"use strict";

/* Complete the solution so that the function will break up camel casing, using a space between words.

Example
"camelCasing"  =>  "camel Casing"
"identifier"   =>  "identifier"
""             =>  "" */

const solution = (string) =>
  [...string].map((el) => el.replace(/[A-Z]/g, ` ${el}`)).join("");

// another solution
/* function solution(string) {
  return(string.replace(/([A-Z])/g, ' $1'));

} */

//test
console.log(solution("camelCasingTest"));
