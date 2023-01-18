package org.ruifsp.kata8;

/*
Given an array of integers.

Return an array, where the first element is the count of positives numbers and the second element is
sum of negative numbers. 0 is neither positive nor negative.

If the input is an empty array or is null, return an empty array.

Example
For input [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, -11, -12, -13, -14, -15], you should return [10, -65].
 */


public class CountPositivesSumNegatives {
    public static int[] countPositivesSumNegatives(int[] input) {

        int count_positives = 0;
        int sum_negatives = 0;

        if (input == null || input.length == 0) return new int[0];

        for (int j : input) {

            if (j > 0) {
                count_positives += 1;
            } else {
                sum_negatives += j;
            }

        }

        return new int[]{count_positives, sum_negatives};
    }
}
