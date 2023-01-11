package org.ruifsp.kata6;

import org.junit.jupiter.api.Test;

import static org.junit.jupiter.api.Assertions.*;

class BouncingBallsTest {

    @Test
    void bouncingBall() {
        assertEquals(3, BouncingBalls.bouncingBall(3.0, 0.66, 1.5));
    }
    @Test
    void bouncingBall1() {
        assertEquals(15, BouncingBalls.bouncingBall(30.0, 0.66, 1.5));
    }
}