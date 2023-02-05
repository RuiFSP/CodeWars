package org.ruifsp.kata7;

import org.junit.jupiter.api.Test;

import static org.junit.jupiter.api.Assertions.assertEquals;

class OddOrEvenTest {

    @Test
    void oddOrEven() {
        assertEquals("odd", OddOrEven.oddOrEven(new int[]{2, 5, 34, 6}));
    }
}