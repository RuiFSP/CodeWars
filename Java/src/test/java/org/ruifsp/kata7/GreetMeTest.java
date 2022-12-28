package org.ruifsp.kata7;

import org.junit.jupiter.api.Test;

import static org.junit.jupiter.api.Assertions.*;

class GreetMeTest {

    @Test
    void greet() {
        assertEquals("Hello Riley!", GreetMe.greet("riley"));
        assertEquals("Hello Riley!", GreetMe.greet("RILEY"));
    }
}