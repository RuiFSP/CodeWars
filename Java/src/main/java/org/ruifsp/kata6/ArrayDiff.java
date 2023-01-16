package org.ruifsp.kata6;

/*
Your goal in this kata is to implement a difference function, which subtracts one list from another and
returns the result.

It should remove all values from list a, which are present in list b keeping their order.

Kata.arrayDiff(new int[] {1, 2}, new int[] {1}) => new int[] {2}
If a value is present in b, all of its occurrences must be removed from the other:

Kata.arrayDiff(new int[] {1, 2, 2, 2, 3}, new int[] {2}) => new int[] {1, 3}
 */

import java.util.stream.IntStream;

public class ArrayDiff {
    public static int[] arrayDiff(int[] a, int[] b) {

        return IntStream.of(a)
                .filter(x -> IntStream.of(b).noneMatch(y -> y == x))
                .toArray();
    }
}

/* another solution
import java.util.Arrays;
import java.util.List;
import java.util.stream.Collectors;

public class Kata {
    public static int[] arrayDiff(int[] a, int[] b) {
        List<Integer> listA = Arrays.stream(a).boxed().collect(Collectors.toList());
        List<Integer> listB = Arrays.stream(b).boxed().collect(Collectors.toList());
        listA.removeAll(listB);
        return listA.stream().mapToInt(e -> e).toArray();
    }
}

 */