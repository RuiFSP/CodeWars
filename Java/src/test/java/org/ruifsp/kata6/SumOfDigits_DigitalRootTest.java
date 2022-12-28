package org.ruifsp.kata6;

import org.junit.jupiter.api.Test;

import static org.junit.jupiter.api.Assertions.*;

class SumOfDigits_DigitalRootTest {

    @Test
    void digital_root() {
        assertEquals(7, SumOfDigits_DigitalRoot.digital_root(16));
        assertEquals(6, SumOfDigits_DigitalRoot.digital_root(456));
    }
}