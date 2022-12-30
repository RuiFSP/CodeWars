package org.ruifsp.kata7;

import org.junit.jupiter.api.Test;

import static org.junit.jupiter.api.Assertions.*;

class ShorterConcatReverseLongerTest {

    @Test
    void shorterReverseLonger() {

        assertEquals("abcdetsrifabcde", ShorterConcatReverseLonger.shorterReverseLonger("first","abcde"));
        assertEquals("bauollehbau", ShorterConcatReverseLonger.shorterReverseLonger("hello", "bau"));
        assertEquals("fghiedcbafghi", ShorterConcatReverseLonger.shorterReverseLonger("abcde", "fghi"));

    }
}