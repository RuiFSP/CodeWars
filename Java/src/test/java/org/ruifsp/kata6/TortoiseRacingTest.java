package org.ruifsp.kata6;

import org.junit.jupiter.api.Test;

import static org.junit.jupiter.api.Assertions.*;

class TortoiseRacingTest {

    @Test
    public void test1() {
        System.out.println("Basic Tests");
        assertArrayEquals(new int[]{0, 32, 18}, TortoiseRacing.race(720, 850, 70));
        assertArrayEquals(new int[]{3, 21, 49}, TortoiseRacing.race(80, 91, 37));
        assertArrayEquals(new int[]{2, 0, 0}, TortoiseRacing.race(80, 100, 40));
    }
}