package org.ruifsp.kata7;

import org.junit.jupiter.api.Test;

import static org.junit.jupiter.api.Assertions.*;

class BreakingChocolateProblemTest {

    @Test
    void breakChocolate() {

        assertEquals(24, BreakingChocolateProblem.breakChocolate(5,5),"The answer for 5x5 should be 24");
        assertEquals(0, BreakingChocolateProblem.breakChocolate(1,1),"The answer for 1x1 should be 0");
    }
}