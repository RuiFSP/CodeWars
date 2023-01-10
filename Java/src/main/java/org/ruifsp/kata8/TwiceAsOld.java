package org.ruifsp.kata8;

/*
Your function takes two arguments:

current father's age (years)
current age of his son (years)

Calculate how many years ago the father was twice as old as his son (or in how many years he will be twice as old).
The answer is always greater or equal to 0, no matter if it was in the past or it is in the future.
 */

public class TwiceAsOld {
    public static int TwiceAsOldFunc(int dadYears, int sonYears){

        return Math.abs(dadYears - 2 * sonYears);

    }
}
