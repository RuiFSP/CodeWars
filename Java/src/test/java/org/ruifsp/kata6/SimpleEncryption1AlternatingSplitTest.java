package org.ruifsp.kata6;

import org.junit.jupiter.api.Test;

import static org.junit.jupiter.api.Assertions.*;

class SimpleEncryption1AlternatingSplitTest {

    @Test
    void encrypt() {
        assertEquals("This is a test!", SimpleEncryption1AlternatingSplit.encrypt("This is a test!", 0));
        assertEquals("hsi  etTi sats!", SimpleEncryption1AlternatingSplit.encrypt("This is a test!", 1));
        assertEquals("s eT ashi tist!", SimpleEncryption1AlternatingSplit.encrypt("This is a test!", 2));
        assertEquals(" Tah itse sits!", SimpleEncryption1AlternatingSplit.encrypt("This is a test!", 3));
        assertEquals("This is a test!", SimpleEncryption1AlternatingSplit.encrypt("This is a test!", 4));
        assertEquals("This is a test!", SimpleEncryption1AlternatingSplit.encrypt("This is a test!", -1));
        assertEquals("hskt svr neetn!Ti aai eyitrsig", SimpleEncryption1AlternatingSplit.encrypt("This kata is very interesting!", 1));
    }

    @Test
    void decrypt() {
        assertEquals("This is a test!", SimpleEncryption1AlternatingSplit.decrypt("This is a test!", 0));
        assertEquals("This is a test!", SimpleEncryption1AlternatingSplit.decrypt("hsi  etTi sats!", 1));
        assertEquals("This is a test!", SimpleEncryption1AlternatingSplit.decrypt("s eT ashi tist!", 2));
        assertEquals("This is a test!", SimpleEncryption1AlternatingSplit.decrypt(" Tah itse sits!", 3));
        assertEquals("This is a test!", SimpleEncryption1AlternatingSplit.decrypt("This is a test!", 4));
        assertEquals("This is a test!", SimpleEncryption1AlternatingSplit.decrypt("This is a test!", -1));
        assertEquals("This kata is very interesting!", SimpleEncryption1AlternatingSplit.decrypt("hskt svr neetn!Ti aai eyitrsig", 1));
    }

    @Test
    void testNullOrEmpty(){
        assertEquals("", SimpleEncryption1AlternatingSplit.encrypt("", 0));
        assertEquals("", SimpleEncryption1AlternatingSplit.decrypt("", 0));
        assertNull(SimpleEncryption1AlternatingSplit.encrypt(null, 0));
        assertNull(SimpleEncryption1AlternatingSplit.decrypt(null, 0));
    }
}