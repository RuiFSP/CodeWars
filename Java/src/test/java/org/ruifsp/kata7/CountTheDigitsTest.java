package org.ruifsp.kata7;

import org.junit.jupiter.api.Test;

import static org.junit.jupiter.api.Assertions.*;

class CountTheDigitsTest {
    private static void testing(int actual, int expected) {
        assertEquals(expected, actual);
    }
    @Test
    void nbDig() {
        System.out.println("Fixed Tests nbDig");
        testing(CountTheDigits.nbDig(5750, 0), 4700);
        testing(CountTheDigits.nbDig(11011, 2), 9481);
        testing(CountTheDigits.nbDig(12224, 8), 7733);
        testing(CountTheDigits.nbDig(11549, 1), 11905);
    }
}