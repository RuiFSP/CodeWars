package org.ruifsp.kata8;

import org.junit.jupiter.api.Test;

import static org.junit.jupiter.api.Assertions.*;

class KeepUpTheLoopTest {

    @Test
    void hoopCount() {
        assertEquals("Great, now move on to tricks", KeepUpTheLoop.hoopCount(11));
        assertEquals("Keep at it until you get it", KeepUpTheLoop.hoopCount(7));
    }
}