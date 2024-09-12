import java.util.ArrayList;
import java.util.List;

class Solution {
    public String largestPalindromic(String num) {
        int[] digitsCounter = new int[10];

        for (int i = 0; i < num.length(); i++) {
            digitsCounter[num.charAt(i) - '0']++;
        }

        List<String> firstHalf = new ArrayList<>();
        String middle = "";

        for (int digit = 9; digit >= 0; digit--) {

            if (digitsCounter[digit] > 1) {
                firstHalf.add(String.valueOf(digit).repeat(digitsCounter[digit] / 2));
            }

            if (digitsCounter[digit] % 2 == 1 && middle.isEmpty()) {
                middle = String.valueOf(digit);
            }
        }

        StringBuilder palindrome = new StringBuilder();

        for (String part : firstHalf) {
            palindrome.append(part);
        }

        String result = palindrome.toString().replaceFirst("^0+", "") + middle
                + palindrome.reverse().toString().replaceFirst("0+$", "");

        return result.isEmpty() ? "0" : result;
    }
}