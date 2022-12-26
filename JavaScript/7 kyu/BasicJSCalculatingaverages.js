"use strict";

/* Let's build a calculator that can calculate the average for an arbitrary number of arguments.

The test expects you to provide a Calculator object with an average method:

Calculator.average()
The test also expects that when you pass no arguments, it returns 0. The arguments are expected to be integers.

It expects Calculator.average(3,4,5) to return 4. */
var Calculator = {
  average: (...args) =>
    args.length == 0 ? 0 : args.reduce((a, b) => b + a) / args.length,
};

//test data
console.log(Calculator.average(3, 4, 5));
//Calculator.average(3, 4, 5, 6, 7, 8, 9, 8, 7, 6, 5, 4, 3);
//Calculator.average();
