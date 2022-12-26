package org.ruifsp.kata7;

import org.junit.jupiter.api.Test;

import static org.junit.jupiter.api.Assertions.*;

class SortArrays1Test {
    @Test
    public void stringArrayTests() {
        String[] ai = {"ana", "pedro", "rui"};
        String[] uai = {"rui", "ana", "pedro"};
        assertEquals(ai[0], SortArrays1.sortArray(uai)[0]);
        assertEquals(ai[1], SortArrays1.sortArray(uai)[1]);
        assertEquals(ai[2], SortArrays1.sortArray(uai)[2]);
    }

    @Test
    public void intArrayTests() {
        int[] ai = {1, 2, 3};
        int[] uai = {2, 3, 1};
        assertEquals(ai[0], SortArrays1.sortArray(uai)[0]);
        assertEquals(ai[1], SortArrays1.sortArray(uai)[1]);
        assertEquals(ai[2], SortArrays1.sortArray(uai)[2]);
    }

    @Test
    public void doubleArrayTests() {
        double[] ai = {1.0, 2.0, 3.0};
        double[] uai = {2.0, 3.0, 1.0};
        assertEquals(ai[0], SortArrays1.sortArray(uai)[0]);
        assertEquals(ai[1], SortArrays1.sortArray(uai)[1]);
        assertEquals(ai[2], SortArrays1.sortArray(uai)[2]);
    }

    @Test
    public void floatArrayTests() {
        float[] ai = {1.1110f, 2.22220f, 3.3330f};
        float[] uai = {2.22220f, 3.3330f, 1.1110f};
        assertEquals(ai[0], SortArrays1.sortArray(uai)[0]);
        assertEquals(ai[1], SortArrays1.sortArray(uai)[1]);
        assertEquals(ai[2], SortArrays1.sortArray(uai)[2]);
    }
    @Test
    public void longArrayTests() {
        long[] ai = {1111111L, 2222222L, 3333333L};
        long[] uai = {2222222L, 3333333L, 1111111L};
        assertEquals(ai[0], SortArrays1.sortArray(uai)[0]);
        assertEquals(ai[1], SortArrays1.sortArray(uai)[1]);
        assertEquals(ai[2], SortArrays1.sortArray(uai)[2]);
    }
    @Test
    public void ArrayTests() {
        Integer[] ai = {1, 2, 3};
        Integer[] uai = {2, 3, 1};
        assertEquals(ai[0], SortArrays1.sortArray(uai)[0]);
        assertEquals(ai[1], SortArrays1.sortArray(uai)[1]);
        assertEquals(ai[2], SortArrays1.sortArray(uai)[2]);
    }



}