package org.ruifsp.kata7;

import org.junit.jupiter.api.Assertions;
import org.junit.jupiter.api.Test;

class NameArrayCappingTest {

    @Test
    void capMe() {
        String[] strings = new String[] {"jo", "nelson", "jurie"};
        Assertions.assertArrayEquals(new String[] {"Jo", "Nelson", "Jurie"}, NameArrayCapping.capMe(strings));
    }

}