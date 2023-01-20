package org.ruifsp.kata6;

/*
There is an array with some numbers. All numbers are equal except for one. Try to find it!

It’s guaranteed that array contains at least 3 numbers.

The tests contain some very huge arrays, so think about performance.

 */

import java.util.Arrays;

public class FindTheUniqueNumber {
    public static double findUniq(double[] arr) {
        // Do the magic
        Arrays.sort(arr);
        return arr[0] != arr[1] ? arr[0] : arr[arr.length-1];
    }
}
