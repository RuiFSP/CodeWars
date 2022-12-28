package org.ruifsp.kata7;

import org.junit.jupiter.api.Test;

import static org.junit.jupiter.api.Assertions.*;

class ArithmeticSequenceTest {

    @Test
    void nthterm() {
        assertEquals(55,ArithmeticSequence.nthterm(0,55,1));
        assertEquals(500,ArithmeticSequence.nthterm(0,100,5));
        assertEquals(42,ArithmeticSequence.nthterm(14,4,7));
        assertEquals(5050,ArithmeticSequence.nthterm(10000,99,-50));
        assertEquals(4500,ArithmeticSequence.nthterm(10000,110,-50));
        assertEquals(99,ArithmeticSequence.nthterm(0,99,1));
    }
}