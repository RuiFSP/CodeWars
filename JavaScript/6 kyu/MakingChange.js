"use strict";

/* Making Change
Complete the method that will determine the minimum number of coins needed to make change for a given amount in American currency.

Coins used will be half-dollars, quarters, dimes, nickels, and pennies, worth 50¢, 25¢, 10¢, 5¢ and 1¢, respectively. They'll be represented by the symbols H, Q, D, N and P (symbols in Ruby, strings in in other languages)

The argument passed in will be an integer representing the value in cents. The return value should be a hash/dictionary/object with the symbols as keys, and the numbers of coins as values. Coins that are not used should not be included in the hash. If the argument passed in is 0, then the method should return an empty hash.

Examples
makeChange(0)   //-->  {}
makeChange(1)   //-->  {"P":1}
makeChange(43)  //-->  {"Q":1, "D":1, "N":1, "P":3}
makeChange(91)  //-->  {"H":1, "Q":1, "D":1, "N":1, "P":1} */

//half-dollars - 50¢ - H
//quarters - 25¢ - Q
//dimes - 10¢ - D
//nickels - 5¢ - N
//pennie - 1¢  P

const makeChange = (amount) => {
  const obj = { H: 50, Q: 25, D: 10, N: 5, P: 1 };
  const output = {};

  Object.entries(obj).forEach(([key, value]) => {
    if (amount / value > 0) {
      output[key] = Math.floor(amount / value);
      amount %= value;
    }
  });

  Object.keys(output).forEach((key) => {
    if (output[key] === 0) {
      delete output[key];
    }
  });

  return output;
};

console.log(makeChange(43));
console.log(makeChange(0));
