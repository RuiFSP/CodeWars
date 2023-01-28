package org.ruifsp.kata7;

import org.junit.jupiter.api.Test;

import static org.junit.jupiter.api.Assertions.*;

class SimpleFun176ReverseLetterTest {
    private void doTest(final String str, final String expected) {
        assertEquals(expected, SimpleFun176ReverseLetter.reverseLetter(str));
    }

    @Test
    public void testSomething() {
        doTest("krishan", "nahsirk");
        doTest("ultr53o?n", "nortlu");
        doTest("ab23c", "cba");
        doTest("krish21an", "nahsirk");
    }
}