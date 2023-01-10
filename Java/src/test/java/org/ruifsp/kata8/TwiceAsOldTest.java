package org.ruifsp.kata8;

import org.junit.jupiter.api.Test;

import static org.junit.jupiter.api.Assertions.*;

class TwiceAsOldTest {

    @Test
    void twiceAsOld() {
        assertEquals(30, TwiceAsOld.TwiceAsOldFunc(30,0));
        assertEquals(16, TwiceAsOld.TwiceAsOldFunc(30,7));
        assertEquals(15, TwiceAsOld.TwiceAsOldFunc(45,30));
    }
}