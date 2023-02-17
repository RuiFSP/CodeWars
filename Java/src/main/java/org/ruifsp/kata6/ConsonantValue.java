package org.ruifsp.kata6;

/*
Given a lowercase string that has alphabetic characters only and no spaces, return the highest
value of consonant substrings. Consonants are any letters of the alphabet except "aeiou".

We shall assign the following values: a = 1, b = 2, c = 3, .... z = 26.

For example, for the word "zodiacs", let's cross out the vowels. We get: "z o d ia cs"

-- The consonant substrings are: "z", "d" and "cs" and the values are z = 26, d = 4 and cs = 3 + 19 = 22.
The highest is 26.
solve("zodiacs") = 26

For the word "strength", solve("strength") = 57
-- The consonant substrings are: "str" and "ngth" with values "str" = 19 + 20 + 18 = 57 and
"ngth" = 14 + 7 + 20 + 8 = 49. The highest is 57.
 */


public class ConsonantValue {
    public static int solve(final String s) {
        int maxValue = 0;
        int currentValue = 0;
        for (int i = 0; i < s.length(); i++) {
            char c = s.charAt(i);
            if ("aeiou".indexOf(c) == -1) {
                currentValue += c - 'a' + 1;
            } else {
                if (currentValue > maxValue) {
                    maxValue = currentValue;
                }
                currentValue = 0;
            }
        }
        if (currentValue > maxValue) {
            maxValue = currentValue;
        }
        return maxValue;
    }
}

/*
functional approach

import static java.util.stream.Stream.of;

class ConsonantValue {
  static int solve(String s) {
    return of(s.split("[aeiou]")).mapToInt(con -> con.chars().map(c -> c - 96).sum()).max().orElse(0);
  }
}
*/