package org.ruifsp.kata8;

import org.junit.jupiter.api.Test;

import static org.junit.jupiter.api.Assertions.*;

class AbbreviateATwoWordNameTest {

    @Test
    void abbrevName() {
        assertEquals("S.H", AbbreviateATwoWordName.abbrevName("Sam Harris"));
        assertEquals("P.F", AbbreviateATwoWordName.abbrevName("Patrick Feenan"));
        assertEquals("E.C", AbbreviateATwoWordName.abbrevName("Evan Cole"));
        assertEquals("P.F", AbbreviateATwoWordName.abbrevName("P Favuzzi"));
        assertEquals("D.M", AbbreviateATwoWordName.abbrevName("David Mendieta"));
    }
}