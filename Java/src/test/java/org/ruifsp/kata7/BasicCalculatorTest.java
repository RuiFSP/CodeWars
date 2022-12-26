package org.ruifsp.kata7;

import org.junit.jupiter.api.Test;

import static org.junit.jupiter.api.Assertions.*;

class BasicCalculatorTest {

    @Test
    public void BasicTest() {
        assertEquals(11.2, BasicCalculator.Calculator.calculate(3.2,"+", 8));
        assertEquals(-4.8, BasicCalculator.Calculator.calculate(3.2,"-", 8));
        assertEquals(0.4, BasicCalculator.Calculator.calculate(3.2,"/", 8));
        assertEquals(25.6, BasicCalculator.Calculator.calculate(3.2,"*", 8));
        assertEquals(-3, BasicCalculator.Calculator.calculate(-3,"+", 0));
        assertEquals(-3, BasicCalculator.Calculator.calculate(-3,"-", 0));
        assertNull(BasicCalculator.Calculator.calculate(-3, "/", 0));
        assertEquals(1, BasicCalculator.Calculator.calculate(-2, "/", -2));
        assertEquals(0, BasicCalculator.Calculator.calculate(-3,"*", 0));
        assertNull(BasicCalculator.Calculator.calculate(-3, "w", 0));
    }

}