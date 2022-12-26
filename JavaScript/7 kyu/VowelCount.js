"use strict";

/* Return the number (count) of vowels in the given string.
We will consider a, e, i, o, u as vowels for this Kata (but not y).
The input string will only consist of lower case letters and/or spaces. */

function getCount(str) {
  const regex = str.match(/[aeiou]/gi);
  return regex ? regex.length : 0;
}

console.log(getCount("abracadabra")); //5

//return (str.match(/[aeiou]/ig)||[]).length; short-circuiting solution
