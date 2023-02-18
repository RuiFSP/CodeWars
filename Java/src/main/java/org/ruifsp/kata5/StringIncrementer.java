package org.ruifsp.kata5;

/*
Your job is to write a function which increments a string, to create a new string.

If the string already ends with a number, the number should be incremented by 1.
If the string does not end with a number. the number 1 should be appended to the new string.
Examples:

foo -> foo1

foobar23 -> foobar24

foo0042 -> foo0043

foo9 -> foo10

foo099 -> foo100

Attention: If the number has leading zeros the amount of digits should be considered.
 */


import java.math.BigInteger;

public class StringIncrementer {
    public static String incrementString(String str) {

        // Split the string into a non-number prefix and a number suffix (if any)
        String prefix = str.replaceAll("\\d*$", "");
        String suffix = str.replace(prefix, "");

        if (suffix.length() > 0) {
            // The string already ends with a number
            int numDigits = suffix.length();
            BigInteger num = new BigInteger(suffix).add(BigInteger.ONE);
            String newSuffix = String.format("%0" + numDigits + "d", num);
            return prefix + newSuffix;
        } else {
            // The string does not end with a number
            return str + "1";
        }
    }
}
