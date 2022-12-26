"use strict";
/* 
An isogram is a word that has no repeating letters, consecutive or non-consecutive. Implement a function that determines whether a string that contains only letters is an isogram. Assume the empty string is an isogram. Ignore letter case.

Example: (Input --> Output)

"Dermatoglyphics" --> true
"aba" --> false
"moOse" --> false (ignore letter case) */

//My solution
const isIsogram = (str) =>
  !str
    .toLowerCase()
    .split("")
    .sort()
    .some((el, i, arr) => el === arr[i + 1]);

//Other solutions:
//1) using set and compare it with the original array
//const isIsogram = (str) => new Set(str.toUpperCase()).size == str.length;

//2) using regex
//const isIsogram = (str) => !/(\w).*\1/i.test(str);

console.log(isIsogram("Dermatoglyphics"));
console.log(isIsogram("isogram"));
console.log(isIsogram("aba"));
console.log(isIsogram("moOse"));
console.log(isIsogram("isIsogram"));
console.log(isIsogram(""));
