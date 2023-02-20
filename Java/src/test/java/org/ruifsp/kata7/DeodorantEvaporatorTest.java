package org.ruifsp.kata7;

import org.junit.jupiter.api.Test;

import static org.junit.jupiter.api.Assertions.*;

class DeodorantEvaporatorTest {

    @Test
    void evaporator() {
        assertEquals(22 , DeodorantEvaporator.evaporator(10, 10, 10));
    }
}