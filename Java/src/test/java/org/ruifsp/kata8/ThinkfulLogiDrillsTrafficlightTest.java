package org.ruifsp.kata8;

import org.junit.jupiter.api.Test;

import static org.junit.jupiter.api.Assertions.*;

class ThinkfulLogiDrillsTrafficlightTest {

    @Test
    void updateLight() {
        assertEquals("green", ThinkfulLogiDrillsTrafficlight.updateLight("red"));
        assertEquals("yellow", ThinkfulLogiDrillsTrafficlight.updateLight("green"));
        assertEquals("red", ThinkfulLogiDrillsTrafficlight.updateLight("yellow"));
    }
}