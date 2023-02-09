package org.ruifsp.kata8;

import org.junit.jupiter.api.Test;

import static org.junit.jupiter.api.Assertions.*;

class ConverNumberToReverseArrayOfDigitsTest {

    @Test
    void digitize() {
        assertArrayEquals(new int[] {1, 3, 2, 5, 3}, ConverNumberToReverseArrayOfDigits.digitize(35231));
        assertArrayEquals(new int[] {0}, ConverNumberToReverseArrayOfDigits.digitize(0));
    }
}