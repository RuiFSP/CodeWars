package org.ruifsp.kata7;

/*
Write a function that can return the smallest value of an array or the index of that value.
The function's 2nd parameter will tell whether it should return the value or the index.

Assume the first parameter will always be an array filled with at least 1 number and no duplicates.
Assume the second parameter will be a string holding one of two values: 'value' and 'index'.

Arrays.findSmallest(new int[]{1,2,3,4,5}, 'value') // => 1
Arrays.findSmallest(new int[]{1,2,3,4,5}, 'index') // => 0
 */

import java.util.Objects;
import java.util.stream.IntStream;

public class SmallestValueOfAnArray {
    public static int findSmallest( final int[] numbers, final String toReturn ) {

        int minValue = IntStream.of(numbers)
                .min()
                .orElse(0);

        int minIndex = IntStream.of(numbers)
                .boxed()
                .toList()
                .indexOf(minValue);

        return Objects.equals(toReturn, "value") ? minValue : minIndex;
    }

}
