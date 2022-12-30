package org.ruifsp.kata7;

/*
Given 2 strings, a and b, return a string of the form: shorter+reverse(longer)+shorter.

In other words, the shortest string has to be put as prefix and as suffix of the reverse of the longest.

Strings a and b may be empty, but not null (In C# strings may also be null. Treat them as if they are empty.).
If a and b have the same length treat a as the longer producing b+reverse(a)+b
 */


public class ShorterConcatReverseLonger {
    public static String shorterReverseLonger(String a, String b) {

        StringBuilder str = new StringBuilder();
        StringBuilder strReverse = new StringBuilder();

        if (a.length() >= b.length()) {

            str.append(b).append(strReverse.append(a).reverse()).append(b);

        } else {

            str.append(a).append(strReverse.append(b).reverse()).append(a);

        }
        return str.toString();

    }

}
