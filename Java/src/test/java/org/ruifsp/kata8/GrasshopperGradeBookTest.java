package org.ruifsp.kata8;

import org.junit.jupiter.api.Test;

import static org.junit.jupiter.api.Assertions.*;

class GrasshopperGradeBookTest {

    @Test
    public void test1() {
        assertEquals('A', GrasshopperGradeBook.getGrade(95,90,93));
        assertEquals('A', GrasshopperGradeBook.getGrade(100,85,96));
        assertEquals('A', GrasshopperGradeBook.getGrade(92,93,94));
        assertEquals('A', GrasshopperGradeBook.getGrade(100,100,100));
    }
    @Test
    public void test2() {
        assertEquals('B', GrasshopperGradeBook.getGrade(70,70,100));
        assertEquals('B', GrasshopperGradeBook.getGrade(82,85,87));
        assertEquals('B', GrasshopperGradeBook.getGrade(84,79,85));
    }
    @Test
    public void test3() {
        assertEquals('C', GrasshopperGradeBook.getGrade(70,70,70));
        assertEquals('C', GrasshopperGradeBook.getGrade(75,70,79));
        assertEquals('C', GrasshopperGradeBook.getGrade(60,82,76));
    }
    @Test
    public void test4() {
        assertEquals('D', GrasshopperGradeBook.getGrade(65,70,59));
        assertEquals('D', GrasshopperGradeBook.getGrade(66,62,68));
        assertEquals('D', GrasshopperGradeBook.getGrade(58,62,70));
    }
    @Test
    public void test5() {
        assertEquals('F', GrasshopperGradeBook.getGrade(44,55,52));
        assertEquals('F', GrasshopperGradeBook.getGrade(48,55,52));
        assertEquals('F', GrasshopperGradeBook.getGrade(58,59,60));
        assertEquals('F', GrasshopperGradeBook.getGrade(0,0,0));
    }
}