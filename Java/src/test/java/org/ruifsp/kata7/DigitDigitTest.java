package org.ruifsp.kata7;

import org.junit.jupiter.api.Test;

import static org.junit.jupiter.api.Assertions.*;

class DigitDigitTest {

    @Test
    void squareDigits() {
        assertEquals(811181, DigitDigit.squareDigits(9119));
        assertEquals(0, DigitDigit.squareDigits(0));
    }
}