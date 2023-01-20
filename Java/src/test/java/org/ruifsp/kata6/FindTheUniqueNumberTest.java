package org.ruifsp.kata6;

import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.*;

class FindTheUniqueNumberTest {


    @Test
    public void sampleTestCases() {
        assertEquals(1.0, FindTheUniqueNumber.findUniq(new double[]{0, 1, 0}));
        assertEquals(2.0, FindTheUniqueNumber.findUniq(new double[]{1, 1, 1, 2, 1, 1}));
    }
}