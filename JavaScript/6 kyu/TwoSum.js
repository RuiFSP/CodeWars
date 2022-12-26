"use strict";

/* Write a function that takes an array of numbers (integers for the tests) and a target number. It should find two different items in the array that, when added together, give the target value. The indices of these items should then be returned in a tuple / list (depending on your language) like so: (index1, index2).

For the purposes of this kata, some tests may have multiple answers; any valid solutions will be accepted.

The input will always be valid (numbers will be an array of length 2 or greater, and all of the items will be numbers; target will always be the sum of two different items from that array).

Based on: http://oj.leetcode.com/problems/two-sum/

twoSum([1, 2, 3], 4) // returns [0, 2] or [2, 0] */

//my solution
const twoSum = (numbers, target) => {
  const pairCombinations = numbers.flatMap((v, i) =>
    numbers.slice(i + 1).map((w) => [v, w])
  );

  const sumNumbers = (arr) => arr.reduce((acc, cur) => acc + cur);

  const finalArray = [];

  pairCombinations.map((el) => {
    if (sumNumbers(el) === Number(target)) finalArray.push(el);
  });

  const [index1, index2] = finalArray.flat();

  return index1 !== index2
    ? [numbers.indexOf(index1), numbers.indexOf(index2)]
    : [numbers.indexOf(index1), numbers.indexOf(index2) + 1];
};

//better solution
/* function twoSum(numbers, target) {
  for (var i = 0; i < numbers.length-1; i++) {
      for (var j = i+1; j < numbers.length; j++) {
          if (numbers[i] + numbers[j] === target) return [i, j];
      }
  }
} */

//console.log(twoSum([1, 2, 3], 4));
//console.log(twoSum([1234, 5678, 9012], 14690));
console.log(twoSum([2, 2, 3], 4));
console.log(twoSum([2, 3, 1], 4));
