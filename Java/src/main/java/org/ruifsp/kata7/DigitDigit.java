package org.ruifsp.kata7;

/*
Welcome. In this kata, you are asked to square every digit of a number and concatenate them.

For example, if we run 9119 through the function, 811181 will come out, because 92 is 81 and 12 is 1. (81-1-1-81)

Example #2: An input of 765 will/should return 493625 because 72 is 49, 62 is 36, and 52 is 25. (49-36-35)

Note: The function accepts an integer and returns an integer.

Happy Coding!
 */


import java.math.BigDecimal;

public class DigitDigit {
    public static int squareDigits(int n) {

        String number = Integer.toString(n);
        StringBuilder final_number = new StringBuilder();

        for (int i = 0; i < number.length(); i++) {
            String digit = String.valueOf(number.charAt(i));

            final_number.append(BigDecimal.valueOf(Math.pow(Integer.parseInt(digit), 2)).stripTrailingZeros());
            System.out.println(final_number);
        }

        return Integer.parseInt(final_number.toString());
    }
}

/*
functional approach
import java.util.stream.Collectors;

public class SquareDigit {

    public int squareDigits(int n) {
        return Integer.parseInt(String.valueOf(n)
                                      .chars()
                                      .map(i -> Integer.parseInt(String.valueOf((char) i)))
                                      .map(i -> i * i)
                                      .mapToObj(String::valueOf)
                                      .collect(Collectors.joining("")));
    }

}

 */