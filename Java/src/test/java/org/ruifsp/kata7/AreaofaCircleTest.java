package org.ruifsp.kata7;

import org.junit.jupiter.api.Test;

import static org.junit.jupiter.api.Assertions.*;

class AreaofaCircleTest {

    @Test
    void area() {

        try {
            AreaofaCircle.area(0);
            fail("Radius of 0 should throw an IllegalArgumentException");
        } catch (IllegalArgumentException ignored) {}

        double x = 3D;
        assertEquals(28.27D, AreaofaCircle.area( x), 0.01);

    }
}