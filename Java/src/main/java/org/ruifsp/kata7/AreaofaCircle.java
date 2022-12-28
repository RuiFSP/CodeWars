package org.ruifsp.kata7;

/*
Complete the function circleArea so that it will return the area of a circle with the given radius.
Round the returned number to two decimal places (except for Haskell).
If the radius is not positive or not a number, return false.

Example:

Circle.area(-1485.86);    //returns false
Circle.area(0);           //returns false
Circle.area(43.2673);     //returns 5881.25
Circle.area(68);          //returns 14526.72
 */

public class AreaofaCircle {
    public static double area(double radius) {

        if(radius <= 0 || Double.isNaN(radius)) {
            throw new IllegalArgumentException("Radius must be a positive number");
        }

        return Math.PI * Math.pow(radius,2);
    }
}
