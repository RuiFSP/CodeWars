package org.ruifsp.kata6;

import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.*;

class MexicanWaveTest {

    @Test
    public void basicTest1() {
        assertArrayEquals(new String[] { "Hello", "hEllo", "heLlo", "helLo", "hellO" }, MexicanWave.wave("hello"));
    }

    @Test
    public void basicTest2() {
        assertArrayEquals(new String[] { "Codewars", "cOdewars", "coDewars", "codEwars", "codeWars", "codewArs", "codewaRs", "codewarS" }, MexicanWave.wave("codewars"));
    }

    @Test
    public void basicTest3() {
        assertArrayEquals(new String[] { }, MexicanWave.wave(""));
    }

    @Test
    public void basicTest4() {
        assertArrayEquals(new String[] { "Two words", "tWo words", "twO words", "two Words", "two wOrds", "two woRds", "two worDs", "two wordS" }, MexicanWave.wave("two words"));
    }

    @Test
    public void basicTest5() {
        assertArrayEquals(new String[] { " Gap ", " gAp ", " gaP " }, MexicanWave.wave(" gap "));
    }
}