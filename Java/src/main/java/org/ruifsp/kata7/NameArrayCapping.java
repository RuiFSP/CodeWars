package org.ruifsp.kata7;

/*
Create a method that accepts an array of names, and returns an array of each name with its first letter capitalized.

example

Kata.capMe(new String[] {"jo", "nelson", "jelly"}) // returns new String[] {"Jo", "Nelson", "Jelly"}
Kata.capMe(new String[] {"KARLY", "DANIEL", "KELSEY"}) // returns new String[] {"Karly", "Daniel", "Kelsey"}
 */

import java.util.Arrays;

public class NameArrayCapping {
    public static String[] capMe(String[] strings) {

        return Arrays.stream(strings)
                .map(word -> word.substring(0, 1).toUpperCase() + word.substring(1).toLowerCase())
                .toArray(String[]::new);
    }
}
