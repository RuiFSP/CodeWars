"use strict";
/* Write a function factorial() that takes a number as an argument and returns the factorial of the number.

Example:

factorial(6); 
// returns `720` because 6 * 5 * 4 * 3 * 2 * 1 = 720 
Assume only positive numbers will be given as an argument for the factorial() function. */

let factorial = (num) => {
  let product = 1;

  for (let i = num; i > 1; i--) {
    console.log(product);
    product *= i;
  }

  return product;
};

console.log(factorial(6));
