package org.ruifsp.kata7;

import org.junit.jupiter.api.Test;
import org.ruifsp.kata7.TwoFightersOneWinner.Fighter;
import org.ruifsp.kata7.TwoFightersOneWinner.TwoFightersOneWinner;

import static org.junit.jupiter.api.Assertions.*;

class TwoFightersOneWinnerTest {

    @Test
    void declareWinner() {
        assertEquals("Lew", TwoFightersOneWinner.declareWinner(new Fighter("Lew", 10, 2),new Fighter("Harry", 5, 4), "Lew"));
        assertEquals("Harry", TwoFightersOneWinner.declareWinner(new Fighter("Lew", 10, 2),new Fighter("Harry", 5, 4), "Harry"));
        assertEquals("Harald", TwoFightersOneWinner.declareWinner(new Fighter("Harald", 20, 5), new Fighter("Harry", 5, 4), "Harry"));
        assertEquals("Harald", TwoFightersOneWinner.declareWinner(new Fighter("Harald", 20, 5), new Fighter("Harry", 5, 4), "Harald"));
        assertEquals("Harald", TwoFightersOneWinner.declareWinner(new Fighter("Jerry", 30, 3), new Fighter("Harald", 20, 5), "Jerry"));
        assertEquals("Harald", TwoFightersOneWinner.declareWinner(new Fighter("Jerry", 30, 3), new Fighter("Harald", 20, 5), "Harald"));
    }
}