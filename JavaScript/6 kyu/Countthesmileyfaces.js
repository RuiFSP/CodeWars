"use strict";
/* Given an array (arr) as an argument complete the function countSmileys that should return the total number of smiling faces.

Rules for a smiling face:

Each smiley face must contain a valid pair of eyes. Eyes can be marked as : or ;
A smiley face can have a nose but it does not have to. Valid characters for a nose are - or ~
Every smiling face must have a smiling mouth that should be marked with either ) or D
No additional characters are allowed except for those mentioned.

Valid smiley face examples: :) :D ;-D :~)
Invalid smiley faces: ;( :> :} :]

Note
In case of an empty array return 0. You will not be tested with invalid input (input will always be an array). Order of the face (eyes, nose, mouth) elements will always be the same. */

const countSmileys = (str) => {
  //valid smiles to lookfor
  const regexExp = /(:|;)(-|~)?(\)|D)/;

  return str.filter((v) => v.match(regexExp)).length;
};

//Test Data

console.log(countSmileys([":)", ";(", ";}", ":-D"])); // should return 2;
console.log(countSmileys([";D", ":-(", ":-)", ";~)"])); // should return 3;
console.log(countSmileys([";]", ":[", ";*", ":$", ";-D"])); // should return 1;
console.log(countSmileys([":>", ";)", ":)", ":)", ":o)", ":~D", ":~D"])); //should return 5
