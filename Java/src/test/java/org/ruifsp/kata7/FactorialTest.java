package org.ruifsp.kata7;

import org.junit.jupiter.api.Test;

import static org.junit.jupiter.api.Assertions.*;

class FactorialTest {

    @Test
    void factorial() {
        assertEquals(1L, Factorial.factorial(0));
        assertEquals(1L, Factorial.factorial(1));
        assertEquals(24L, Factorial.factorial(4));
        assertEquals(5040L, Factorial.factorial(7));
    }
}