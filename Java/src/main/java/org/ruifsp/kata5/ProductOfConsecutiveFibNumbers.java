package org.ruifsp.kata5;

/*
The Fibonacci numbers are the numbers in the following integer sequence (Fn):

0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, ...

such as

F(n) = F(n-1) + F(n-2) with F(0) = 0 and F(1) = 1.

Given a number, say prod (for product), we search two Fibonacci numbers F(n) and F(n+1) verifying

F(n) * F(n+1) = prod.

Your function productFib takes an integer (prod) and returns an array:

[F(n), F(n+1), true] or {F(n), F(n+1), 1} or (F(n), F(n+1), True)
depending on the language if F(n) * F(n+1) = prod.

If you don't find two consecutive F(n) verifying F(n) * F(n+1) = prodyou will return

[F(n), F(n+1), false] or {F(n), F(n+1), 0} or (F(n), F(n+1), False)
F(n) being the smallest one such as F(n) * F(n+1) > prod.

Some Examples of Return:
(depend on the language)

productFib(714) # should return (21, 34, true),
                # since F(8) = 21, F(9) = 34 and 714 = 21 * 34

productFib(800) # should return (34, 55, false),
                # since F(8) = 21, F(9) = 34, F(10) = 55 and 21 * 34 < 800 < 34 * 55
-----
productFib(714) # should return [21, 34, true],
productFib(800) # should return [34, 55, false],
-----
productFib(714) # should return {21, 34, 1},
productFib(800) # should return {34, 55, 0},
-----
productFib(714) # should return {21, 34, true},
productFib(800) # should return {34, 55, false},
Note:
You can see examples for your language in "Sample Tests".
 */

public class ProductOfConsecutiveFibNumbers {
    public static long[] productFib(long prod) {

        long n1_fib = 0, n2_fib = 1;
        long[] result = new long[3];

        while (n1_fib * n2_fib <= prod) {

            if (n1_fib * n2_fib == prod) {
                result[0] = n1_fib; result[1] = n2_fib; result[2] = 1;
                return result;
            }
            n2_fib += n1_fib;
            n1_fib = n2_fib - n1_fib;

        }

        result[0] = n1_fib; result[1] = n2_fib;
        return result;

    }

}


/*
simplified solution
	public static long[] productFib(long prod) {
	long a = 0L;
    long b = 1L;
    while (a * b < prod) {
      long tmp = a;
      a = b;
      b = tmp + b;
    }
    return new long[] { a, b, a * b == prod ? 1 : 0 };
   }


 */