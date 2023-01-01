package org.ruifsp.kata6;

import org.junit.jupiter.api.Test;

import static org.junit.jupiter.api.Assertions.*;

class PlayingWithDigitsTest {

    @Test
    void digPow() {
        assertEquals(1, PlayingWithDigits.digPow(89,1));
        assertEquals(-1, PlayingWithDigits.digPow(92,1));
        assertEquals(51, PlayingWithDigits.digPow(46288,3));
    }
}