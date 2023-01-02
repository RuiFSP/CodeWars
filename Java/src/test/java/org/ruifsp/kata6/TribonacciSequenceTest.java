package org.ruifsp.kata6;


import org.junit.jupiter.api.Assertions;
import org.junit.jupiter.api.Test;

class TribonacciSequenceTest {


    @Test
    void tribonacci() {

        Assertions.assertArrayEquals(new double []{1,1,1,3,5,9,17,31,57,105}, TribonacciSequence.tribonacci(new double []{1,1,1},10));

    }
}