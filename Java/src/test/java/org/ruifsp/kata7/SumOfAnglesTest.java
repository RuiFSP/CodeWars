package org.ruifsp.kata7;

import org.junit.jupiter.api.Test;

import static org.junit.jupiter.api.Assertions.*;

class SumOfAnglesTest {

    @Test
    void sumOfAngles() {
        assertEquals(180, SumOfAngles.sumOfAngles(3));
        assertEquals(360, SumOfAngles.sumOfAngles(4));
    }
}