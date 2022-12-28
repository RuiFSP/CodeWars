package org.ruifsp.kata7;

import org.junit.jupiter.api.Test;

import static org.junit.jupiter.api.Assertions.*;

class JadenCasingStringsTest {

    JadenCasingStrings jadenCase = new JadenCasingStrings();

    @Test
    void toJadenCase() {
        assertEquals("Most Trees Are Blue", jadenCase.toJadenCase("most trees are blue"));
    }
    @Test
    void toJadenCaseNull(){
        assertNull(null, jadenCase.toJadenCase(null));
    }

    @Test
    void toJadenCaseEmpty(){
        assertNull(null, jadenCase.toJadenCase(" "));
    }


}