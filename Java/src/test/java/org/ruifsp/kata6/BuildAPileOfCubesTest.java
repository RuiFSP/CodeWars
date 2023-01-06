package org.ruifsp.kata6;

import org.junit.jupiter.api.Test;

import static org.junit.jupiter.api.Assertions.*;

class BuildAPileOfCubesTest {

    @Test
    void findNb() {

        assertEquals(2022,BuildAPileOfCubes.findNb(4183059834009L));
        assertEquals(-1,BuildAPileOfCubes.findNb(24723578342962L));
        assertEquals(4824,BuildAPileOfCubes.findNb(135440716410000L));
        assertEquals(3568,BuildAPileOfCubes.findNb(40539911473216L));

    }
}