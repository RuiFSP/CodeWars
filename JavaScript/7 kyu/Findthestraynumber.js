"use strict";

/* You are given an odd-length array of integers, in which all of them are the same, except for one single number.

Complete the method which accepts such an array, and returns that single different number.

The input array will always be valid! (odd-length >= 3)

Examples
[1, 1, 2] ==> 2
[17, 17, 3, 17, 17, 17, 17] ==> 3 */

//using filter
const stray = (numbers) =>
  numbers.find((el) => numbers.indexOf(el) === numbers.lastIndexOf(el));

console.log(stray([(1, 1, 2)]));
