package org.ruifsp.kata8;

/*
Write a function which calculates the average of the numbers in a given list.
Note: Empty arrays should return 0.
*/

import java.util.Arrays;

public class CalculateAverage {
    public static double find_average(int[] array){
        return Arrays.stream(array).average().orElse(0);
    }
}

