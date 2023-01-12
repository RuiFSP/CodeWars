package org.ruifsp.kata7;

import org.junit.jupiter.api.Test;

import static org.junit.jupiter.api.Assertions.*;

class GrownOfAPopulationTest {

    private static void testing(int actual, int expected) {
        assertEquals(expected, actual);
    }
    @Test
    void nbYear() {
        System.out.println("Fixed Tests: nbYear");
        testing(GrownOfAPopulation.nbYear(1500, 5, 100, 5000),15);
        testing(GrownOfAPopulation.nbYear(1500000, 2.5, 10000, 2000000), 10);
        testing(GrownOfAPopulation.nbYear(1500000, 0.25, 1000, 2000000), 94);
    }
}