package org.ruifsp.kata6;

import org.junit.jupiter.api.Test;

import static org.junit.jupiter.api.Assertions.*;

class ConsonantValueTest {

    @Test
    void solve() {
        assertEquals(ConsonantValue.solve("zodiac"), 26);
        assertEquals(ConsonantValue.solve("chruschtschov"), 80);
        assertEquals(ConsonantValue.solve("khrushchev"), 38);
        assertEquals(ConsonantValue.solve("strengthc"), 57);
        assertEquals(ConsonantValue.solve("twelfthstreet"), 103);
        assertEquals(ConsonantValue.solve("mischtschenkoana"), 80);
    }
}