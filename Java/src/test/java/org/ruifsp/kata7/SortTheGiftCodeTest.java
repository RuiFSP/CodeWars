package org.ruifsp.kata7;

import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.*;


class SortTheGiftCodeTest {

    @Test
    void sortGiftCode1(){

        SortTheGiftCode gs = new SortTheGiftCode();
        assertEquals("abcdef",gs.sortGiftCode("fedcba"));
    }

    @Test
    void sortGiftCode2(){

        SortTheGiftCode gs = new SortTheGiftCode();
        assertEquals("abcdefghijklmnopqrstuvwxyz",gs.sortGiftCode("zyxwvutsrqponmlkjihgfedcba"));
    }
}