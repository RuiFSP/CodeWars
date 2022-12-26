"use strict";

/* Task
You will be given an array of numbers. You have to sort the odd numbers in ascending order while leaving the even numbers at their original positions.

Examples
[7, 1]  =>  [1, 7]
[5, 8, 6, 3, 4]  =>  [3, 8, 6, 5, 4]
[9, 8, 7, 6, 5, 4, 3, 2, 1, 0]  =>  [1, 8, 3, 6, 5, 4, 7, 2, 9, 0] */

const sortArray = (array) => {
  //Get odd numbers from array and sort them
  const odds = array.filter((x) => x % 2).sort((a, b) => a - b);

  //evaluates each number in array if x% 2 is true , then removes saved value in odds array and place it in array, else keeps the number from original array
  return array.map((x) => (x % 2 ? odds.shift() : x));
};

console.log(sortArray([1, 11, 2, 8, 3, 4, 5]));
