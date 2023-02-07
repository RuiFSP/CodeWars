package org.ruifsp.kata7;

import org.junit.jupiter.api.Test;

import static org.junit.jupiter.api.Assertions.*;

class IsThisATriangleTest {

    @Test
    void isTriangle() {
        assertTrue(IsThisATriangle.isTriangle(1, 2, 2));
        assertFalse(IsThisATriangle.isTriangle(7, 2, 2));
    }
}