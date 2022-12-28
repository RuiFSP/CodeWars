package org.ruifsp.kata7;

/*
Usually when you buy something, you're asked whether your credit card number, phone number or answer
to your most secret question is still correct. However, since someone could look over your shoulder,
you don't want that shown on your screen. Instead, we mask it.

Your task is to write a function maskify, which changes all but the last four characters into '#'.

Examples
"4556364607935616" --> "############5616"
     "64607935616" -->      "#######5616"
               "1" -->                "1"
                "" -->                 ""

// "What was the name of your first pet?"

"Skippy" --> "##ippy"

"Nananananananananananananananana Batman!"
-->
"####################################man!"


 */

public class CreditCardMask {
    public static String maskify(String str) {

        return str.length() <= 4 ? str : new String(new char[str.length() - 4]).replace("\0","#") + str.substring(str.length() - 4);
    }

}
