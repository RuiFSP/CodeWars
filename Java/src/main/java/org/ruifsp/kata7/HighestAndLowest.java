package org.ruifsp.kata7;

/*
In this little assignment you are given a string of space separated numbers, and have to return the highest
and lowest number.

Notes
All numbers are valid Int32, no need to validate them.
There will always be at least one number in the input string.
Output string must be two numbers separated by a single space, and highest number is first.
 */

import java.util.Arrays;
import java.util.IntSummaryStatistics;

public class HighestAndLowest {
    public static String highAndLow(String numbers) {

        IntSummaryStatistics summaryData = Arrays
                .stream(numbers.split(" "))
                .mapToInt(Integer::parseInt)
                .summaryStatistics();

        return String.format("%d %d", summaryData.getMax(), summaryData.getMin());

    }

}


