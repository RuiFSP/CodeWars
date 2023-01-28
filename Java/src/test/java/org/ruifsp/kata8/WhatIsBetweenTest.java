package org.ruifsp.kata8;

import org.junit.jupiter.api.Test;

import static org.junit.jupiter.api.Assertions.*;

class WhatIsBetweenTest {

    @Test
    void between() {
        assertArrayEquals(new int[]{1, 2, 3, 4}, WhatIsBetween.between(1, 4));
        assertArrayEquals(new int[]{-2, -1, 0, 1, 2}, WhatIsBetween.between(-2, 2));
    }
}