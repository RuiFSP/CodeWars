package org.ruifsp.kata7;

import org.junit.jupiter.api.Test;

import static org.junit.jupiter.api.Assertions.*;

class AnagramDetectionTest {

    @Test
    void isAnagram() {
        assertTrue(AnagramDetection.isAnagram("foefet", "toffee"));
        assertTrue(AnagramDetection.isAnagram("Buckethead", "DeathCubeK"));
        assertTrue(AnagramDetection.isAnagram("Twoo", "Woot"));
        assertFalse(AnagramDetection.isAnagram("apple", "pale"));
    }
}