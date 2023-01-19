package org.ruifsp.kata7;

import java.util.Collections;
import java.util.List;

public class OnesAndZeros {
    public static int ConvertBinaryArrayToInt(List<Integer> binary) {

        Collections.reverse(binary);

        int num = 0;

        for (int i = 0; i < binary.toArray().length; i++) {
            int value_of_index = binary.get(i);

            if (value_of_index == 1) {
                num += Math.pow(2,i) * value_of_index;
            }

        }

        return num;
    }
}

/* Most voted
import java.util.List;

public class BinaryArrayToNumber {

    public static int ConvertBinaryArrayToInt(List<Integer> binary) {
        return binary.stream().reduce((x, y) -> x * 2 + y).get();
    }
}
 */