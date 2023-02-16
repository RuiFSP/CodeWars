package org.ruifsp.kata7;

import org.junit.jupiter.api.Test;

import static org.junit.jupiter.api.Assertions.*;

class LargestPairSumInArrayTest {

    @Test
    void largestPairSum() {
        assertEquals(42, LargestPairSumInArray.largestPairSum(new int[]{10,14,2,23,19}));
        assertEquals(0, LargestPairSumInArray.largestPairSum(new int[]{-100,-29,-24,-19,19}));
        assertEquals(10, LargestPairSumInArray.largestPairSum(new int[]{1,2,3,4,6,-1,2}));
        assertEquals(-18, LargestPairSumInArray.largestPairSum(new int[]{-10,-8,-16,-18,-19}));
    }
}