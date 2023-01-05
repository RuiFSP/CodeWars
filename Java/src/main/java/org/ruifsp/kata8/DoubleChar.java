package org.ruifsp.kata8;

/*
Given a string, you have to return a string in which each character (case-sensitive) is repeated once.

Examples (Input -> Output):
* "String"      -> "SSttrriinngg"
* "Hello World" -> "HHeelllloo  WWoorrlldd"
* "1234!_ "     -> "11223344!!__  "
 */

import java.util.Arrays;
import java.util.stream.Collectors;

public class DoubleChar {
    public static String doubleChar(String s){
        //enter your code here

        return Arrays.stream(s.split(""))
                .map(letter -> letter+letter)
                .collect(Collectors.joining());
    }

}
