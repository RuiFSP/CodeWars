"use strict";
/* Consider an array/list of sheep where some sheep may be missing from their place. We need a function that counts the number of sheep present in the array (true means present).

For example, */

data = [
  true,
  true,
  true,
  false,
  true,
  true,
  true,
  true,
  true,
  false,
  true,
  false,
  true,
  false,
  false,
  true,
  true,
  true,
  true,
  true,
  false,
  false,
  true,
  true,
];

//const countSheeps = (arrayOfSheep) =>
// arrayOfSheep.filter((el) => el == true).length;

//alternative with object Boolean
const countSheeps = (arrayOfSheep) => arrayOfSheep.filter(Boolean).length;

console.log(countSheeps(data));
