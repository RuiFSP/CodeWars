package org.ruifsp.kata6;

import org.junit.jupiter.api.Test;

import static org.junit.jupiter.api.Assertions.*;

class GiveMeADiamondTest {

    @Test
    public void testDiamond3() {
        String expected = """
                 *
                ***
                 *
                """;

        assertEquals(expected, GiveMeADiamond.print(3));
    }

    @Test
    public void testDiamond5() {
        String expected = """
                  *
                 ***
                *****
                 ***
                  *
                """;

        assertEquals(expected, GiveMeADiamond.print(5));
    }

    @Test
    public void testDiamond1() {
        assertEquals("*\n", GiveMeADiamond.print(1));
    }

    @Test
    public void testDiamond0() {
        assertNull(GiveMeADiamond.print(0));
    }

    @Test
    public void testDiamondMinus2() {
        assertNull(GiveMeADiamond.print(-2));
    }

    @Test
    public void testDiamond2() {
        assertNull(GiveMeADiamond.print(2));
    }
}