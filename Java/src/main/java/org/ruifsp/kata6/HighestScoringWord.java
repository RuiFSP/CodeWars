package org.ruifsp.kata6;

/*
Given a string of words, you need to find the highest scoring word.

Each letter of a word scores points according to its position in the alphabet: a = 1, b = 2, c = 3 etc.

For example, the score of abad is 8 (1 + 2 + 1 + 4).

You need to return the highest scoring word as a string.

If two words score the same, return the word that appears earliest in the original string.

All letters will be lowercase and all inputs will be valid.
 */

public class HighestScoringWord {
    public static String high(String s) {

        String alphabet = "abcdefghijklmnopqrstuvwxyz";

        String[] arr = s.split(" ");
        int max_sum = 0;
        String max_word = "";

        for (String value : arr) {

            int sum = 0;

            for (int i = 0; i < value.length(); i++) {
                sum += alphabet.indexOf(value.charAt(i)) + 1;
            }

            if (sum > max_sum) {
                max_sum = sum;
                max_word = value;
            }

        }

        return max_word;
    }
}

/*
top voted solution

import java.util.*;

public class Kata {
  public static String high(String s) {
    return Arrays.stream(s.split(" "))
                .max(Comparator.comparingInt(
                        a -> a.chars().map(i -> i - 96).sum()
                )).get();
  }
}

 */


