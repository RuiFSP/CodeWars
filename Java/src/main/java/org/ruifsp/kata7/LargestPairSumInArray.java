package org.ruifsp.kata7;

/*
Given a sequence of numbers, find the largest pair sum in the sequence.

For example

[10, 14, 2, 23, 19] -->  42 (= 23 + 19)
[99, 2, 2, 23, 19]  --> 122 (= 99 + 23)
Input sequence contains minimum two elements and every element is an integer.
 */

import java.util.Arrays;

public class LargestPairSumInArray {
    public static int largestPairSum(int[] numbers){

        return Arrays.stream(numbers)
                .boxed()
                .sorted((a, b) -> Integer.compare(b, a))
                .limit(2)
                .mapToInt(Integer::intValue)
                .sum();

    }
}
