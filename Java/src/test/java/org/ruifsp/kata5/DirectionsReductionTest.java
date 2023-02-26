package org.ruifsp.kata5;

import org.junit.jupiter.api.Test;

import static org.junit.jupiter.api.Assertions.*;

class DirectionsReductionTest {

    @Test
    void dirReduc() {
        assertArrayEquals(new String[]{"WEST"}, DirectionsReduction.dirReduc(new String[]{"NORTH", "SOUTH", "SOUTH", "EAST", "WEST", "NORTH", "WEST"}));
        assertArrayEquals(new String[]{}, DirectionsReduction.dirReduc(new String[]{"NORTH","SOUTH","SOUTH","EAST","WEST","NORTH"}));

    }

}