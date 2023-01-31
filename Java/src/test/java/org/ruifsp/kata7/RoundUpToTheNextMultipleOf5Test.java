package org.ruifsp.kata7;

import org.junit.jupiter.api.Test;

import java.util.Arrays;

import static org.junit.jupiter.api.Assertions.*;

class RoundUpToTheNextMultipleOf5Test {

    @Test
    public void basicTests() {
        int[][] arr = {
                {0, 0},
                {1, 5},
                {3, 5},
                {5, 5},
                {7, 10},
                {39, 40}
        };
        Arrays.stream(arr)
                .forEach(
                        (testCase) -> assertEquals(
                                testCase[1],
                                RoundUpToTheNextMultipleOf5.roundToNext5(testCase[0])));
    }
}