package org.ruifsp.kata7;

import org.junit.jupiter.api.Test;

import static org.junit.jupiter.api.Assertions.*;

class FindTheNextPerfectSquareTest {

    @Test
    public void test1() {
        assertEquals(144, FindTheNextPerfectSquare.findNextSquare(121));
    }

    @Test
    public void test2() {
        assertEquals(676, FindTheNextPerfectSquare.findNextSquare(625));
    }

    @Test
    public void test3() {
        assertEquals(-1, FindTheNextPerfectSquare.findNextSquare(114));
    }
}