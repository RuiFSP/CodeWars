package org.ruifsp.kata8;

/*
The cockroach is one of the fastest insects. Write a function which takes its speed in km per hour
and returns it in cm per second, rounded down to the integer (= floored).

For example:

1.08 --> 30
Note! The input is a Real number (actual type is language dependent) and is >= 0. The result should be an Integer.
 */

public class BeginnerSeries4Cockroach {
    public int cockroachSpeed(double x){

        return (int) (x * 100000 / 3600);

    }
}
