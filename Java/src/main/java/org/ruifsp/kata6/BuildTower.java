package org.ruifsp.kata6;

/*
Build Tower
Build a pyramid-shaped tower, as an array/list of strings, given
a positive integer number of floors. A tower block is represented with "*" character.

For example, a tower with 3 floors looks like this:

[
  "  *  ",
  " *** ",
  "*****"
]
And a tower with 6 floors looks like this:

[
  "     *     ",
  "    ***    ",
  "   *****   ",
  "  *******  ",
  " ********* ",
  "***********"
]
 */


public class BuildTower {
    public static String[] towerBuilder(int nFloors) {

        String[] tower = new String[nFloors];
        for (int i = 0; i < nFloors; i++) {
            String spaces = " ".repeat(nFloors - i - 1);
            String stars = "*".repeat(2 * i + 1);
            tower[i] = spaces + stars + spaces;
        }
        return tower;
    }
}
