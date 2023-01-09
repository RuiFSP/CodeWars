package org.ruifsp.kata6;

/*
Implement a pseudo-encryption algorithm which given a string S and an integer N concatenates all the odd-indexed
characters of S with all the even-indexed characters of S, this process should be repeated N times.

Examples:

encrypt("012345", 1)  =>  "135024"
encrypt("012345", 2)  =>  "135024"  ->  "304152"
encrypt("012345", 3)  =>  "135024"  ->  "304152"  ->  "012345"

encrypt("01234", 1)  =>  "13024"
encrypt("01234", 2)  =>  "13024"  ->  "32104"
encrypt("01234", 3)  =>  "13024"  ->  "32104"  ->  "20314"
Together with the encryption function, you should also implement a decryption function which reverses the process.

If the string S is an empty value or the integer N is not positive, return the first argument without changes.
 */


public class SimpleEncryption1AlternatingSplit {

    public static String encrypt(final String text, final int n) {
        if (text == null || text.length() == 0 || n <= 0) {
            return text;
        }

        String result = text;
        StringBuilder even = new StringBuilder();
        StringBuilder odd = new StringBuilder();

        for (int i = 0; i < n; i++) {
            for (int j = 0; j < result.length(); j++) {
                if (j % 2 == 0) {
                    even.append(result.charAt(j));
                } else {
                    odd.append(result.charAt(j));
                }
            }
            result = odd.toString() + even;
            even = new StringBuilder();
            odd = new StringBuilder();
        }
        return result;
    }

    public static String decrypt(final String encryptedText, final int n) {

        if (encryptedText == null || encryptedText.length() == 0 || n <= 0) {
            return encryptedText;
        }

        String result = encryptedText;
        int halfLength = result.length() / 2;

        for (int i = 0; i < n; i++) {
            StringBuilder temp = new StringBuilder();
            for (int j = 0; j < halfLength; j++) {
                temp.append(result.charAt(j + halfLength));
                temp.append(result.charAt(j));
            }
            if (result.length() % 2 != 0) {
                temp.append(result.charAt(result.length() - 1));
            }
            result = temp.toString();
        }
        return result;
    }

}
