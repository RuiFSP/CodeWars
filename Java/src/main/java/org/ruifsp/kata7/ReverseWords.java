package org.ruifsp.kata7;

import java.util.Arrays;
import java.util.stream.Collectors;

/*
Complete the function that accepts a string parameter, and reverses each word in the string. All spaces in the string should be retained.

Examples
"This is an example!" ==> "sihT si na !elpmaxe"
"double  spaces"      ==> "elbuod  secaps"
 */

public class ReverseWords {
    public static String reverseWords(final String original) {

        String[] words = original.split(" ");

        //to pass the condition if it has only spaces
        if (words.length == 0) {
            return original;
        }

        return Arrays.stream(words)
                .map(word -> new StringBuilder(word).reverse().toString())
                .collect(Collectors.joining(" "));
    }
}