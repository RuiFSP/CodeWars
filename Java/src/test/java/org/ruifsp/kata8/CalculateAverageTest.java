package org.ruifsp.kata8;

import org.junit.jupiter.api.Test;

import static org.junit.jupiter.api.Assertions.*;

class CalculateAverageTest {

    private static final double DELTA = 1e-15;

    @Test
    void find_average() {

        assertEquals(1,CalculateAverage.find_average(new int[]{1,1,1}),DELTA);
        assertEquals(2,CalculateAverage.find_average(new int[]{1,2,3}),DELTA);
        assertEquals(0,CalculateAverage.find_average(new int[]{}),DELTA);

    }
}