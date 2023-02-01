package org.ruifsp.kata6;

import org.junit.jupiter.api.Test;

import static org.junit.jupiter.api.Assertions.*;

class ReverseOrRotateTest {
    private static void testing(String actual, String expected) {
        assertEquals(expected, actual);
    }
    @Test
    void revRot() {
        System.out.println("Fixed Tests: revRot");
        testing(ReverseOrRotate.revRot("1234", 0), "");
        testing(ReverseOrRotate.revRot("", 0), "");
        testing(ReverseOrRotate.revRot("1234", 5), "");
        String s = "733049910872815764";
        testing(ReverseOrRotate.revRot(s, 5), "330479108928157");
    }
}