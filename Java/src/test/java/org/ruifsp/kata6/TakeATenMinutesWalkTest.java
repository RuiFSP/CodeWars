package org.ruifsp.kata6;

import org.junit.jupiter.api.Test;

import static org.junit.jupiter.api.Assertions.*;

class TakeATenMinutesWalkTest {

    @Test
    void isValid() {
        assertTrue(TakeATenMinutesWalk.isValid(new char[]{'n', 's', 'n', 's', 'n', 's', 'n', 's', 'n', 's'}));
        assertFalse(TakeATenMinutesWalk.isValid(new char[] {'w','e','w','e','w','e','w','e','w','e','w','e'}));
        assertFalse(TakeATenMinutesWalk.isValid(new char[] {'w'}));
        assertFalse(TakeATenMinutesWalk.isValid(new char[] {'n','n','n','s','n','s','n','s','n','s'}));
    }
}