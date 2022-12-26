package org.ruifsp.kata8;

import org.junit.jupiter.api.Test;

import static org.junit.jupiter.api.Assertions.*;

class MultiplyTest {

    @Test
    void multiply() {
        assertEquals(10.0,Multiply.multiply(2.0,5.0));
    }
}