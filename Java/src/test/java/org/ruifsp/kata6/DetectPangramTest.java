package org.ruifsp.kata6;

import org.junit.jupiter.api.Test;

import static org.junit.jupiter.api.Assertions.*;

class DetectPangramTest {


    @Test
    void check1() {
        String pangram1 = "The quick brown fox jumps over the lazy dog.";
        DetectPangram pg = new DetectPangram();
        assertTrue(pg.check(pangram1));
    }
    @Test
    void check2() {
        String pangram2 = "You shall not pass!";
        DetectPangram pg = new DetectPangram();
        assertFalse(pg.check(pangram2));
    }
    @Test
    void check3() {
        String pangram3 = "Jackdaws love my big sphinx of quartz";
        DetectPangram pg = new DetectPangram();
        assertTrue(pg.check(pangram3));
    }


}