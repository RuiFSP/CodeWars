package org.ruifsp.Kata4;

/*
Write a function that takes a positive integer and returns the next smaller positive integer containing the same digits.

For example:

nextSmaller(21) == 12
nextSmaller(531) == 513
nextSmaller(2071) == 2017
Return -1 (for Haskell: return Nothing, for Rust: return None), when there is no smaller number that contains
the same digits. Also return -1 when the next smaller number with the same digits would require
the leading digit to be zero.

nextSmaller(9) == -1
nextSmaller(111) == -1
nextSmaller(135) == -1
nextSmaller(1027) == -1 // 0721 is out since we don't write numbers with leading zeros
some tests will include very large numbers.
test data only employs positive integers.
The function you write for this challenge is the inverse of this kata: "Next bigger number with the same digits."
 */

import java.util.Arrays;

public class NextSmallerNumberWithTheSameDigits {
    public static long nextSmaller(long n) {
        // Convert the number to an array of digits
        char[] digits = Long.toString(n).toCharArray();

        // Find the largest index i such that digits[i] > digits[i+1]
        int i = digits.length - 2;
        while (i >= 0 && digits[i] <= digits[i+1]) {
            i--;
        }

        if (i < 0) {
            // There is no smaller number with the same digits
            return -1;
        }

        // Find the largest index j such that digits[j] < digits[i]
        int j = digits.length - 1;
        while (j >= 0 && digits[j] >= digits[i]) {
            j--;
        }

        // Swap digits[i] and digits[j]
        char temp = digits[i];
        digits[i] = digits[j];
        digits[j] = temp;

        // Reverse the suffix starting at i+1
        Arrays.sort(digits, i+1, digits.length);
        for (int k = i+1, l = digits.length-1; k < l; k++, l--) {
            char tmp = digits[k];
            digits[k] = digits[l];
            digits[l] = tmp;
        }

        String result = new String(digits);

        if (result.charAt(0) == '0') {
            // The next smaller number requires a leading zero, which is not allowed
            return -1;
        } else {
            return Long.parseLong(result);
        }
    }
}
