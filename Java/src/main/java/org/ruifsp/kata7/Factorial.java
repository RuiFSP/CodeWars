package org.ruifsp.kata7;

/*
Your task is to write function factorial.

https://en.wikipedia.org/wiki/Factorial
 */

public class Factorial {
    public static long factorial(int n) {

        return n <= 1 ? 1 : n * factorial(n - 1);
    }
}
