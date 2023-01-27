package org.ruifsp.kata7;

import org.junit.jupiter.api.Test;

import static org.junit.jupiter.api.Assertions.*;

class AlternateCapitalizationTest {

    @Test
    void capitalize() {
        assertArrayEquals(new String[]{"AbCdEf", "aBcDeF"}, AlternateCapitalization.capitalize("abcdef"));
        assertArrayEquals(new String[]{"CoDeWaRs", "cOdEwArS"}, AlternateCapitalization.capitalize("codewars"));
        assertArrayEquals(new String[]{"AbRaCaDaBrA", "aBrAcAdAbRa"}, AlternateCapitalization.capitalize("abracadabra"));
        assertArrayEquals(new String[]{"CoDeWaRrIoRs", "cOdEwArRiOrS"}, AlternateCapitalization.capitalize("codewarriors"));
    }
}