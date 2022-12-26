package org.ruifsp.kata7;

/*
An anagram is the result of rearranging the letters of a word to produce a new word (see wikipedia).

Note: anagrams are case insensitive

Complete the function to return true if the two arguments given are anagrams of each other; return false otherwise.

Examples
"foefet" is an anagram of "toffee"

"Buckethead" is an anagram of "DeathCubeK"
 */

import java.util.Arrays;

public class AnagramDetection {
    public static boolean isAnagram(String test, String original) {
        // your code goes here

        char[] charArrayTest = test.toLowerCase().toCharArray();
        char[] charArrayOriginal = original.toLowerCase().toCharArray();

        Arrays.sort(charArrayTest);
        Arrays.sort(charArrayOriginal);

        return Arrays.equals(charArrayTest, charArrayOriginal);
    }

}
