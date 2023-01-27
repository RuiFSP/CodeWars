package org.ruifsp.kata7;

/*
Given a string, capitalize the letters that occupy even indexes and odd indexes separately,
and return as shown below. Index 0 will be considered even.

For example, capitalize("abcdef") = ['AbCdEf', 'aBcDeF']. See test cases for more examples.

The input will be a lowercase string with no spaces.

Good luck!
 */

public class AlternateCapitalization {
    public static String[] capitalize(String s){

        StringBuilder evenUpperCase = new StringBuilder();
        StringBuilder oddUpperCase = new StringBuilder();

        for (int i = 0; i < s.toCharArray().length; i++) {
            char ch = s.charAt(i);

            if(i % 2 == 0) {
                evenUpperCase.append(Character.toUpperCase(ch));
                oddUpperCase.append(Character.toLowerCase(ch));
            } else {
                evenUpperCase.append(Character.toLowerCase(ch));
                oddUpperCase.append(Character.toUpperCase(ch));
            }

        }
        return new String[] {evenUpperCase.toString(),oddUpperCase.toString()};

    }

}
