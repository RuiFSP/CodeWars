package org.ruifsp.kata8;

import org.junit.jupiter.api.Test;

import static org.junit.jupiter.api.Assertions.*;

class BeginnerSeries4CockroachTest {

    @Test
    void cockroachSpeed() {

        BeginnerSeries4Cockroach cockroach = new BeginnerSeries4Cockroach();

        assertEquals(30, cockroach.cockroachSpeed(1.08));
        assertEquals(30, cockroach.cockroachSpeed(1.09));
        assertEquals(0, cockroach.cockroachSpeed(0));

    }
}