package org.ruifsp.kata8;

import org.junit.jupiter.api.Test;

import static org.junit.jupiter.api.Assertions.*;

class PowerOf2Test {

    @Test
    void powersOfTwo() {
        assertArrayEquals(new long[]{1}, PowerOf2.powersOfTwo(0));
        assertArrayEquals(new long[]{1,2}, PowerOf2.powersOfTwo(1));
        assertArrayEquals(new long[]{1,2,4,8,16}, PowerOf2.powersOfTwo(4));
    }
}