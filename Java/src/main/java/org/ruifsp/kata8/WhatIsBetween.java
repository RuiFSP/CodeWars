package org.ruifsp.kata8;

/*
Complete the function that takes two integers (a, b, where a < b) and return an array
of all integers between the input parameters, including them.

For example:

a = 1
b = 4
--> [1, 2, 3, 4]

 */

import java.util.stream.IntStream;

public class WhatIsBetween {
    public static int[] between(int a, int b) {
        // your code here
        return IntStream.rangeClosed(a,b).toArray();
    }
}
