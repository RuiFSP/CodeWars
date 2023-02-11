package org.ruifsp.kata6;

import org.junit.jupiter.api.Test;

import static org.junit.jupiter.api.Assertions.*;

class SumOfDigitsDigitalRootTest {

    @Test
    void digital_root() {
        assertEquals(7, SumOfDigitsDigitalRoot.digital_root(16));
        assertEquals(6, SumOfDigitsDigitalRoot.digital_root(456));
    }
}