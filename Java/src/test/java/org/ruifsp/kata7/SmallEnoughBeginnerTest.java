package org.ruifsp.kata7;

import org.junit.jupiter.api.Test;

import static org.junit.jupiter.api.Assertions.*;

class SmallEnoughBeginnerTest {

    @Test
    void smallEnough() {
        assertTrue(SmallEnoughBeginner.smallEnough(new int[]{66, 101}, 200));
        assertFalse(SmallEnoughBeginner.smallEnough(new int[]{78, 117, 110, 99, 104, 117, 107, 115}, 100));
        assertTrue(SmallEnoughBeginner.smallEnough(new int[]{101, 45, 75, 105, 99, 107}, 107));
        assertTrue(SmallEnoughBeginner.smallEnough(new int[]{80, 117, 115, 104, 45, 85, 112, 115}, 120));
    }
}