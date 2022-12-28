package org.ruifsp.kata7;

import org.junit.jupiter.api.Test;

import static org.junit.jupiter.api.Assertions.*;

class CreditCardMaskTest {

    @Test
    void maskify() {

        assertEquals("############5616",CreditCardMask.maskify("4556364607935616"));
        assertEquals("#######5616",CreditCardMask.maskify("64607935616"));
        assertEquals("1",CreditCardMask.maskify("1"));
        assertEquals("",CreditCardMask.maskify(""));
        assertEquals("##ippy",CreditCardMask.maskify("Skippy"));
        assertEquals("####################################man!",CreditCardMask.maskify("Nananananananananananananananana Batman!"));
    }
}